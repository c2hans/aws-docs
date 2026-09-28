---
source_url: https://docs.aws.amazon.com/solutions/building-perforce-helix-core-on-aws/index.html
---

---
title: 'Guidance for Building Perforce Helix Core on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/building-perforce-helix-core-on-aws/
source: aws-documentation
generated_on: 2026-09-28
---

# Guidance for Building Perforce Helix Core on AWS

## Overview

This Guidance demonstrates how to install and configure Perforce Helix Core, a popular version management tool for game developers, on AWS. It shows how to deploy Perforce with high availability across multiple AWS Regions and also covers secure connectivity from on-premises data centers and remote clients. By following this Guidance, game developers can implement a Perforce Helix Core installation on AWS, aligning to best practices and keeping costs low.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/building-perforce-helix-core-on-aws.pdf)

![Architecture diagram](/images/solutions/building-perforce-helix-core-on-aws/images/building-perforce-helix-core-on-aws-1.png)

1. **Step 1**: Choose a file system to store your depot. If your depot is less than 16 TB, we recommend running Helix Core on Amazon Elastic Block Store (Amazon EBS) GP3 volumes. For larger depots, we recommend Amazon FSx for NetApp ONTAP or Amazon FSx for OpenZFS. To optimize costs, FSx for ONTAP deduplication and compression are well suited for use with Helix Core depots.
1. **Step 2**: The Perforce Helix Edge Server Proxy in the studio data center connects to the primary AWS Region with AWS Direct Connect or AWS Site-to-Site VPN, depending on bandwidth and connection availability needs. On-site Perforce clients connect to the proxy to gain the benefits of local performance for commits.
1. **Step 3**: Remote users connect to the nearest edge server through AWS Client VPN, another virtual private network (VPN) solution, or with a virtual workstation.
1. **Step 4**: AWS Transit Gateway connects Amazon Virtual Private Clouds (Amazon VPCs) to on-premises networks and connects to VPN through a hub-and-spoke model that simplifies complex peering relationships and encrypts data in transit.
1. **Step 5**: These connections go through a NAT Gateway, which allows resources in a private subnet to connect to services outside of the Amazon VPC. External services cannot initiate a connection with the private resources.
1. **Step 6**: Users choose a Perforce commit-edge server to connect to based on the closest Region. This commit-edge architecture offers the best overall performance with most commands running locally.
1. **Step 7**: The primary and replica servers run in separate Availability Zones to increase availability. High availability and disaster recovery can be achieved through either a snapshot or replica strategy (with edge server replicas as an option). Restoring from an Amazon EBS snapshot or from AWS Backup is slower than replica failover, but more cost effective.
1. **Step 8**: AWS Backup is used for Amazon FSx backups. For Amazon EBS, snapshots are the standard backup mechanism. Though AWS Backup works with Amazon EBS, it is not required for this solution.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy?  This sample code shows how to deploy P4 Server (formerly Helix Core), P4 Code Review (formerly Helix Swarm), and the P4 Auth Service (formerly the Helix Auth Service) using Amazon Route53 as the DNS provider.

[Go to sample code](https://github.com/aws-games/cloud-game-development-toolkit/tree/main/modules/perforce/examples/create-resources-complete)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

AWS CloudFormation allows consistent, repeatable deployments of the application and resources, removing sources of error during deployment that may impact security, reliability, and costs. Amazon CloudWatch provides operational metrics and monitoring for the application and resources, logging to a single location, no matter how many resources you are using. Operational and health metrics are also captured at scale and are on by default for all services. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Transit Gateway encrypts traffic any time it traverses network links, both inside and outside of AWS. Transit Gateway is a secure, centrally managed service to provide secure peering for both inter- and intra-Region networking. Client VPN provides a secure connection to the hosted Perforce Helix Core applications from off-site clients. For virtual workstations, NICE DCV secures both pixels and end-user inputs using end-to-end encryption between the client and server. It also requires authentication from the client before allowing a connection. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Backup centrally manages and automates data protection for the various storage mechanisms used in this architecture diagram. AWS Backup simplifies the backup and recovery of Amazon FSx and, if desired, Amazon EBS stores your Perforce depot and builds a foundation for disaster recovery and business continuity. Additionally, Amazon Elastic Compute Cloud (Amazon EC2) allows you to deploy Helix Core standby replicas in different Availability Zones, allowing instant failover in case of an Availability Zone issue. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EC2 provides global infrastructure to place Helix Core edge servers closer to your globally distributed users. Deploying Helix Core edge servers across multiple AWS Regions allows studios to give lower latency access to developers globally by placing edge instances closer to their location. Replication occurs on the AWS high-speed global network, rather than relying on public internet. This allows edge servers to keep in sync more rapidly and frequently. Additionally, high performance storage is critical for allowing Helix Core to respond quickly and scale to multiple users. Both Amazon EBS and Amazon FSx provide high speed SSD based storage for responsive file retrieval and commits. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon EC2 provides many different sizes of instances, allowing developers to choose the exact instance size they need. Instances can be scaled up and down as projects transition through various phases of the game development pipeline. Additionally, Amazon FSx provides a cost-effective solution for larger Helix Core depots. Amazon FSx is well suited to the use patterns of large Helix Core depots, and Amazon EBS is an even more cost-effective choice when depot sizes are below 16 TB. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2 allows studios to create instances on demand and provides efficient CPU options. Allowing studios to move from on-premises hardware to the cloud enables them to run compute power on an as-needed basis. This reduces waste from redundant or obsolete hardware and means that studios’ Perforce infrastructure will run from at least 90% renewable energy. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
