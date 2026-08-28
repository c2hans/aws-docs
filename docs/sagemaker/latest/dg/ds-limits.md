---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/ds-limits.html
---

# Limits
<a name="ds-limits"></a>

Spaces run as pods on HyperPod EKS nodes with attached EBS volumes. The number of Spaces that can be deployed per node is constrained by AWS infrastructure limits.

**EBS Volume Limits per Node**

Reference: [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume\_limits.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html)

EC2 nodes have a maximum number of EBS volumes that can be attached. Since each Space typically uses one EBS volume, this limits how many Spaces with dedicated EBS storage can run on a single node.

**Maximum Pods per HyperPod Node**

Reference: [https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-prerequisites.html)

Each HyperPod instance type supports a maximum number of pods based on available IP addresses from the VPC CNI plugin. Since each Space runs as a pod, this directly caps the number of Spaces per node.

**Impact**

The effective limit for Spaces per node is whichever constraint is reached first.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
