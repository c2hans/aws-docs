---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/sqs-lambda.html
---

# Using Amazon SQS with AWS Lambda in the AWS Toolkit for JetBrains
<a name="sqs-lambda"></a>

The following procedure details how to configure Amazon SQS queues as Lambda triggers in the AWS Toolkit for JetBrains.

**To configure an Amazon SQS queue as a Lambda triggers**

1. From the AWS Toolkit for JetBrains, expand the AWS Explorer to view your AWS services.

1. From the AWS Explorer, expand the **Amazon SQS** service to view a list of your existing queues.

1. Right-click the queue you want to work with and choose **Configure Lambda Trigger**.

1. In the dialog box, from the drop-down menu, choose the Lambda function that you want to trigger.

1. Choose **Configure**.

1. If the Lambda function lacks the necessary IAM permissions for Amazon SQS to run it, the toolkit generates a minimal policy that you can add to the IAM role for the Lambda function.

   Choose **Add Policy**.

After you configure your queue, you get a status message about the applied changes, including any applicable error messages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
