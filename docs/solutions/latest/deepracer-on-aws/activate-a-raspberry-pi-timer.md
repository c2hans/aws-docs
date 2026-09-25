---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/activate-a-raspberry-pi-timer.html
---

# Activate a Raspberry Pi timer
<a name="activate-a-raspberry-pi-timer"></a>

You onboard timers with the same workflow as cars. Only administrators can activate a timer.

The activation wizard is the same as the one shown in [Activate a car](activate-a-car.md).

 **To activate a timer**

1. Choose **Devices** under **Device management** in the left sidebar.

1. From the device list, choose **Add device** to open the activation wizard.

1. For device type, select **Timer**.

1. Select a **fleet** for the timer.

1. For **device name**, enter a name.

1. Choose **Generate** to produce the activation command.

1. Run the command on the Raspberry Pi.

The timer then appears in the fleet and is remotely manageable.

**Note**
Supported timer hardware is Raspberry Pi 3B\+ and 4B.
