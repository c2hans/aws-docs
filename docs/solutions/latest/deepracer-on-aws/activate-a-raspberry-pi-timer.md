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

1. Select **Sensors are active-low (IR break-beam)** if your sensors pull the signal low when the car crosses. Most infrared break-beam receivers work this way. Leave it clear for pressure strips.

1. Choose **Generate** to produce the activation command.

1. Run the command on the Raspberry Pi as the root user. The command installs the AWS Systems Manager Agent (SSM Agent) and the timer service, and starts the service.

After the command finishes, the timer appears in the fleet and you can manage it remotely. To use it for lap timing, see [Record laps automatically with a timer](timekeeping.md#record-laps-automatically).

The timer reads the finish line sensors on `GPIO 17` and `GPIO 27` of the Raspberry Pi’s 40-pin header. It publishes each crossing to AWS IoT Core over HTTPS and doesn’t open any listening port on the Raspberry Pi.

**Note**
The **Timer** device type is unavailable if the deployment has no AWS IoT Core endpoint configured, because timers publish lap crossings to AWS IoT Core.

**Note**
The timer has been tested on Raspberry Pi 3B\+ and 4B.
