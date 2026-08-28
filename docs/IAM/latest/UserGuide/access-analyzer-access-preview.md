---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-access-preview.html
---

# Preview access
<a name="access-analyzer-access-preview"></a>

In addition to helping you identify resources that are shared with an external entity, AWS IAM Access Analyzer also shows you a preview of IAM Access Analyzer findings before deploying resource permissions so you can validate that your policy changes grant only intended public and cross-account access to your resource. This helps you start with intended external access to your resources.

You can preview and validate public and cross-account access to your Amazon S3 buckets in the [Amazon S3](https://aws.amazon.com/s3/) console. You can also use IAM Access Analyzer APIs to preview public and cross-account access for your Amazon S3 buckets, AWS KMS keys, IAM roles, Amazon SQS queues and Secrets Manager secrets by providing proposed permissions for your resource.

**Topics**
+ [Previewing access in Amazon S3 console](access-analyzer-preview-access-s3-console.md)
+ [Previewing access with IAM Access Analyzer APIs](access-analyzer-preview-access-apis.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
