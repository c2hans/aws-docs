---
source_url: https://docs.aws.amazon.com/solutions/secure-blockchain-validation-using-aws-nitro-enclaves/index.html
---

# Guidance for Secure Blockchain Validation Using AWS Nitro Enclaves

## Overview

This Guidance shows how to deploy a secure, scalable, and cost-efficient blockchain key management solution for blockchain validation workloads like Ethereum 2.0 proof-of-stake networks. It leverages AWS Nitro Enclaves to run Web3Signer, a core component for building secure blockchain networks. This solution provides sample code for securely configuring, bootstrapping, and operating Web3Signer within the isolated Nitro Enclaves environment using the AWS Cloud Development Kit (AWS CDK). This allows you to establish reliable and secure blockchain networks while safeguarding sensitive data and mitigating potential risks.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/secure-blockchain-validation-using-aws-nitro-enclaves.pdf)

![Architecture diagram](/images/solutions/secure-blockchain-validation-using-aws-nitro-enclaves/images/secure-blockchain-validation-using-aws-nitro-enclaves-1.png)

1. **Step 1**: Run the AWS Cloud Development Kit (AWS CDK) stack through your local machine.
1. **Step 2**: Once you run the AWS CDK stack, the required container artifacts are uploaded to the Amazon Elastic Container Registry (Amazon ECR). All Docker containers will be pulled from Amazon ECR later.
1. **Step 3**: Config artifacts are encrypted through a symmetric encryption key using AWS Key Management Service (AWS KMS).
1. **Step 4**: Encrypted config artifacts are stored in Amazon DynamoDB.
1. **Step 5**: Run the Web3Signer initialization with an AWS Systems Manager command.
1. **Step 6**: AWS Nitro Enclaves automatically decrypt config artifacts through AWS KMS using cryptographic attestation.
1. **Step 7**: The Web3Signer process starts with Nitro Enclaves and exposes the HTTPS API on a parent Amazon Elastic Compute Cloud (Amazon EC2) instance.
1. **Step 8**: Control the Web3Signer status through the AWS Lambda console. The state command provides information about the current status of the Lambda function.
1. **Step 9**: Requests are routed through a Network Load Balancer to the next healthy Amazon EC2 instance that runs isolated in a private subnet.
1. **Step 10**: Requests originating from the Amazon EC2 validator or consensus client can be routed to a Web3Signer instance through a Network Load Balancer. The validator client is not enclosed in this Guidance.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-secure-blockchain-validation-using-aws-nitro-enclaves)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance provides mechanisms for implementing changes (AWS CDK), gathering feedback (GitHub), and secure instance management (Systems Manager). This allows you to safely make updates, incorporate improvements, and operate resources without compromising security. Adhering to proven operational best practices helps achieve reliable, high-performing workloads. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

By implementing the robust security controls of this Guidance, you protect your information, systems, and assets. For example, resources are protected by deploying them in a separate VPC with private subnets, allowing internet access only through NAT gateways. Access to Amazon EC2 instances is restricted, with no inbound access allowed and administrator access granted only through Systems Manager. Data, including sensitive private key material and Web3Signer configurations, is encrypted using AWS KMS and stored in DynamoDB, with cryptographic attestation ensuring decryption only within the Nitro Enclaves. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

The Guidance implements a highly available network topology with an Auto Scaling group deployed across two different Availability Zones, ensuring at least two active instances at any time. A Network Load Balancer distributes traffic between these instances. The application-level architecture is designed for reliability, with loosely coupled dependencies, stateless compute processes inside the Nitro Enclaves, and the ability to automatically recover from failures. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Guidance leverages an Auto Scaling group to match demand and help ensure that only the minimum resources required are running. The blockchain validation client and consensus client can be deployed in private and public subnets, respectively, within the same VPC to decrease latency and improve performance. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Guidance avoids services and storage options with high monthly fixed costs. For long-term operation, the Amazon EC2 instances should be part of an Amazon EC2 Instance Savings Plan, which can reduce costs compared to using on-demand instances. The default instance type is C6A.xlarge, the smallest instance currently supporting Nitro Enclaves. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By using an Auto Scaling group, this Guidance helps to ensure the high availability of your workloads while minimizing the number of Amazon EC2 instances running. This solution can be easily extended to scale out or in as needed, optimizing resource utilization based on demand. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
