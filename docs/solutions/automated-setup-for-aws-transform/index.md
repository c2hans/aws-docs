---
source_url: https://docs.aws.amazon.com/solutions/automated-setup-for-aws-transform/index.html
---

---
title: 'Guidance for Automated Setup for AWS Transform'
canonical_url: https://docs.aws.amazon.com/solutions/automated-setup-for-aws-transform/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Automated Setup for AWS Transform

## Overview

This Guidance helps organizations accelerate their VMware workload migration and modernization by automating the deployment of AWS Transform using infrastructure as code, eliminating manual provisioning overhead and ensuring consistent adherence to AWS security best practices. AWS Transform uses AI-powered migration planning with graph neural networks to analyze application dependencies from your VMware environment and create actionable migration wave plans through a conversational interface. The service orchestrates the entire migration journey—from discovery and dependency mapping to network conversion and workload replication—while automatically provisioning the necessary AWS accounts, security controls, and infrastructure across your organization. Migration artifacts, inventory data, and wave plans are centrally stored and tracked, with comprehensive monitoring and logging enabled throughout the process. You gain a predictable, cost-efficient path to modernization with reduced operational overhead, faster time-to-value, and intelligent automation that transforms complex VMware infrastructure data into structured, executable migration strategies.

## Benefits

### Accelerate your VMware migration

Transform complex VMware dependencies into actionable migration waves using graph neural networks and AI-powered planning. Reduce manual assessment effort and move workloads to production on AWS faster.

### Migrate with integrated security governance

Protect migration data end-to-end with AWS Key Management Service encryption, AWS IAM Identity Center access controls, and AWS CloudTrail audit logging. Maintain compliance across accounts without building custom governance frameworks.

### Automate multi-account migration orchestration

Provision target infrastructure across accounts and Regions using AWS CloudFormation and AWS CDK templates. Monitor migration progress in near real time with centralized Amazon CloudWatch observability from discovery through cutover.

## How it works

This architecture diagram shows the automated setup of AWS Transform for VMware workload migration, covering environment setup, data collection, and workload migration phases. [Download the architecture diagram.](downloads/automated-setup-of-aws-transform-for-vmware.pdf)

![Architecture diagram for Automated Setup of AWS Transform for VMware](/images/solutions/automated-setup-for-aws-transform/images/automated-setup-of-aws-transform-for-vmware.png)

1. **Step 1**: The customer VMware environment hosts the workloads to be migrated. RVTools can be used along with optional import/export functionality for customers running VMware NSX.
1. **Step 2**: AWS Transform discovery tool gathers and collects data and dependencies for migration. Many other data sources are supported for discovery. AWS Replication Agent migrates virtual machines to AWS.
1. **Step 3**: AWS Transform for VMware workspaces are available globally. A full list of supported AWS Regions can be found in the Supported Regions for AWS Transform section of the AWS Transform User Guide.
1. **Step 4**: AWS Transform for VMware helps optimize infrastructure and reduces operational overhead, giving you a more predictable, cost-efficient path to modernization.
1. **Step 5**: As part of AWS Transform, the Wave Planning capability uses graph neural networks to analyze application dependencies and plan migration waves. AWS Transform utilizes an AI-powered migration planning capability with a conversational interface to transform complex VMware infrastructure data into actionable migration strategies through intelligent dependency analysis and structured validation.
1. **Step 6**: The AWS migration planning account hosts AWS Transform for migration planning activities.
1. **Step 7**: AWS Key Management Service encrypts data using AWS managed keys by default or optional customer managed keys (CMKs).
1. **Step 8**: AWS Organizations enables centralized management of AWS accounts through organizational units (OUs).
1. **Step 9**: Amazon CloudWatch monitors AWS Transform activities, resources, and metrics in the management account.
1. **Step 10**: AWS Identity and Access Management Identity Center provides centralized access management across all AWS accounts.
1. **Step 11**: Amazon Simple Storage Service buckets store key migration artifacts, including inventory data, dependency mappings, wave plans, and application groupings. By default, the artifacts are stored in service-managed buckets. Customers can optionally configure their own Amazon S3 bucket for greater control over data storage, encryption, and access policies. Discovery data and migration artifacts are also stored there.
1. **Step 12**: AWS CloudFormation automates resource provisioning across AWS accounts and Regions for test and production environments.
1. **Step 13**: AWS CloudTrail logs API activities in AWS accounts, while AWS Transform tracks migration activities.
1. **Step 14**: The AWS target (provisioning) account hosts migrated production workloads and applications.
1. **Step 15**: The AWS Transform network migration capability converts on-premises networks to AWS using AWS CloudFormation, AWS CDK templates. Terraform and Amazon Landing Zone Accelerator are also supported.
1. **Step 16**: AWS Transform orchestrates end-to-end migration by coordinating across various AWS tools and services, including AWS Application Migration Service server migration or rehost capability.
1. **Step 17**: Amazon Elastic Compute Cloud and Amazon Elastic Block Store host migrated VMware virtual machines with recommended AMI instance types and storage.
1. **Step 18**: The network foundation relies on Amazon Virtual Private Cloud and AWS Transit Gateway working in tandem, where Amazon VPC provides dedicated network isolation for migrated workloads while Transit Gateway acts as the central hub connecting these VPCs. NAT gateways enable secure internet access for private subnet resources.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-automated-setup-of-aws-transform)

[Read usage guidelines](/solutions/guidance-disclaimers/)
