---
source_url: https://docs.aws.amazon.com/solutions/swift-alliance-connect-virtual-on-aws/index.html
---

---
title: 'Guidance for SWIFT Alliance Connect Virtual on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/swift-alliance-connect-virtual-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for SWIFT Alliance Connect Virtual on AWS

## Overview

This Guidance demonstrates how to integrate Society for Worldwide Interbank Financial Telecommunication (SWIFT) messaging protocols with AWS infrastructure. This helps to facilitate interoperability and exchange of financial information and transactions between central banks and other financial institutions. Central banks can take advantage of the global reach and reliability of SWIFT, while also leveraging the scalability, security, and cost-effectiveness of AWS to facilitate the secure exchange of financial information and transactions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/swift-alliance-connect-virtual-on-aws.pdf)

![Architecture diagram](/images/solutions/swift-alliance-connect-virtual-on-aws/images/swift-alliance-connect-virtual-on-aws-1.png)

1. **Step 1**: Deploy the architecture to span two Availability Zones (AZs).
1. **Step 2**: Configure an Amazon Virtual Private Cloud (Amazon VPC) with private subnets according to AWS best practices and following SWIFT's Customer Security Program (CSP) guidance.
1. **Step 3**: An Amazon Elastic Compute Cloud (Amazon EC2) instance runs Alliance Messaging Hub (AMH) and SWIFT Alliance Access (SAA) or Lite2.
1. **Step 4**: An EC2 instance runs SWIFT Alliance Gateway (SAG) and SWIFTNet Link (SNL).
1. **Step 5**: Optionally, an Amazon Relational Database Service (Amazon RDS) Oracle instance runs in active or standby mode to store configuration and message data for AMH.
1. **Step 6**: AWS Systems Manager removes the need for a jump server.
1. **Step 7**: Amazon CloudWatch provides the mechanism to store, access, and monitor logs and metrics of the SWIFT environment.
1. **Step 8**: A Dual Alliance Connect Virtual EC2 instance, based on Juniper vSRX platform, provides AWS Virtual Private Network (AWS VPN) connectivity to the SWIFT network.
1. **Step 9**: An AWS VPN gateway connects the Amazon VPC to AWS Direct Connect.
1. **Step 10**: AWS Direct Connect establishes private connectivity between AWS and data centers or colocation environments through a Direct Connect (DX) gateway.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation automates the deployment of AWS resources required for SWIFT connectivity to help ensure consistency and reduce manual errors. CloudWatch logs centralize logging for SWIFT connectivity components, facilitating analysis of operational data across multiple AWS services and enabling the creation of metrics and alerts based on log patterns. AWS Config maintains a detailed inventory of AWS resources and configuration changes, tracking modifications to critical resources involved in SWIFT message processing and ensuring compliance with internal policies and industry regulations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS Key Management Service (AWS KMS) safeguards SWIFT connectivity by enabling secure creation and management of cryptographic keys, providing centralized control over data encryption across AWS services. Systems Manager centrally manages AWS resources, including patch management and automation of security tasks, while allowing secure access to instances without open inbound ports. Amazon VPC isolates the network environment, enabling precise control of network traffic and secure connections to on-premises networks. AWS Transit Gateway simplifies network architecture and enhances security posture by centralizing connectivity between VPCs and on-premises networks. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS KMS enhances the reliability of SWIFT connectivity by providing secure key management for data encryption for compliance with SWIFT's security framework. Amazon DynamoDB, a highly available database solution, improves data availability and consistency, supporting critical SWIFT data storage and access requirements. Systems Manager automates the management, patching, and configuration of EC2 instances running SWIFT components, reducing downtime and human error. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EC2 provides scalable compute resources for hosting critical SWIFT components, enabling efficient performance tuning and load balancing. Amazon RDS, a managed database service optimized for high-volume data operations, enhances database performance for SWIFT transactions. AWS KMS helps ensure efficient encryption and decryption processes, essential for maintaining the speed of secure financial communications. Systems Manager proactively manages and monitors the SWIFT infrastructure, helping to prevent performance issues. AWS Direct Connect establishes dedicated network connections, reducing latency and improving performance for SWIFT connectivity. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2, Amazon RDS, and AWS KMS offer flexible pricing models and resource allocation options, optimizing costs for SWIFT connectivity. Systems Manager automates management tasks and provides insights into resource utilization, reducing operational overhead and identifying cost-saving opportunities. Transit Gateway centralizes network management, simplifying the network architecture and potentially reducing data transfer costs. DynamoDB, a fully managed NoSQL database service, optimizes resource usage and energy consumption by automatically scaling to meet demand. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2 and Amazon RDS offer energy-efficient instance types and enable better resource utilization through features like auto-scaling, reducing idle capacity and energy waste. AWS KMS contributes to sustainability by enabling efficient encryption at scale without significant additional computational overhead. Transit Gateway centralizes network management, potentially reducing the number of network devices needed and improving overall network efficiency. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
