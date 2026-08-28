---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/monitor-with-workflow-monitor-configure-signal-maps-delete.html
---

# Deleting the signal map of your AWS media workflow
<a name="monitor-with-workflow-monitor-configure-signal-maps-delete"></a>

If you not longer need a signal map, it can be deleted. If you have monitoring templates deployed on the signal map, the deletion process will ask you to delete any CloudWatch and EventBridge resources that have been deployed to this signal map. Deleting the deployed resources does not affect the templates that created them. This resource deletion is to ensure that you do not have CloudWatch and EventBridge resources that are deployed but not used.

**To delete a signal map**

1. From the workflow monitor console's navigation pane, select **Signal maps** and select the radio button next to the signal map you want to delete.

1. Select the **Delete** button. You will be asked to confirm the deletion of the monitoring resources. Select **Delete** to begin the monitoring resource deletion process.

1. The **Monitor deployment** column will display the current status. When the status has changed to **DELETE\_COMPLETE**, select the **Delete** button again.

1. You will be asked to confirm deletion of the signal map. Select **Delete** to proceed and delete the signal map.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
