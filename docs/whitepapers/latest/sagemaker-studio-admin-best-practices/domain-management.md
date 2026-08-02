---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/domain-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Domain management
<a name="domain-management"></a>

An [Amazon SageMaker AI Domain](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-entity-status.html) consists of:
+ An associated [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) volume
+ A list of authorized users
+ A variety of security, application, policy, and [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) configurations

The following diagram provides a high-level view of various components that constitute a SageMaker AIStudio domain:

![A diagram depicting a high-level view of various components that constitute a SageMaker AI Studio Domain.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/sagemaker-studio-domain.png)
