---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhccost04-bp01.html
---

# DRHCCOST04-BP01 Implement mechanisms to manage the lifecycle of Amazon S3 data, EBS volumes, and snapshots
<a name="drhccost04-bp01"></a>

 Apply data lifecycle management practices to hybrid edge environments.

 **Desired outcome:** You can implement familiar mechanisms like you would in-Region to manage the lifecycle of your hybrid edge data.

 **Benefits of establishing this best practice:** Through the use of familiar mechanisms, you can retain relevant data.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance-50"></a>

 Outposts contain fixed capacity specific to their configuration. You can manage the lifecycle of your data with familiar services such as [S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3OutpostsLifecycleManaging.html) for Amazon S3 on Outposts and [Data Lifecycle Manager](https://aws.amazon.com/about-aws/whats-new/2021/02/introducing-amazon-ebs-local-snapshots-on-outposts/) for Amazon EBS. Consider [archiving Amazon S3 content to AWS Regions using DataSync](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/) if possible.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
