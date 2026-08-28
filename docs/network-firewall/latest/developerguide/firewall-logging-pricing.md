---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging-pricing.html
---

# Pricing for AWS Network Firewall logging
<a name="firewall-logging-pricing"></a>

You are charged for Amazon CloudWatch *vended logs*, on top of the basic charges for using Network Firewall. Additionally, you incur charges when querying logs, whether through CloudWatch and or through Amazon Athena for logs stored in Amazon S3. Vended logs are specific AWS service logs published by AWS on your behalf at volume discount pricing.

Your logging costs can vary depending on factors such as the destination type that you choose and the amount of data that you log. For example, flow logging sends logs for all of the network traffic that reaches your firewall's stateful rules, but alert logging sends logs only for network traffic that your stateful rules drop or explicitly alert on.

Review the following resources to understand the pricing considerations for using firewall logs:
+ For information about CloudWatch vended log pricing, see [Logs](https://aws.amazon.com/cloudwatch/pricing/) on the *Amazon CloudWatch pricing* page.
+ For information about Network Firewall pricing, see [Network Firewall pricing](https://aws.amazon.com/network-firewall/pricing/).
+ For information about Amazon S3 pricing, see [Amazon S3 pricing](https://aws.amazon.com/S3/pricing/).
+ For information about Amazon Athena pricing, see [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
