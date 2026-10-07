---
source_url: https://docs.aws.amazon.com/solutions/edit-in-the-cloud-on-aws/index.html
---

---
title: 'Guidance for Edit in the Cloud on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/edit-in-the-cloud-on-aws/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Edit in the Cloud on AWS

## Overview

overview

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/edit-in-the-cloud-on-aws.pdf)

![Architecture diagram](/images/solutions/edit-in-the-cloud-on-aws/images/edit-in-the-cloud-on-aws-1.png)

1. **Step 1**: The AWS CloudFormation template deploys an Amazon Elastic Compute Cloud (Amazon EC2) instance for Windows Server 2019. Teradici Cloud Access Software or Amazon DCV and NVIDIA T4 GPU drivers are included to run your non-linear editor (NLE) software of choice. During deployment, this solution gives you the option to install either Teradici's Cloud Access Software or Amazon DCV. You can then access the cloud workstation using the PC over IP (PCoIP) client from Teradici or the Amazon DCV client.
1. **Step 2**: AWS Directory Service provides user authentication.
1. **Step 3**: Amazon FSx for Windows File Server accesses digital assets through the Amazon EC2 instance using your editor of choice. FSx for Windows File Server will auto-mount the network share upon startup of the Windows Amazon EC2 instance. FSx for Windows File Server will store your media assets to be used by your NLE.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/media-entertainment/edit-in-the-cloud-on-aws.html)
[Go to sample code](https://github.com/aws-solutions-library-samples/edit-in-the-cloud-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudTrail provides comprehensive tracking of all infrastructure assets. Integrated logging from Amazon EC2 instances, FSx for Windows File Server, and Directory Service delivers observability of the components for this solution. This monitoring system enables real-time tracking and immediate response to operational issues. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This solution implements a multi-layered security approach through Directory Service for user administration and authentication. FSx for Windows File Server integrates with Microsoft Active Directory for seamless Windows environment management. AWS Identity and Access Management (IAM) roles enforce least-privilege access through granular permissions. Security groups control network traffic between specified Internet Protocol (IP) ranges and the edit host instance. Additionally, the architecture implements specific controls for FSx for Windows File Server access through security group configurations. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

FSx for Windows File Server manages core reliability functions. These include file server setup, storage volume provisioning, data replication, and failover management. This automated approach eliminates administrative overhead for consistent system performance. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance relies on the Amazon EC2 G4dn instance which provides high performance and is cost effective for graphics applications that are optimized for NVIDIA GPUs. G4dn instances have up to 1.8X better graphics performance and up to 2X video transcoding capability over the previous generation G3 instances. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The cost for running this Guidance varies based on several factors, including how long you keep your Amazon EC2 instance running, how much data you transfer into AWS, and other service costs associated with this Guidance. For example, this Guidance does not deploy an Amazon Simple Storage Service (Amazon S3) bucket; however, it allows you to configure your own Amazon S3 bucket for media file storage. Lastly, you can measure the efficiency of the workloads, and the costs associated with delivery, by using AWS Systems Manager Application Manager. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Video editors, loggers, graphic designers, colorists, and other post-production team members work on cloud-based virtual computers using an Amazon EC2 instance and FSx for Windows File Server storage instead of dedicated systems at their desk. This reduces idle resources, the need for temporary transfer storage devices, and also provides the right-size computer to meet your project’s requirements [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
