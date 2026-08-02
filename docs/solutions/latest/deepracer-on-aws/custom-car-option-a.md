---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/custom-car-option-a.html
---

# Option A: Upgrade an existing AWS DeepRacer Evo
<a name="custom-car-option-a"></a>

If you own an AWS DeepRacer Evo, you can replace the Intel compute module with a Raspberry Pi 5 while reusing the existing chassis, servo, ESC, and wheel/motor assembly.

To complete the upgrade:

1. Print the 3D chassis components:

   Print the following components from the [AWS DeepRacer Community custom car repository](https://github.com/aws-deepracer-community/deepracer-custom-car) on the GitHub website. Printing all parts takes approximately 5–6 hours on a standard 3D printer using PLA filament at 25% infill.
   + PiMount Front (front camera mount)
   + PiMount Plate with legs (main plate for DeepRacer chassis)
   + PiMount Back (rear mount)
   + Body mounts (×2)

1. Remove the Intel compute module and all associated cabling from the AWS DeepRacer Evo chassis.

1. Assemble the 3D-printed chassis:

   Bolt the front camera mount and rear mount to the main plate using M2×15 mm nylon standoffs. Attach the body mounts to secure the DeepRacer shell. Insert 3× brass M2.5 screws into the main plate to prepare for mounting the Raspberry Pi.

1. Assemble the compute stack:

   1. Attach the [Raspberry Pi Active Cooler](https://www.amazon.com/dp/B0FRZ6JHRT) (available for purchase on the Amazon website) to the Raspberry Pi 5.

   1. Seat the [GPIO header extender](https://www.amazon.com/dp/B0DP225QXN) (available for purchase on the Amazon website) onto the GPIO pins.

   1. Using M2.5 nylon standoffs from the [standoff kit](https://www.amazon.com/dp/B0FPMC9917) (available for purchase on the Amazon website), mount the [Waveshare PCA9685 servo driver HAT](https://www.amazon.com/dp/B0D63DPNK1) (available for purchase on the Amazon website) on top of the GPIO extender. Leave clearance for the cooler fan.

   1. Secure the assembled stack to the 3D-printed main plate using the pre-installed M2.5 brass screws.

1. Wire the electronics:
**Risk of hardware damage**
Before connecting the ESC to the servo hat, **remove the center (power/positive) wire** from the ESC’s 3-pin PWM cable. This middle wire carries approximately 6V from the ESC’s BEC output. Leaving it connected will permanently damage both the servo hat and the Raspberry Pi 5.

   Connect the ESC’s 2-wire PWM cable (signal \+ ground only) to **channel 0** on the PCA9685 servo hat. Connect the 3-wire steering servo cable to **channel 1**. Ensure all ground connections share a common ground reference with the Raspberry Pi.

1. Install the camera:

   1. Install the [Raspberry Pi Camera Module 2](https://www.amazon.com/dp/B07G9VLPZH) (available for purchase on the Amazon website) in the 3D-printed front camera mount using 4× M2×15 mm nylon screws. Tighten the bottom screws first to seat the lower edge of the camera flush with the mount.

   1. Connect the [200 mm camera extension cable](https://www.amazon.com/dp/B0D12L3RDG) (available for purchase on the Amazon website) between the camera module and the Raspberry Pi 5 CSI port.

   1. The camera mounts upside down. After the first boot, add the following line to `/etc/rc.local` before the `exit 0` line to apply a permanent 180° rotation at startup:

      ```
      v4l2-ctl --set-ctrl=rotate=180
      ```

1. Mount the assembly onto the car:

   Attach the completed 3D-printed chassis (with compute stack and camera installed) to the DeepRacer Evo car chassis. Connect the speed controller and steering servo wires as described in the wiring step. Plug in the battery using the connector for the car.

1. Proceed to [Install the software](custom-car-software.md).

![Raspberry Pi 5 compute stack mounted on the Evo chassis top plate.](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/custom-car/deepracer_car_top_view.png)

![Waveshare PCA9685 servo driver HAT mounted on GPIO header extender above Raspberry Pi 5.](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/custom-car/deepracer_servo_hat.png)
