---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-mac-connection-modes-user.html
---

# WorkSpaces Applications macOS Client Connection Mode
<a name="client-application-mac-connection-modes-user"></a>

The WorkSpaces Applications macOS client supports two connection modes: *Classic mode* and *Desktop view*. Your administrator will set up the connection mode for you.

**Classic mode**

When you use classic application mode, you work with remote streaming applications in the WorkSpaces Applications session window. If your administrator has made more than one application available to you, you can open multiple applications during your session. All applications that you open are displayed in the same WorkSpaces Applications session window.

When you connect to WorkSpaces Applications in classic mode, the WorkSpaces Applications Application Launcher window opens and displays the list of applications that are available for you to stream. When you open a streaming application in this mode, the Application Launcher window closes, and the application opens in the WorkSpaces Applications session window.

**Desktop view**

When you connect to WorkSpaces Applications and choose **Desktop view**, WorkSpaces Applications provides a standard Windows desktop view for your streaming session. The icons of applications that are available for you to stream appear on the Windows desktop. In addition, the WorkSpaces Applications toolbar, which enables you to configure settings for your streaming session, appears in the top left area of your streaming session window.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
