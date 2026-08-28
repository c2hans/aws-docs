---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html
---

# Configuring file system access for Lambda functions
<a name="configuration-filesystem"></a>

You can configure a Lambda function to mount a file system to a local directory. Lambda supports the following file system types:
+ **[Amazon Elastic File System (Amazon EFS)](configuration-filesystem-efs.md)** – Serverless file system that scales automatically with your workloads.
+ **[Amazon S3 Files](configuration-filesystem-s3files.md)** – Serverless file system for mounting your Amazon S3 bucket. Amazon S3 Files provides access to your Amazon S3 objects as files using standard file system operations such as read and write on the local mount path.

**Note**
A Lambda function can use either Amazon EFS or Amazon S3 Files, but not both. If your function is already configured with one file system type, you must remove it before configuring the other.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
