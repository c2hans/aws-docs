---
source_url: https://docs.aws.amazon.com/solutions/core-banking-backup-and-disaster-recovery-on-aws/index.html
---

---
title: 'Guidance for Core Banking Backup and Disaster Recovery on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/core-banking-backup-and-disaster-recovery-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Core Banking Backup and Disaster Recovery on AWS

## Overview

This Guidance helps credit unions back up application and database layers of core banking platforms for disaster recovery. Financial institutions that store data must be prepared not only for natural disasters, but also for cyberattacks, ransomware attacks, and data breaches. To keep customer’s personally identifiable information (PII) safe, credit unions must prioritize and plan for efficient disaster recovery to quickly resume continuity of business operations. This Guidance helps credit unions prepare for disaster recovery while also staying compliant with requirements such as General Data Protection Regulation (GDPR), Gramm-Leach-Bliley Act (GLBA), and Federal Financial Institutions Examination Council (FFIEC).

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/core-banking-backup-and-disaster-recovery-on-aws.pdf)

![Architecture diagram](/images/solutions/core-banking-backup-and-disaster-recovery-on-aws/images/core-banking-backup-and-disaster-recovery-on-aws-1.png)

1. **Step 1**: AWS Direct Connect provides transparent and resilient connectivity by connecting customer data centers to the AWS Cloud.
1. **Step 2**: AWS Database Migration Service (AWS DMS) migrates and replicates data from the on-premises data center to Amazon Relational Database Service (Amazon RDS). The source database remains fully operational during the migration, minimizing downtime to applications that rely on the database.
1. **Step 3**: Set up AWS Elastic Disaster Recovery (AWS DRS) Agents on your source servers to initiate secure data replication. With AWS DRS, you can recover your applications on AWS from your existing infrastructure.
1. **Step 4**: Use the AWS Management Console to configure replication and launch settings, monitor data replication, and launch instances for drills or recovery.
1. **Step 5**: Data is replicated to a staging area subnet in your AWS account in the AWS Region you select. The staging area design reduces costs by using Amazon Elastic Block Store (Amazon EBS) and minimal Amazon Elastic Compute Cloud (Amazon EC2) resources to maintain ongoing replication.
1. **Step 6**: AWS DRS automatically converts your servers to boot and run natively on AWS when you launch instances for drills or recovery. If you need to recover applications, you can launch recovery instances on AWS within minutes, using the most up-to-date server state or a previous point in time. You can choose to keep your applications running on AWS or initiate replication to your primary site once the issue is resolved. You can fail back to your primary site whenever you're ready.
1. **Step 7**: Use Amazon CloudWatch to capture, react to, and display application health. You can monitor changes to application infrastructure by using AWS CloudTrail and AWS Config. These services monitor activity within your AWS account. For application-level insights, use AWS X-Ray to monitor your application.
1. **Step 8**: With AWS Identity and Access Management (IAM), you can specify who or what can access services and resources in AWS. AWS Key Management Service (AWS KMS) lets you create, manage, and control cryptographic keys across your applications and other AWS services. AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, API keys, and other secrets throughout their lifecycles.
1. **Step 9**: Amazon Route 53 monitors the health of your application endpoints and directs traffic to your primary Region. When Route 53 detects a failure in your primary Region, it will automatically switch and route traffic to your application running in AWS.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

To maintain operational health, you must detect failures and quickly recover from them. You should configure applications to emit the relevant telemetry for detecting issues and establish processes to capture and react to events. CloudWatch provides useful tools to capture, react to, and display application health. Drift between primary and secondary sites can lead to failure in recovery during a disaster. Financial institutions can monitor changes to their application infrastructure by using CloudTrail and AWS Config. Once drift is detected, institutions can automate a response through CloudWatch Events. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Use IAM policies to assign permissions that determine who is allowed to manage AWS resources, especially AWS DRS and AWS DMS. Communication between AWS DRS Agents and the replication server are based on Transport Layer Security (TLS) 1.2. These requests are signed using an access key ID and a secret access key that is associated with an IAM principle. As an additional step, we recommend encrypting Amazon EBS volumes using AWS KMS. AWS DMS uses Secure Sockets Layer (SSL) for endpoint connections with TLS. You can also configure AWS DMS to use AWS KMS for encrypting the storage used by the replication instance and its endpoint connection information. Further, we recommend encrypting the Amazon RDS database using AWS KMS and storing database credentials within Secrets Manager. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS DRS continuously replicates machines into a staging area within the target AWS account and your preferred Region. In case of a disaster, AWS DRS automates the conversion of replicated servers into fully provisioned workloads in the recovery Region. For disruptions caused by ransomware, data corruption, accidental user error, or bad patches, you can use AWS DRS to recover these servers on AWS from a previous point in time. Further, AWS DRS provides continuous block-level replication, recovery orchestration, and automated server conversion capabilities. These allow customers to achieve a crash-consistent recovery point objective (RPO) of seconds and a recovery time objective (RTO) typically ranging between 5–20 minutes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS DRS is highly automated, eliminating time-consuming and manual tasks. Server conversion technology makes relevant changes to the boot volume of the recovered server so that it can boot in AWS. This includes injecting appropriate hypervisor drivers and networking changes. As a managed service, AWS DMS takes care of assessing, converting, and migrating database instances into AWS. To speed up full load and improve the change data capture (CDC) process, we recommend creating separate AWS DMS tasks for tables which have a high number of records or data manipulation language (DML) activities to prevent data migration from smaller tables that can slow down tasks. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The AWS DRS staging area design reduces costs by using affordable storage and minimal compute resources to maintain ongoing replication. You can achieve further price reductions through Savings Plans for Amazon EC2 and Reserved Instances for Amazon RDS. These discounts provide considerable cost savings when compared to On-Demand pricing. To provide the capacity guarantee that financial institutions need for regulatory requirements, customers can purchase zonal Reserved Instances (RIs). Zonal RIs are specific to an instance type and assigned to a specific Availability Zone. Zonal RIs increase availability, regardless of other customer demands for capacity. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Through the use of managed services, this architecture minimizes the environmental impact from backend resources. The AWS DRS staging area design reduces the infrastructure carbon footprint by provisioning minimal compute resources to maintain ongoing replication while still achieving RTOs of minutes and RPOs of seconds. To further reduce environmental impact, continuously monitor CloudWatch metrics during disaster events to help ensure that the scaled environment is not overprovisioned. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
