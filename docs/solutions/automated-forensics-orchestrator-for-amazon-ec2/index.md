---
source_url: https://docs.aws.amazon.com/solutions/automated-forensics-orchestrator-for-amazon-ec2/index.html
---

---
title: 'Guidance for Automated Forensics Orchestrator for Amazon EC2 and EKS'
canonical_url: https://docs.aws.amazon.com/solutions/automated-forensics-orchestrator-for-amazon-ec2/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Automated Forensics Orchestrator for Amazon EC2 and EKS

## Overview

This Guidance demonstrates how to establish a comprehensive, automated forensics orchestration workflow for Security Operations Centers using AWS services. It helps organizations rapidly respond to potential security breaches by automating critical forensics processes for Amazon EC2 instances and EKS clusters. The solution shows how to implement automated isolation of affected resources, capture essential forensics evidence including memory and disk images, and streamline investigation workflows across multi-account and multi-region environments. Through its serverless architecture and integrated security features, this Guidance enables SOC teams to efficiently conduct forensic analysis, continuously monitor for threats, and maintain a robust security posture while reducing manual overhead and accelerating incident response times.

## Benefits

### Accelerate incident response and investigation

Reduce investigation time from hours to minutes with automated forensic workflows that capture and analyze both memory and disk data when security issues are detected. Maintain business continuity while thoroughly investigating potential threats.

### Strengthen security with automated containment

Automatically isolate potentially compromised instances while preserving forensic evidence for investigation. Protect your infrastructure by implementing consistent, automated response procedures for security findings.

### Streamline forensic data management

Maintain complete chain of custody with automated evidence collection and secure storage. Query forensic timelines and investigation results through a centralized interface while ensuring compliance requirements.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/automated-forensics-orchestrator-for-amazon-ec2.pdf)

![Architecture diagram](/images/solutions/automated-forensics-orchestrator-for-amazon-ec2/images/automated-forensics-orchestrator-for-amazon-ec2-1.png)

1. **Step 1**: Prior to running the workflow, you will need a forensic Amazon Machine Image (AMI). You can use Amazon EC2 Image Builder to build a new forensic AMI or an existing forensic AMI.
1. **Step 2**: AWS Step Functions leverages the forensic AMI to perform memory and disk investigation.
1. **Step 3**: In the AWS application account, AWS Config managed rules, Amazon GuardDuty, and third-party tools detect malicious activities that are specific to Amazon Elastic Compute Cloud (Amazon EC2) resources. For example, an EC2 instance queries a low reputation domain name that is associated with known abused domains. The findings are sent to AWS Security Hub in the security account through their native or existing integration.
1. **Step 4**: By default, all Security Hub findings are then sent to Amazon EventBridge to invoke automated downstream workflows.
1. **Step 5**: For a specified event, EventBridge provides an instance ID for the forensics process to target, and initiates the Step Functions workflow.
1. **Step 6**: Step Functions triages the request through the following approach: It first gets the instance information. It then determines if isolation is required based on the Security Hub action and if acquisition is required based on tags associated with the instance. Finally, it initiates the acquisition flow based on triaging output.
1. **Step 6a**: Amazon DynamoDB stores triaging details.
1. **Step 6b**: Two acquisition flows are initiated in parallel: The Memory Forensics Flow is a Step Functions workflow that captures the memory data and stores it in Amazon Simple Storage Service (Amazon S3). Post memory acquisition, the instance is isolated using security groups. To help ensure the chain of custody, a new security group gets attached to the targeted instance and removes any access for users, admins, or developers. Isolation is initiated based on the selected Security Hub action. The Disk Forensics Flow is a Step Functions workflow that takes a snapshot of an Amazon Elastic Block Store (Amazon EBS) volume and shares it with the forensic account.
1. **Step 6c**: DynamoDB stores acquisition details.
1. **Step 6d**: Once the disk or memory acquisition process is complete, a notification is sent to an investigation Step Functions state machine to begin the automated investigation of the captured data.
1. **Step 6e**: When the Step Functions jobs are complete, DynamoDB stores the state of forensic tasks and their results.
1. **Step 7**: Investigation Step Functions starts a forensic instance from an existing forensic AMI loaded with customer forensic tools. Step Functions loads the memory data from Amazon S3 for investigation, creates an EBS volume from the snapshot, and attaches the EBS volume for disk analysis.
1. **Step 8**: AWS Systems Manager documents (SSM documents) run forensic investigation.
1. **Step 9**: Amazon Simple Notification Service (Amazon SNS) shares investigation details with customers.
1. **Step 10**: AWS AppSync can query the forensic timeline. For more details, refer to Sample AppSync API to query forensic details.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/welcome.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/automated-forensic-orchestrator-for-amazon-ec2)

[Read usage guidelines](/solutions/guidance-disclaimers/)
