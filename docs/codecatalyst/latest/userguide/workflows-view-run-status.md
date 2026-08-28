---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/workflows-view-run-status.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Workflow run states
<a name="workflows-view-run-status"></a>

A workflow run can be in one of the following states:
+ **Succeeded** – The workflow run was processed successfully.
+ **Failed** – One or more actions in the workflow run failed.
+ **In progress** – The workflow run is currently being processed.
+ **Stopped** – A person stopped the workflow run while it was in progress.
+ **Stopping** – The workflow run is currently being stopped.
+ **Cancelled** – The workflow run was canceled by CodeCatalyst because the associated workflow was deleted or updated while the run was in progress.
+ **Superseded** – Only occurs if you have configured [superseded run mode](workflows-configure-runs.md#workflows-configure-runs-superseded). The workflow run was canceled by CodeCatalyst because a later workflow run superseded it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
