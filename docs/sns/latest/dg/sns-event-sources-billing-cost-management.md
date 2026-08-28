---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-event-sources-billing-cost-management.html
---

# Billing & cost management services
<a name="sns-event-sources-billing-cost-management"></a>

The following table describes how AWS Billing and Cost Management integrates with Amazon SNS to provide notifications for budgets, price changes, and cost anomalies.

You can leverage this integration to set-up Amazon SNS topics to receive real-time alerts about your AWS spending, helping you monitor costs and respond to unexpected charges efficiently.

| AWS service | Benefit of using with Amazon SNS |
| --- | --- |
| [AWS Billing and Cost Management](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) – Provides features that help you monitor your costs and pay your bill. | Receive budget notifications, price change notifications, and anomaly alerts. For more information, see the following pages in the AWS Billing User Guide:+  [Creating an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-sns-policy.html) <br />+  [Setting up notifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-notification.html) <br />+  [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-ad.html)  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
