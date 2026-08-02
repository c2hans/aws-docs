---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-cloudtrail.html
---

# AWS CloudTrail
<a name="aws-cloudtrail"></a>

 To embrace the DevOps principles of collaboration, communication, and transparency, it’s important to understand who is making modifications to your infrastructure. In AWS, this transparency is provided by [AWS CloudTrail](https://aws.amazon.com/cloudtrail). All AWS interactions are handled through AWS API calls that are monitored and logged by AWS CloudTrail. All generated log files are stored in an Amazon S3 bucket that you define. Log files are encrypted using [Amazon S3 server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingServerSideEncryption.html) (SSE). All API calls are logged whether they come directly from a user or on behalf of a user by an AWS service. Numerous groups can benefit from CloudTrail logs, including operations teams for support, security teams for governance, and finance teams for billing.
