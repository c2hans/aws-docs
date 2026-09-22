---
source_url: https://docs.aws.amazon.com/solutions/cloud-edge-global-access-on-aws/index.html
---

---
title: 'Guidance for Cloud Edge Global Access on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/cloud-edge-global-access-on-aws/
source: aws-documentation
generated_on: 2026-09-22
---

# Guidance for Cloud Edge Global Access on AWS

## Overview

This Guidance shows how to deploy a software-defined wide area network (SD-WAN) router to provide resilient communications and applications at the edge. It enables you to use your organic transmission systems—whether hardware or virtual as well as government or commercial—to access the AWS global infrastructure. This affords you unified access to both your cloud environments and your edge locations, helping you mitigate infrastructure limitations. This Guidance currently uses the Juniper Session Smart Router (Zero Trust to enhance security), but you can adjust it to be SD-WAN agnostic.

## How it works

### Overview

This architecture diagram shows the high-level functional components deployed in AWS GovCloud (US) and commercial partitions. It supports up to 10 commercial AWS Regions or AWS Local Zones and a variety of interface quantities and instance sizes.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-edge-global-access-on-aws.pdf?target=_blank)Step 1The AWS commercial partition contains software-defined wide area network (SD-WAN) Routers used to service edge nodes connected through internet connectivity options. These can be scaled up to 10 Regions and deployed in multiple highly available Availability Zones (AZs).Step 2SD-WAN orchestration runs from the AWS GovCloud (US) partition. It can be deployed to be highly available in multiple AZs or multiple Regions.Step 3AWS Global Accelerator provides rapid egress from the commercial internet onto the AWS global infrastructure for higher security, faster throughput, and lower latency.Step 4SD-WAN Routers in the AWS GovCloud (US) partition provide direct access to Impact Level 4 or 5 (IL4 or IL5) workloads or the internet.Step 5Multiple AWS GovCloud (US) Regions provide high availability.Step 6SD-WAN Routers use the AWS backbone for secure inter-partition connectivity and can fully encrypt all traffic using Federal Information Processing Standards (FIPS).Step 7The cloud-edge global access SD-WAN Routers are software-based and can be run on existing hardware or on the SD-WAN vendor's own hardware.Step 8Traffic egresses from the cloud-edge global access SD-WAN Routers to on-premises datacenters or the internet, depending on the mission's needs.### Core orchestration flow

This architecture diagram shows the core orchestration flow for the deployment of an SD-WAN controller. Because all routers running in the cloud are provisioned before step 4, you can fully build out the configurations using the “as build” details from those routers. This diagram also provides steps for data protection.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/cloud-edge-global-access-on-aws.pdf#page=2?target=_blank)Step 1The Amazon Elastic Compute Cloud (Amazon EC2) deployment machine runs an AWS Cloud Development Kit (AWS CDK) for Terraform.Step 2AWS CDK for Terraform is used to deploy into AWS partitions.Step 3The SD-WAN controller is provisioned from an Amazon Machine Image (AMI) through the AWS CDK for Terraform.Step 4The automation builds vendor-specific SD-WAN configuration files.Step 5The SD-WAN controller is configured using AWS Systems Manager documents.Step 6Configuration snapshots are automated and stored in Amazon Simple Storage Service (Amazon S3).Step 7AWS Backup provides snapshots to the SD-WAN controller disk.## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Using infrastructure as code (IaC), AWS CDK for Terraform enables complete and quick deployment, with a time expectation of 45 minutes from start to finish. Global Accelerator provides a highly available, distributed-denial-of-service-resilient anycast address assigned to SD-WAN routers deployed on AWS. Additionally, used for remote management of machines, Systems Manager removes the need for Secure Shell (SSH) access or bastion hosts. Its documents provide a mechanism for programmatically deploying configurations into the SD-WAN control plane and modifications to the deployed infrastructure. Finally, AWS Lambda functions automatically create deployable ISO images (which are disk image files) for edge routers, simplifying the deployment process. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses multiple partitions—commercial and government—to maintain data sovereignty. And to maintain security, the control plane exists by default within AWS GovCloud (US). This setup also enables you to directly connect with existing AWS deployments in IL4 or IL5 environments. Additionally, the Systems Manager Parameter Store enables you to safely store sensitive data outside the deployed Amazon EC2 instances. And Systems Manager Session Manager removes the need for direct SSH access into the deployed instances. When enabled, AWS Shield also protects these instances from volumetric attacks. Global Accelerator and Amazon Virtual Private Cloud (Amazon VPC) Flow Logs both provide a historical record of network traffic data seen across the deployment. Finally, AWS GuardDuty provides visibility into the VPC environments and external threats. If needed, AWS security groups can lock down external-to-internal and internal-to-internal traffic. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses multiple Regions, AWS Local Zones, and AZs to maintain a highly available SD-WAN network on top of the AWS infrastructure. The SD-WAN routers provide fault detection and rerouting, and AWS provides infrastructure resilience. As a result, this architecture can sustain multiple outages simultaneously without losing its communication capability. Additionally, Global Accelerator enables remote locations to access AWS resources from more than 600 AWS global points of presence in the most efficient manner. Finally, AWS Backup uses Lambda to automatically back up configurations and relevant public key infrastructure data in case you need to manually recover SD-WAN controllers. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

This Guidance helps you realize your network and resiliency goals while minimizing your technical and administrative burden. For example, Global Accelerator delivers extremely low-latency connectivity from the edge to AWS. AWS prefix lists enable you to easily adjust security rules when many locations need access to the cloud-edge environment. Additionally, AWS CDK for Terraform supports a standards-based multicloud-capable IaC architecture. Systems Manager handles the initial configuration of the SD-WAN controller, which then configures all the SD-WAN routers. You can also configure Amazon EC2 instance sizes within AWS CDK for Terraform, defining router quantity, location, and size based on your operational needs. Finally, this Guidance provides an ISO-builder process, powered by Lambda. By decreasing the usual number of steps from over 20 to just 5, this process helps remote teams with minimal training to efficiently and rapidly deploy new routers. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The bandwidth costs in this Guidance are pay per use, and you can optimize costs by rightsizing your environments at deployment time. For example, you can configure Amazon EC2 instance sizes and quantities based on your current needs, then scale them up and down as needed. Additionally, you can use Amazon CloudWatch alarms to automate dynamic capacity adjustments. In a high-availability deployment, CloudWatch monitors the primary router and enables a secondary router when the network load requires an increase in capacity. It then shuts down the secondary router once the high load subsides, helping you lower costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance lets you optimize compute by rightsizing your Amazon EC2 instances for your needs. Amazon EC2 also scales automatically based on demand. This enables you to reduce your energy use for compute. Additionally, CloudWatch lets you automate dynamic capacity adjustment, further reducing your carbon footprint. CloudWatch keeps a secondary router disabled until it is needed to support the primary router for large network loads. It then shuts down the secondary router once the high load subsides, helping you avoid energy waste. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
