---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/sqs-sns.html
---

# Using Amazon SQS with Amazon SNS in the AWS Toolkit for JetBrains
<a name="sqs-sns"></a>

The following procedure details how to subscribe Standard Amazon SQS queues to Amazon SNS topics using the AWS Toolkit for JetBrains.

**Note**
You can't subscribe FIFO Amazon SQS queues to Amazon SNS topics.

**To subscribe a Standard Amazon SQS queue to an Amazon SNS topic**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue you want to work with and choose **Subscribe to SNS topic...**.

1. In the dialog box, from the drop-down menu, choose an Amazon SNS topic, and then choose **Subscribe**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
