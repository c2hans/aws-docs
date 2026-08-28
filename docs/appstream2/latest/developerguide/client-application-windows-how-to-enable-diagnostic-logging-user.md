---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/client-application-windows-how-to-enable-diagnostic-logging-user.html
---

# Logging
<a name="client-application-windows-how-to-enable-diagnostic-logging-user"></a>

To help with troubleshooting if an issue with the WorkSpaces Applications client occurs, you can enable diagnostic logging. The log files that are sent to WorkSpaces Applications (AWS) include detailed information about your device and connection to the AWS network. You can enable automatic log uploads so that these files are sent to WorkSpaces Applications (AWS) automatically. You can also upload log files on an as-needed basis, before or during an WorkSpaces Applications streaming session.

**Automatic logging**

You can enable automatic logging when you install the WorkSpaces Applications client. For information about how to enable automatic logging when you install the WorkSpaces Applications client, see step 5 in [Setup for Windows](client-application-windows-installation-user.md).

**On-demand logging**

If an issue occurs during an WorkSpaces Applications streaming session, you can also send log files on an as-needed basis. If an issue occurs that causes the WorkSpaces Applications client to stop responding, a notification prompts you to choose whether to send an error report and the associated log files to WorkSpaces Applications (AWS).

The following procedures describe how to send log files before you sign in to an WorkSpaces Applications streaming session and during an WorkSpaces Applications streaming session.

**To send log files before an WorkSpaces Applications streaming session**

1. On your local PC where the WorkSpaces Applications client is installed, in the lower left of your screen, choose the Windows search icon on the taskbar, and enter **AppStream** in the Search box.

1. In the search results, select ** Amazon AppStream** to start the WorkSpaces Applications client.

1. At the bottom of the WorkSpaces Applications sign-in page, choose the **Send Diagnostic Logs** link.

1. To continue connecting to WorkSpaces Applications, if your WorkSpaces Applications administrator has provided you with a web address (URL) to use to connect to WorkSpaces Applications for application streaming, enter the URL, and then choose **Connect**.

**To send log files during an WorkSpaces Applications streaming session**

1. If you are not already connected to WorkSpaces Applications and streaming an application, use the WorkSpaces Applications client to start a streaming session.

1. In the upper right of the WorkSpaces Applications session window, choose the **Profiles** icon, and then choose **Send Diagnostic Logs**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
