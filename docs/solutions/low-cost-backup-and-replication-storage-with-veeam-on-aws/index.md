---
source_url: https://docs.aws.amazon.com/solutions/low-cost-backup-and-replication-storage-with-veeam-on-aws/index.html
---

---
title: 'Guidance for Low Cost Backup and Replication Storage with Veeam on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/low-cost-backup-and-replication-storage-with-veeam-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for Low Cost Backup and Replication Storage with Veeam on AWS

## Overview

This Guidance demonstrates how to send long-term Veeam backups to AWS Cloud storage. The tools provided automate the creation of the cloud resources needed to store Veeam backups. You can use your existing backup infrastructure and reduce risk of data loss, increase backup recovery time, and lower cost with AWS Cloud storage.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/low-cost-backup-and-replication-storage-with-veeam-on-aws.pdf?target=_blank)

![Architecture diagram](/images/solutions/low-cost-backup-and-replication-storage-with-veeam-on-aws/images/low-cost-backup-and-replication-storage-with-veeam-on-aws-1.png)

1. **Step 1**: Veeam Backup & Replication server is responsible for coordinating, controlling, and managing backup infrastructure, settings, jobs, recovery tasks, and other processes.
1. **Step 2**: Veeam uses the scale-out backup repository to tier data automatically between local (performance tier) and Amazon Simple Storage Service (Amazon S3) object storage (capacity and archive tiers).
1. **Step 3**: Veeam supports connections to AWS accounts through HTTPS or using AWS Direct Connect.
1. **Step 4**: The scale-out backup repository consists of one or more backup repositories that provide fast access to data. The repository can be expanded with Amazon S3 object storage repositories for long-term storage.
1. **Step 5**: Veeam launches an Amazon Elastic Compute Cloud (Amazon EC2) instance to support proxying data from capacity tiers to archive tiers.
1. **Step 6**: Backups can be archived to Amazon S3 Glacier for longer term storage and reduced costs.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance helps you enable long-term object storage for Veeam Backup & Replication on AWS. It includes sample AWS CloudFormation code that allows object storage backup using Amazon S3, extending the functionality of Veeam Backup & Replication. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses AWS Identity and Access Management (IAM) to centrally manage users, security credentials, and permissions. Backup data is stored in Amazon S3 buckets. Access to the buckets is restricted through IAM and all public access is blocked in these buckets. The data is encrypted at rest by default. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Veeam Backup & Replication can help with disaster recovery. This software protects data from logical errors such as system failures, application errors, or accidental deletion. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Veeam Backup & Replication helps many small and medium-sized businesses protect on-premises infrastructure. These businesses want to reduce the amount of physical backup infrastructure that is needed to purchase and maintain, while ensuring that backups reside in highly durable, cost-effective storage. AWS storage services such as Amazon S3, AWS Storage Gateway, and AWS Snowball Edge seamlessly integrate with Veeam Backup & Replication to meet these needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Cost is based on the amount of data or infrastructure that is backed up to AWS through Veeam. Amazon S3 offers a pay by use pricing model with tiered pricing based on the storage class (storage classes in this Guidance include Standard, Glacier, and Glacier Deep Archive). Data transfer to Amazon S3 from the internet or Direct Connect is not charged. Data transferred out of Amazon S3 is charged by the gigabyte (GB). [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance demonstrates how you can choose the type of storage you want based on the cost, resiliency, and data access requirements of your backup and archived data. Options to store data in Amazon S3 Infrequent Access (IA) or Amazon S3 Glacier provide you with a cost optimized and computationally efficient solution to back up and archive data. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Veeam Backup & Replication**: This implementation guide details the process for sending backups created by Veeam Backup & Replication to supported Amazon Simple Storage Service (Amazon S3) object storage classes by using the Veeam scale-out backup repository capability.

[Learn more](/prescriptive-guidance/latest/patterns/back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication.html)

- **Veeam Backup & Replication**: This sample code deploys the required AWS constructs to add an object storage backup repository to Veeam Backup & Replication.

[Learn more](https://github.com/VeeamHub/veeam-aws-cloudformation/tree/master/veeam-backup-and-replication)

[Read usage guidelines](/solutions/guidance-disclaimers/)
