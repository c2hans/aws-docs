---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/administrator-controls.html
---

# Administrator Controls
<a name="administrator-controls"></a>

WorkSpaces Applications provides administrative controls that you can use to limit the ways in which users can transfer data between their local computer and an WorkSpaces Applications fleet instance. You can limit or disable the following when you [create or update an WorkSpaces Applications stack](set-up-stacks-fleets-install.md):
+ Clipboard/copy and paste actions
+ File upload and download, including folder and drive redirection
+ Printing

When you create an WorkSpaces Applications image, you can specify which USB devices are available to redirect to WorkSpaces Applications fleet instances from the WorkSpaces Applications client for Windows. The USB devices that you specify will be available for use during users’ WorkSpaces Applications streaming sessions. For more information, see [Qualify USB Devices for Use with Streaming Applications](qualify-usb-devices.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
