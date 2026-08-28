---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/device-delete.html
---

# Deleting a Link input device
<a name="device-delete"></a>

You don't delete Link input devices. Instead, if someone deregisters the Link device, the Link input device (which is the interface for the device in the console) no longer appears in the **Devices** section. Note that this is the only way that the Link input device is ever removed.
+ If someone powers down the device, the Link input device still appears in the list.
+ If the device is disconnected from the internet, or if the connection from MediaLive to the Link device is down, the Link input device still appears in the list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
