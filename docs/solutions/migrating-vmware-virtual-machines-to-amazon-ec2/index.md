---
source_url: https://docs.aws.amazon.com/solutions/migrating-vmware-virtual-machines-to-amazon-ec2/index.html
---

---
title: 'Guidance for Migrating VMware Virtual Machines to Amazon EC2'
canonical_url: https://docs.aws.amazon.com/solutions/migrating-vmware-virtual-machines-to-amazon-ec2/
source: aws-documentation
generated_on: 2026-10-06
---

# Guidance for Migrating VMware Virtual Machines to Amazon EC2

Simplify VMware migration through an automated migration process for your virtual machines

## Overview

This Guidance shows how to migrate your VMware virtual machines (VMs) to Amazon Elastic Compute Cloud (Amazon EC2) using AWS Transform MGN (AWS MGN). Migrating on-premises VMware workloads to Amazon EC2 offers enhanced scalability, improved performance, and reduced operational costs. AWS MGN streamlines the migration process with seamless, automated block-level replication, allowing you to thoroughly test migrated VMs on Amazon EC2 while continuously replicating the original source server. This Guidance minimizes the cutover window and facilitates live migrations with no downtime or minimal customer impact.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/migrating-vmware-virtual-machines-to-amazon-ec2.pdf)

![Architecture diagram](/images/solutions/migrating-vmware-virtual-machines-to-amazon-ec2/images/migrating-vmware-virtual-machines-to-amazon-ec2-1.png)

1. **Step 1**: Initialize AWS Transform MGN (AWS MGN) with the required AWS Identity and Access Management (IAM) permissions.
1. **Step 2**: Follow Network Settings preparations to create Amazon Virtual Private Cloud (Amazon VPC) subnets to use for your replicated, test, and cutover Amazon Elastic Compute Cloud (Amazon EC2) instances along with the respective security groups.
1. **Step 3**: Create Amazon VPC interface endpoints to connect privately to the Amazon EC2 and AWS MGN APIs. Confirm that the security group attached to the VPC endpoints allows ingress traffic on port 443.
1. **Step 4**: Create post-launch actions in AWS MGN to install the AWS Systems Manager (SSM) agent and uninstall no longer needed VMware tools from Windows and Linux EC2 instances.
1. **Step 5**: Add source servers to AWS MGN by installing the AWS Replication Agent over TCP port 443 on each individual VM to begin the initial synchronization process.
1. **Step 6**: The AWS Replication Agents open an outbound connection over TCP port 1500 from the source servers to the replication servers. These communications must be allowed by the customer gateway and VMWare NSX-T edge gateway. The replication servers copy the source volumes into Amazon Elastic Block Store (Amazon EBS) volumes.
1. **Step 7**: The replication servers call the Amazon Simple Storage Service (Amazon S3) API to retrieve software component and configuration.
1. **Step 8**: Launch a test EC2 instance for each source server that is "ready for testing" in the AWS MGN console. Validate and test the EC2 instances and verify the post-launch actions.
1. **Step 9**: After testing and validation completion, launch cutover instances and finalize the migration.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment.

[Open implementation guide](https://aws-solutions-library-samples.github.io/migration/migrating-vmware-virtual-machines-to-amazon-ec2.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS MGN is natively integrated with Amazon EC2 and Systems Manager services. AWS MGN helps you migrate VMware VMs to Amazon EC2, perform non-disruptive tests, achieve cutover (within minutes), and automate optimization or application modernization using Systems Manager. AWS MGN allows you to migrate applications to AWS without disrupting operations, using an automated process that requires no changes to applications, architecture, or servers, minimizing manual effort. It enables application benchmarking, test cutovers to identify issues before impacting operations, and simplified configuration and management of migrated resources through Systems Manager. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

AWS MGN enhances data replication security through traffic encryption, access controls, and VPC endpoints, enabling private connections between VPC resources and AWS services. Security groups restrict access to VPC endpoints from allowed IP ranges. AWS MGN uses TLS over TCP ports 443 (management plane) and TCP port 1500 (data plane), improving security in the default configuration. VPC endpoints keep traffic between EC2 instances and AWS services within the AWS network. Security groups further safeguard workloads and communication between on-premises and cloud environments. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS MGN has a retry mechanism to handle replication issues and provides detailed error information with explanations and mitigation steps when user intervention is needed (for example, network connectivity or authentication problems). Further, AWS MGN test and cutover instances together with Systems Manager allow you to validate whether workload meets functional and non-functional requirements as before the migration. AWS MGN allows to focus on the migration and rely on the service reliability to deal with temporary network unavailability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Once initial replication is complete, the AWS MGN agent compresses and sends deltas which has minimal performance hit on the replicating servers. AWS MGN uses LZ4 compression during transit resulting in 60-70% compression depending on the type of data. The agent setup doesn’t require reboot, making it ideal for production servers. Replication servers continue to run their workload without any interruption from the agent or replication, improving cost reduction and network bandwidth. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS MGN Launch settings allow launching test or cutover instances with instance types matched to the source VM’s hardware configuration and usage patterns, optimizing cost and performance. Additionally, AWS MGN uses an optimal number of lightweight replication instances to replicate data between multiple VMware VMs and can continuously replicate the data without launching test or cutover instances. This helps eliminate the need to pay for compute resources equivalent to the source environment during replication. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS MGN Launch settings help improve the efficiency of your migrated workload by using the fewest compute resources while achieving high utilization. Further, with lightweight, auto-scaled replication instances, you don't provision the full compute required for the source environment during replication, effectively minimizing your workload’s environmental impact. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
