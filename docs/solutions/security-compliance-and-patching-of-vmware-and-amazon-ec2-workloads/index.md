---
source_url: https://docs.aws.amazon.com/solutions/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads/index.html
---

---
title: 'Guidance for Security Compliance and Patching of VMware and Amazon EC2 Workloads'
canonical_url: https://docs.aws.amazon.com/solutions/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Security Compliance and Patching of VMware and Amazon EC2 Workloads

## Overview

This Guidance helps you set up centralized patching and compliance management for your VMware virtual machines (VMs) both on-premises and in the cloud. Using AWS Systems Manager, you can establish a secure maintenance and compliance system for patching and controls. By collecting all security findings in a single location, you can reduce the administrative burden around patching and compliance while also gaining operational efficiencies and improving observability.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads.pdf?target=_blank)

![Architecture diagram](/images/solutions/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads/images/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads-1.png)

1. **Step 1**: This Guidance requires an inventory and data collection from the workloads. AWS Systems Manager uses an agent (SSM Agent). Install the SSM Agent into the VMware Cloud on AWS or on-premises nodes to manage. The SSM Agent requires communication with the AWS API over standard HTTPS ports. Because the SSM Agent always starts the communication, allowing any inbound rules is not necessary (egress tcp ports 443 and 80).
1. **Step 2**: Systems Manager is the operations hub for your AWS applications and resources and is broken into four core feature groups: Operations Management, Application Management, Change Management, and Node Management.
1. **Step 3**: AWS Security Hub enables automated checks for standard best practices, such as AWS Foundational Security Best Practices (FSBP), Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 and v1.4.0, and Payment Card Industry Data Security Standard (PCI DSS). Note: At the time of publication of this Guidance, Security Hub reports the resource type of all managed nodes as "Amazon Elastic Compute Cloud (Amazon EC2) instance." This includes on-premises servers and VMs that you have registered for use with Systems Manager.
1. **Step 4**: Support teams log in to Systems Manager to perform administrative tasks, such as hybrid activations and patch policy creation.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Dive deep into the implementation guide for additional customization options and service configurations to tailor to your specific needs.

[Open guide](https://aws-solutions-library-samples.github.io/cloud-operations/security-compliance-and-patching-of-vmware-and-amazon-ec2-workloads.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Patch Manager, a capability of Systems Manager, allows you to deploy software patches automatically across on-premises or cloud instances. You can set a patch baseline with rules that state which patches should automatically be installed, or you can choose to have Patch Manager show you a report of all missing patches. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Security Hub offers a centralized view of your security findings. Once established, other services will automatically send security findings to Security Hub so you can easily check whether or not your services are in compliance. Security Hub acts on security findings by either alerting you, raising the finding on a dashboard, or kicking off an automation to resolve the finding. This helps you to discover vulnerabilities as soon as they occur and remediate them once discovered. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

VMware Cloud on AWS is the preferred service for AWS for all vSphere-based workloads. VMware Cloud on AWS includes vSphere High Availability (HA) which restarts VMs automatically in the event of a failed ESXi host. Distributed Resource Scheduler (DRS) is also enabled, which can be used along with vMotion to live migrate running VMs off of hosts before maintenance is performed. VMware Cloud on AWS helps you avoid or minimize downtime for VMware workloads running on AWS. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

VMware Cloud on AWS allows you to provision ESXi hosts dynamically using a feature called Elastic Distributed Resource Scheduler (eDRS). eDRS will grow or shrink the VMware Cloud on AWS clusters based on the workloads running on top of those clusters. eDRS accomplishes this by responding to the total CPU and memory load within the VMware Cloud on AWS cluster. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

The Guidance doesn’t require additional servers or OS licensing, minimizing overall costs. With the exclusion of the servers being patched, this Guidance is fully serverless and uses managed services. Patching is automated, which can reduce operational costs compared to manual patching. The main service costs to consider are: [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

VMware Cloud on AWS with eDRS can shut down extra capacity, which saves on resource consumption, such as power and cooling. eDRS also allows you to design for the smallest possible footprint and dynamically scale to meet your workload demands. Additionally, Security Hub and Systems Manager are managed and operated by AWS. As such, you do not need to deploy additional servers and infrastructure to accomplish your compliance and patching requirements. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
