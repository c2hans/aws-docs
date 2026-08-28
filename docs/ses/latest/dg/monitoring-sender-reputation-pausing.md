---
source_url: https://docs.aws.amazon.com/ses/latest/dg/monitoring-sender-reputation-pausing.html
---

# Automatically pausing email sending
<a name="monitoring-sender-reputation-pausing"></a>

To protect your sender reputation, you can temporarily pause email sending for messages sent using specific configuration sets, or for all messages sent from your Amazon SES account in a specific AWS Region.

By using Amazon CloudWatch and Lambda, you can create a solution that automatically pauses your email sending when your reputation metrics (such as bounce rate or complaint rate) exceed certain thresholds. This topic contains procedures for setting up this solution.

**Topics**
+ [Automatically pausing email sending for your entire Amazon SES account](monitoring-sender-reputation-pausing-account.md)
+ [Automatically pausing email sending for a configuration set](monitoring-sender-reputation-pausing-configuration-set.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
