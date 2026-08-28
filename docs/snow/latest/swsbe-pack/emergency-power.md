---
source_url: https://docs.aws.amazon.com/snow/latest/swsbe-pack/emergency-power.html
---

# Emergency shutdown
<a name="emergency-power"></a>

Use this procedure to turn the equipment off during an emergency, such as fire, water, smoke, or hazard to personnel.

**Important**
Do not turn off the Snowball Edge device by unplugging the power cable from the device or the power cable from the power source while the device is operating. Loss of data may occur.

**To shut down a Snowball Edge device in an emergency**

1. Press and release the power button located above the LCD screen. It takes about 20 seconds for the device to shut down. While the device is shutting down, the LCD screen displays a message indicating the device is shutting down.
![Shutdown message on LCD screen.](http://docs.aws.amazon.com/snow/latest/swsbe-pack/images/shutdown-screen.png)

1. After the device has shut down, disconnect the device power cable from the power source.

**To shut down a hardware security module in an emergency**
+ Unplug both power cables from the device or both power cables from the power source.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Snow Family Device Guides. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query snow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
