---
source_url: https://docs.aws.amazon.com/solutions/swift-alliance-lite2-on-aws/index.html
---

# Guidance for SWIFT Alliance Lite2 on AWS

## Overview

This Guidance enables financial institutions to securely connect to the SWIFT network using cloud-native VPN solutions on AWS instead of traditional hardware devices. While deployable in a single Availability Zone for small to medium messaging volumes, the architecture can be expanded to dual Availability Zones to achieve maximum reliability and fault tolerance for critical financial operations.

## Benefits

### Fortify financial network resilience

Establish a secure, highly available SWIFT connectivity infrastructure that automatically adapts to potential disruptions. Leverage multi-Availability Zone architecture, automated security controls, and intelligent failover mechanisms for continuous, compliant financial messaging with minimal operational overhead.

### Accelerate secure financial communications

Transform your SWIFT network infrastructure by combining advanced security, performance, and cost efficiency. Eliminate manual configuration complexities by using automated deployment, centralized monitoring, and optimized network connectivity that meets stringent financial industry security standards.

### Optimize sustainable financial technology

Modernize your financial network infrastructure with an environmentally conscious, high-performance cloud environment. Reduce your carbon footprint by leveraging energy-efficient AWS services that automatically scale, optimize resource utilization, and provide comprehensive visibility into your SWIFT infrastructure.

## How it works

### Alliance Connect Virtual Gold

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Gold connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-lite2-on-aws.pdf)Step 1The architecture operates across two Availability Zones (AZs) for redundancy.Step 2Configure Amazon Virtual Private Cloud (Amazon VPC) with private subnets that meet AWS and SWIFT Customer Security Programme (CSP) security standards.Step 3The Amazon Elastic Compute Cloud (Amazon EC2) instance hosts SWIFT AutoClient. At any given time, only one AutoClient instance can connect to SWIFT Production.Step 4AWS Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5Amazon CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS Virtual Private Network (AWS VPN) connectivity to the SWIFT network.Step 7An AWS VPN gateway links the Amazon VPC to AWS Direct Connect for reliable, private connectivity.Step 8Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Silver

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Silver connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-lite2-on-aws.pdf)Step 1The architecture operates across two Availability AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts SWIFT AutoClient. At any given time, only one AutoClient instance can connect to SWIFT Production.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.Step 8An AWS VPN gateway links the Amazon VPC to Direct Connect for reliable, private connectivity.Step 9Direct Connect provides private connectivity between AWS and data centers or colocation environments.### Alliance Connect Virtual Bronze

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-lite2-on-aws.pdf)Step 1The architecture operates across two Availability AZs for redundancy.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts SWIFT AutoClient. At any given time, only one AutoClient instance can connect to SWIFT Production.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A dual Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.### Alliance Connect Virtual Bronze (Single Instance)

This architecture diagram shows a standardized environment for connecting to the SWIFT network using Alliance Connect Virtual Bronze connectivity with a single instance.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/swift-alliance-lite2-on-aws.pdf)Step 1The architecture operates on only one AZ for customers who want to have a single AutoClient instance set up.Step 2Configure Amazon VPC with private subnets that meet AWS and SWIFT CSP security standards.Step 3The EC2 instance hosts SWIFT AutoClient. At any given time, only one AutoClient instance can connect to SWIFT Production.Step 4Systems Manager provides secure remote access, eliminating the need for a dedicated jump server.Step 5CloudWatch collects, stores, and monitors logs and metrics from the SWIFT environment.Step 6A single Alliance Connect Virtual EC2 instance, powered by Juniper vSRX, establishes secure AWS VPN connectivity to the SWIFT network.Step 7An internet gateway allows communication between the Amazon VPC to the SWIFT network over internet, providing redundancy and failover capability.[Read usage guidelines](/solutions/guidance-disclaimers/)
