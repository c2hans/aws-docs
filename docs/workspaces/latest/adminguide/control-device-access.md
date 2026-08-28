---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/control-device-access.html
---

# Control device access for WorkSpaces Personal
<a name="control-device-access"></a>

You can specify the types of devices that have access to WorkSpaces based on the device platform. You can use certificates to restrict access to WorkSpaces to trusted devices (also known as managed devices).

**To control device access to WorkSpaces**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose your directory.

1. Under Access control options, choose **Edit**.

1. Under Trusted devices, specify which device types can access WorkSpaces by selecting either **Allow all**, **Trusted devices**, or **Deny all**. For more information, see [Restrict access to trusted devices for WorkSpaces Personal](trusted-devices.md).

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
