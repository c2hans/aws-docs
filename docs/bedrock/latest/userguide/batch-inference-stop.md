---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html
---

# Stop a batch inference job
<a name="batch-inference-stop"></a>

To learn how to stop an ongoing batch inference job, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To stop a batch inference job**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. From the left navigation pane, select **Batch inference**.

1. Select a job to go to the job details page or select the option button next to a job.

1. Choose **Stop job**.

1. Review the message and choose **Stop job** to confirm.
**Note**
You're charged for tokens that have already been processed.

------
#### [ API ]

To stop a batch inference job, send a [StopModelInvocationJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StopModelInvocationJob.html) request with an [Amazon Bedrock control plane endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#br-cp) and provide the ID or ARN of the job in the `jobIdentifier` field.

If the job was successfully stopped, you receive an HTTP 200 response.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
