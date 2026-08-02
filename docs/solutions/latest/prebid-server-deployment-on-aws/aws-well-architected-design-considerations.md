---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/aws-well-architected-design-considerations.html
---

# AWS Well-Architected design considerations
<a name="aws-well-architected-design-considerations"></a>

This solution uses the best practices from the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/), which helps customers design and operate reliable, secure, efficient, and cost-effective workloads in the cloud.

This section describes how the design principles and best practices of the Well-Architected Framework benefit this solution.

## Operational excellence
<a name="operational-excellence"></a>

This section describes how we architected this solution using the principles and best practices of the [operational excellence pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html).

 **Perform operations as code** - This solution’s infrastructure is entirely specified using AWS Cloud Development Kit(CDK) v2.0 in Python 3.x and deployed as a CloudFormation template. Application logging and metric workflows are automated with [Amazon EventBridge](https://aws.amazon.com/eventbridge/) and Lambda.

 **Make frequent, small, reversible changes** - This solution is designed to be customized by the end user, if desired. The solution can be forked from the [GitHub repository](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws) into a customer’s account, customized, rebuilt, hosted in a customer’s Amazon S3 buckets, and deployed via CDK. This process can be repeated iteratively to test changes to the default solution.

 **Use managed services** - Operational burden is reduced through the use of Amazon ECS to automatically manage and scale application containers in response to client request traffic.

## Security
<a name="security"></a>

This section describes how we architected this solution using the principles and best practices of the [security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

 **Implement a strong identity foundation** - All interactions among resources created by the solution are secured using [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles, policies, and signature V4 request signing. All credentials used to interact among resources are temporary, and typically have a lifetime of less than one hour.

 **Maintain traceability** - Runtime logging by Lambda functions installed by the solution is sent to [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) and preserved with the default retention settings.

 **Apply security at all layers** - Interactions among resources require permissions defined in the related resource’s IAM role. AWS WAF protects public application endpoints from common web exploits. Security groups restrict inbound and outbound traffic at the resource level within the customers Amazon VPC.

 **Protect data in transit and at rest** - All data is encrypted in transit via TLS-protected API requests. All persistent resources are configured for encryption at rest. Application-level data is encrypted with [AWS Key Management Service](https://aws.amazon.com/kms/) using customer managed keys.

## Reliability
<a name="reliability"></a>

This section describes how we architected this solution using the principles and best practices of the [reliability pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

 **Automatically recover from failure** - The solution uses [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics and alarms are used to monitor the operation of the solution with the ability to notify users or other systems when thresholds are breached.

 **Scale horizontally to increase aggregate workload availability** - Client traffic is horizontally scaled with Amazon Elastic Container Service, distributed across containers using [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/).

 **Stop guessing capacity** - Resource demand is automatically monitored with Amazon ECS, maintaining optimal resource levels to satisfy demand without over- or under-provisioning.

## Performance efficiency
<a name="performance-efficiency"></a>

This section describes how we architected this solution using the principles and best practices of the [performance efficiency pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

 **Go global in minutes** - The AWS CDK stack can be used to create a stack in any compatible Region, with the ability to deploy multiple stacks in the same Region for testing and production.

 **Use serverless architectures** - Amazon ECS uses [AWS Fargate](https://aws.amazon.com/fargate/) serverless deployment to manage container resources at cloud scale without the operational burden of managing physical servers.

 **Consider mechanical sympathy** - Application metrics data is transformed, partitioned, and stored in Amazon S3 and [AWS Glue](https://docs.aws.amazon.com/glue/) in accordance with common data access patterns to improve query performance.

## Cost optimization
<a name="cost-optimization"></a>

This section describes how we architected this solution using the principles and best practices of the [cost optimization pillar](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

 **Adopt a consumption model** - Serverless computing is used to only pay for consumed compute resources on Amazon ECS.

## Sustainability
<a name="sustainability"></a>

This section describes how we architected this solution using the principles and best practices of the [sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

 **Maximize utilization** - Managed services allow for optimal resource provisioning to ensure high utilization while minimizing idle resources to maximize the energy efficiency of the underlying hardware.

 **Use managed services** - This solution uses managed services such as Fargate and Lambda, which share resources across a broad customer base and reduces the amount of infrastructure needed to support cloud workloads.
