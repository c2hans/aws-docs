---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-working-with-variables-determine-output-vars.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Determining which predefined variables your workflow emits
<a name="workflows-working-with-variables-determine-output-vars"></a>

Use the following procedure to determine which predefined variables a workflow emits when it runs. You can then reference these variables within the same workflow.

For more information about predefined variables, see [Using predefined variables](workflows-using-predefined-variables.md).

**To determine the predefined variables that your workflow emits**
+ Do one of the following:
  + **Run the workflow once**. After the run finishes, the variables emitted by the workflow are displayed on the **Variables** tab of the run details page. For more information, see [Viewing workflow run status and details](workflows-view-run.md).
  + **Consult the [List of predefined variables](workflow-ref-action-variables.md)**. This reference lists the variable name (key) and value for each predefined variable.

**Note**
The maximum total size of a workflow's variables is listed in [Quotas for workflows in CodeCatalyst](workflows-quotas.md). If the total size exceeds the maximum, the action that occurs after the maximum is reached may fail.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
