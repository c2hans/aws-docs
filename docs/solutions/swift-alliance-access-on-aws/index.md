---
source_url: https://docs.aws.amazon.com/solutions/swift-alliance-access-on-aws/index.html
---

---
title: 'Guidance for SWIFT Alliance Access on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/swift-alliance-access-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for SWIFT Alliance Access on AWS

## Overview

This Guidance enables financial institutions to integrate SWIFT Alliance Access with AWS infrastructure through a secure, cloud-optimized architecture. By leveraging deployment across two Availability Zones and aligning with SWIFT Customer Security Programme (CSP) requirements, it accelerates the transition to modern financial messaging while ensuring operational resilience, enhanced scalability, and robust compliance.

## Benefits

### Streamline financial messaging operations

Deploy a highly available SWIFT connectivity solution across multiple Availability Zones. Focus on your core financial services while AWS manages the underlying infrastructure for your SWIFT Alliance Access environment.

### Enhance security and compliance

Implement defense-in-depth strategies with private subnets, encrypted communications, and centralized key management. Meet SWIFT CSP requirements while simplifying security management across your financial messaging infrastructure.

### Optimize costs with flexible deployment options

Scale your SWIFT Alliance Access environment based on transaction volumes with right-sized compute resources and optional database deployments. Reduce capital expenditure by paying only for the resources you use.

## How it works

### Alliance Connect Virtual Gold

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Gold connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-access-on-aws.pdf)Step 1This architecture operates across two Availability Zones (AZs) for redundancy.Step 2Configure Amazon Virtual Private Cloud (Amazon VPC) with private subnets that meet AWS and SWIFT Customer Security Programme (CSP) security.Step 3The Amazon Elastic Compute Cloud (Amazon EC2) instance hosts SWIFT Alliance Access (SAA) for SWIFT message processing.Step 4The EC2 instance hosts SWIFT Alliance Gateway (SAG) and SWIFTNet Link (SNL) for secure financial transmission..Step 5(Optional) Amazon Relational Database Service (Amazon RDS) operates in active or standby mode, storing configuration and message data for SAA. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6AWS Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7Amazon CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS Virtual Private Network (AWS VPN) connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon Virtual Private Cloud (Amazon VPC) to AWS Direct Connect for reliable, private connectivity.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Silver

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Silver connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-access-on-aws.pdf)Step 1This architecture operates across two AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security.Step 3The EC2 instance hosts SAA for SWIFT message processing.Step 4The EC2 instance hosts SAG and SNL for secure financial transmission.Step 5(Optional) Amazon RDS operates in active or standby mode, storing configuration and message data for SAA. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS VPN connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9aAn internet gateway allows communication between the Amazon VPC to the SWIFT network over the internet, providing redundancy and failover capability.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Bronze

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-access-on-aws.pdf)Step 1This architecture operates across two AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security.Step 3The EC2 instance hosts SAA for SWIFT message processing.Step 4The EC2 instance hosts SAG and SNL for secure financial transmission.Step 5(Optional) Amazon RDS operates in active or standby mode, storing configuration and message data for SAA. Note that while customers can use external databases, SWIFT only supports the embedded database.Step 6Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 7CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 8A dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, establishes AWS VPN connectivity to the SWIFT network.Step 9An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9aAn internet gateway allows communication between the Amazon VPC to the SWIFT network over the internet, providing redundancy and failover capability.Step 10Direct Connect provides private connectivity between AWS and data centers or colocation environments.[Read usage guidelines](/solutions/guidance-disclaimers/)
