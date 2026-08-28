---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-delete.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deleting a Dev Environment for your space
<a name="spaces-devenv-delete"></a>

You can delete a Dev Environment that is no longer needed or that no longer has an owner. For more information about considerations for deleting a Dev Environment, see [Deleting a Dev Environment](devenvironment-delete.md).

You must have the **Space administrator** role to view this page and to manage Dev Environments at the space level.

**To delete Dev Environments in your space**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space.
**Tip**
If you belong to more than one space, choose a space in the top navigation bar.

1. Choose **Settings**, and then choose **Dev Environments**.

1. Choose the selector next to the Dev Environment you want to manage. Choose **Delete**. To confirm, type `delete`, and then choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
