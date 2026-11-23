---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-from-vmware-to-the-aws-cloud/resource-management.html
---

# Resource management

This section covers how to transition the following VMware resource management functions to AWS cloud-native services:
+ vSphere resource allocation and optimization
+ vSphere HA

## vSphere resource allocation and optimization
<a name="vsphere-resource-allocation-and-optimization.188931ff-f180-556a-88f7-9fd62cc0f56b"></a>

VMware vSphere Distributed Resource Scheduler (DRS) automatically monitors and balances workload resources across ESXi hosts in a cluster. When in AWS, the hypervisor host and the underlying infrastructure are managed by AWS. With this approach, you can focus on application and business outcomes, reducing your operational overhead.

AWS automated resource management solutions including the following:
+ [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) dynamically adjusts Amazon EC2 instance numbers based on demand.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/) (ELB) distributes incoming traffic across multiple instances.
+ [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) analyzes and recommends optimal instance configurations.
+ [Instance Scheduler on AWS](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/solution-overview.html) enables automated scheduling of instance operations.

Collectively, these AWS solutions deliver resource optimization capabilities without the operational overhead associated with on-premises infrastructure management.

## vSphere HA
<a name="vsphere-ha.cc07f454-f682-5410-b013-369fa68d0959"></a>

High availability (HA) in VMware vSphere HA and AWS follow fundamentally different approaches. vSphere HA provides automatic failover and restart of virtual machines across ESXi hosts for on-premises workloads. AWS manages infrastructure-level availability through its underlying platform, backed by [service-level agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/) and service-level objectives (SLOs) for all paid, generally available services.

AWS services such as AWS Transform MGN and AWS Database Migration Service (AWS DMS) facilitate migrations between different environments. The AWS approach provides your organization with more flexibility and control of your resources.

To help guide your approach for resource management, following are key specifications:
+ **Virtual machine management** – The [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html) serves as a central management resource for managing EC2 instances.
+ **Automation and orchestration** – AWS provides multiple automation services such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) for IaC and [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) for resource management. These AWS services support comprehensive automation of resource provisioning and management within the cloud environment.
+ **Monitoring and logging** – AWS offers [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for resource and application monitoring, and [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) handles logging and auditing of AWS account activities. AWS monitoring combines [VPC Flow Logs ](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)for network traffic analysis and [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) for application request tracking, providing complete visibility into network and application performance. These integrated services enable organizations to maintain visibility and track operational metrics across their respective environments.
+ **Security and compliance** – AWS integrated security services include [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html) for centralized security management, [AWS WAF](https://docs.aws.amazon.com/waf/) for web application protection, [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) for DDoS protection, and [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for access control. These AWS services provide multi-layered security and compliance capabilities across the cloud infrastructure.
+ **Management and governance** – To optimize cloud operations, AWS Systems Manager enables centralized management of AWS resources. Cost management is addressed through [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) and [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html). [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps manage multiple AWS accounts. [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/) monitors your applications and automatically adjusts capacity to maintain steady, predictable performance at the lowest possible cost. [AWS License Manager](https://aws.amazon.com/license-manager) makes it easier to manage licenses in AWS and on-premises servers. These services collectively enable efficient resource management, cost optimization, and operational excellence in AWS environments.
