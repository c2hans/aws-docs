---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/manage-and-configure-assets-with-aws-config.html
---

# Manage and Configure Assets with AWS Config
<a name="manage-and-configure-assets-with-aws-config"></a>

[AWS Config](https://aws.amazon.com/config/) provides a detailed view of the configuration of many types of AWS resources in your AWS account. This includes how the resources are related to one another, and how they were previously configured, so you can see how the configurations and relationships change over time.

![AWS Config monitoring changing resources and applying rules for API access and storage.](http://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/images/aws-config-architecture.png)

*Figure 1 – Monitor configuration changes over time with AWS Config *

An AWS resource is an entity that you can work with in AWS, such as an EC2 instance, an [Amazon Elastic Block Store (amazon EBS)](https://aws.amazon.com/ebs/) volume, a security group, or an [Amazon Virtual Private Cloud (Amazon VPC)](https://aws.amazon.com/vpc/). For a complete list of AWS resources supported by AWS Config, see [Supported AWS Resource Types for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html).

With AWS Config, you can do the following:
+ Evaluate your AWS resource configurations to verify the settings are correct.
+ Get a snapshot of the current configurations of the supported resources that are associated with your AWS Account.
+ Get configurations of one or more resources that exist in your account.
+ Get historical configurations of one or more resources.
+ Get a notification when a resource is created, modified, or deleted.
+ See relationships between resources (for example, find all resources that use a particular security group).

Conformance Packs can be used to simplify the deployment of collections of AWS Config rules and remediation actions and can be used as starting point for creating your own rules.
