---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/app-block-builder-actions.html
---

# App Block Builder Actions
<a name="app-block-builder-actions"></a>

You can perform the following actions on an app block builder, depending on the current state (status) of the app block builder instance.

**Delete**
Permanently delete an app block builder.
The instance must be in a **Stopped** state.

**Connect**
Connect to a running app block builder. This action starts a desktop streaming session with the app block builder to install and add applications, and create an app block.
The instance must be in a **Running** state.

**Start**
Start a stopped app block builder. A running instance is billed to your account.
The instance must be in a **Stopped** state, and associated with an app block.

**Stop**
Stop a running app block builder. A stopped instance is not billed to your account.
The instance must be in a **Running** state.

**Update**
Update any of the app block builder properties, except the name.
The instance must be in a **Stopped** state.

None of these actions can be performed on an instance in any of the following intermediate states:
+ **Pending**
+ **Stopping**
+ **Starting**
+ **Deleting**

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
