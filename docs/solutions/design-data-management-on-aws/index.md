---
source_url: https://docs.aws.amazon.com/solutions/design-data-management-on-aws/index.html
---

---
title: 'Guidance for Design Data Management (SOS) on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/design-data-management-on-aws/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Design Data Management (SOS) on AWS

## Overview

This Guidance helps guide you through the process of building a design data management system in the cloud using a Design Data Management (SOS) environment. This includes setting up a Design Data Management (SOS) primary server and a network file system (NFS) server. By setting up this environment, you can provide your team with global access to design data.

## How it works

This architecture diagram shows how you can set up a design data management platform on AWS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/design-data-management-on-aws.pdf)

![Architecture diagram](/images/solutions/design-data-management-on-aws/images/design-data-management-on-aws-1.png)

1. **Step 1**: Use the Design Data Management (SOS) Amazon Machine Image (AMI) to set up an SOS primary server on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The AMI is preconfigured with the latest SOS server, a license server, a PostgreSQL database to store design projects, and an Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 2**: The SOS server runs continuous hot backups of intellectual property and other design data to the S3 bucket.
1. **Step 3**: The SOS server persistently stores design projects to an Amazon Elastic Block Store (Amazon EBS) volume. The server is preconfigured to use the recommended gp2 volume with 500 GB disk space by Keysight.
1. **Step 4**: Use an Elastic IP Address (EIP), a feature of Amazon EC2, to export the NFS, allowing NFS clients to mount across Availability Zones, Regions, and on-premises data centers.
1. **Step 5**: Configure the NFS server on an EC2 instance backed by a non-volatile memory express (NVMe) EBS volume. Deploy the SOS cache server on the same instance.
1. **Step 6**: Semiconductor workflows use the NFS mount for running jobs in batch mode or mounted on workstations using a virtual desktop interface (VDI).
1. **Step 7**: Use AWS Client VPN to connect to the Design Data Management (SOS) environment on AWS.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

You can use AWS CloudFormation and AMIs to quickly launch multiple environments across multiple AWS Regions. CloudFormation allows you to build repeatable design data management workflows on AWS. AMIs allow you to install and configure the entire environment, including Design Data Management (SOS)-configured NFS servers to suite large chip design workloads. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Engineers can use Client VPN to connect to the Design Data Management (SOS) environment on AWS. Client VPN secures both terminal sessions and custom VDI sessions. Client VPN also allows users to connect to the virtual environment using a VPN connection, which encrypts users’ data and identities. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

This Guidance uses Amazon S3 and Amazon EBS to create a short-term and long-term backup strategy. Your data will be stored on a reliable EBS volume that syncs the design database every hour. Backups are performed to an S3 bucket when changes are committed, which is either daily or when engineering change orders (ECOs) are complete. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The IOPS required for front-end (logical) chip design demand instance types have local attached NVMe volumes. By leveraging EC2 instances that have local NVMe volumes, you can achieve local I/O performance of 3.3M IOPS. This makes these NVMe volumes well suited for the chip design workloads that will often require millions of IOPS for front-end design. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

CloudFormation enables customer to quickly launch and tear down environments, and Amazon S3 has multiple storage tiers based on access to help reduce customer cost. Since you will only need to have the design data available in an NFS when engineering teams are working, CloudFormation helps you launch an environment only when needed. By storing design data in inexpensive S3 tiers and copying only needed data to the NFS file system, you can save on costs compared to running an operational environment and storing data 24/7. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

In this Guidance, CloudFormation reduces the amount of time that resources are in production, meaning the design data and the engineering environments are only available when engineers require them to be. This results in resources only being available during working hours and being shut down overnight and during weekends. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
