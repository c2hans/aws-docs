---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cloudtrail.html
---

# AWS CloudTrail
<a name="aws-cloudtrail"></a>

 To embrace the DevOps principles of collaboration, communication, and transparency, it’s important to understand who is making modifications to your infrastructure. In AWS, this transparency is provided by [AWS CloudTrail](https://aws.amazon.com/cloudtrail). All AWS interactions are handled through AWS API calls that are monitored and logged by AWS CloudTrail. All generated log files are stored in an Amazon S3 bucket that you define. Log files are encrypted using [Amazon S3 server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) (SSE). All API calls are logged whether they come directly from a user or on behalf of a user by an AWS service. Numerous groups can benefit from CloudTrail logs, including operations teams for support, security teams for governance, and finance teams for billing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
