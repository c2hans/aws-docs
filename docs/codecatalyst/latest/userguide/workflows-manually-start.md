---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-manually-start.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Starting a workflow run manually
<a name="workflows-manually-start"></a>

In Amazon CodeCatalyst, you can start a workflow run manually from the CodeCatalyst console.

For more information about workflow runs, see [Running a workflow](workflows-working-runs.md).

**Note**
You can also start a workflow run automatically by [configuring a trigger](workflows-add-trigger.md).

**To start a workflow run manually**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Choose your project.

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the name of your workflow. You can filter by the source repository or branch name where the workflow is defined, or filter by workflow name or status.

1. Choose **Run**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
