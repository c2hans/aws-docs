---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-storage.html
---

# Storage in Batch Transform
<a name="batch-transform-storage"></a>

When you run a batch transform job, Amazon SageMaker AI attaches an Amazon Elastic Block Store storage volume to Amazon EC2 instances that process your job. The volume stores your model, and the size of the storage volume is fixed at 30 GB. You have the option to encrypt your model at rest in the storage volume.

**Note**
If you have a large model, you may encounter an `InternalServerError`.

For more information about Amazon EBS storage and features, see the following pages:
+ [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) in the Amazon EC2 User Guide
+ [Amazon EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html) in the Amazon EC2 User Guide

**Note**
G4dn instances come with their own local SSD storage. To learn more about G4dn instances, see the [Amazon EC2 G4 Instances](https://aws.amazon.com/ec2/instance-types/g4/) page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
