---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/mvpc-cross-account-delete-connection.html
---

# Delete a managed VPC connection to an Amazon MSK cluster
<a name="mvpc-cross-account-delete-connection"></a>

The cross-account user can delete a managed VPC connection for an MSK cluster from the client account console. Because the cluster owner user doesn’t own the managed VPC connection, the connection can’t be deleted from the cluster admin account. Once a VPC connection is deleted, it no longer incurs cost.

**To delete a managed VPC connection using the MSK console**

1. From the client account, open the Amazon MSK console at [AWS Management Console](https://console.aws.amazon.com/msk).

1. In the navigation pane, select **Managed VPC connections**.

1. From the connection list, select the connection that you want to delete.

1. Confirm that you want to delete the VPC connection.

To delete a managed VPC connection using the API, use the `DeleteVpcConnection` API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
