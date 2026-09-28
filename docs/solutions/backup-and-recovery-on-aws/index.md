---
source_url: https://docs.aws.amazon.com/solutions/backup-and-recovery-on-aws/index.html
---

---
title: 'Guidance for Backup & Recovery on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/backup-and-recovery-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Backup & Recovery on AWS

## Overview

This Guidance demonstrates how to backup your cloud data and resources and perform recovery operations within your cloud environment. It will help you scale when your cloud presence grows, and due to the iterative nature of the capitabilities, you won’t need to start from the beginning. Deploying this Guidance helps ensure you are meeting your business goals, recovery point objectives (RPOs), and recovery time objectives (RTOs), so you have a clear path to host cloud production workloads.

## How it works

This Guidance demonstrates how to backup your cloud data and resources and perform recovery operations within your cloud environment. It will help you scale when your cloud presence grows, and due to the iterative nature of the capitabilities, you won’t need to start from the beginning. Deploying this Guidance helps ensure you are meeting your business goals, recovery point objectives (RPOs), and recovery time objectives (RTOs), so you have a clear path to host cloud production workloads.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/backup-and-recovery-on-aws.pdf)

![Architecture diagram](/images/solutions/backup-and-recovery-on-aws/images/backup-and-recovery-on-aws-1.png)

1. **Step 1**: Create and publish backup, recovery, and tagging standards for backup operations.
1. **Step 2**: Create a central backup AWS account to centralize all backups in AWS Organizations.
1. **Step 3**: Activate AWS Backup in Organizations and delegate backup management to the central backup account.
1. **Step 4**: Deploy role-based access for backup management through AWS IAM Identity Center (successor to AWS Single Sign-On).
1. **Step 5**: Deploy AWS Backup supporting resources, such as backup vaults, through AWS CloudFormation service-managed stack sets.
1. **Step 6**: Configure backup policies, create a default AWS Backup policy for Organizations, and attach AWS Backup policies to the organizational units in Organizations.
1. **Step 7**: Implement preventative guardrails through service control policies to protect AWS Backup resources.
1. **Step 8**: Encrypt backup data with a centralized AWS Key Management Service (AWS KMS) key.
1. **Step 9**: Centralize monitoring and alerting through AWS Config and AWS Backup Audit Manager.
## Related content

- **Central IT**

[Central IT](https://aws.amazon.com/solutions/cloud-foundations/glossary/#Central_IT)

[Read usage guidelines](/solutions/guidance-disclaimers/)
