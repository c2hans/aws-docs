---
source_url: https://docs.aws.amazon.com/solutions/playout-origination-and-master-control-operation-on-aws/index.html
---

---
title: 'Guidance for Playout Origination and Master Control Operation on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/playout-origination-and-master-control-operation-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Playout Origination and Master Control Operation on AWS

## Overview

This Guidance shows you how to transition your linear playout origination and master control operations to the cloud. By harnessing computing capacity, storage options, and the extensive [Media Services](https://aws.amazon.com/media-services/) offerings of AWS, you can achieve efficient resource allocation, scalability, cost effectiveness, and resiliency. This Guidance provides best practices, helping you modernize your content delivery and viewer engagement while optimizing operational efficiency.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/playout-origination-and-master-control-operation-on-aws.pdf)

![Architecture diagram](/images/solutions/playout-origination-and-master-control-operation-on-aws/images/playout-origination-and-master-control-operation-on-aws-1.png)

1. **Step 1**: An AWS independent software vendor (ISV) provides third-party feeds hosted on Amazon Elastic Compute Cloud (Amazon EC2). AWS Elemental MediaConnect delivers contribution feeds.
1. **Step 2**: A separate virtual private cloud (VPC) hosting a live event cloud production environment contributes feeds to the playout VPC using VPC peering.
1. **Step 3**: Redundant broadcast routers running on Amazon EC2 instances in two Availability Zones (AZs) receive and switch between sources. The broadcast router sends the feeds to the playout channel engines hosted on Amazon EC2.
1. **Step 4**: The playout channel engines send the "program out" feed—combining the sources and other elements, such as graphics—back to the broadcast routers. AWS Elemental MediaLive and AWS Elemental MediaPackage also receive the feeds.
1. **Step 5**: AWS Elemental MediaTailor performs dynamic ad-insertion on the over-the-top feed for distribution using Amazon CloudFront.
1. **Step 6**: The playout channel output is also sent to the distribution, where MediaConnect and MediaLive deliver it to terrestrial or satellite distribution chains.
1. **Step 7**: Multi-viewer and video scopes running on Amazon EC2 monitor video feeds present in the broadcast router for quality assurance.
1. **Step 8**: Monitoring tools generate alarms to implement automatic video routing after processing by AWS Lambda.
1. **Step 9**: AWS Systems Manager facilitates centralized management and patching of all components, and AWS Secrets Manager stores all credentials needed to remotely access the instances.
1. **Step 10**: Amazon CloudWatch, Amazon Managed Grafana, and AWS Cost Explorer monitor the performance and cost of all system components.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses CloudWatch and Amazon Managed Grafana to let you visualize and analyze operating system states, helping you quickly identify and remediate noncompliant components. You can then use Lambda to invoke actions based on events or alarms created by these monitoring components. Lambda lets you implement complex incident recovery logic for multiple systems, supporting operators by removing complex manual tasks. Additionally, this Guidance simplifies resource management by using AWS Systems Manager Patch Manager to automatically scan and patch Amazon EC2 instances. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance lets you scope down AWS Identity and Access Management(IAM) policies to the minimum permissions required for your Guidance to function properly, helping you limit unauthorized access to resources. Additionally, Secrets Manager stores all passwords required to access the bastion servers and application interfaces and helps you protect access to resources. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses two AZs, reducing the risk of AZ-level events impacting the output of your system. Additionally, AWS media services like MediaLive and MediaConnect support redundant primary and backup inputs, helping you build resilient video workflows. Lambda adds resiliency and reliability to your workflows through automatic scaling, retries, and high availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance uses CloudWatch to collect and visualize near real-time logs, metrics, and event data in automated dashboards, helping you streamline infrastructure and application maintenance. You can easily monitor various metrics that indicate optimal instance sizing for applications running on Amazon EC2. Additionally, you can use MediaConnect in conjunction with protocols, such as Real-time Transport Protocol (RTP) with forward error correction or Secure Reliable Transport (SRT), to deliver video at a high rate without packet loss. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

This Guidance lets you take advantage of highly predictable baseline usage requirements and reduce your data transfer costs by making a long-term commitment through MediaConnect reserved output bandwidth. MediaConnect and MediaLive pricing is based on the output bitrate of the video feeds being processed, so you can optimize costs by tuning the video and encoding quality. MediaLive also supports reserved pricing for inputs, outputs, and add-on features. Additionally, AWS ISV products, such as broadcast routers and playout engines, run on Amazon EC2 instances and have stable 24/7 workloads. Savings Plans can help reduce the cost of 24/7 operations. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance uses managed services such as MediaConnect, Lambda, Amazon Managed Grafana, and Amazon Simple Storage Service (Amazon S3), minimizing workload requirements. MediaConnect scales based on demand so you don’t have to manage the underlying infrastructure. This reduces waste and energy consumption, ultimately helping you reduce your carbon footprint. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
