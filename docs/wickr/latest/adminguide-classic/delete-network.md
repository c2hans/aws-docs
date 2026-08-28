---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide-classic/delete-network.html
---

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Delete network in AWS Wickr
<a name="delete-network"></a>

You can delete your AWS Wickr network.

**Note**
If you delete a premium free trial network, you won't be able to create another one.

Complete the following procedure to delete your Wickr network.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. Choose **Manage network**.

1. On the **Networks** page, find the network you want to delete.

1. On the right-hand side of the network you want to delete, select the three dots, and then choose **Delete network**.

1. Type **confirm** in the pop-up window, and then choose **Delete**.

   It can take a few minutes for the network to delete.
**Note**
Data retained by your data retention configuration (if enabled) will not be deleted when you delete your network. For more information, see [ Data retention for AWS Wickr](https://docs.aws.amazon.com/wickr/latest/adminguide/data-retention.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
