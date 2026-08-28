---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-custom-action.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Developing a custom action
<a name="workflows-custom-action"></a>

You can develop a custom action to use in your workflows using the CodeCatalyst Action Development Kit (ADK). You can then publish the action to the CodeCatalyst actions catalog, so that other CodeCatalyst users can view and use it in their workflows.

**To develop, test, and publish an action (high-level tasks)**

1. Install the required tools and packages necessary to develop an action.

1. Create a CodeCatalyst repository to store your action code.

1. Initialize the action. This lays down the source files required by the action, including an action definition file (`action.yml`) that you can update with your own code.

1. Bootstrap the action code to get the necessary tools and libraries to build, test, and release the action project.

1. Build the action on your local computer, and push the changes to your CodeCatalyst repository.

1. Test the action with unit tests locally, and run the ADK-generated workflow in CodeCatalyst.

1. Publish the action to the CodeCatalyst actions catalog by choosing the **Publish** button in the CodeCatalyst console.

For detailed steps, see the [Amazon CodeCatalyst Action Development Kit Developer Guide](https://docs.aws.amazon.com/codecatalyst/latest/adk/what-is-action-development-kit.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
