---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/control-a-device-remotely.html
---

# Control a device remotely
<a name="control-a-device-remotely"></a>

To control a device, choose **Devices** under **Device management** in the left sidebar, then select a device to open its action panel. The following actions are available.

![The device details panel with remote control actions](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/device-management/device-details-view.png)

 **Restart service**
Restarts the AWS DeepRacer service to recover a crashed or unresponsive car without a full power cycle. The service typically returns within about 30 seconds. This action is unavailable when the car is offline.

 **Emergency stop**
Immediately stops a car that will not stop racing. This action requires confirmation and applies to cars only, because timers have no motor.
The emergency stop is not instantaneous. It takes a few seconds to reach the car. If the car is offline when you trigger the stop, the command is queued and delivered when the car reconnects. Because status can be briefly stale, always keep a facilitator physically watching each track as the ultimate safety measure.

 **Change tail-light color**
Changes a car’s tail-light color, for example, green, red, or blue, to identify a specific car on the track.
