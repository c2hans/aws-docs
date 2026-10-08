---
source_url: https://docs.aws.amazon.com/solutions/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws/index.html
---

---
title: 'Guidance for Building an Enterprise-Ready Network Foundation for RISE with SAP on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Building an Enterprise-Ready Network Foundation for RISE with SAP on AWS

## Overview

This Guidance demonstrates how to implement a secure AWS landing zone for RISE with SAP. By setting up direct connections and VPN tunnels, you can establish secure network connectivity between your organization’s infrastructure and AWS. This enables you to create a well-structured multi-account foundation for your SAP and non-SAP workloads, all in an environment that you manage. Without requiring extensive cloud expertise, this approach helps you accelerate deployments, implement security best practices, and create a foundation that scales with your SAP environment.

## Benefits

### Streamline SAP network integration with standardized architecture

Deploy a secure, compliant multi-account structure that simplifies connectivity between your environment and RISE with SAP. Reduce implementation time while ensuring your network meets SAP requirements.

### Enhance business continuity with redundant connectivity

Implement dual-path network connectivity combining Direct Connect and Site-to-Site VPN for automatic failover. Maintain continuous access to critical SAP applications even during network disruptions or maintenance events.

### Strengthen security posture with layered network controls

Enforce consistent security policies through dedicated inspection VPCs and centralized traffic management. Protect sensitive SAP workloads without compromising on the low-latency performance required for business operations.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws.pdf)

![Architecture diagram](/images/solutions/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws/images/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws-1.png)

1. **Step 1**: Create an AWS account. Follow this guide if you do not already have one. This establishes your fundamental AWS presence and access to AWS services.
1. **Step 2**: Deploy the installer stack for the Landing Zone Accelerator on AWS environment using either the documentation for a deployment based on AWS Cloud Development Kit (AWS CDK) or the documentation for a deployment based on AWS CloudFormation. This sets up the foundational multi-account AWS environment structure using Landing Zone Accelerator on AWS.
1. **Step 3**: (Optional) Configure the AWS Site-to-Site VPN gateway within the Landing Zone Accelerator on AWS networking config file. This enables a secure, encrypted tunnel between the on-premises network and AWS.
1. **Step 4a**: (Optional) Request an AWS Direct Connect connection through the AWS Management Console, then order the Direct Connect connection(s) with an AWS Partner or network provider. This establishes a dedicated private network connection between the on-premises network and AWS. Note: Depending on the type of connectivity and on-premises locations, establishing connectivity may take hours, or it may take weeks or months. Review the AWS Direct Connect Getting Started page for more details.
1. **Step 4b**: Update the Direct Connect gateway's virtual interface with your Direct Connect physical connection ID (obtained above) within the Landing Zone Accelerator on AWS networking config file. This links your physical Direct Connect connection to your AWS environment configuration.
1. **Step 5**: Configure your network's customer gateway device for the Site-to-Site VPN and the Direct Connect connection to enable your on-premises network equipment to communicate with AWS.
1. **Step 6**: Configure Direct Connect and Site-to-Site VPN for failover. This enables continuous connectivity by enabling automatic switching between Direct Connect and the VPN.
1. **Step 7**: Provide your AWS Transit Gateway details to SAP (using the AWS connectivity questionnaire provided by SAP) to connect to the RISE with SAP environment, then accept the incoming transit gateway association request. This enables network connectivity between your AWS environment and RISE with SAP.
1. **Step 8**: (Optional) Configure the AWS Network Firewall within Landing Zone Accelerator on AWS to secure the connectivity between your network and the RISE with SAP environment.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/sap/building-an-enterprise-ready-network-foundation-for-rise-with-sap-on-aws.html)

## Related content

- **Landing Zone Accelerator on AWS**: This sample code deploys a multi-account cloud foundation to support highly-regulated workloads and complex compliance requirements.

[Learn more](https://github.com/awslabs/landing-zone-accelerator-on-aws/)

- **RISE with SAP on AWS Cloud**: This technical documentation outlines connectivity solutions for integrating RISE with SAP on AWS with on-premises and cloud environments.

[Learn more](/sap/latest/general/connectivity-rise.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
