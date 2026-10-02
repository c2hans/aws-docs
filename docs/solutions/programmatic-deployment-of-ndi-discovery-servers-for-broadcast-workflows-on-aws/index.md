---
source_url: https://docs.aws.amazon.com/solutions/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/index.html
---

---
title: 'Guidance for Programmatic Deployment of NDI Discovery Servers for Broadcast Workflows on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/
source: aws-documentation
generated_on: 2026-10-02
---

# Guidance for Programmatic Deployment of NDI Discovery Servers for Broadcast Workflows on AWS

## Overview

This Guidance demonstrates how to programmatically deploy a resilient Network Device Interface (NDI) Discovery Server architecture within an Amazon Virtual Private Cloud (Amazon VPC). The included AWS CloudFormation template provisions a pair of Amazon Elastic Compute Cloud (Amazon EC2) instances across two Availability Zones, downloads the NDI software, and installs it following best practices. This foundational infrastructure allows you to seamlessly integrate NDI technology for live video transport within your AWS environment, supporting broadcast workflows such as live cloud production and content production.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws.pdf)

![Architecture diagram](/images/solutions/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/images/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws-1.png)

1. **Step 1**: The AWS CloudFormation template defines the AWS resources and their configurations. In this first step, the template is used to deploy a CloudFormation Stack.
1. **Step 2**: CloudFormation provisions or updates the resources specified in the template.
1. **Step 3**: CloudFormation creates an AWS Identity and Access Management (IAM) instance profile. An instance profile is a container that passes an IAM role to an Amazon Elastic Compute Cloud (Amazon EC2) instance. It defines the permissions that the Amazon EC2 instance will have when interacting with other AWS services. The instance profile includes an IAM role and an IAM policy that specify the allowed actions and resources.
1. **Step 4**: CloudFormation creates a security group, which acts as a virtual firewall that controls inbound and outbound traffic to Amazon EC2 instances.
1. **Step 5**: CloudFormation creates two Amazon EC2 instances, one in the private subnet 1 within Availability Zone 1, and another in the private subnet 2 within Availability Zone 2. These Amazon EC2 instances use the instance profile from Step 3 and the security group from Step 4. They host the NDI Discovery Server application installed during the launch process.
1. **Step 6**: CloudFormation creates an Amazon Route 53 Private Hosted Zone with the Address records for the two Amazon EC2 instances, which manage DNS and route traffic.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance allows you to automate key administrative and maintenance processes for your NDI Discovery Servers. By using AWS Systems Manager, you can securely connect to your instances, perform automated patch management, and streamline permission management through IAM roles and policies. This improves security through least privilege access and reduces operational overhead. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

With CloudFormation, you can programmatically deploy resources with predefined security configurations and controls. We recommend you use IAM roles and policies to grant least privilege permissions, Amazon Virtual Private Cloud (Amazon VPC) security groups to control traffic, and Systems Manager to remove the need for SSH keys. This comprehensive approach minimizes the attack surface and automates the deployment of security best practices. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Deploy your NDI Discovery Servers across multiple Amazon VPC subnets and Availability Zones (AZs). This redundancy protects against AZ-level failures, while CloudFormation and Route 53 automate deployments and manage DNS, respectively. Extend the Guidance to use an Auto Scaling group for self-healing capabilities. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EC2 provides the foundation to build high-performance, scalable architectures that meet your business requirements. This Guidance utilizes Amazon EC2 Linux instances to host the NDI Discovery Servers application. Amazon EC2 offers a selection of instance types and sizes, so you can match your instances with your performance needs. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 instances can start and stop on demand, avoiding unnecessary costs, and Amazon EC2 Reserved Instances provide a significant discount compared to On-Demand pricing. Monitor performance and utilization with AWS Cost Explorer to identify opportunities, downsize instances, and minimize costs without compromising performance. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Using Amazon EC2 burstable instance types, like T3 instances, allows your instances to operate at a baseline CPU utilization and burst above that when needed, optimizing resource usage and reducing energy consumption. Continuously monitor performance and 'rightsize' your instances to align with your workload requirements to minimize over-provisioning your resources and further reduce the environmental impact of this Guidance. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
