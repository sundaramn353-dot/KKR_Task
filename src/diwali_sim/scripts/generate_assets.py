#!/usr/bin/env python3
"""Procedural asset generator for the Diwali street simulation.

Generates (all self-contained, no downloads, standard library only):
  * SDF models           -> diwali_sim/models/<name>/{model.sdf,model.config}
  * textures (PNG)       -> rangoli, kolam, banner
  * world                -> diwali_sim/worlds/diwali_street.sdf
  * controllable lights  -> diwali_sim/config/festival_lights.yaml
  * synthetic WAV files  -> diwali_festival/sounds/
  * occupancy-grid map   -> diwali_robot/maps/diwali_street.{pgm,yaml}

Run:  python3 generate_assets.py        (output is already committed; re-run after edits)
"""
import math
import random
import struct
import wave
import zlib
from pathlib import Path
from xml.dom import minidom

PKG = Path(__file__).resolve().parent.parent
SRC = PKG.parent
MODELS = PKG / 'models'
WORLDS = PKG / 'worlds'
CONFIG = PKG / 'config'
SOUNDS = SRC / 'diwali_festival' / 'sounds'
MAPS = SRC / 'diwali_robot' / 'maps'
WORLD = 'diwali_street'
rnd = random.Random(7)

# ----------------------------------------------------------------------------
# Street layout (metres). Street runs along world X; road centre line y = 0.
# ----------------------------------------------------------------------------
ROAD_HALF = 3.5          # road y in [-3.5, 3.5]
SIDEWALK_OUT = 5.5       # sidewalk y in [3.5, 5.5]
WALL_Y = 6.5             # compound wall centre line |y|
STREET_X = 52.0          # barricades at the outer city-road limits
HOUSE_X = [-18.0, -6.0, 6.0, 18.0]
HOUSE_Y = 15.3           # house origin |y|; local +x faces the street
POLE_X = [-24.0, -12.0, 0.0, 12.0, 24.0]
POLE_Y = 4.5
FW_SITES = {'fw_n1': (-14.0, 32.0), 'fw_n2': (14.0, 32.0),
            'fw_s1': (-14.0, -32.0), 'fw_s2': (14.0, -32.0)}
CITY_TOWER_X = [-42.0, -21.0, 0.0, 21.0, 42.0]
CITY_TOWER_Y = (-42.0, 42.0)
OBST = []                # (x0, y0, x1, y1) world rectangles used for the Nav2 map


# ----------------------------------------------------------------------------
# SDF helpers
# ----------------------------------------------------------------------------
def P(t):
    t = tuple(t) + (0.0,) * (6 - len(t))
    return '<pose>' + ' '.join(f'{v:.4f}' for v in t) + '</pose>'


def box(x, y, z):
    return f'<box><size>{x:.4f} {y:.4f} {z:.4f}</size></box>'


def cyl(r, l):
    return f'<cylinder><radius>{r:.4f}</radius><length>{l:.4f}</length></cylinder>'


def sph(r):
    return f'<sphere><radius>{r:.4f}</radius></sphere>'


def mat(rgb, rough=0.8, metal=0.0, emis=None, albedo=None, alpha=1.0):
    r, g, b = (c / 255.0 for c in rgb)
    s = (f'<material><ambient>{r:.3f} {g:.3f} {b:.3f} {alpha}</ambient>'
         f'<diffuse>{r:.3f} {g:.3f} {b:.3f} {alpha}</diffuse>'
         f'<specular>0.2 0.2 0.2 1</specular>')
    if emis:
        er, eg, eb = (c / 255.0 for c in emis)
        s += f'<emissive>{er:.3f} {eg:.3f} {eb:.3f} 1</emissive>'
    s += '<pbr><metal>'
    if albedo:
        s += f'<albedo_map>{albedo}</albedo_map>'
    s += f'<roughness>{rough}</roughness><metalness>{metal}</metalness></metal></pbr></material>'
    return s


def vis(name, geom, pose=(0, 0, 0), material='', shadow=True):
    sh = '' if shadow else '<cast_shadows>false</cast_shadows>'
    return (f'<visual name="{name}">{P(pose)}<geometry>{geom}</geometry>{material}{sh}</visual>')


def col(name, geom, pose=(0, 0, 0)):
    return f'<collision name="{name}">{P(pose)}<geometry>{geom}</geometry></collision>'


def link(name, body):
    return f'<link name="{name}">{body}</link>'


def pretty(xml):
    d = minidom.parseString(xml.encode('utf-8'))
    s = d.toprettyxml(indent='  ')
    return '\n'.join(l for l in s.split('\n') if l.strip()) + '\n'


def write(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def write_model(name, desc, body, static=True):
    sdf = (f'<sdf version="1.9"><model name="{name}"><static>{str(static).lower()}</static>'
           f'{body}</model></sdf>')
    write(MODELS / name / 'model.sdf', pretty(sdf))
    cfg = (f'<model><name>{name}</name><version>1.0</version>'
           f'<sdf version="1.9">model.sdf</sdf>'
           f'<author><name>diwali_sim generator</name><email>none@example.com</email></author>'
           f'<description>{desc}</description></model>')
    write(MODELS / name / 'model.config', pretty(cfg))


# ----------------------------------------------------------------------------
# Textures (pure-python PNG writer)
# ----------------------------------------------------------------------------
def write_png(path, wd, ht, fn):
    raw = bytearray()
    for j in range(ht):
        raw.append(0)
        for i in range(wd):
            raw += bytes(fn((i + 0.5) / wd, 1.0 - (j + 0.5) / ht))

    def chunk(t, d):
        c = struct.pack('>I', len(d)) + t + d
        return c + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)

    png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', wd, ht, 8, 2, 0, 0, 0)) +
           chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b''))
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(png)


def rangoli_px(u, v):
    x, y = u * 2 - 1, v * 2 - 1
    r, th = math.hypot(x, y), math.atan2(y, x)
    ground = (62, 56, 52)
    if r > 0.97:
        return ground
    if r > 0.90:                                   # beaded border
        return (245, 245, 235) if int((th + math.pi) * 24 / math.pi) % 2 == 0 else (200, 30, 60)
    petals = [(214, 40, 80), (255, 140, 0), (255, 205, 0), (30, 150, 70)]
    if 0.45 < r < 0.40 + 0.48 * abs(math.cos(4 * th)):   # outer lotus petals
        return petals[int((th + math.pi) / (math.pi / 4)) % 4]
    if r > 0.45:
        return (40, 36, 100)
    if r > 0.30:                                   # ring
        return (250, 250, 250) if int((th + math.pi) * 6 / math.pi) % 2 == 0 else (40, 70, 180)
    if r < 0.06:
        return (255, 255, 255)
    if r < 0.12 + 0.18 * abs(math.cos(4 * th + math.pi / 8)):
        return (255, 210, 0)
    return (230, 60, 120)


def kolam_px(u, v):
    x, y = u * 2 - 1, v * 2 - 1
    ground = (52, 50, 56)
    if abs(x) + abs(y) > 0.92:
        return ground
    k = math.pi / 0.2
    val = math.cos(k * (x + y)) + math.cos(k * (x - y))
    if abs(val) < 0.16:
        return (245, 245, 240)                      # rice-flour lines
    dx = (x / 0.2 + 0.5) % 1.0 - 0.5
    dy = (y / 0.2 + 0.5) % 1.0 - 0.5
    if dx * dx + dy * dy < 0.012:
        return (255, 255, 255)                      # pulli dots
    return ground


def banner_px(u, v):
    if v < 0.14 or v > 0.86:
        tri = abs(((u * 40) % 1.0) - 0.5) * 2
        if abs((v if v < 0.5 else 1 - v) - (0.05 + 0.05 * tri)) < 0.018:
            return (255, 205, 60)
        return (150, 20, 35)
    uc = (math.floor(u * 12) + 0.5) / 12
    dx, dy = (u - uc) * 4.0, v - 0.5
    r2 = dx * dx + dy * dy
    if r2 < 0.012:
        return (255, 245, 170)
    if r2 < 0.03:
        return (255, 120, 20)
    if r2 < 0.06:
        return (230, 170, 30)
    return (255, 150, 10)


# ----------------------------------------------------------------------------
# Models
# ----------------------------------------------------------------------------
BRASS = (205, 155, 60)


def make_diya(name, lit):
    flame = (255, 140, 20)
    V = [
        vis('foot', cyl(0.03, 0.012), (0, 0, 0.006), mat(BRASS, 0.35, 0.7)),
        vis('bowl', cyl(0.05, 0.022), (0, 0, 0.023), mat(BRASS, 0.3, 0.8)),
        vis('oil', cyl(0.042, 0.004), (0, 0, 0.035), mat((70, 40, 10), 0.2)),
        vis('lip', box(0.05, 0.03, 0.02), (0.055, 0, 0.03), mat(BRASS, 0.3, 0.8)),
        vis('wick', cyl(0.003, 0.02), (0.06, 0, 0.045), mat((30, 20, 10), 0.9)),
        vis('flame', sph(0.014), (0.06, 0, 0.064), mat(flame, 0.5, emis=(255, 170, 40)), shadow=False),
    ]
    L = ''
    if lit:   # real light source: emissive materials do NOT illuminate neighbours
        L = ('<light name="flame_light" type="point">' + P((0.06, 0, 0.09)) +
             '<cast_shadows>false</cast_shadows><diffuse>1 0.62 0.22 1</diffuse>'
             '<specular>1 0.55 0.2 1</specular><intensity>0.7</intensity>'
             '<attenuation><range>3</range><constant>0.2</constant><linear>0.6</linear>'
             '<quadratic>1.0</quadratic></attenuation></light>')
    write_model(name, 'Brass oil lamp (diya) with emissive flame' + (' and point light' if lit else ''),
                link('link', ''.join(V) + L))


def make_rangoli(name, tex, size, fn, thick=0.004):
    img = f'model://rangoli/materials/textures/{tex}'
    V = vis('floor_art', box(size, size, thick), (0, 0, thick / 2),
            mat((255, 255, 255), 0.9, albedo=img), shadow=False)
    write_model(name, 'Texture-based floor decoration (visual only, no collision)', link('link', V))


def curve(L, n, sag):
    pts = []
    for k in range(n):
        t = k / (n - 1)
        pts.append(((t - 0.5) * L, -sag * (1 - (2 * t - 1) ** 2)))
    return pts


def wire(pts, prefix, rgb):
    out = []
    for k in range(len(pts) - 1):
        (x0, z0), (x1, z1) = pts[k], pts[k + 1]
        ln = math.hypot(x1 - x0, z1 - z0)
        out.append(vis(f'{prefix}{k}', box(ln, 0.012, 0.012), ((x0 + x1) / 2, 0, (z0 + z1) / 2, 0,
                       -math.atan2(z1 - z0, x1 - x0), 0), mat(rgb, 0.7), shadow=False))
    return out


def make_led_string(name, L, n, sag):
    cols = [(255, 40, 40), (40, 255, 80), (60, 120, 255), (255, 210, 40), (255, 60, 220)]
    pts = curve(L, n, sag)
    V = wire(pts, 'w', (25, 25, 25))
    for k, (x, z) in enumerate(pts):
        c = cols[k % 5]
        V.append(vis(f'bulb{k}', sph(0.035), (x, 0, z - 0.04), mat(c, 0.3, emis=c), shadow=False))
    write_model(name, f'Decorative LED string {L} m (emissive bulbs, visual only)', link('link', ''.join(V)))


def make_garland(name, L, n, sag):
    cols = [(255, 120, 0), (255, 190, 10), (230, 90, 0)]
    pts = curve(L, n, sag)
    V = []
    for k, (x, z) in enumerate(pts):
        V.append(vis(f'f{k}', sph(0.045), (x, 0, z), mat(cols[k % 3], 0.9), shadow=False))
        if k % 4 == 2:
            for j in range(1, 4):
                V.append(vis(f'f{k}_s{j}', sph(0.04), (x, 0, z - 0.11 * j), mat(cols[(k + j) % 3], 0.9),
                             shadow=False))
    write_model(name, f'Marigold flower garland {L} m (visual only)', link('link', ''.join(V)))


def make_toran(name):
    V = [vis('string', box(1.6, 0.015, 0.015), (0, 0, 0), mat((90, 60, 30)), shadow=False)]
    for k in range(9):
        x = -0.7 + k * 0.175
        V.append(vis(f'leaf{k}', box(0.07, 0.015, 0.2), (x, 0, -0.1), mat((35, 120, 45), 0.8), shadow=False))
        V.append(vis(f'flower{k}', sph(0.04), (x + 0.087, 0, -0.05), mat((255, 150, 0), 0.9), shadow=False))
    write_model(name, 'Mango-leaf and marigold door toran (visual only)', link('link', ''.join(V)))


def make_streetlight():
    V = [vis('pole', cyl(0.06, 6.0), (0, 0, 3.0), mat((50, 52, 56), 0.5, 0.6)),
         vis('base', cyl(0.12, 0.3), (0, 0, 0.15), mat((50, 52, 56), 0.5, 0.6)),
         vis('arm', box(1.3, 0.06, 0.06), (0.6, 0, 5.95), mat((50, 52, 56), 0.5, 0.6)),
         vis('head', box(0.55, 0.22, 0.08), (1.2, 0, 5.93), mat((60, 60, 60), 0.5, 0.5)),
         vis('lens', box(0.45, 0.16, 0.02), (1.2, 0, 5.88), mat((255, 225, 160), 0.3, emis=(255, 215, 140)),
             shadow=False)]
    C = [col('pole', cyl(0.1, 6.0), (0, 0, 3.0))]
    L = ('<light name="lamp" type="spot">' + P((1.2, 0, 5.85)) +
         '<cast_shadows>false</cast_shadows><diffuse>1 0.84 0.55 1</diffuse>'
         '<specular>0.6 0.5 0.3 1</specular><intensity>3</intensity>'
         '<attenuation><range>16</range><constant>0.5</constant><linear>0.04</linear>'
         '<quadratic>0.008</quadratic></attenuation><direction>0 0 -1</direction>'
         '<spot><inner_angle>0.5</inner_angle><outer_angle>1.15</outer_angle><falloff>1.0</falloff></spot>'
         '</light>')
    write_model('streetlight', 'Sodium-style streetlight with spot light (pole collision only)',
                link('link', ''.join(V) + ''.join(C) + L))


def make_banner():
    tex = 'model://festival_banner/materials/textures/banner.png'
    V = [vis('cloth_front', box(9.2, 0.02, 0.95), (0, 0.01, 4.15), mat((255, 255, 255), 0.95, albedo=tex), shadow=False),
         vis('cloth_back', box(9.2, 0.02, 0.95), (0, -0.01, 4.15), mat((255, 255, 255), 0.95, albedo=tex), shadow=False),
         vis('bar', cyl(0.025, 9.6), (0, 0, 4.7), mat((60, 40, 20)), shadow=False)]
    V[2] = V[2].replace('<pose>0.0000 0.0000 4.7000 0.0000 0.0000 0.0000</pose>',
                        '<pose>0.0000 0.0000 4.7000 0.0000 1.5708 0.0000</pose>')
    C = []
    for s in (-1, 1):
        V.append(vis(f'pole{s}', cyl(0.05, 4.9), (s * 4.8, 0, 2.45), mat((70, 70, 75), 0.6, 0.5)))
        C.append(col(f'pole{s}', cyl(0.07, 4.9), (s * 4.8, 0, 2.45)))
    write_model('festival_banner', 'Deepavali banner on two poles (pole collision only)',
                link('link', ''.join(V) + ''.join(C)))


def make_house(name, wall, trim):
    V, C = [], []
    stone, oxide, roof, rib = (155, 145, 130), (140, 55, 40), (170, 80, 50), (120, 50, 35)
    wood = (95, 55, 30)
    V.append(vis('plinth', box(9.6, 8.6, 0.5), (1.0, 0, 0.25), mat(stone, 0.9)))
    V.append(vis('plinth_stripe', box(9.64, 8.64, 0.07), (1.0, 0, 0.45), mat((170, 50, 35), 0.9)))
    V.append(vis('step1', box(0.5, 2.4, 0.32), (6.05, 0, 0.16), mat(stone, 0.9)))
    V.append(vis('step2', box(0.5, 2.4, 0.16), (6.55, 0, 0.08), mat(stone, 0.9)))
    V.append(vis('body', box(7.0, 8.0, 3.2), (0, 0, 2.1), mat(wall, 0.85)))
    V.append(vis('base_band', box(7.06, 8.06, 0.45), (0, 0, 0.725), mat(oxide, 0.9)))
    V.append(vis('door_frame', box(0.12, 1.5, 2.3), (3.52, 0, 1.65), mat(trim, 0.7)))
    V.append(vis('door', box(0.08, 1.2, 2.15), (3.58, 0, 1.575), mat(wood, 0.7)))
    V.append(vis('door_knob', sph(0.03), (3.64, 0.4, 1.5), mat(BRASS, 0.3, 0.8)))
    for s, sg in (('l', -1), ('r', 1)):
        y = sg * 2.6
        V.append(vis(f'win_frame_{s}', box(0.1, 1.1, 1.2), (3.52, y, 2.1), mat(trim, 0.7)))
        V.append(vis(f'win_glow_{s}', box(0.05, 0.9, 1.0), (3.57, y, 2.1),
                     mat((255, 190, 100), 0.4, emis=(150, 95, 40)), shadow=False))
        for b in range(5):
            V.append(vis(f'win_bar_{s}{b}', box(0.03, 0.03, 1.0), (3.62, y - 0.36 + b * 0.18, 2.1),
                         mat((25, 25, 25), 0.5, 0.5)))
    for k, y in enumerate((-3.9, -1.3, 1.3, 3.9)):       # thinnai pillars
        V.append(vis(f'pillar{k}', cyl(0.1, 2.4), (5.5, y, 1.7), mat((232, 226, 210), 0.8)))
    V.append(vis('veranda_beam', box(0.15, 8.8, 0.15), (5.7, 0, 2.85), mat(wood, 0.7)))

    def slab(nm, cx, cz, length, width, thick, th):
        V.append(vis(nm, box(length, width, thick), (cx, 0, cz, 0, th, 0), mat(roof, 0.75)))
        s, k = -length / 2 + 0.25, 0
        while s < length / 2 - 0.1:
            h = thick / 2 + 0.02
            V.append(vis(f'{nm}_rib{k}', box(0.07, width, 0.04),
                         (cx + s * math.cos(th) + h * math.sin(th), 0, cz - s * math.sin(th) + h * math.cos(th),
                          0, th, 0), mat(rib, 0.8)))
            s += 0.42
            k += 1

    th = math.atan2(1.5, 4.2)
    slab('roof_front', 2.1, 4.26, 4.46, 9.0, 0.12, th)
    slab('roof_back', -2.1, 4.26, 4.46, 9.0, 0.12, -th)
    slab('veranda_roof', 4.65, 3.16, 2.335, 8.8, 0.1, 0.172)
    V.append(vis('ridge', cyl(0.12, 9.0), (0, 0, 5.02, math.pi / 2, 0, 0), mat((140, 60, 40), 0.8)))
    for k, w_ in enumerate((5.8, 3.47, 1.2)):             # stepped gable infill
        for sg in (-1, 1):
            V.append(vis(f'gable{k}_{sg}', box(w_, 0.3, 0.42), (0, sg * 3.85, 3.91 + 0.42 * k), mat(wall, 0.85)))
    # tulasi maadam in the yard
    V.append(vis('tulasi_base', box(0.6, 0.6, 0.6), (7.0, -2.8, 0.3), mat((235, 230, 220), 0.9)))
    V.append(vis('tulasi_stripe', box(0.62, 0.62, 0.1), (7.0, -2.8, 0.45), mat(oxide, 0.9)))
    V.append(vis('tulasi_top', cyl(0.22, 0.12), (7.0, -2.8, 0.66), mat((235, 230, 220), 0.9)))
    V.append(vis('tulasi_plant', sph(0.24), (7.0, -2.8, 0.95), mat((40, 130, 50), 0.9)))
    C.append(col('body', box(9.6, 8.6, 5.0), (1.0, 0, 2.5)))
    C.append(col('steps', box(1.4, 2.4, 0.3), (6.3, 0, 0.15)))
    C.append(col('tulasi', box(0.6, 0.6, 0.9), (7.0, -2.8, 0.45)))
    write_model(name, 'South Indian (Tamil) residential house: raised plinth, thinnai veranda, '
                'clay-tile gable roof, tulasi maadam. Single simplified collision box.',
                link('link', ''.join(V) + ''.join(C)))


def make_city_tower(name, facade, accent, floors):
    width, depth, floor_h = 10.0, 9.0, 2.8
    height = floors * floor_h
    V, C = [], []
    V.append(vis('structure', box(width, depth, height), (0, 0, height / 2), mat(facade, 0.75)))
    V.append(vis('roof', box(width + 0.5, depth + 0.5, 0.35),
                 (0, 0, height + 0.175), mat(accent, 0.55, 0.25)))
    V.append(vis('podium', box(width + 0.35, depth + 0.35, 0.55),
                 (0, 0, 0.275), mat(accent, 0.6, 0.15)))
    for floor in range(floors):
        z = floor * floor_h + 1.55
        for bay in range(4):
            pos = (bay - 1.5) * 2.0
            glass = (255, 190, 90) if (floor + bay) % 3 else (110, 190, 255)
            glow = tuple(int(c * 0.55) for c in glass)
            V.append(vis(f'front_window_{floor}_{bay}', box(1.05, 0.07, 1.25),
                         (pos, -depth / 2 - 0.04, z), mat(glass, 0.3, emis=glow), shadow=False))
            V.append(vis(f'back_window_{floor}_{bay}', box(1.05, 0.07, 1.25),
                         (pos, depth / 2 + 0.04, z), mat(glass, 0.3, emis=glow), shadow=False))
            V.append(vis(f'left_window_{floor}_{bay}', box(0.07, 1.05, 1.25),
                         (-width / 2 - 0.04, pos * 0.85, z), mat(glass, 0.3, emis=glow), shadow=False))
            V.append(vis(f'right_window_{floor}_{bay}', box(0.07, 1.05, 1.25),
                         (width / 2 + 0.04, pos * 0.85, z), mat(glass, 0.3, emis=glow), shadow=False))
    for x in (-width / 2 + 0.15, width / 2 - 0.15):
        V.append(vis(f'corner_{x}', box(0.22, depth + 0.1, height),
                     (x, 0, height / 2), mat(accent, 0.5, 0.2)))
    C.append(col('building_collision', box(width, depth, height), (0, 0, height / 2)))
    write_model(name, f'{floors}-storey city tower with emissive festive windows',
                link('link', ''.join(V + C)))


def emitter(name, topic, kind, size, pos, rate, life, vmin, vmax, psize, c0, c1, scale=None, emitting=False):
    s = f'<scale_rate>{scale}</scale_rate>' if scale is not None else ''
    return (f'<particle_emitter name="{name}" type="{kind}"><emitting>{str(emitting).lower()}</emitting>'
            f'<size>{size}</size><particle_size>{psize} {psize} {psize}</particle_size>'
            f'<lifetime>{life}</lifetime><min_velocity>{vmin}</min_velocity><max_velocity>{vmax}</max_velocity>'
            f'<rate>{rate}</rate>{P(pos)}<color_start>{c0}</color_start><color_end>{c1}</color_end>'
            f'{s}<topic>{topic}</topic></particle_emitter>')


def firework_body(site):
    t = f'/festival/fw/{site}'
    E = [
        emitter('rocket', f'{t}/rocket', 'box', '0.3 0.3 0.3', (0, 0, 0.6), 60, 1.5, 20, 22, 0.3,
                '1 0.9 0.5 1', '1 0.4 0.1 0'),
        emitter('smoke', f'{t}/smoke', 'box', '0.4 0.4 0.4', (0, 0, 0.6), 25, 3.5, 6, 12, 0.9,
                '0.55 0.55 0.55 0.5', '0.25 0.25 0.25 0', 0.4),
        emitter('gold', f'{t}/gold', 'ellipsoid', '1 1 1', (0, 0, 28), 350, 2.2, 5, 9, 0.35,
                '1 0.78 0.15 1', '1 0.35 0 0'),
        emitter('red', f'{t}/red', 'ellipsoid', '1 1 1', (0, 0, 28), 350, 2.2, 5, 9, 0.35,
                '1 0.1 0.1 1', '0.6 0 0 0'),
        emitter('blue', f'{t}/blue', 'ellipsoid', '1 1 1', (0, 0, 28), 350, 2.2, 5, 9, 0.35,
                '0.2 0.4 1 1', '0.05 0.1 0.6 0'),
        emitter('green', f'{t}/green', 'ellipsoid', '1 1 1', (0, 0, 28), 350, 2.2, 5, 9, 0.35,
                '0.2 1 0.3 1', '0 0.5 0.1 0'),
        emitter('sparkle', f'{t}/sparkle', 'ellipsoid', '4 4 4', (0, 0, 28), 150, 1.6, 1, 3, 0.12,
                '1 1 1 1', '1 0.8 0.3 0'),
    ]
    V = vis('tube', cyl(0.08, 0.8), (0, 0, 0.4), mat((40, 40, 45), 0.7), shadow=False)
    V += vis('sand', cyl(0.5, 0.1), (0, 0, 0.05), mat((120, 100, 70), 1.0), shadow=False)
    return link('link', V + ''.join(E))


def sparkler_body(sid):
    V = vis('stick', cyl(0.004, 0.35), (0, 0, 0.175), mat((90, 90, 95), 0.5, 0.8), shadow=False)
    V += vis('holder', cyl(0.04, 0.05), (0, 0, 0.025), mat((100, 70, 40), 0.9), shadow=False)
    E = emitter('sparks', f'/festival/sparkler/{sid}', 'ellipsoid', '0.03 0.03 0.03', (0, 0, 0.36), 120, 0.5,
                0.6, 1.8, 0.035, '1 0.85 0.4 1', '1 0.4 0.05 0', emitting=True)
    L = ('<light name="spark_light" type="point">' + P((0, 0, 0.4)) +
         '<cast_shadows>false</cast_shadows><diffuse>1 0.75 0.35 1</diffuse><specular>1 0.7 0.3 1</specular>'
         '<intensity>0.5</intensity><attenuation><range>3</range><constant>0.3</constant><linear>0.5</linear>'
         '<quadratic>0.8</quadratic></attenuation></light>')
    return link('link', V + E + L)


# Ogre particle emitters spray along their local +X, so fountains pitch the emitter by -90 deg (X -> up).
UP = (0, -math.pi / 2, 0)


def glow(name, z, rgb, intensity, rng):
    return (f'<light name="{name}" type="point">' + P((0, 0, z)) +
            f'<cast_shadows>false</cast_shadows><diffuse>{rgb} 1</diffuse><specular>{rgb} 1</specular>'
            f'<intensity>{intensity}</intensity><attenuation><range>{rng}</range><constant>0.3</constant>'
            '<linear>0.4</linear><quadratic>0.5</quadratic></attenuation></light>')


def flower_pot_body(cid, c0='1 0.9 0.55 1', c1='1 0.45 0.05 0'):
    """Anar / flower pot: clay pot with a continuous golden fountain, topic /festival/cracker/<cid>."""
    V = vis('pot', cyl(0.075, 0.16), (0, 0, 0.08), mat((170, 85, 40), 0.9), shadow=False)
    V += vis('band', cyl(0.077, 0.03), (0, 0, 0.09), mat((40, 120, 60), 0.6), shadow=False)
    V += vis('neck', cyl(0.035, 0.05), (0, 0, 0.185), mat((150, 70, 35), 0.9), shadow=False)
    E = emitter('fountain', f'/festival/cracker/{cid}', 'box', '0.02 0.02 0.02', (0, 0, 0.21) + UP, 220, 0.9,
                2.5, 4.5, 0.03, c0, c1, emitting=True)
    return link('link', V + E + glow('pot_light', 0.6, '1 0.75 0.35', 0.8, 4))


def cracker_cake_body(cid):
    """Multi-shot 'sky shot' box: 3x3 tubes in a gift-wrapped crate, colourful sparks spurting up."""
    V = vis('crate', box(0.36, 0.36, 0.24), (0, 0, 0.12), mat((200, 30, 40), 0.6), shadow=False)
    V += vis('ribbon_x', box(0.37, 0.05, 0.245), (0, 0, 0.12), mat((240, 190, 40), 0.4, 0.3), shadow=False)
    V += vis('ribbon_y', box(0.05, 0.37, 0.245), (0, 0, 0.12), mat((240, 190, 40), 0.4, 0.3), shadow=False)
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            V += vis(f'tube{i}{j}'.replace('-', 'm'), cyl(0.035, 0.04), (i * 0.11, j * 0.11, 0.25),
                     mat((30, 30, 35), 0.8), shadow=False)
    E = emitter('shots', f'/festival/cracker/{cid}', 'box', '0.25 0.25 0.02', (0, 0, 0.28) + UP, 90, 1.4,
                5, 8, 0.06, '1 0.2 0.6 1', '0.3 0.6 1 0', emitting=True)
    return link('link', V + E + glow('cake_light', 0.8, '1 0.4 0.7', 0.7, 5))


def rocket_bottle_body():
    """Glass bottle holding three unlit rockets (visual only)."""
    V = vis('bottle', cyl(0.045, 0.22), (0, 0, 0.11), mat((60, 140, 80), 0.1, 0.0, alpha=0.6), shadow=False)
    V += vis('bottle_neck', cyl(0.02, 0.06), (0, 0, 0.25), mat((60, 140, 80), 0.1, 0.0, alpha=0.6), shadow=False)
    for k, (dx, dy, rgb) in enumerate(((0.012, 0.0, (220, 40, 40)), (-0.008, 0.01, (40, 90, 220)),
                                       (-0.008, -0.01, (240, 180, 30)))):
        V += vis(f'stick{k}', cyl(0.003, 0.5), (dx, dy, 0.3), mat((180, 150, 100), 0.9), shadow=False)
        V += vis(f'rocket{k}', cyl(0.014, 0.12), (dx, dy, 0.6), mat(rgb, 0.6), shadow=False)
        V += vis(f'tip{k}', sph(0.014), (dx, dy, 0.66), mat(rgb, 0.6), shadow=False)
    return link('link', V)


def cracker_string_body(n=24, pitch=0.05):
    """Ladi / saram: a fuse cord threaded with red crackers, laid out along local X (visual only)."""
    L = (n - 1) * pitch
    V = vis('fuse', box(L + 0.1, 0.006, 0.006), (0, 0, 0.012), mat((70, 60, 40), 0.9), shadow=False)
    for k in range(n):
        side = 1 if k % 2 else -1
        x = -L / 2 + k * pitch
        V += vis(f'c{k}', cyl(0.009, 0.05), (x, side * 0.022, 0.012, math.pi / 2, 0, 0),
                 mat((210, 30, 30) if k % 3 else (40, 150, 60), 0.6), shadow=False)
    return link('link', V)


def build_models():
    make_diya('diya', True)
    make_diya('diya_visual_only', False)
    write_png(MODELS / 'rangoli/materials/textures/rangoli_mandala.png', 384, 384, rangoli_px)
    write_png(MODELS / 'rangoli/materials/textures/kolam_white.png', 384, 384, kolam_px)
    make_rangoli('rangoli', 'rangoli_mandala.png', 1.6, rangoli_px)
    make_rangoli('kolam', 'kolam_white.png', 1.6, kolam_px)
    make_rangoli('kolam_small', 'kolam_white.png', 1.0, kolam_px)
    write_png(MODELS / 'festival_banner/materials/textures/banner.png', 512, 128, banner_px)
    make_banner()
    make_led_string('led_string_9m', 9.0, 36, 0.55)
    make_led_string('led_string_4m', 4.0, 16, 0.25)
    make_garland('marigold_garland', 4.0, 36, 0.25)
    make_toran('toran')
    make_streetlight()
    for nm, wall, trim in (('tamil_house', (240, 225, 190), (230, 215, 190)),
                           ('tamil_house_teal', (110, 190, 185), (235, 230, 215)),
                           ('tamil_house_pink', (230, 150, 170), (235, 230, 215)),
                           ('tamil_house_yellow', (240, 200, 90), (235, 225, 200))):
        make_house(nm, wall, trim)
    for nm, facade, accent, floors in (
            ('city_tower_blue', (45, 70, 105), (230, 130, 35), 6),
            ('city_tower_teal', (45, 105, 105), (255, 170, 45), 5),
            ('city_tower_rose', (110, 65, 85), (255, 190, 70), 4)):
        make_city_tower(nm, facade, accent, floors)
    # single reusable firework site (world uses per-site inline copies with their own topics)
    write_model('firework_site', 'Visual-only firework launch site: particle emitters controlled via '
                '/festival/fw/demo/EMITTER (gz.msgs.ParticleEmitter)', firework_body('demo'))
    write_model('sparkler', 'Visual-only sparkler (particle emitter + small light), topic '
                '/festival/sparkler/demo', sparkler_body('demo'))
    write_model('flower_pot', 'Anar / flower pot cracker with a golden fountain, topic /festival/cracker/demo',
                flower_pot_body('demo'))
    write_model('cracker_cake', 'Multi-shot cracker box with colourful sparks, topic /festival/cracker/demo_cake',
                cracker_cake_body('demo_cake'))
    write_model('rocket_bottle', 'Bottle holding three unlit rockets (visual only)', rocket_bottle_body())
    write_model('cracker_string', 'Ladi / saram string of red crackers (visual only)', cracker_string_body())


# ----------------------------------------------------------------------------
# World
# ----------------------------------------------------------------------------
def xf(hx, hy, yaw, lx, ly):
    c, s = math.cos(yaw), math.sin(yaw)
    return hx + lx * c - ly * s, hy + lx * s + ly * c


def rect_local(hx, hy, yaw, x0, y0, x1, y1):
    pts = [xf(hx, hy, yaw, a, b) for a in (x0, x1) for b in (y0, y1)]
    OBST.append((min(p[0] for p in pts), min(p[1] for p in pts), max(p[0] for p in pts), max(p[1] for p in pts)))


def street_base():
    V, C = [], []
    V.append(vis('ground', box(140, 140, 0.1), (0, 0, -0.05), mat((58, 48, 38), 0.98), shadow=False))
    C.append(col('ground', box(140, 140, 0.1), (0, 0, -0.05)))
    V.append(vis('road', box(2 * STREET_X, 2 * ROAD_HALF, 0.02), (0, 0, 0.01), mat((38, 38, 42), 0.95)))
    C.append(col('road', box(2 * STREET_X, 2 * ROAD_HALF, 0.02), (0, 0, 0.01)))
    for sg in (-1, 1):
        yc = sg * (ROAD_HALF + SIDEWALK_OUT) / 2
        V.append(vis(f'sidewalk{sg}', box(2 * STREET_X, SIDEWALK_OUT - ROAD_HALF, 0.15), (0, yc, 0.075), mat((150, 148, 142), 0.9)))
        C.append(col(f'sidewalk{sg}', box(2 * STREET_X, SIDEWALK_OUT - ROAD_HALF, 0.15), (0, yc, 0.075)))
        V.append(vis(f'edge_line{sg}', box(2 * STREET_X, 0.1, 0.003), (0, sg * 3.2, 0.0215), mat((235, 235, 225), 0.8), shadow=False))
    for k in range(-12, 13):
        V.append(vis(f'dash{k}', box(2.0, 0.12, 0.003), (k * 4.0, 0, 0.0215), mat((240, 220, 90), 0.8), shadow=False))
    for sg in (-1, 1):                                   # end-of-street barricades
        x = sg * STREET_X
        C.append(col(f'barricade{sg}', box(0.4, 2 * WALL_Y + 0.2, 1.0), (x, 0, 0.5)))
        n = 7
        wd = (2 * WALL_Y) / n
        for k in range(n):
            c = (205, 40, 40) if k % 2 == 0 else (240, 240, 235)
            V.append(vis(f'barr{sg}_{k}', box(0.4, wd, 0.5), (x, -WALL_Y + wd * (k + 0.5), 0.75), mat(c, 0.8)))
            V.append(vis(f'barrl{sg}_{k}', box(0.4, wd, 0.5), (x, -WALL_Y + wd * (k + 0.5), 0.25), mat((60, 60, 60), 0.9)))
        OBST.append((x - 0.2, -WALL_Y - 0.1, x + 0.2, WALL_Y + 0.1))
    return V, C


def compound_walls():
    V, C = [], []
    n = 0
    cream, oxide = (235, 225, 200), (150, 60, 40)
    for sg in (-1, 1):
        cur = -STREET_X + 0.2
        gaps = sorted((hx - 1.6, hx + 1.6) for hx in HOUSE_X)
        segs = []
        for g0, g1 in gaps:
            segs.append((cur, g0))
            cur = g1
        segs.append((cur, STREET_X - 0.2))
        for a, b in segs:
            ln, cx, y = b - a, (a + b) / 2, sg * WALL_Y
            V.append(vis(f'wall{n}', box(ln, 0.25, 1.3), (cx, y, 0.65), mat(cream, 0.9)))
            V.append(vis(f'band{n}', box(ln, 0.27, 0.3), (cx, y, 0.15), mat(oxide, 0.9)))
            V.append(vis(f'cap{n}', box(ln, 0.35, 0.08), (cx, y, 1.34), mat((200, 190, 170), 0.9)))
            C.append(col(f'wall{n}', box(ln, 0.25, 1.4), (cx, y, 0.7)))
            OBST.append((a, y - 0.15, b, y + 0.15))
            n += 1
        for hx in HOUSE_X:
            y = sg * WALL_Y
            for s2 in (-1, 1):
                px = hx + s2 * 1.75
                V.append(vis(f'gp{n}', box(0.5, 0.5, 2.0), (px, y, 1.0), mat(cream, 0.9)))
                V.append(vis(f'gpc{n}', box(0.62, 0.62, 0.1), (px, y, 2.05), mat((200, 190, 170), 0.9)))
                C.append(col(f'gp{n}', box(0.5, 0.5, 2.1), (px, y, 1.05)))
                OBST.append((px - 0.3, y - 0.3, px + 0.3, y + 0.3))
                lx = hx + s2 * 1.5
                V.append(vis(f'leaf{n}', box(0.06, 1.5, 1.2), (lx, y + sg * 0.85, 0.9), mat((30, 30, 32), 0.5, 0.6)))
                C.append(col(f'leaf{n}', box(0.06, 1.5, 1.2), (lx, y + sg * 0.85, 0.9)))
                OBST.append((lx - 0.05, min(y, y + sg * 1.6), lx + 0.05, max(y, y + sg * 1.6)))
                n += 1
    return V, C


def build_world():
    inc, lights = [], []
    inline = []
    cnt = {}

    def include(model, base, x, y, z=0.0, yaw=0.0):
        cnt[base] = cnt.get(base, 0) + 1
        inc.append(f'<include><uri>model://{model}</uri><name>{base}_{cnt[base]}</name>{P((x, y, z, 0, 0, yaw))}</include>')

    variants = ['tamil_house', 'tamil_house_teal', 'tamil_house_pink', 'tamil_house_yellow']
    for sg in (1, -1):
        hy, hyaw = sg * HOUSE_Y, -sg * math.pi / 2
        for i, hx in enumerate(HOUSE_X):
            v = variants[(i + (0 if sg > 0 else 2)) % 4]

            def L(lx, ly, lz=0.0, lyaw=0.0):
                wx, wy = xf(hx, hy, hyaw, lx, ly)
                return wx, wy, lz, hyaw + lyaw

            include(v, 'house', hx, hy, 0.0, hyaw)
            rect_local(hx, hy, hyaw, -3.8, -4.3, 5.8, 4.3)
            rect_local(hx, hy, hyaw, 5.8, -1.2, 6.8, 1.2)
            rect_local(hx, hy, hyaw, 6.7, -3.1, 7.3, -2.5)
            include('rangoli' if i % 2 == 0 else 'kolam', 'rangoli', *L(7.6, 0.0, 0.0))
            include('kolam_small', 'kolam', *L(4.5, 0.0, 0.5))
            for k in range(8):                                   # ring of diyas around the rangoli
                a = k * math.pi / 4
                include('diya_visual_only', 'diya_ring', *L(7.6 + math.cos(a), math.sin(a), 0.0, a))
            for y in (-3.3, -2.65, -2.0, 2.0, 2.65, 3.3):
                include('diya_visual_only', 'diya_veranda', *L(5.2, y, 0.5))
            for y in (-0.65, 0.65):                              # only these emit real light
                include('diya', 'diya_lit', *L(5.2, y, 0.5))
            for y in (-2.1, 2.1):
                include('marigold_garland', 'garland', *L(5.65, y, 2.85, math.pi / 2))
                include('led_string_4m', 'led4', *L(5.72, y, 2.6, math.pi / 2))
            include('toran', 'toran', *L(3.62, 0.0, 2.72, math.pi / 2))
    # gate-pillar and wall-top diyas (visual only)
    for sg in (1, -1):
        for hx in HOUSE_X:
            for s2 in (-1, 1):
                include('diya_visual_only', 'diya_gate', hx + s2 * 1.75, sg * WALL_Y, 2.1)
        for x in range(-28, 29, 4):
            if all(abs(x - hx) > 2.4 for hx in HOUSE_X):
                include('diya_visual_only', 'diya_wall', float(x), sg * WALL_Y, 1.38)
    # streetlights + LED strings across the street + banners
    for x in POLE_X:
        for sg in (1, -1):
            include('streetlight', 'streetlight', x, sg * POLE_Y, 0.0, -sg * math.pi / 2)
            OBST.append((x - 0.2, sg * POLE_Y - 0.2, x + 0.2, sg * POLE_Y + 0.2))
        include('led_string_9m', 'led_across', x, 0.0, 5.3, math.pi / 2)
    for x in (-18.0, 18.0):
        include('festival_banner', 'banner', x, 0.0, 0.0, math.pi / 2)
        for sg in (-1, 1):
            OBST.append((x - 0.15, sg * 4.8 - 0.15, x + 0.15, sg * 4.8 + 0.15))
    # Parallel city boulevards and their pavements extend the festival district beyond the old street.
    city_v, city_c = [], []
    for road_index, road_y in enumerate((-27.0, 27.0)):
        city_v.append(vis(f'boulevard{road_index}', box(2 * STREET_X, 6.0, 0.03),
                          (0, road_y, 0.015), mat((42, 44, 49), 0.95)))
        city_c.append(col(f'boulevard{road_index}', box(2 * STREET_X, 6.0, 0.03),
                          (0, road_y, 0.015)))
        for side in (-1, 1):
            pavement_y = road_y + side * 4.0
            city_v.append(vis(f'pavement{road_index}_{side}', box(2 * STREET_X, 2.0, 0.14),
                              (0, pavement_y, 0.07), mat((145, 145, 140), 0.9)))
            city_c.append(col(f'pavement{road_index}_{side}', box(2 * STREET_X, 2.0, 0.14),
                              (0, pavement_y, 0.07)))
        for dash_x in range(-48, 49, 8):
            city_v.append(vis(f'lane{road_index}_{dash_x}', box(3.0, 0.12, 0.004),
                              (float(dash_x), road_y, 0.034), mat((240, 220, 90), 0.8), shadow=False))
    inline.append('<model name="city_boulevards"><static>true</static>' +
                  link('link', ''.join(city_v + city_c)) + '</model>')
    tower_models = ('city_tower_blue', 'city_tower_teal', 'city_tower_rose')
    for side_index, tower_y in enumerate(CITY_TOWER_Y):
        for tower_index, tower_x in enumerate(CITY_TOWER_X):
            tower = tower_models[(tower_index + side_index) % len(tower_models)]
            include(tower, 'city_tower', tower_x, tower_y)
            OBST.append((tower_x - 5.0, tower_y - 4.5, tower_x + 5.0, tower_y + 4.5))
    # Persistent sparkler/cracker props glow along both city boulevards.
    for sid, (x, y) in enumerate((
            (x, side * 31.0) for side in (-1, 1) for x in (-40.0, -27.0, 27.0, 40.0)), start=4):
        inline.append(f'<model name="city_cracker_sp{sid}"><static>true</static>'
                      f'{P((x, y, 0))}{sparkler_body(f"sp{sid}")}</model>')
    # Ground crackers along both main-street sidewalks: alternating flower-pot and multi-shot-box groups,
    # each with a rocket bottle and a ladi string. Visual only, but pots/boxes/bottles reach the LiDAR plane,
    # so their footprints go into the Nav2 map.
    cid = 0
    for sg in (1, -1):
        for k, x in enumerate((-21.0, -15.0, -9.0, -3.0, 3.0, 9.0, 15.0, 21.0)):
            y = sg * 4.0
            if (k + (sg < 0)) % 2 == 0:
                silver = cid % 4 == 2
                body = flower_pot_body(f'cp{cid}', *(('0.85 0.9 1 1', '0.5 0.6 1 0') if silver else ()))
                inline.append(f'<model name="flower_pot_cp{cid}"><static>true</static>{P((x, y, 0.15))}{body}</model>')
            else:
                inline.append(f'<model name="cracker_cake_cp{cid}"><static>true</static>'
                              f'{P((x, y, 0.15, 0, 0, 0.3))}{cracker_cake_body(f"cp{cid}")}</model>')
            cid += 1
            OBST.append((x - 0.25, y - 0.25, x + 0.25, y + 0.25))
            OBST.append((x + 0.4, sg * 4.6 - 0.05, x + 0.5, sg * 4.6 + 0.05))
            include('rocket_bottle', 'rocket_bottle', x + 0.45, sg * 4.6, 0.15)
            include('cracker_string', 'cracker_string', x + 1.4, sg * 4.1, 0.15, sg * 0.2)
    # inline firework sites + sparklers (each needs unique topic names)
    for site, (x, y) in FW_SITES.items():
        inline.append(f'<model name="{site}"><static>true</static>{P((x, y, 0))}{firework_body(site)}</model>')
    spark_pos = []
    for sid, (hx, sg, lx, ly) in enumerate([(-18.0, 1, 7.9, 1.3), (6.0, 1, 7.9, -1.3),
                                           (-6.0, -1, 7.9, 1.3), (18.0, -1, 7.9, -1.3)]):
        hy, hyaw = sg * HOUSE_Y, -sg * math.pi / 2
        wx, wy = xf(hx, hy, hyaw, lx, ly)
        inline.append(f'<model name="sparkler_sp{sid}"><static>true</static>{P((wx, wy, 0))}{sparkler_body(f"sp{sid}")}</model>')
    # base street + walls
    V, C = street_base()
    V2, C2 = compound_walls()
    inline.append('<model name="street_base"><static>true</static>' + link('link', ''.join(V + C)) + '</model>')
    inline.append('<model name="compound_walls"><static>true</static>' + link('link', ''.join(V2 + C2)) + '</model>')
    # sky: stars + moon (emissive visuals only; the directional light below does the lighting)
    stars = []
    for k in range(240):
        az, el = rnd.uniform(0, 2 * math.pi), rnd.uniform(math.radians(8), math.radians(88))
        R = 320.0
        c = rnd.choice([(255, 255, 255), (200, 220, 255), (255, 235, 200)])
        stars.append(vis(f's{k}', sph(rnd.uniform(0.35, 0.8)),
                         (R * math.cos(el) * math.cos(az), R * math.cos(el) * math.sin(az), R * math.sin(el)),
                         mat((20, 20, 20), 1.0, emis=c), shadow=False))
    maz, mel = 2.2, 0.8
    mpos = (320 * math.cos(mel) * math.cos(maz), 320 * math.cos(mel) * math.sin(maz), 320 * math.sin(mel))
    stars.append(vis('moon', sph(9.0), mpos, mat((30, 30, 30), 1.0, emis=(235, 238, 255)), shadow=False))
    inline.append('<model name="night_sky"><static>true</static>' + link('link', ''.join(stars)) + '</model>')
    n = math.sqrt(sum(c * c for c in mpos))
    mdir = ' '.join(f'{-c / n:.4f}' for c in mpos)
    # controllable world-level lights (names are what /festival/lighting adjusts via /world/<w>/light_config)
    yaml = ['# generated by diwali_sim/scripts/generate_assets.py', 'lights:']
    wl = []
    for k, x in enumerate(POLE_X):
        nm = f'string_light_{k}'
        wl.append(f'<light name="{nm}" type="point">{P((x, 0, 5.0))}<cast_shadows>false</cast_shadows>'
                  '<diffuse>1 0.72 0.35 1</diffuse><specular>1 0.7 0.35 1</specular><intensity>1.0</intensity>'
                  '<attenuation><range>16</range><constant>0.4</constant><linear>0.06</linear>'
                  '<quadratic>0.01</quadratic></attenuation></light>')
        yaml += [f'  - name: {nm}', f'    pose: [{x}, 0.0, 5.0, 0.0, 0.0, 0.0]', '    diffuse: [1.0, 0.72, 0.35]',
                 '    range: 16.0', '    attenuation: [0.4, 0.06, 0.01]', '    base_intensity: 1.0']
    write(CONFIG / 'festival_lights.yaml', '\n'.join(yaml) + '\n')

    plugins = ''.join(
        f'<plugin filename="{f}" name="{n_}">{extra}</plugin>' for f, n_, extra in [
            ('gz-sim-physics-system', 'gz::sim::systems::Physics', ''),
            ('gz-sim-user-commands-system', 'gz::sim::systems::UserCommands', ''),
            ('gz-sim-scene-broadcaster-system', 'gz::sim::systems::SceneBroadcaster', ''),
            ('gz-sim-sensors-system', 'gz::sim::systems::Sensors', '<render_engine>ogre2</render_engine>'),
            ('gz-sim-particle-emitter-system', 'gz::sim::systems::ParticleEmitter', '')])
    world = (f'<sdf version="1.9"><world name="{WORLD}">'
             '<physics name="default_physics" type="dart"><max_step_size>0.004</max_step_size>'
             '<real_time_factor>1.0</real_time_factor></physics>' + plugins +
             '<gravity>0 0 -9.8</gravity>'
             '<scene><ambient>0.07 0.08 0.14 1</ambient><background>0.005 0.007 0.02 1</background>'
             '<shadows>true</shadows><grid>false</grid></scene>'
             '<light name="moon" type="directional"><cast_shadows>true</cast_shadows>' + P((0, 0, 50)) +
             f'<diffuse>0.35 0.42 0.7 1</diffuse><specular>0.1 0.12 0.2 1</specular><intensity>0.5</intensity>'
             f'<direction>{mdir}</direction></light>' + ''.join(wl) + ''.join(inline) + ''.join(inc) +
             '</world></sdf>')
    write(WORLDS / 'diwali_street.sdf', pretty(world))
    return len(inc)


# ----------------------------------------------------------------------------
# Map for Nav2 (rasterised from the same geometry as the world)
# ----------------------------------------------------------------------------
def write_map():
    res, ox, oy, wm, hm = 0.05, -54.0, -54.0, 108.0, 108.0
    Wd, Ht = int(wm / res), int(hm / res)
    img = bytearray([254]) * (Wd * Ht)

    def fill(x0, y0, x1, y1, val):
        j0, j1 = max(0, int((x0 - ox) / res)), min(Wd, int(math.ceil((x1 - ox) / res)))
        i0, i1 = max(0, int((oy + hm - y1) / res)), min(Ht, int(math.ceil((oy + hm - y0) / res)))
        for i in range(i0, i1):
            img[i * Wd + j0:i * Wd + j1] = bytes([val]) * max(0, j1 - j0)

    for r in OBST:
        fill(*r, 0)
    MAPS.mkdir(parents=True, exist_ok=True)
    (MAPS / 'diwali_street.pgm').write_bytes(f'P5\n{Wd} {Ht}\n255\n'.encode() + bytes(img))
    write(MAPS / 'diwali_street.yaml',
          'image: diwali_street.pgm\nmode: trinary\nresolution: 0.05\n'
          f'origin: [{ox}, {oy}, 0.0]\nnegate: 0\noccupied_thresh: 0.65\nfree_thresh: 0.25\n')


# ----------------------------------------------------------------------------
# Sounds (synthetic, so no third-party audio is needed)
# ----------------------------------------------------------------------------
def save_wav(name, samples, sr=22050):
    SOUNDS.mkdir(parents=True, exist_ok=True)
    with wave.open(str(SOUNDS / name), 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(b''.join(struct.pack('<h', int(max(-1, min(1, s)) * 30000)) for s in samples))


def build_sounds():
    sr = 22050
    d = 1.4
    ph, out = 0.0, []
    for i in range(int(sr * d)):                      # rising whistle
        t = i / sr
        ph += 2 * math.pi * (500 + 1300 * t / d) / sr
        out.append(0.35 * math.sin(ph) * (1 - t / d) + rnd.uniform(-0.03, 0.03))
    save_wav('firework_launch.wav', out)
    out = []
    for i in range(int(sr * 2.0)):                    # burst: noise + thump
        t = i / sr
        out.append(0.9 * rnd.uniform(-1, 1) * math.exp(-t * 3.2) + 0.6 * math.sin(2 * math.pi * 55 * t) * math.exp(-t * 5))
    save_wav('firework_burst.wav', out)
    out = [0.0] * int(sr * 1.8)
    for _ in range(70):                               # crackle: sparse clicks, thinning out
        p = int((rnd.random() ** 1.6) * (len(out) - 400))
        amp = rnd.uniform(0.3, 0.9)
        for k in range(rnd.randint(30, 90)):
            out[p + k] += amp * rnd.uniform(-1, 1) * math.exp(-k / 18.0)
    save_wav('firework_crackle.wav', out)
    out = []
    for i in range(int(sr * 3.5)):                    # temple-bell-like partials
        t = i / sr
        out.append(sum(a * math.sin(2 * math.pi * f * t) * math.exp(-t * dcy) for f, a, dcy in
                       ((523, 0.4, 1.2), (1318, 0.25, 1.8), (1580, 0.2, 2.2), (2150, 0.1, 3.0))))
    save_wav('temple_bell.wav', out)


if __name__ == '__main__':
    build_models()
    n = build_world()
    write_map()
    build_sounds()
    print(f'world includes: {n}, obstacle rects: {len(OBST)}')
