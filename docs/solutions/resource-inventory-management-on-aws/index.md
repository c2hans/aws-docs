---
source_url: https://docs.aws.amazon.com/solutions/resource-inventory-management-on-aws/index.html
---

---
title: 'Guidance for Resource Inventory Management on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/resource-inventory-management-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Resource Inventory Management on AWS

## Overview

This Guidance shows you how to implement the Resource Inventory Management capability. The Resource Inventory Management capability enables the collection, visibility, tracking, configuration validation, and service mapping of cloud resources. By tracking and monitoring your cloud resources, you can find opportunities for cost optimization, efficient allocation of resources, and increased governance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/resource-inventory-management-on-aws.pdf)

![Architecture diagram](/images/solutions/resource-inventory-management-on-aws/images/resource-inventory-management-on-aws-1.png)

1. **Step 1**: Create an Amazon Simple Storage Service (Amazon S3) bucket that will hold the AWS resource configuration snapshots and history.
1. **Step 2**: Optionally, create an AWS Key Management Service (AWS KMS) key in the Security Tooling organizational unit (OU) account. This account will be used to encrypt configuration history and snapshot files using server-side encryption with AWS KMS customer-managed keys (CMKs). If you do not use an AWS KMS key, the AWS Config data will be encrypted at rest using AES-256 encryption.
1. **Step 3**: Deploy an AWS Config configuration recorder and delivery channel to all operating Regions (Regions that you are not prohibited with service control policies [SCPs]) in all member accounts. Configure the delivery channel to send resource configuration information to the S3 bucket in the Log Archive account for audit and retention purposes.
1. **Step 4**: Deploy AWS Config configuration recorder and delivery channel to all available Regions in the Management account. Configure the delivery channel to send management account resource configuration information to the S3 bucket in the Log Archive account.
1. **Step 5**: Delegate AWS Config administration to the Security Tooling OU account to allow for AWS Config administration outside of the management account.
1. **Step 6**: Deploy an AWS Config multi-account, multi-Region data aggregator in the Security Tooling OU account to aggregate account and Region data for the organization. This will provide visibility to organization resources and AWS Config configuration compliance.
1. **Step 7**: Deploy AWS Config Rules to organization accounts to evaluate resource compliance. You can deploy rules with organization AWS Config rules, with conformance packs, or by using automation, such as AWS CloudFormation StackSets.
## Related content

- **read the whitepaper**

[read the whitepaper](/whitepapers/latest/establishing-your-cloud-foundation-on-aws/welcome.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
