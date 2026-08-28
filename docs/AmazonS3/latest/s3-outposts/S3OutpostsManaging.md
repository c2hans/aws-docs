---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsManaging.html
---

# Managing S3 on Outposts storage
<a name="S3OutpostsManaging"></a>

With Amazon S3 on Outposts, you can create S3 buckets on your AWS Outposts and easily store and retrieve objects on premises for applications that require local data access, local data processing, and data residency. S3 on Outposts provides a new storage class, S3 Outposts (`OUTPOSTS`), which uses the Amazon S3 APIs, and is designed to store data durably and redundantly across multiple devices and servers on your AWS Outposts. You communicate with your Outpost bucket by using an access point and endpoint connection over a virtual private cloud (VPC). You can use the same APIs and features on Outpost buckets as you do on Amazon S3 buckets, including access policies, encryption, and tagging. You can use S3 on Outposts through the AWS Management Console, AWS Command Line Interface (AWS CLI), AWS SDKs, or REST API. For more information, see [What is Amazon S3 on Outposts?](S3onOutposts.md)

For more information about managing and sharing your Amazon S3 on Outposts storage capacity, see the following topics.

**Topics**
+ [Managing S3 Versioning for your S3 on Outposts bucket](S3OutpostsManagingVersioning.md)
+ [Creating and managing a lifecycle configuration for your Amazon S3 on Outposts bucket](S3OutpostsLifecycleManaging.md)
+ [Replicating objects for S3 on Outposts](S3OutpostsReplication.md)
+ [Sharing S3 on Outposts by using AWS RAM](outposts-sharing-with-ram.md)
+ [Other AWS services that use S3 on Outposts](S3OutpostsOtherServices.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
