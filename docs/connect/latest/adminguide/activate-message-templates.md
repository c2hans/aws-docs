---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/activate-message-templates.html
---

# Activate a message template
<a name="activate-message-templates"></a>

To help you manage the development and use of individual message templates, Connect Customer supports versioning for all types of message templates. Versioning provides a way for you to create a history of changes to a template—each version is a snapshot of a template at a certain point in time. Versioning also provides a way for you to control the contents and settings of messages that use a template.

You can only activate message templates that have been **Saved as new version**. This is to prevent accidentally activating templates that are drafts.

When a template version is **Activated**, it is available to be added to the [Flow block in Connect Customer: Send message](send-message.md) and might be available to agents through the agent workspace.

**To activate a messaging template**

Log in to Connect Customer admin website with an Admin account or a user account that has **Content Management** - **Message templates** - **Create** in it's security profile.

1. On the left navigation menu, choose **Message templates**.

1. On the **Message templates** page, save the template using the **Save as new version** option.

1. On the **Messaging templates** page re-open the template you just saved.

1. Use the dropdown menu to choose the version of the template to activate.
![The Version number for a template.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-template-version.png)

1. Choose **Activate**.
![The Activate button on the message template page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/message-template-version-activate.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
