---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-flow-log.html
---

# Delete an AWS Transit Gateway Flow Logs record
<a name="delete-flow-log"></a>

You can delete a transit gateway flow log using the Amazon VPC console.

These procedures disable the flow log service for a resource. Deleting a flow log does not delete the existing log streams from CloudWatch Logs or log files from Amazon S3. Existing flow log data must be deleted using the respective service's console. In addition, deleting a flow log that publishes to Amazon S3 does not remove the bucket policies and log file access control lists (ACLs).

**To delete a transit gateway flow log**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit gateways**.

1. Choose a **Transit gateway ID**.

1. In the Flow logs section, choose the flow logs that you want to delete.

1. Choose **Actions**, and then choose **Delete flow logs**.

1. Confirm that you want to delete the flow by choosing **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
