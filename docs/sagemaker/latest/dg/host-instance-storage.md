---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/host-instance-storage.html
---

# Instance storage volumes
<a name="host-instance-storage"></a>

When you create an endpoint, Amazon SageMaker AI attaches an Amazon Elastic Block Store (Amazon EBS) storage volume to Amazon EC2 instances that hosts the endpoint. The size of the storage volume is scalable, and storage options are divided into two categories: SSD-backed storage and HDD-backed storage.

For more information about Amazon EBS storages and features, see the following pages.
+ [Amazon EBS Features](https://aws.amazon.com/ebs/features/)
+ [ Amazon EBS User Guide ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)

For a full list of the host instance storage volumes, see [Host Instance Storage Volumes Table](https://aws.amazon.com/releasenotes/host-instance-storage-volumes-table/)

**Note**
Amazon SageMaker AI attaches an Amazon Elastic Block Store (Amazon EBS) storage volume to Amazon EC2 instances only when you create [Asynchronous inference](async-inference.md) or [Real-time inference](realtime-endpoints.md) endpoint types. For more information on customizing Amazon EBS storage volume, see [SageMaker AI endpoint parameters for large model inference](large-model-inference-hosting.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
