---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/repositorylinks-delete.html
---

# Delete a repository link
<a name="repositorylinks-delete"></a>

You can use the **delete-repository-link** command in the AWS Command Line Interface (AWS CLI) to delete a repository link.

Before you can delete a repository link, you must delete all sync configurations associated with the repository link.

**Important**
After you run the command, the repository link is deleted. No confirmation dialog box is displayed. You can create a new repository link, but the Amazon Resource Name (ARN) is not reused.

**To delete a repository link**
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **delete-repository-link** command, specifying the ID of the repository link to delete.

  ```
  aws codeconnections delete-repository-link --repository-link-id 6053346f-8a33-4edb-9397-10394b695173
  ```

  This command returns nothing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
