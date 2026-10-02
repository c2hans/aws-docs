---
source_url: https://docs.aws.amazon.com/solutions/swift-alliance-message-hub-on-aws/index.html
---

---
title: 'Guidance for SWIFT Alliance Message Hub on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/swift-alliance-message-hub-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for SWIFT Alliance Message Hub on AWS

## Overview

This Guidance enables financial institutions to integrate SWIFT Alliance Message Hub with Alliance Connect Virtual through a secure, cloud-optimized architecture. By leveraging deployment across two Availability Zones and aligning with SWIFT Customer Security Programme (CSP) requirements, the Guidance establishes centralized messaging protocols to streamline message processing, simplify integration patterns, and maintain robust compliance.

## Benefits

### Accelerate high-volume message processing

Deploy a robust, scalable environment for SWIFT Alliance Message Hub designed for high-throughput financial institutions. Process large transaction volumes efficiently while maintaining performance during peak periods.

### Build resilient financial infrastructure

Implement redundant connectivity options with both dedicated and internet-based connections to the SWIFT network. Maintain continuous operations with multi-Availability Zone deployment across the highly reliable AWS global infrastructure.

### Simplify operational management

Automate deployment and maintenance of your SWIFT environment using infrastructure-as-code and centralized management tools. Gain comprehensive visibility into your messaging operations with integrated monitoring and logging capabilities.

## How it works

### Alliance Connect Virtual Gold

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Gold connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-message-hub-on-aws.pdf)Step 1This architecture operates across two Availability Zones (AZs) for redundancy.Step 2Configure Amazon Virtual Private Cloud (Amazon VPC) with private subnets that meet AWS and SWIFT Customer Security Programme (CSP) security.Step 3The Amazon Elastic Compute Cloud (Amazon EC2) instance hosts the Alliance Message Hub (AMH) for SWIFT message processing.Step 4The EC2 instance hosts SWIFT Alliance Gateway (SAG) and SWIFTNet Link (SNL) for secure financial transmission..Step 5(Optional) Amazon Relational Database Service (Amazon RDS) operates in active or standby mode, storing configuration and message data for AMH. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6AWS Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7Amazon CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS Virtual Private Network (AWS VPN) connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon Virtual Private Cloud (Amazon VPC) to AWS Direct Connect for reliable, private connectivity.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Silver

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Silver connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-message-hub-on-aws.pdf)Step 1This architecture operates across two AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security.Step 3The EC2 instance hosts AMH for SWIFT message processing.Step 4The EC2 instance hosts SAG and SNL for secure financial transmission.Step 5(Optional) Amazon RDS operates in active or standby mode, storing configuration and message data for AMH. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS VPN connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9aAn internet gateway allows communication between the Amazon VPC to the SWIFT network over the internet, providing redundancy and failover capability.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Bronze*

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-message-hub-on-aws.pdf)Step 1This architecture operates across two AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security.Step 3The EC2 instance hosts AMH for SWIFT message processing.Step 4The EC2 instance hosts SAG and SNL for secure financial transmission.Step 5(Optional) Amazon RDS operates in active or standby mode, storing configuration and message data for AMH. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS VPN connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9aAn internet gateway allows communication between the Amazon VPC to the SWIFT network over the internet, providing redundancy and failover capability.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.Notes*Bronze may be appropriate for development environments but is not recommended for AMH due to its suitability for low volume traffic. AMH is designed for high volume institutions.[Read usage guidelines](/solutions/guidance-disclaimers/)
