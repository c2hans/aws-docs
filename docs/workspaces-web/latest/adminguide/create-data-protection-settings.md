---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/create-data-protection-settings.html
---

# Create data protection settings in Amazon WorkSpaces Secure Browser
<a name="create-data-protection-settings"></a>

You can create data protection settings in WorkSpaces Secure Browser.

**To create data protection settings**

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. In the left-hand navigation pane, choose **Data Protection Settings**.

1. Choose **Create Data Protection Settings**.

1. Enter a display name (required) and description (optional) for the setting.

1. Select the default settings for inline redaction. You can set the following:
   + The level of strictness of all data types
   + The domains on which redaction should be enforced

1. Choose your base inline redaction data types from the supported types, or create a custom data type. You can set overrides for each data type, including the level of strictness and domain exceptions.

1. Add any **Tags** (optional) for reporting.

1. When you are done, choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
