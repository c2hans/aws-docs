---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-control-tower-landing-zone/introduction.html
---

# Designing an AWS Control Tower landing zone
<a name="introduction"></a>

*Vikas Dewangan, Emelie Akerstrom, and Pooja Banerjee, Amazon Web Services*

Typically, you begin a cloud adoption journey by conceptualizing and designing a landing zone, which is a well-architected, multi-account AWS environment that is scalable and secure. A landing zone creates an agile and scalable cloud environment. It also helps you quickly launch and deploy workloads and applications into your infrastructure, which helps accelerate your digital transformation and cloud journey. You can use [AWS Control Tower](https://aws.amazon.com/controltower/) to set up and govern a secure, multi-account AWS environment for your landing zone based on AWS best practices. The landing zone includes foundational AWS services that are created before you deploy workloads.

Enterprises can use a landing zone at various stages of their cloud adoption journey. Some enterprises have recently started their journey on AWS, aren't aware of AWS best practices for multi-account strategy, security, and networking, and aren't sure how to set up their landing zones. Other enterprises have been using AWS for a while and want to scale their landing zone to deploy additional workloads.

This guide is for enterprises that have decided to set up an AWS Control Tower landing zone and want to create a design document that covers the key functionality of the landing zone. The guide covers best practices and patterns for setting up the account structure and configuring networking, logging, authentication, and other aspects of the landing zone. It also provides examples of how to present this information in your design documents. The key outcome from this exercise is a design artifact that documents the decisions that were made and the architectures that were agreed upon as the basis of implementing the landing zone. This could be followed by new cloud-native application development or the migration of existing workloads into the landing zone.

## Design process
<a name="design-process"></a>

IT infrastructure teams and enterprise architects usually create a design document that addresses the important parts of a landing zone. Stakeholders must approve the design document before the landing zone is implemented. This guide accelerates the design process for IT infrastructure teams, enterprise architects, and cloud migration teams by providing a landing zone design template that's aligned with the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/). It helps you accelerate your cloud adoption by outlining the foundational pillars of the landing zone design. The key landing zone topics covered in this design guide are:
+ [Setting up a landing zone ](setup.md) – Provides an overview of the basic landing zone setup, including where it should be deployed, which parameters to use, and which resources are deployed.
+ [Configuring account structure and OUs](account-structure.md) – Shares a sample account structure that includes different accounts and organizational units (OUs) for a landing zone.
+ [Using controls to govern resources and monitor compliance](controls.md) – Identifies and explains the preventive, detective, and proactive controls that must be enabled in AWS Control Tower for the landing zone's governance.
+ [Networking integration](networking.md) – Helps you design connectivity between the virtual private clouds (VPCs) in your landing zone and on-premises applications by using native AWS services such as AWS Transit Gateway, AWS Direct Connect, and AWS Site-to-Site VPN.
+ [Authentication and authorization](authentication.md) – Explains how AWS IAM Identity Center integrates with AWS Control Tower and how to integrate your own identity provider.
+ [Centralizing logging and monitoring](logging-monitoring.md) – Reviews the monitoring, logging, log archival, and alerting strategy for the landing zone.
+ [Managing the configuration of AWS resources](config-mgmt.md) – Explains how you can manage resource configurations, track changes, and view compliance data by using AWS Config.

## AWS services
<a name="services"></a>

This design guide covers the following AWS services to set up the landing zone:
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) automates the landing zone setup by using best practices for identity, federated access, controls, and account structure.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) integrates with AWS Control Tower, captures actions as events, and provides a record of actions taken by a user, role, or AWS service.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)helps you assess, audit, and evaluate the configurations of your AWS resources. AWS Control Tower automatically enables AWS Config in its AWS Regions and uses it to implement detective controls. The configuration history and snapshots are delivered to an Amazon Simple Storage Service (Amazon S3) bucket in the Log Archive account. (See [Security OU – Log Archive account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/log-archive.html) in the *AWS Security Reference Architecture*.)
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) establishes a dedicated network connection from on-premises environments to the AWS Cloud.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps securely control access to your AWS resources. IAM or IAM Identity Center authenticates that you're an approved user before you perform operations, such as provisioning accounts in [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) or creating new OUs in the AWS Control Tower console, in your landing zone.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that consolidates multiple AWS accounts into an organization that you centrally manage. In AWS Control Tower, AWS Organizations helps you to centrally manage billing, control access, compliance, and security, in addition to sharing resources across your [member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-ram.html).
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) monitors the resources and applications that run on AWS. [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) lets you monitor and troubleshoot applications that span multiple accounts within a Region.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and the data stored in Amazon S3.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)is a cloud-based single sign-on (SSO) service that helps you centrally manage SSO access for all your AWS accounts and cloud applications. AWS Control Tower integrates with IAM Identity Center to manage users, roles, and multi-account access.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. S3 buckets store the AWS Control Tower logs and AWS access logs.
+  [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) provides a unified user interface (UI) to centrally track and resolve operational issues across your applications and resources.
+  [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses. AWS Control Tower sends security notifications, such as non-compliance with detective controls, to SNS topics that clients can subscribe to.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

You should expect the following business outcomes from using this design guide:
+ Lead design conversations for an AWS Control Tower landing zone confidently.
+ Address all foundational pillars of an AWS Control Tower landing zone effectively.
+ Create a strong foundation for migrating workloads to the AWS Cloud.

## Attachments
<a name="attachments-156d118c-ed00-4c5b-9a02-63c2673a3342"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
