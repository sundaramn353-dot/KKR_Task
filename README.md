# South Indian Diwali city simulation — ROS 2 Jazzy + Gazebo Harmonic (Ubuntu 24.04)

**Status: generated and statically checked only** (XML well-formedness, Python byte-compile, YAML parse, offline
unit-style test of the festival sequencing logic). It has **not** been launched in Gazebo/ROS here — see
"Unverified items" before relying on it.

## Packages
| package | build type | role |
|---|---|---|
| `diwali_sim` | ament_cmake (resources only) | Diwali city world (legacy internal name `diwali_street.sdf`), illuminated city towers, boulevards, cracker/sparkler props, textures, launch files, asset generator |
| `diwali_festival` | ament_python | `festival_manager` node + `fireworks_controller`, `lighting_controller`, `sound_controller`, `gz_interface` |
| `diwali_robot` | ament_cmake (resources only) | xacro diff-drive robot + LiDAR, bridge yaml, SLAM Toolbox + Nav2 config, pre-generated map |
| `diwali_interfaces` | ament_cmake (rosidl) | one message, `FestivalStatus` (everything else is std_msgs / std_srvs) |

No package compiles C++: fireworks use Gazebo's own `ParticleEmitter` system, so no custom plugin or
`GZ_SIM_SYSTEM_PLUGIN_PATH` is needed (`diwali_sim/plugins/README.md` explains when you would add one).

## Install
```bash
sudo apt update
# Stages 1-3 (world, festival, robot)
sudo apt install ros-jazzy-ros-gz ros-jazzy-xacro ros-jazzy-robot-state-publisher ros-jazzy-rviz2 \
                 python3-yaml pulseaudio-utils            # or alsa-utils / ffmpeg for sound
# Optional: Python Gazebo Transport bindings (otherwise the `gz` CLI fallback is used, slower)
sudo apt install python3-gz-transport13 python3-gz-msgs10   # check: apt-cache policy python3-gz-transport13
# Stage 4-5 only (mapping + navigation)
sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup ros-jazzy-slam-toolbox
sudo apt install ros-jazzy-teleop-twist-keyboard  # keyboard control for the AMR
```
## Build
```bash
mkdir -p ~/diwali_ros2_ws && cp -r src ~/diwali_ros2_ws/ && cd ~/diwali_ros2_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y        # add --skip-keys "slam_toolbox nav2_bringup nav2_map_server" for stages 1-3
colcon build --symlink-install
source install/setup.bash
```
## Run
```bash
ros2 launch diwali_sim diwali_world.launch.py                       # 1. world only
ros2 launch diwali_sim diwali_world.launch.py festival:=true        # 2. + festival manager (Mode A autonomous)
ros2 launch diwali_sim diwali_world.launch.py festival:=true autonomous:=false   # Mode B only
ros2 launch diwali_sim diwali_robot.launch.py festival:=true        # 3. + robot
ros2 launch diwali_sim full_diwali_sim.launch.py                    # 4. everything + Nav2 (map included)
ros2 launch diwali_sim full_diwali_sim.launch.py mode:=slam         #    mapping instead of Nav2
```
Options: `headless:=true` (server only), `sound:=false`, `rviz:=false`, `x:= y:= yaw:=` (robot spawn).

### City + AMR driving
The city scene includes a longer main road, parallel boulevards, illuminated high-rises, and always-glowing
sparkler/cracker props. The differential-drive AMR with LiDAR is spawned in the middle of the main road at `x=0`,
`y=0`. Launch Gazebo, the AMR, and the festival manager (for occasional fireworks) together:

```bash
ros2 launch diwali_sim diwali_robot.launch.py festival:=true sound:=false
```

In a second terminal, source ROS and the workspace, then run keyboard teleoperation:

```bash
source /opt/ros/jazzy/setup.bash
source ~/Downloads/whatsapp/diwali_ros2_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use the keys printed by teleop in its terminal; press `Ctrl+C` there to stop driving. For an immediate
firework burst while the festival manager is running, publish to `/festival/fireworks` using the example
in the Festival interface section below.

## Festival interface
| topic / service | type | QoS | notes |
|---|---|---|---|
| `/festival/fireworks` | `std_msgs/String` | reliable, volatile, depth 10 | `<effect>[@<site>]`: `rocket golden_burst red_burst blue_burst green_burst sparkle finale sparkler_on sparkler_off stop random`; sites `fw_n1 fw_n2 fw_s1 fw_s2` |
| `/festival/lighting` | `std_msgs/String` | same | `on off dim bright twinkle festive` |
| `/festival/sound` | `std_msgs/String` | same | `firework_launch firework_burst firework_crackle temple_bell` |
| `/festival/event_status` | `diwali_interfaces/FestivalStatus` | reliable, transient_local, depth 1 | 1 Hz + on every event |
| `/festival/set_autonomous` `enable_fireworks` `enable_lighting` `enable_sound` | `std_srvs/SetBool` | services | runtime switches |

```bash
ros2 topic pub --once /festival/fireworks std_msgs/msg/String "{data: 'golden_burst'}"
ros2 topic pub --once /festival/fireworks std_msgs/msg/String "{data: 'finale'}"
ros2 topic pub --once /festival/lighting  std_msgs/msg/String "{data: 'twinkle'}"
ros2 service call /festival/set_autonomous std_srvs/srv/SetBool "{data: false}"
ros2 topic echo /festival/event_status --once
```
Excess triggering is limited by a per-minute cap (`max_events_per_minute`, default 6), per-site busy
checks and a 25–50 s autonomous interval. Every rejected event is reported in `event_status.last_event`.

### How the ROS→Gazebo link works
`ros_gz_bridge` has no mapping for `gz.msgs.ParticleEmitter` or light commands, so `gz_interface.py`
talks Gazebo Transport directly: it publishes `gz.msgs.ParticleEmitter {emitting}` on
`/festival/fw/<site>/<emitter>` and calls the UserCommands service `/world/diwali_street/light_config`.
Test without ROS: `gz topic -t /festival/fw/fw_n1/gold -m gz.msgs.ParticleEmitter -p 'emitting: {data: true}'`.

## Lighting concepts used
- **Emissive material**: the surface itself glows; it casts no light on neighbours (diya flames, LED bulbs, lit windows).
- **Point light**: omnidirectional, falls off with `attenuation` (only 2 lit diyas per house, plus 5 string lights).
- **Spot light**: cone (streetlights). **Directional light**: parallel rays, sun/moon (`moon`, bluish, shadows).
- **Ambient**: uniform fill from `<scene><ambient>`, kept low for night.
Light counts are deliberately limited for frame rate; most diyas use `diya_visual_only`.

## Fireworks: what is and is not real
Particle emitters are continuous, not an explosion simulator. A shell is approximated by a rocket/smoke stream
(~1.5 s) followed by a 0.4 s pulse of an ellipsoid emitter at 28 m (gold/red/blue/green) plus sparkles. Sparklers are
always-on point emitters (`/festival/sparkler/sp0..sp3`). Visual only, no physics.

## Mapping and navigation
```bash
ros2 launch diwali_sim full_diwali_sim.launch.py mode:=slam
ros2 run teleop_twist_keyboard teleop_twist_keyboard        # drive the road, then yards visible through gates
mkdir -p ~/diwali_ros2_ws/src/diwali_robot/maps
ros2 run nav2_map_server map_saver_cli -f ~/diwali_ros2_ws/src/diwali_robot/maps/my_street
ros2 launch diwali_sim full_diwali_sim.launch.py map:=$HOME/diwali_ros2_ws/src/diwali_robot/maps/my_street.yaml
```
A map rasterised from the world geometry (`maps/diwali_street.yaml`) is included so Nav2 works without mapping.
Frames: `map → odom` (AMCL/SLAM), `odom → base_footprint` (Gazebo DiffDrive via `/tf`), the rest from
`robot_state_publisher` (`/tf_static`, `/joint_states`). Spawn pose (0, 0) matches AMCL `initial_pose`.
**LiDAR note:** `gpu_lidar` is rendering-based and sees visuals, not just collisions. Decorations are kept off the
0.30 m scan plane near the road; yard items behind walls may still appear through gates.

## Regenerating assets
`python3 src/diwali_sim/scripts/generate_assets.py` rewrites models, textures, world, lights yaml, map and WAVs.

## Unverified items (check these first)
1. Never launched here: run `gz sdf --check src/diwali_sim/worlds/diwali_street.sdf` (needs `GZ_SIM_RESOURCE_PATH` for includes) and `xacro` + `gz sdf -p` on the robot.
2. **Emitter direction/shape**: I could not confirm how Ogre2 orients `box`/`ellipsoid` emitters. If bursts are not spherical or the rocket stream is not vertical, adjust emitter `<pose>` rotation or `type` in `generate_assets.py: firework_body`. Size/velocity values are starting points.
3. Python binding names `gz.transport13` / `gz.msgs10` and the `<topic>` element of `<particle_emitter>` should be confirmed on your install; `force_gz_cli:=true` bypasses the bindings.
4. `Light` message handling in `/light_config` (full message is sent each time); confirm lights change with `/festival/lighting dim`.
5. Nav2 yaml is Jazzy-style but unrun; diff against `nav2_bringup/params/nav2_params.yaml` if a node rejects a parameter.
6. Sounds are synthetic, played on the host (not spatial, not captured by Gazebo). No external assets or downloads are used.
7. ~240 includes and ~15 lights: lower `diya` counts or lights if the frame rate is poor.
