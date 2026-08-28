---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-install-client.html
---

# Have Your Users Install the WorkSpaces Applications Client Themselves
<a name="user-install-client"></a>

For step-by-step guidance that you can provide your users to help them install the WorkSpaces Applications client, see [Setup for Windows](client-application-windows-installation-user.md) or [Setup and installation for macOS](client-application-mac-installation-user.md).

**Important**
For the Windows client, if your organization has deployed antivirus software that prevents users from running .exe files, you must add an exception to allow your users to run the WorkSpaces Applications client installation .exe program. Otherwise, when users try to install the client, either nothing happens, or they receive an error after they start the installation program.

After users install the client, if you plan to let your users use USB devices during their WorkSpaces Applications streaming sessions, the following requirements must be met:
+ You must qualify the USB devices that can be used with WorkSpaces Applications. For more information, see [Qualify USB Devices for Use with Streaming Applications](qualify-usb-devices.md).
+ After their devices are qualified, your users must share the devices with WorkSpaces Applications every time they start a new streaming session. For guidance that you can provide your users to them complete this task, see [USB Devices](client-application-windows-how-to-share-usb-devices-user.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
