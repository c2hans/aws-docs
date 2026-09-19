---
source_url: https://docs.aws.amazon.com/solutions/swift-alliance-cloud-on-aws/index.html
---

---
title: 'Guidance for SWIFT Alliance Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/swift-alliance-cloud-on-aws/
source: aws-documentation
generated_on: 2026-09-18
---

# Guidance for SWIFT Alliance Cloud on AWS

## Overview

This Guidance demonstrates how financial institutions can securely connect to the SWIFT network using Alliance Connect Virtual on AWS. By leveraging multiple AWS Availability Zones, it provides a highly available setup that modernizes financial messaging operations while delivering key advantages including cost efficiency, scalability, and streamlined compliance management.

## Benefits

### Streamline financial messaging operations

Deploy a highly available SWIFT connectivity solution across multiple AWS Availability Zones. Modernize your financial messaging infrastructure while maintaining security compliance and reducing operational overhead through automated management.

### Enhance security and compliance posture

Implement a comprehensive security framework with encrypted communications, secure access controls, and continuous monitoring. Meet SWIFT CSP requirements while gaining visibility through automated compliance checks and detailed audit trails.

### Optimize costs with flexible deployment options

Choose from multiple deployment workflows to match your specific business requirements and budget. Scale resources efficiently based on transaction volumes while eliminating hardware procurement cycles and reducing infrastructure management costs.

## How it works

### Alliance Connect Virtual Gold

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Gold connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-cloud-on-aws.pdf)Step 1The architecture operates across two Availability Zones (AZs) for redundancy.Step 2Configure Amazon Virtual Private Cloud (Amazon VPC) with private subnets that meet AWS and SWIFT Customer Security Programme (CSP) security standards.Step 3The Amazon Elastic Compute Cloud (Amazon EC2) instance hosts the optional Alliance Cloud footprint.Step 4AWS Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5Amazon CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS Virtual Private Network (AWS VPN) connectivity to the SWIFT network.Step 7An AWS VPN gateway links the Amazon VPC to AWS Direct Connect for reliable, private connectivity.Step 8Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Silver

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Silver connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-cloud-on-aws.pdf)Step 1The architecture operates across two Availability AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts the optional Alliance Cloud footprint.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.Step 8An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Bronze

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-cloud-on-aws.pdf)Step 1The architecture operates across two Availability AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts the optional Alliance Cloud footprint.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.### Alliance Connect Virtual Bronze (Single Instance)

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity with a single instance.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-cloud-on-aws.pdf)Step 1The architecture operates on only one AZ for customers who want to have single Alliance Cloud instance set up.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts the Alliance Cloud footprint.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A single Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.[Read usage guidelines](/solutions/guidance-disclaimers/)
