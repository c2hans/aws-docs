---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages-repositories-create.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Creating a package repository
<a name="packages-repositories-create"></a>

Perform the following steps to create a package repository in CodeCatalyst.

**To create a package repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to the project in which you want to create a package repository.

1. From the navigation pane, choose **Packages**.

1. On the **Package repositories** page, choose **Create package repository**.

1. In the **Package repository details** section, add the following:

   1. **Repository name**. Consider using a descriptive name with details such as your project or team name, or how the repository will be used.

   1. (Optional) **Description**. A repository description is especially helpful when you have multiple repositories across multiple teams in a project.

1. In the **Upstream repositories** section, choose **Select upstream repositories** to add any package repositories that you want to access through your CodeCatalyst package repository. You can add **Gateway repositories** to connect to external package repositories or other **CodeCatalyst repositories**.

   1. When a package is requested from a package repository, upstream repositories will be searched in the order they appear in this list. Once a package is found, CodeCatalyst will stop searching. To change the order of the upstream repositories, you can drag and drop the repositories in the list.

1. Choose **Create** to create your package repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
