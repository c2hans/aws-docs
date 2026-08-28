---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/AMG-edit-delete-workspace.html
---

# Delete a Amazon Managed Grafana workspace
<a name="AMG-edit-delete-workspace"></a>

If you delete an Amazon Managed Grafana workspace, all the configuration data for that workspace is also deleted. This includes dashboards, data source configuration, alerts, and snapshots.

**To delete an Amazon Managed Grafana workspace**

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/).

1. In the left navigation pane, choose the menu icon.

1. Choose **All workspaces**.

1. Choose the name of the workspace that you want to delete.

1. Choose **Delete**.

1. To confirm the deletion, enter the name of the workspace and choose **Delete**.

**Note**
This procedure deletes a workspace. Other resources may not be deleted. For example, IAM roles that were in use by the workspace are not deleted (but may be unlocked if they are no longer in use).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
