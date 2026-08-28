---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-monitoring-firehose.html
---

# Sending capacity provider system logs to Firehose
<a name="lambda-managed-instances-monitoring-firehose"></a>

You can send capacity provider system logs to Amazon Data Firehose. With Firehose, you can stream logs in real time to various destinations, including third-party analytics tools and custom endpoints.

**Note**
You can configure capacity provider system logs to be sent to Firehose using the AWS CLI, AWS CloudFormation, and all AWS SDKs.

## Pricing
<a name="lambda-managed-instances-firehose-pricing"></a>

For more information about pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs).

## Setting up Firehose log delivery
<a name="lambda-managed-instances-firehose-setup"></a>

To send capacity provider system logs to Firehose, create a CloudWatch Logs subscription filter on your capacity provider's log group. The subscription filter routes log events to your Firehose delivery stream.

By default, your capacity provider's log group is named `/aws/lambda/capacity-provider/{{<capacity-provider-name>}}`. Use this log group when creating the subscription filter.

For instructions on setting up a subscription filter for Firehose, including IAM role creation and permissions, see [Subscription filters with Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html#FirehoseExample) in the *Amazon CloudWatch User Guide*.

## Cross-account logging
<a name="lambda-managed-instances-firehose-cross-account"></a>

You can configure your capacity provider to send logs to a Firehose delivery stream in a different AWS account. This requires setting up a destination and configuring appropriate permissions in both accounts.

For instructions on setting up cross-account logging, including required IAM roles and policies, see [Setting up a new cross-account subscription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CrossAccountSubscriptions.html) in the *Amazon CloudWatch User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
