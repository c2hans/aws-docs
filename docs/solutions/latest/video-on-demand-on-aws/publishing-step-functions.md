---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/publishing-step-functions.html
---

# Publishing Step Functions
<a name="publishing-step-functions"></a>

After the video is encoded, MediaConvert sends a notification to Amazon CloudWatch. An Amazon CloudWatch Events rule invokes the publishing AWS Step Functions step function, which validates the outputs, and updates the DynamoDB table with the new content details.

When the workflow is finished, Amazon SNS and/or Amazon SQS sends a publish notification based on the configuration you choose. If you choose to archive your source content, the source files are tagged to allow the [Amazon S3 lifecycle policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html) to move files to Amazon Glacier or Amazon Deep Archive.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
