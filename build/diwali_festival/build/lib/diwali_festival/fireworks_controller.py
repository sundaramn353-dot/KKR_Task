"""Fireworks sequencing on top of Gazebo's ParticleEmitter system.

Honest description of the effect: Gazebo Harmonic particle emitters are continuous emitters, not a
burst/explosion system. A "firework" is therefore a timed choreography of several emitters
(see diwali_sim/scripts/generate_assets.py: firework_body):

  rocket + smoke : narrow vertical stream of bright / grey particles (reads as a rising rocket)
  gold/red/blue/green : ellipsoid emitter at ~28 m, switched on for 0.4 s => expanding shell
  sparkle        : small white-gold particles around the burst

Each emitter listens on /festival/fw/<site>/<emitter> (gz.msgs.ParticleEmitter, field `emitting`).
"""
import random

BURSTS = {'golden_burst': 'gold', 'red_burst': 'red', 'blue_burst': 'blue', 'green_burst': 'green'}
EMITTERS = ('rocket', 'smoke', 'gold', 'red', 'blue', 'green', 'sparkle')
EFFECTS = ('rocket', 'golden_burst', 'red_burst', 'blue_burst', 'green_burst', 'sparkle', 'finale',
           'sparkler_on', 'sparkler_off', 'stop', 'random')
RISE_S = 1.5


def _launch():
    return [(0.0, 'sound', 'firework_launch'), (0.0, 'emit', 'rocket', True), (0.0, 'emit', 'smoke', True),
            (RISE_S, 'emit', 'rocket', False), (RISE_S + 0.6, 'emit', 'smoke', False)]


def _burst(color, t0=RISE_S):
    return [(t0, 'sound', 'firework_burst'), (t0, 'emit', color, True), (t0, 'emit', 'sparkle', True),
            (t0 + 0.4, 'emit', color, False), (t0 + 1.2, 'sound', 'firework_crackle'),
            (t0 + 1.4, 'emit', 'sparkle', False)]


def timeline(effect):
    if effect == 'rocket':
        return _launch()
    if effect in BURSTS:
        return _launch() + _burst(BURSTS[effect])
    if effect == 'sparkle':
        return [(0.0, 'emit', 'sparkle', True), (1.5, 'emit', 'sparkle', False)]
    return None


class FireworksController:
    def __init__(self, gz, sites, sparklers, sound, logger=None):
        self.gz, self.sites, self.sparklers, self.sound, self._log = gz, list(sites), list(sparklers), sound, logger
        self._queue = []                       # (abs_time, site, action, args...)
        self._busy_until = {s: 0.0 for s in self.sites}
        for s in self.sites:
            for e in EMITTERS:
                self.gz.prime(self._topic(s, e))
        for sp in self.sparklers:
            self.gz.prime(self._spark_topic(sp))

    @staticmethod
    def _topic(site, emitter):
        return f'/festival/fw/{site}/{emitter}'

    @staticmethod
    def _spark_topic(sid):
        return f'/festival/sparkler/{sid}'

    def _schedule(self, now, site, steps, offset=0.0):
        for st in steps:
            self._queue.append((now + offset + st[0], site) + tuple(st[1:]))
        self._queue.sort(key=lambda q: q[0])
        end = now + offset + max(s[0] for s in steps) + 0.5
        self._busy_until[site] = max(self._busy_until[site], end)

    def free_sites(self, now):
        return [s for s in self.sites if self._busy_until[s] <= now]

    def trigger(self, effect, site, now):
        """Returns (accepted: bool, reason: str)."""
        if effect == 'stop':
            self.stop_all()
            return True, 'stopped'
        if effect in ('sparkler_on', 'sparkler_off'):
            for sp in self.sparklers:
                self.gz.set_emitting(self._spark_topic(sp), effect == 'sparkler_on')
            return True, effect
        if effect == 'finale':
            free = self.free_sites(now)
            if not free:
                return False, 'all sites busy'
            colors = list(BURSTS.values())
            for i, s in enumerate(free):
                steps = _launch() + _burst(colors[i % 4])
                self._schedule(now, s, steps, offset=i * 0.7)
            return True, f'finale on {len(free)} site(s)'
        steps = timeline(effect)
        if steps is None:
            return False, f'unknown effect "{effect}"'
        if site is None:
            free = self.free_sites(now)
            if not free:
                return False, 'all sites busy'
            site = random.choice(free)
        elif site not in self._busy_until:
            return False, f'unknown site "{site}"'
        elif self._busy_until[site] > now:
            return False, f'site {site} busy'
        self._schedule(now, site, steps)
        return True, site

    def tick(self, now):
        while self._queue and self._queue[0][0] <= now:
            item = self._queue.pop(0)
            _, site, action = item[0], item[1], item[2]
            if action == 'emit':
                self.gz.set_emitting(self._topic(site, item[3]), item[4])
            elif action == 'sound':
                self.sound.play(item[3])

    def stop_all(self):
        self._queue.clear()
        for s in self.sites:
            self._busy_until[s] = 0.0
            for e in EMITTERS:
                self.gz.set_emitting(self._topic(s, e), False)
