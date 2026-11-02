"""Thin wrapper around Gazebo Transport.

Why this exists: ros_gz_bridge has no mapping for gz.msgs.ParticleEmitter, so ROS 2 cannot
publish it directly. This adapter talks to Gazebo Harmonic's transport layer instead:

  * preferred: Python bindings (python3-gz-transport13 + python3-gz-msgs10)
  * fallback : the `gz` command line tool (slower, one process per call, but no extra packages)
"""
import shutil
import subprocess

try:  # Harmonic = gz-transport13 / gz-msgs10
    from gz.transport13 import Node as GzNode
    from gz.msgs10.particle_emitter_pb2 import ParticleEmitter
    from gz.msgs10.light_pb2 import Light
    from gz.msgs10.boolean_pb2 import Boolean
    HAVE_PY_BINDINGS = True
except Exception:  # pragma: no cover - depends on the machine
    HAVE_PY_BINDINGS = False


class GzInterface:
    def __init__(self, world='diwali_street', logger=None, force_cli=False):
        self.world = world
        self._log = logger
        self.use_py = HAVE_PY_BINDINGS and not force_cli
        self._node = GzNode() if self.use_py else None
        self._pubs = {}
        self._procs = []
        self.gz_bin = shutil.which('gz')
        mode = 'python bindings' if self.use_py else ('gz CLI' if self.gz_bin else 'NONE (dry run)')
        self._info(f'Gazebo transport backend: {mode}')

    # -- logging helpers -------------------------------------------------------------------
    def _info(self, msg):
        if self._log:
            self._log.info(msg)

    def _warn(self, msg):
        if self._log:
            self._log.warn(msg)

    # -- particle emitters -----------------------------------------------------------------
    def prime(self, topic):
        """Advertise early so Gazebo transport discovery has finished before the first command."""
        if self.use_py and topic not in self._pubs:
            self._pubs[topic] = self._node.advertise(topic, ParticleEmitter)

    def set_emitting(self, topic, emitting):
        emitting = bool(emitting)
        if self.use_py:
            self.prime(topic)
            msg = ParticleEmitter()
            msg.emitting.data = emitting
            return self._pubs[topic].publish(msg)
        return self._cli(['topic', '-t', topic, '-m', 'gz.msgs.ParticleEmitter', '-p',
                          f'emitting: {{data: {str(emitting).lower()}}}'])

    # -- lights ----------------------------------------------------------------------------
    def set_light(self, name, pose, diffuse, intensity, range_, attenuation):
        """Calls /world/<world>/light_config (UserCommands system) with a full gz.msgs.Light."""
        service = f'/world/{self.world}/light_config'
        if self.use_py:
            msg = Light()
            msg.name = name
            msg.type = Light.POINT
            msg.intensity = float(intensity)
            msg.range = float(range_)
            msg.attenuation_constant, msg.attenuation_linear, msg.attenuation_quadratic = attenuation
            msg.cast_shadows = False
            msg.diffuse.r, msg.diffuse.g, msg.diffuse.b, msg.diffuse.a = (*diffuse, 1.0)
            msg.specular.r, msg.specular.g, msg.specular.b, msg.specular.a = (*diffuse, 1.0)
            msg.pose.position.x, msg.pose.position.y, msg.pose.position.z = pose[:3]
            ok, _ = self._node.request(service, msg, Light, Boolean, 300)
            return ok
        r, g, b = diffuse
        text = (f'name: "{name}" type: POINT intensity: {intensity} range: {range_} '
                f'attenuation_constant: {attenuation[0]} attenuation_linear: {attenuation[1]} '
                f'attenuation_quadratic: {attenuation[2]} cast_shadows: false '
                f'diffuse {{r: {r} g: {g} b: {b} a: 1}} specular {{r: {r} g: {g} b: {b} a: 1}} '
                f'pose {{position {{x: {pose[0]} y: {pose[1]} z: {pose[2]}}}}}')
        return self._cli(['service', '-s', service, '--reqtype', 'gz.msgs.Light', '--reptype',
                          'gz.msgs.Boolean', '--timeout', '300', '--req', text])

    # -- CLI fallback ----------------------------------------------------------------------
    def _cli(self, args):
        if not self.gz_bin:
            self._warn('No Gazebo transport backend available; command dropped: gz ' + ' '.join(args[:3]))
            return False
        self._procs = [p for p in self._procs if p.poll() is None]
        if len(self._procs) > 24:
            return False  # protect against process storms
        self._procs.append(subprocess.Popen([self.gz_bin] + args, stdout=subprocess.DEVNULL,
                                            stderr=subprocess.DEVNULL))
        return True
