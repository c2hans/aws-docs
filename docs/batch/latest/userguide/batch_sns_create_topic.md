---
source_url: https://docs.aws.amazon.com/batch/latest/userguide/batch_sns_create_topic.html
---

# Tutorial: Create and subscribe to an Amazon SNS topic
<a name="batch_sns_create_topic"></a>

 For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule.

**To create an Amazon SNS topic**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. Choose **Topics**, **Create topic**.

1. For **Type**, choose **Standard**.

1. For **Name**, enter **JobFailedAlert** and choose **Create topic**.

1. On the **JobFailedAlert** screen, choose **Create subscription**.

1. For **Protocol**, choose **Email**.

1. For **Endpoint**, enter an email address that you currently have access to and choose **Create subscription**.

1. Check your email account, and wait to receive a subscription confirmation email message. When you receive it, choose **Confirm subscription**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Batch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query batch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
