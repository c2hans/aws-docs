---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/adk/deleting-action-version.html
---

# Deleting an action version
<a name="deleting-action-version"></a>

Use the following instructions to delete a published version of an action. Deleting a version removes it from the action catalog so that it is no longer available for use in workflows. Any workflows that currently use the deleted version will stop working.

**Important**
To avoid disruption to those who are currently using your action in their workflows, only delete an action version if you've reached the version limit, or if the version contains security vulnerabilities or other critical issues that are impossible to solve with a new version.

**To delete an action version**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to the CodeCatalyst project page.

1. In the navigation pane, choose **CI/CD**, and then choose **Actions**.

   Your custom actions appear.

1. Choose the name of the action whose version you want to delete.

1. Choose the radio button next to the version.

1. Choose **Delete**.
**Note**
If there is only one version available, it cannot be deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
