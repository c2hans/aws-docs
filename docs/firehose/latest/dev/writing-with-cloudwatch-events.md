---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/writing-with-cloudwatch-events.html
---

# Send CloudWatch Events to Firehose
<a name="writing-with-cloudwatch-events"></a>

You can configure Amazon CloudWatch to send events to a Firehose stream by adding a target to a CloudWatch Events rule.

**To create a target for a CloudWatch Events rule that sends events to an existing Firehose stream**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Create rule**.

1. On the **Step 1: Create rule** page, for **Targets**, choose **Add target**, and then choose **Firehose stream**.

1. Choose an existing **Firehose stream**.

For more information about creating CloudWatch Events rules, see [Getting Started with Amazon CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CWE_GettingStarted.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
