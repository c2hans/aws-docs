---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide-classic/data-retention.html
---

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Data retention for AWS Wickr
<a name="data-retention"></a>

AWS Wickr Data retention can retain all conversations in network. This includes direct message conversations and conversations in Groups or Rooms between in-network (internal) members and those with other teams (external) with whom your network is federated. Data retention is only available to AWS Wickr Premium plan users and enterprise customers who opt in for data retention. For more information on the Premium plan, see [Wickr Pricing](https://aws.amazon.com/wickr/pricing/)

When a network administrator configures and activates data retention for their network, all messages and files shared in their network are retained in accordance with the organization's compliance policies. These .txt file outputs are accessible by the network administrator in an external location (eg: local storage, Amazon S3 bucket, or any other storage as per user's choice), from where they can be analyzed, erased, or transferred.

**Note**
Wickr never accesses your messages and files. Therefore, it is your responsibility to configure a data retention system.

**Topics**
+ [View data retention details in AWS Wickr](view-data-retention-details.md)
+ [Configure data retention for AWS Wickr](configure-data-retention.md)
+ [Get the data retention logs for your Wickr network](getting-data-retention-logs.md)
+ [Data retention metrics and events for your Wickr network](metrics-events.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
