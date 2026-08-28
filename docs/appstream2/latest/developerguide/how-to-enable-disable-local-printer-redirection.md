---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/how-to-enable-disable-local-printer-redirection.html
---

# How to Enable Local Printer Redirection
<a name="how-to-enable-disable-local-printer-redirection"></a>

By default, local printer redirection is enabled when the WorkSpaces Applications client is installed. However, if local printer redirection is not enabled on the stack that your users access for streaming sessions, you can enable it in the WorkSpaces Applications console by performing the following steps.

**To enable local printer redirection by using the WorkSpaces Applications console**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2/home](https://console.aws.amazon.com/appstream2/home).

1. In the left navigation pane, choose **Stacks**.

1. Choose the stack for which you want to enable local printer redirection.

1. Choose the **User Settings** tab, and then expand the **Clipboard, file transfer, print to local device, and authentication permissions** section.

1. For **Print to local device**, verify that **Enabled** is selected. If not, choose **Edit**, and then choose **Enabled**.

1. Choose **Update**.

Alternatively, you can enable local printer redirection by using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS CLI).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
