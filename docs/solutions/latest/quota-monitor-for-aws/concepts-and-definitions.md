---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution.

 **hub template**

AWS CloudFormation template for AWS and all associated components in the primary AWS account that will be used to monitor quotas. See **monitoring account**.

 **limit**

The maximum allocated value for a quota. The term limit was used previously as a synonym for quota.

 **monitored account**

Secondary AWS accounts where a spoke CloudFormation template has been launched to support quota monitoring.

 **monitoring account**

The primary AWS account where the hub CloudFormation template is deployed to monitor secondary AWS accounts.

 **organization**

An entity that you create to consolidate and manage your AWS accounts. An organization has one management account along with zero or more member accounts.

 **organizational unit**

A container for accounts within a [root](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) of an organization. An organizational unit (OU) can contain other OUs.

 **prerequisite template**

AWS CloudFormation template used to fulfill the prerequisites needed for monitoring quotas across AWS Organizations.

 **quota**

The maximum number of service resources, actions, operations, and items for your AWS account. Previously known as limit. See [quotas](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#Q).

 **Service Quotas**

An AWS service that helps you manage quotas for many AWS services from one location. Along with looking up the quota values, you can also request a quota increase from the Service Quotas console. See [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html).

 **spoke template**

AWS CloudFormation template to launch the Quota Monitor for AWS solution and all associated components in secondary accounts to support quota monitoring (monitored accounts).

 **StackSets**

AWS CloudFormation StackSets extend the capability of stacks by enabling you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation.

For a general reference of AWS terms, refer to the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).
