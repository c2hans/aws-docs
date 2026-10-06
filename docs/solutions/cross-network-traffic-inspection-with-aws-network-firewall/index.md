---
source_url: https://docs.aws.amazon.com/solutions/cross-network-traffic-inspection-with-aws-network-firewall/index.html
---

---
title: 'Guidance for Cross Network Traffic Inspection with AWS Network Firewall'
canonical_url: https://docs.aws.amazon.com/solutions/cross-network-traffic-inspection-with-aws-network-firewall/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for Cross Network Traffic Inspection with AWS Network Firewall

## Overview

This Guidance demonstrates how to automate the deployment of centralized network security infrastructure that inspects and filters traffic across multiple cloud environments. It shows how to establish a reliable, highly available architecture that protects workloads across multiple Availability Zones while reducing operational overhead. By automating configuration management with built-in validation checks, the Guidance prevents misconfigurations and helps ensure consistent security policy enforcement. Organizations can benefit from simplified network security management while maintaining operational resilience and scalability.

## Benefits

### Deploy automated policies

Update and deploy network security rules through a streamlined configuration process. Changes automatically trigger validation and implementation across your infrastructure.

### Centralize security management

Manage network security for thousands of VPCs from a single control point, simplifying policy administration and helping ensure consistent protection across your organization.

### Track security changes

Audit security policy modifications through version-controlled workflows, enabling team collaboration while maintaining comprehensive change history.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/cross-network-traffic-inspection-with-aws-network-firewall.pdf)

![Architecture diagram](/images/solutions/cross-network-traffic-inspection-with-aws-network-firewall/images/cross-network-traffic-inspection-with-aws-network-firewall-1.png)

1. **Step 1**: The AWS CloudFormation template deploys an inspection virtual private cloud (VPC) with four subnets in randomly selected Availability Zones (AZs) within the AWS Region where the Guidance is deployed.
1. **Step 1a**: The Guidance uses two of the subnets to create AWS Transit Gateway attachments for your VPCs if you provide an existing Transit Gateway gateway ID.
1. **Step 1b**: The Guidance uses the other two subnets to create AWS Network Firewall endpoints in two randomly selected AZs within the AWS Region where the Guidance is deployed.
1. **Step 2**: The CloudFormation template creates an Amazon Simple Storage Service (Amazon S3) bucket with a default network firewall configuration that allows all traffic. This initiates AWS CodePipeline to run a validation stage and a deployment stage.
1. **Step 2a**: Validation stage: The Guidance validates the Network Firewall configuration by using APIs with dry run mode enabled. This allows you to find unexpected issues before attempting an actual change. This stage also checks whether all the referenced files in the configuration exist in the JSON file structure.
1. **Step 2b**: Deployment stage: The Guidance creates a new firewall, firewall policy, and rule groups. If any of the resources already exist, the Guidance updates the resources. This stage also helps with detecting any changes and remediates by applying the latest configuration from the S3 bucket.
1. **Step 2c**: The rule group changes roll back to the original state if one of the rule group changes fails. The appliance mode activates for the attachment from Transit Gateway to Amazon Virtual Private Cloud (Amazon VPC) to avoid asymmetric traffic.
1. **Step 3**: The Guidance creates an Amazon VPC route tables for each AZ. The default route destination target for each is the Amazon VPC endpoint for Network Firewall.
1. **Step 4**: The Guidance creates a shared route table with firewall subnets. The default route destination target is the transit gateway ID. This route is only created if the transit gateway ID is provided in the CloudFormation input parameters.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **We'll walk you through it**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](/solutions/latest/centralized-network-inspection-on-aws/solution-overview.html)

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions/centralized-network-inspection-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
