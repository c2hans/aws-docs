---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car.html
---

# Build a custom AWS DeepRacer car
<a name="custom-car"></a>

You can build a custom vehicle that is fully compatible with the DeepRacer on AWS solution. You can follow two build paths supported by the [AWS DeepRacer Community open-source project](https://github.com/aws-deepracer-community/deepracer-custom-car) on the GitHub website:
+  **Option A**—Replace the Intel Atom processor in an existing AWS DeepRacer Evo with a Raspberry Pi 5, servo driver HAT, and Raspberry Pi-compatible camera, while reusing the existing chassis and wheel/motor assembly.
+  **Option B**—Build a new vehicle from scratch using a 1/18-scale RC truck chassis, Raspberry Pi 5, servo driver HAT, camera, and 3D-printed mounting components.

Both options use the same software installation procedure. Custom cars that you build with either option are fully compatible with reinforcement learning models that you train using the DeepRacer on AWS solution.

The following table compares the two build options to help you decide which path is right for you.

| Category | Option A: Upgrade existing DeepRacer Evo | Option B: Build from scratch |
| --- | --- | --- |
| Best for | Customers who have an existing AWS DeepRacer Evo car. This is the fastest and easiest path. | Customers who do not have an existing AWS DeepRacer car and cannot procure one. This is the only available path in that case. |
| Compute module | Raspberry Pi 5, servo driver HAT, and camera | Raspberry Pi 5, servo driver HAT, and camera |
| Software | Same installation procedure for both options | Same installation procedure for both options |
| Model compatibility | Fully compatible with reinforcement learning models trained using the DeepRacer on AWS solution | Fully compatible with reinforcement learning models trained using the DeepRacer on AWS solution |
| Batteries | Single battery | Two batteries |
| Chassis | Reuses existing chassis, ESC, servo, and wheel/motor assembly | Requires a 1/18-scale RC truck chassis and off-the-shelf components |
| Soldering | Not required | Required (soldering iron needed) |
| ESC knowledge | Not required | Required (you must swap the Electronic Speed Controller) |
| 3D printing | Required — front camera mount, main plate (with legs), rear mount, and body mounts (×2) | Required — front camera mount, main plate (without legs), rear mount, body mounts (×2), and additional chassis-specific mounting components |
| Approximate cost | $220 | $350 |
| Estimated assembly time (excluding 3D printing) | 2 hours | 3–5 hours |
+  [Parts list](custom-car-parts-list.md)
+  [Option A: Upgrade an existing AWS DeepRacer Evo](custom-car-option-a.md)
+  [Option B: Build from scratch](custom-car-option-b.md)
+  [Install the software](custom-car-software.md)
+  [Start the ROS server](custom-car-software-start-ros.md)
+  [Calibrate and test](custom-car-testing.md)
