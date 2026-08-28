---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.html
---

# Creating and managing a lifecycle configuration for your Amazon S3 on Outposts bucket
<a name="S3OutpostsLifecycleManaging"></a>

You can use S3 Lifecycle to optimize storage capacity for Amazon S3 on Outposts. You can create lifecycle rules to expire objects as they age or are replaced by newer versions. You can create, enable, disable, or delete a lifecycle rule.

For more information about S3 Lifecycle, see [Creating and managing a lifecycle configuration for your Amazon S3 on Outposts bucket](#S3OutpostsLifecycleManaging).

**Note**
The AWS account that creates the bucket owns it and is the only one that can create, enable, disable, or delete a lifecycle rule.

To create and manage the lifecycle configuration for your S3 on Outposts bucket, see the following topics.

**Topics**
+ [Creating and managing a lifecycle rule by using the AWS Management Console](S3OutpostsLifecycleConsole.md)
+ [Creating and managing a lifecycle configuration by using the AWS CLI and SDK for Java](S3OutpostsLifecycleCLIJava.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
