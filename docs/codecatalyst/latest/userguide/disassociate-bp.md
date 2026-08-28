---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/disassociate-bp.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Disassociating a blueprint from a project to stop updates
<a name="disassociate-bp"></a>

If you don't want new updates from a blueprint, you can disassociate the blueprint from your project. Resources and functional software components added to your project from the blueprint will remain in your project.

**Important**
To disassociate a blueprint from your CodeCatalyst project, you must be signed in with an account that has the **Space administrator**, **Power user**, or **Project administrator** role in the space.

**To disassociate a blueprint from your project**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. In the CodeCatalyst console, navigate to the space, and then choose the project where you want to disassociate a blueprint.

1. In the navigation pane, choose **Blueprints**.

1. Choose the blueprint with the resources your want to disassociate, choose the **Actions** dropdown menu, and then choose **Disassociate blueprint**.

1. Enter `confirm` to confirm the disassociation.

1. Choose **Confirm**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
