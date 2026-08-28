---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/syncconfigurations-delete.html
---

# Delete a sync configuration
<a name="syncconfigurations-delete"></a>

You can use the **delete-sync-configuration** command in the AWS Command Line Interface (AWS CLI) to delete a sync configuration.

**Important**
After you run the command, the sync configuration is deleted. No confirmation dialog box is displayed. You can create a new sync configuration, but the Amazon Resource Name (ARN) is not reused.

**To delete a sync configuration**
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **delete-sync-configuration** command, specifying the sync type and resource name for the sync configuration that you want to delete.

  ```
  aws codeconnections delete-sync-configuration --sync-type CFN_STACK_SYNC --resource-name mystack
  ```

  This command returns nothing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
