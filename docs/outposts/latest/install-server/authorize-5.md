---
source_url: https://docs.aws.amazon.com/outposts/latest/install-server/authorize-5.html
---

# Verify the NSK LEDs for your Outposts server
<a name="authorize-5"></a>

After the provisioning process completes, check the NSK LEDs.

AWS Outposts supports two versions of NSK: Atlas 2.0 and Atlas 3.0. Both NSK versions have a RGB **Status** LED. In addition, the Atlas 3.0 has a green **Power** LED.

The following image shows the location of the LEDs on the Atlas 2.0 and Atlas 3.0:

![An image of the Atlas 2.0 and 3.0 NSKs with the RGB Status LED on each NSK and the green Power LED on the Atlas 3.0.](http://docs.aws.amazon.com/outposts/latest/install-server/images/nsk-led-status.png)

**To verify the Status and Power LEDs on the NSK**

1. Check the color of the RGB Status LED. If the color is green, the NSK is healthy. If the color is not green, contact Support.

1. If you have an Atlas 3.0 NSK, check the green Power LED. If the green light is on, the NSK is correctly connected to the host and has power. If the green light is not on, contact Support.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Outposts. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query outposts` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
