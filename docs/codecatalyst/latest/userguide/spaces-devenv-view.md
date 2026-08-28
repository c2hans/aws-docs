---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces-devenv-view.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Viewing Dev Environments for your space
<a name="spaces-devenv-view"></a>

You can view the type, status, and details for all Dev Environments in your space. For more information about creating and running Dev Environments, see [Creating a Dev Environment](devenvironment-create.md).

You must have the **Space administrator** role to view this page and to manage Dev Environments at the space level.

**To view Dev Environments in your space**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your CodeCatalyst space.
**Tip**
If you belong to more than one space, choose a space in the top navigation bar.

1. Choose **Settings**, and then choose **Dev Environments**.

   The page lists all Dev Environments in your space. You can view the **Resource** name, the resource **alias** if applicable, the type of **IDE**, the default or configured **Compute** and **Storage**, and the configured **Timeout** for each Dev Environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
