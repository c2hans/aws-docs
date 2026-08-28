---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/clone-model-distillation-job.html
---

# Clone a distillation job
<a name="clone-model-distillation-job"></a>

You can use the Amazon Bedrock console to clone your distillation job. Clone your distillation job to run multiple jobs with similar settings. Use cloning to try again with a job that you stopped or had an issue. The new job inherits all settings except Service access configuration, any VPC settings, and any Tags.

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. From the left navigation pane, choose **Custom models** under **Tune**.

1. Choose the distillation job that you want to clone, then choose **Clone job**.

1. If needed, adjust your job's settings.

1. Choose **Create distillation job** to start the new job.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
