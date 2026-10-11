# keep_in_mind

Reusable ideas, patterns and gotchas worth carrying into the cuboid sorter — the things
worth taking from a course *without* necessarily running it.

Not a narrative (that's `A_new_beginning.md`) and not hardware facts
(that's `HARDWARE.md`). This is: **techniques to reuse, traps to avoid.**

Started 2026-08-26.

---

## Design patterns to copy into my own nodes

### The `/JoyState` manual-override pattern
A single global `Bool` answering "who is allowed to drive?" — exactly one of {human with
handle} or {autonomous node}. Five lines, and it buys a **physical kill switch** for an
autonomous robot, which is worth a lot while testing.

```python
from std_msgs.msg import Bool

self.Joy_active = False
self.create_subscription(Bool, '/JoyState', self.joy_state_cb, 1)

def joy_state_cb(self, msg):
    self.Joy_active = msg.data

# wherever cmd_vel is published:
if self.Joy_active:
    self.pub_cmdVel.publish(Twist())   # stop and yield to the human
    return
```

**Toggle with R2** (button index 9 on my DragonRise handle).

Two traps:
- It **toggles**, it doesn't set — nothing can query the current mode.
- Subscription is depth-1 volatile, so **a node started later never learns the current
  state**. Start a node while the handle holds control and both publish `/cmd_vel`,
  fighting over the chassis.

`follow_line.py` and `patrol.py` both honour it. `yahboom_keyboard.py` **does not** — it
publishes unconditionally and will fight anything else running.

### Speed limits as ROS parameters, not constants
```python
self.declare_parameter("linear_speed_limit", 1.0)
self.declare_parameter("angular_speed_limit", 5.0)
```
Lets the ceiling be lowered at launch without editing source — exactly what's wanted when
testing an autonomous robot in a room with a metre of clearance:
```bash
ros2 run <pkg> <node> --ros-args -p linear_speed_limit:=0.15
```
**Copy this into my own nodes.**

### The Mecanum axis switch
```python
if xspeed_switch: twist.linear.x = speed * x     # forward/back
else:             twist.linear.y = speed * x     # strafe
```
The same "forward" input becomes strafe depending on a mode flag. The sorter needs this
distinction when lining up on a cuboid — approach vs. sideways correction.

### Always publish stops in a `finally:`
`/cmd_vel` has **no watchdog** (see below). Any node that drives must guarantee a stop on
exit, exception, or Ctrl-C.

---

## Hard constraints to design around

### `/cmd_vel` has no watchdog — one frame runs the motors forever
Verified: published one `linear.x = 0.1` frame, sent nothing else, wheels ran indefinitely.
Only an explicit zero stopped them. **If the program crashes, SSH drops, or the terminal
closes mid-drive, the robot keeps driving.**

### There is no arm feedback of any kind
`/YB_Node` publishes only `/battery`, `/imu/data_raw`, `/odom_raw`, `/scan0`, `/scan1`.
No arm position, effort or current. So:
- **Grasp success cannot be detected from motor load.** Must be visual, or inferred from
  commanded gripper closure.
- Arm backlash and repeatability can only be measured by eye.

### The acceleration ramp makes timed pulses useless
A 1-second command at 0.08 m/s delivered 5.2 cm of an expected 8 cm. Measured per second
at 0.1 m/s: 7.9 cm, then ~10 cm thereafter, plus ~0.9 cm of coast after the stop frame.
**Ramps exist at both ends.** Never control distance by timing — use closed-loop on
`/odom_raw`.

### Odometry integrates wheel rotation, not motion
With wheels in the air it reported 59 cm of travel while stationary. The same error occurs
on slip. **LiDAR corrects odometry, it does not replace it** — `odom -> base_footprint`
always comes from the wheels; SLAM only corrects `map -> odom`. Bad odometry scaling makes
scan matching start from a bad guess. That's why the velocity calibrations matter.

### One serial port, one owner
`/dev/ttyUSB0` = `/dev/myserial` = the STM32 = everything (wheels, arm, IMU, LiDAR, LED,
buzzer). The micro-ROS agent owns it whenever running. **Kill the agent before any script
that talks to the board directly** (`calibrate_arm.py`, `config_robot.py`), and give the
port a moment to release — starting too soon returns `version: None`.

---

## Interface quirks worth remembering

### LED strip: `a` is the LED index, not alpha
| `a` | effect |
|---|---|
| `0.0` (or `255`) | **all 8 LEDs** |
| `1.0`–`8.0` | that single LED; `8` = rightmost |

Per-LED addressing on an 8-pixel strip = a genuine status display. Since the buzzer often
has to stay silent, this is the robot's only practical output: one LED per cuboid
collected, or a colour-coded readout of the target bin. Dim via channel values (`r: 0.15`),
not `a`.

### Two arm topics, complementary
| Topic | Use |
|---|---|
| `/arm6_joints` | whole-arm **pose**, all six at once |
| `/arm_joint` | **one** joint by `id`, leaves the pose untouched |

**Grasp sequence:** `arm6_joints` to position over the cuboid, then `arm_joint` on servo 6
to close — so gripping cannot nudge the five carefully positioned joints.

`time` in both is the movement **duration in ms**, not a speed — servos divide angular
distance by it. Too short for the distance and they run flat out and arrive late, silently.

### Gripper: joint 6, `30` = wide open, `180` = fully closed
Usable range 30–180. Higher squeezes harder.

### Chassis vs arm command semantics
- `/cmd_vel` is a **velocity that persists** until countermanded → needs stop discipline.
- `/arm6_joints` is a **position target with a deadline** → arrives and holds, safe to
  send once.

---

## Working techniques that paid off

### Run loggers in the background on the robot, not in a fixed window
Fixed-duration watchers kept finishing before I could get to the hardware. Writing a
logger to a file with `setsid ... > /tmp/x.txt &` and reading it afterwards removes all
timing pressure — press buttons at your own pace, read the results later.

### Screenshot the robot's desktop over SSH
```bash
DISPLAY=:0 gnome-screenshot -f /tmp/screen.png     # then scp it back
```
Turned "the calibration isn't working" into a two-second fix, because the problem
(block outside the target box) was instantly visible.

### `rqt_reconfigure` is just `ros2 param set`
Every checkbox in that GUI sets a ROS parameter. Anything the manual asks you to do there
can be done over SSH:
```bash
ros2 param set /calibrate_linear start_test true
```
This makes the calibration and patrol sections usable without a keyboard at the robot.

### `pkill -f` can match the process doing the killing
`pkill -9 -f joy_node` killed my own SSH session, because the remote shell's command line
*contained the string*. Kill by PID from `pgrep` instead.

### Read the vendor source before running it
Repeatedly faster than debugging afterwards. Found: the undocumented AprilTag requirement,
an unabortable confirmation prompt, an unconditional "success" message, a dead leftover
driver, and the `/JoyState` gate — all before they could waste time.

---

## Vendor documentation errors found so far

Numbers refer to my local (pre-update) course numbering.

| Where | Error |
|---|---|
| Course 0 §3 | `ros2 topic pub` example has quotes inside the braces — won't parse |
| Course 0 §3 | Reconnect instruction says "enter the following command" then gives none (`sh ~/start_agent.sh`) |
| Course 0 §3 | `calibrate_arm.py`: `if adjust == 'y' or 'Y':` is always true — cannot be aborted |
| Course 0 §3 | `Calibration successfully!` prints unconditionally; only `state=` values are evidence |
| Course 0 §3 | Offset calibration never mentions the block needs an **AprilTag** |
| Course 0 | Folder skips §5 entirely (4 → 6) |
| Chassis §1 | Published-topic table calls `/rgb` "right front radar data" — it's the LED strip |
| Chassis §1 | Rotation command has a stray `} 0.0}` — won't parse |
| Chassis §1 | Six-servo command repeats the quotes-inside-braces error |
| Chassis §1 | §3.3.3 shows `a: 1.0` as "publish red" next to a photo of a fully-lit strip — that command lights **one** LED |
| Chassis §2 | Button table is for a PS2-style pad; my DragonRise indices differ |
| Chassis §3 | §4.41 "source code analysis" shows **ROS1** `rospy.Publisher(...)`; the real file is `rclpy` |

**Pattern:** the hardware has been reliable. Nearly every obstacle came from documentation
or vendor code, and each was solved by reading source or running a deliberate experiment —
not by improvising a replacement.
