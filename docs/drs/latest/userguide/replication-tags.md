---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/replication-tags.html
---

# Elastic Disaster Recovery tags
<a name="replication-tags"></a>

Add custom **tags** to resources created by AWS Elastic Disaster Recovery in your AWS account. You can add up to 50 tags.

These are resources required to facilitate data replication, drilling and recovery. Each tag consists of a key and an optional value. You can add a custom tag to all of the AWS resources that are created on your AWS account during the normal operation of AWS Elastic Disaster Recovery.

To add new tags:

1.  Choose **Add new tag**.

1.  Enter a **custom tag key** and an optional tag value.

**Note**
AWS Elastic Disaster Recovery already adds tags to every resource it creates, including service tags and user tags.
These resources include:
Amazon EC2 instances
Amazon EC2 launch templates
Amazon EBS volumes
Snapshots

Learn more about AWS tags in [Tag your Amazon EC2 resources.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
