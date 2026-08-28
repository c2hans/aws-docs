---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up.html
---

# Prerequisites to start using MediaConvert
<a name="setting-up"></a>

Before you start using MediaConvert, you need an AWS account, at least one input file stored in Amazon S3 or on an HTTP/HTTPS server, an Amazon S3 bucket for your output files, and an IAM role with the correct permissions.

For information on how to upload files to Amazon S3, see [Uploading objects in the *Amazon S3 User Guide*](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html).

For information about creating an Amazon S3 bucket for your output destination, see [Creating a bucket in the *Amazon S3 User Guide*](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).

The following topics describe how to sign up for an AWS account and then how to configure your IAM role.

**Topics**
+ [Setting up IAM permissions](iam-role.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
