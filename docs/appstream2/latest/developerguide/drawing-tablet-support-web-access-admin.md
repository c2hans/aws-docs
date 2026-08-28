---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/drawing-tablet-support-web-access-admin.html
---

# Drawing Tablet Support
<a name="drawing-tablet-support-web-access-admin"></a>

Drawing tablets, also known as pen tablets, are computer input devices that let users draw with a stylus (pen). With WorkSpaces Applications, your users can connect a drawing tablet, such as a Wacom drawing tablet, to their local computer and use the tablet with their streaming applications.

Following are requirements and considerations for enabling your users to use drawing tablets with their streaming applications.
+ To enable your users to use this feature, you must configure your WorkSpaces Applications fleet to use an image that runs Windows Server 2019.
+ To use this feature, users must access WorkSpaces Applications through the Google Chrome or Mozilla Firefox browsers only, or the WorkSpaces Applications client.
+ Streaming applications must support Windows Ink technology. For more information, see [Pen interactions and Windows Ink in Windows apps](https://docs.microsoft.com/en-us/windows/uwp/design/input/pen-and-stylus-interactions).
+ Some applications, such GIMP, must detect drawing tablets on the streaming instance to support pressure sensitivity. If this is the case, your users must use the WorkSpaces Applications client to access WorkSpaces Applications and stream these applications. In addition, you must qualify your users' drawing tablets, and users must share their drawing tablets with WorkSpaces Applications every time they start a new streaming session. For step-by-step guidance, see [Qualify USB Devices for Use with Streaming Applications](qualify-usb-devices.md).
+ This feature is not supported on Chromebooks.

To get started with using drawing tablets during application streaming sessions, users connect their drawing tablet to their local computer with USB and use a supported web browser or the WorkSpaces Applications client, if it is installed, to start a streaming session. No USB redirection is required to use this feature.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
