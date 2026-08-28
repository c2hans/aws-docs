---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud.html
---

# Migrate an F5 BIG-IP workload to F5 BIG-IP VE on the AWS Cloud
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud"></a>

*Deepak Kumar, Amazon Web Services*

## Summary
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-summary"></a>

Organizations are looking to migrate to the AWS Cloud to increase their agility and resilience. After you migrate your [F5 BIG-IP ](https://www.f5.com/products/big-ip-services)security and traffic management solutions to the AWS Cloud, you can focus on agility and adoption of high-value operational models across your enterprise architecture.

This pattern describes how to migrate an F5 BIG-IP workload to an [F5 BIG-IP Virtual Edition (VE)](https://www.f5.com/products/big-ip-services/virtual-editions) workload on the AWS Cloud. The workload will be migrated by rehosting the existing environment and deploying aspects of replatforming, such as service discovery and API integrations. [AWS CloudFormation templates](https://github.com/F5Networks/f5-aws-cloudformation) accelerate your workload’s migration to the AWS Cloud.

This pattern is intended for technical engineering and architectural teams that are migrating F5 security and traffic management solutions, and accompanies the guide [Migrating from F5 BIG-IP to F5 BIG-IP VE on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/welcome.html) on the AWS Prescriptive Guidance website.

## Prerequisites and limitations
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-prereqs"></a>

**Prerequisites **
+ An existing on-premises F5 BIG-IP workload.
+ Existing F5 licenses for BIG-IP VE versions.
+ An active AWS account.
+ An existing virtual private cloud (VPC) configured with an egress through a NAT gateway or Elastic IP address, and configured with access to the following endpoints: Amazon Simple Storage Service (Amazon S3), Amazon Elastic Compute Cloud (Amazon EC2), AWS Security Token Service (AWS STS), and Amazon CloudWatch. You can also modify the [Modular and scalable VPC architecture](https://aws.amazon.com/quickstart/architecture/vpc/) Quick Start as a building block for your deployments.
+ One or two existing Availability Zones, depending on your requirements.
+ Three existing private subnets in each Availability Zone.
+ AWS CloudFormation templates, [available in the F5 GitHub repository](https://github.com/F5Networks/f5-aws-cloudformation/blob/master/template-index.md).

During the migration, you might also use the following, depending on your requirements:
+ An [F5 Cloud Failover Extension](https://clouddocs.f5.com/products/extensions/f5-cloud-failover/latest/) to manage Elastic IP address mapping, secondary IP mapping, and route table changes.
+ If you use multiple Availability Zones, you will need to use the F5 Cloud Failover Extensions to handle the Elastic IP mapping to virtual servers.
+ You should consider using [F5 Application Services 3 (AS3)](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/), [F5 Application Services Templates (FAST)](https://clouddocs.f5.com/products/extensions/f5-appsvcs-templates/latest/), or another infrastructure as code (IaC) model to manage the configurations. Preparing the configurations in an IaC model and using code repositories will help with the migration and your ongoing management efforts.

**Expertise**
+ This pattern requires familiarity with how one or more VPCs can be connected to existing data centers. For more information about this, see [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) in the Amazon VPC documentation.
+ Familiarity is also required with F5 products and modules, including [Traffic Management Operating System (TMOS)](https://www.f5.com/services/resources/white-papers/tmos-redefining-the-solution), [Local Traffic Manager (LTM)](https://www.f5.com/products/big-ip-services/local-traffic-manager), [Global Traffic Manager (GTM)](https://techdocs.f5.com/kb/en-us/products/big-ip_gtm/manuals/product/gtm-concepts-11-5-0/1.html#unique_9842886), [Access Policy Manager (APM)](https://www.f5.com/products/security/access-policy-manager), [Application Security Manager (ASM)](https://www.f5.com/pdf/products/big-ip-application-security-manager-overview.pdf), [Advanced Firewall Manager (AFM)](https://www.f5.com/products/security/advanced-firewall-manager), and [BIG-IQ](https://www.f5.com/products/automation-and-orchestration/big-iq).

**Product versions**
+ We recommend that you use F5 BIG-IP [version 13.1](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-ve-13-1-0.html) or later, although the pattern supports F5 BIG-IP [version 12.1](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/releasenotes/product/relnote-bigip-12-1-4.html) or later.

## Architecture
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-architecture"></a>

**Source technology stack**
+ F5 BIG-IP workload

**Target technology stack  **
+ Amazon CloudFront
+ CloudWatch
+ Amazon EC2
+ Amazon S3
+ Amazon VPC
+ AWS Global Accelerator
+ AWS STS
+ AWS Transit Gateway
+ F5 BIG-IP VE

**Target architecture **

![Architecture to migrate an F5 BIG-IP workload to an F5 BIG-IP VE workload.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/586fe806-fac1-48d3-9eb1-45a6c86430dc/images/16d7fc09-1ffe-4721-b503-d971db84cbae.png)

## Tools
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-tools"></a>
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) speeds up distribution of your web content by delivering it through a worldwide network of data centers, which lowers latency and improves performance.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) helps you request temporary, limited-privilege credentials for users.
+ [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a central hub that connects virtual private clouds (VPCs) and on-premises networks.
+ [Amazon Virtual Private Cloud (Amazon VPC) ](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

## Epics
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-epics"></a>

### Discovery and assessment
<a name="discovery-and-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Assess the performance of F5 BIG-IP. | Collect and record the performance metrics of the applications on the virtual server, and metrics of systems that will be migrated. This will help to correctly size the target AWS infrastructure for better cost optimization. | F5 Architect, Engineer and Network Architect, Engineer |
| Evaluate the F5 BIG-IP operating system and configuration. | Evaluate which objects will be migrated and if a network structure needs to be maintained, such as VLANs. | F5 Architect, Engineer |
| Evaluate F5 license options. | Evaluate which license and consumption model you will require. This assessment should be based on your evaluation of the F5 BIG-IP operating system and configuration. | F5 Architect, Engineer |
| Evaluate the public applications. | Determine which applications will require public IP addresses. Align those applications to the required instances and clusters to meet performance and service-level agreement (SLA) requirements. | F5 Architect, Cloud Architect, Network Architect, Engineer, App Teams |
| Evaluate internal applications. | Evaluate which applications will be used by internal users. Make sure you know where those internal users sit in the organization and how those environments connect to the AWS Cloud. You should also make sure those applications can use domain name system (DNS) as part of the default domain. | F5 Architect, Cloud Architect, Network Architect, Engineer, App Teams |
| Finalize the AMI. | Not all F5 BIG-IP versions are created as Amazon Machine Images (AMIs). You can use the F5 BIG-IP Image Generator Tool if you have specific required quick-fix engineering (QFE) versions. For more information about this tool, see the "Related resources" section. | F5 Architect, Cloud Architect, Engineer |
| Finalize the instance types and architecture. | Decide on the instance types, VPC architecture, and interconnected architecture. | F5 Architect, Cloud Architect, Network Architect, Engineer |

### Complete security and compliance-related activities
<a name="complete-security-and-compliance-related-activities"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Document the existing F5 security policies. | Collect and document existing F5 security policies. Make sure you create a copy of them in a secure code repository. | F5 Architect, Engineer |
| Encrypt the AMI. | (Optional) Your organization might require encryption of data at rest. For more information about creating a custom Bring Your Own License (BYOL) image, see the "Related resources" section. | F5 Architect, Engineer Cloud Architect, Engineer |
| Harden the devices. | This will help protect against potential vulnerabilities. | F5 Architect, Engineer |

### Configure your new AWS environment
<a name="configure-your-new-aws-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create edge and security accounts. | Sign in to the AWS Management Console and create the AWS accounts that will provide and operate the edge and security services. These accounts might be different from the accounts that operate VPCs for shared services and applications. This step can be completed as part of a landing zone. | Cloud Architect, Engineer |
| Deploy edge and security VPCs. | Set up and configure the VPCs required to deliver edge and security services. | Cloud Architect, Engineer |
| Connect to the source data center. | Connect to the source data center that hosts your F5 BIG-IP workload. | Cloud Architect, Network Architect, Engineer |
| Deploy the VPC connections. | Connect the edge and security service VPCs to the application VPCs. | Network Architect, Engineer |
| Deploy the instances. | Deploy the instances by using the CloudFormation templates from the "Related resources" section. | F5 Architect, Engineer |
| Test and configure instance failover. | Make sure that the AWS Advanced HA iAPP template or F5 Cloud Failover Extension is configured and operating correctly. | F5 Architect, Engineer |

### Configure networking
<a name="configure-networking"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the VPC topology. | Open the Amazon VPC console and make sure that your VPC has all the required subnets and protections for the F5 BIG-IP VE deployment. | Network Architect, F5 Architect, Cloud Architect, Engineer |
| Prepare your VPC endpoints. | Prepare the VPC endpoints for Amazon EC2, Amazon S3, and AWS STS if an F5 BIG-IP workload does not have access to a NAT Gateway or Elastic IP address on a TMM interface. | Cloud Architect, Engineer |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the configuration. | Migrate the F5 BIG-IP configuration to F5 BIG-IP VE on the AWS Cloud. | F5 Architect, Engineer |
| Associate the secondary IPs. | Virtual server IP addresses have a relationship with the secondary IP addresses assigned to the instances. Assign secondary IP addresses and make sure "Allow remap/reassignment" is selected. | F5 Architect, Engineer |

### Test configurations
<a name="test-configurations"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the virtual server configurations. | Test the virtual servers. | F5 Architect, App Teams |

### Finalize operations
<a name="finalize-operations"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the backup strategy. | Systems must be shut down to create a full snapshot. For more information, see "Updating an F5 BIG-IP virtual machine" in the "Related resources" section. | F5 Architect, Cloud Architect, Engineer |
| Create the cluster failover runbook. | Make sure that the failover runbook process is complete. | F5 Architect, Engineer |
| Set up and validate logging. | Configure F5 Telemetry Streaming to send logs to the required destinations. | F5 Architect, Engineer |

### Complete the cutover
<a name="complete-the-cutover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Cut over to the new deployment. |  | F5 Architect, Cloud Architect, Network Architect, Engineer, AppTeams |

## Related resources
<a name="migrate-an-f5-big-ip-workload-to-f5-big-ip-ve-on-the-aws-cloud-resources"></a>

**Migration guide**
+ [Migrating from F5 BIG-IP to F5 BIG-IP VE on the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/welcome.html)

**F5 resources**
+ [CloudFormation templates in the F5 GitHub repository](https://github.com/F5Networks/f5-aws-cloudformation)
+ [F5 in AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=74d946f0-fa54-4d9f-99e8-ff3bd8eb2745)
+ [F5 BIG-IP VE overview](https://www.f5.com/products/big-ip-services/virtual-editions)
+ [Example Quickstart - BIG-IP Virtual Edition with WAF (LTM \+ ASM)](https://github.com/F5Networks/f5-aws-cloudformation-v2/tree/main/examples/quickstart)
+ [F5 Application services on AWS: an overview (video)](https://www.youtube.com/watch?v=kutVjRHOAXo)
+ [F5 Application Services 3 Extension User Guide ](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/)
+ [F5 cloud documentation](https://clouddocs.f5.com/training/community/public-cloud/html/intro.html)
+ [F5 iControl REST wiki](https://clouddocs.f5.com/api/icontrol-rest/)
+ [F5 Overview of single configuration files (11.x - 15.x)](https://support.f5.com/csp/article/K13408)
+ [F5 whitepapers](https://www.f5.com/services/resources/white-papers)
+ [F5 BIG-IP Image Generator Tool](https://clouddocs.f5.com/cloud/public/v1/ve-image-gen_index.html)
+ [Updating an F5 BIG-IP VE virtual machine](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-ve-setup-vmware-esxi-11-5-0/3.html)
+ [Overview of the UCS archive "platform-migrate" option](https://support.f5.com/csp/article/K82540512)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
