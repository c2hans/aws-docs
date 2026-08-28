---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-16.html
---

# ACCT.16 Enable AWS Cost Anomaly Detection
<a name="acct-16"></a>

Enable [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to receive alerts when your AWS spending deviates from expected patterns. Cost Anomaly Detection uses machine learning to identify unusual spending without requiring you to define thresholds. It complements the budget alerts in [ACCT.10 Configure AWS Budgets to monitor your spending](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-10.html) by detecting unexpected cost spikes that may indicate compromised credentials, unauthorized resource usage, or misconfigured services.

For accounts created after March 27, 2023, Cost Anomaly Detection is enabled automatically when you activate [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), with a default monitor that tracks all AWS services and sends daily summary emails.

**To verify or enable Cost Anomaly Detection**

1. Open the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/).

1. In the left navigation pane, choose **Cost Anomaly Detection**.

1. If no monitors exist, choose **Create monitor**.

1. For monitor type, choose **AWS services** to monitor all deployed services.

1. Configure an alert subscription with your preferred email recipients and choose **Create monitor**.

For more information, see [Getting started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) in the AWS Billing and Cost Management documentation.

**Note**
AWS Cost Anomaly Detection is available at no additional charge.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
