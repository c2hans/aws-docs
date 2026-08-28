---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/customization.html
---

# Customization
<a name="customization"></a>

 This solution uses a serverless architecture that you can update and extend for your specific video processing needs. For example, you can add or replace Amazon SNS with [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) to allow upstream workflows to subscribe and get notifications on the workflow outputs. You can also add multiple folders and job settings files in the source S3 bucket to accommodate different use cases. For details, refer to [Working with mulitple job settings files](job-settings-file.md#working-with-multiple-job-settings-files).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
