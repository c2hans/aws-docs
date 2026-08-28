---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-08.html
---

# ACCT.08 Prevent public access to private Amazon S3 buckets
<a name="acct-08"></a>

By default, the root user of the AWS account and the IAM principal that created the bucket have permissions to read and write to Amazon S3 buckets. Additional IAM principals are granted access by using identity-based policies, and access conditions can be enforced by using a bucket policy. You can create bucket policies that grant the general public access to the bucket, creating a *public *bucket.

Buckets created on or after April 28, 2023 have the **Block Public Access** setting enabled by default. For buckets created before this date, a misconfigured bucket policy can unintentionally grant public access. You can help prevent this by enabling the **Block Public Access** setting for each bucket. If you have no current or future use cases for a public Amazon S3 bucket, enable this setting at the AWS account level.

**To prevent public access to Amazon S3 buckets**

1. Follow the steps in [Configure block public access settings for your Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/configuring-block-public-access-bucket.html) in the Amazon S3 documentation.

AWS Trusted Advisor generates a yellow finding for Amazon S3 buckets that allow list or read access to the public and generates a red finding for buckets that allow public uploads or deletes. Follow [ACCT.12 Monitor for and resolve AWS Trusted Advisor high-risk items](acct-12.md) to identify and correct misconfigured buckets. In the Amazon S3 console, you can see if your bucket is publicly accessible from the **Buckets** list.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
