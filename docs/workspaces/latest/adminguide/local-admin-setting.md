---
source_url: https://docs.aws.amazon.com/workspaces/latest/adminguide/local-admin-setting.html
---

# Manage local administrator permissions for WorkSpaces Personal
<a name="local-admin-setting"></a>

**Note**
This feature is only available for directories managed through AWS Directory Service, including AD Connector, AWS Managed Microsoft AD, and Simple AD.

You can specify whether users are local administrators on their WorkSpaces, which enables them to install application and modify settings on their WorkSpaces. Users are local administrators by default. If you modify this setting, the change applies to all new WorkSpaces that you create and any WorkSpaces that you rebuild.

**To modify local administrator permissions**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **Directories**.

1. Choose your directory.

1. Under Local administrator settings, choose **Edit**.

1. To ensure that users are local administrators, choose **Enable local administrator setting**.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
