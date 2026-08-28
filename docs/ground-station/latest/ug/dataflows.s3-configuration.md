---
source_url: https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.s3-configuration.html
---

# Set up and configure Amazon S3
<a name="dataflows.s3-configuration"></a>

 You can utilize a Amazon S3 bucket to receive your downlink signals using AWS Ground Station. To create the destination *s3-recording-config*, you must be able to specify a Amazon S3 bucket and an IAM role which authorizes AWS Ground Station to write files to the bucket.

 See [Amazon S3 Recording Config](how-it-works.config.md#how-it-works.config-s3-recording) for restrictions on the Amazon S3 bucket, IAM role, or AWS Ground Station config creation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
