---
source_url: https://docs.aws.amazon.com/solutions/knfsd-file-cache-on-aws/index.html
---

---
title: 'Guidance for KNFSD File Cache on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/knfsd-file-cache-on-aws/
source: aws-documentation
generated_on: 2026-09-25
---

# Guidance for KNFSD File Cache on AWS

## Overview

This Guidance helps organizations overcome high data access latency and limited throughput when accessing remote NFS storage by deploying a high-performance caching layer on Amazon EC2 between the remote source and AWS compute workloads. KNFSD File Cache proxy nodes are deployed in the same Availability Zone as the compute fleet, creating an in-line cache for data stored on on-premises NFS filers or in remote AWS Regions. Compute nodes mount and access the cached data using standard NFS protocols (v3, v4.1, or v4.2) without requiring any modifications to existing client configurations. For workloads with high compute node counts, an auto-scaling group of additional proxy nodes provides a second tier of caching to handle increased demand. You can dramatically reduce data access latency, improve throughput, and seamlessly scale NFS file serving to large compute fleets while maintaining your existing infrastructure and client setups.

## Benefits

### Accelerate remote data access

Reduce latency for compute workloads by caching remote NFS data closer to where it is processed on AWS. Your compute nodes access frequently used files from local proxy caches instead of repeatedly retrieving data across slower wide-area connections.

### Scale to large compute fleets

Support high compute node counts without modifying client configurations by deploying a two-tier, auto-scaling cache architecture. Your teams can expand compute capacity while the caching layer automatically adjusts to meet growing demand.

### Connect securely across environments

Extend your existing on-premises or multi-region NFS storage to AWS without re-architecting your storage infrastructure. AWS Direct Connect, AWS Site-to-Site VPN, and inter-region VPC peering provide secure, reliable connectivity options to fit your network requirements.

## How it works

### KNFSD File Cache

This architecture diagram shows how to deploy a Kernel NFS Daemon (KNFSD) File Cache NFS Caching Proxy to scale the presentation of a remote NFS filer to a fleet of compute nodes on AWS

[Download the architecture diagram](downloads/knfsd-file-cache-on-aws.pdf)Step 1Original source data to be accessed by compute nodes running in AWS is stored in a NFS filer hosted either in an on-premises data center or in an Amazon Virtual Private Cloud (Amazon VPC) in a different AWS region.Step 2Securely connect the remote facility to AWS using AWS Direct Connect or AWS Site-to-Site VPN for on-premises facilities or use Inter-Region Peering to connect the two VPCs across AWS regions.Step 3Proxy and in-line cache the remote filer by deploying a KNFSD File Cache proxy node on an Amazon Elastic Cloud Compute (Amazon EC2) instance deployed in a private subnet in the same Availability Zone of the VPC hosting the compute nodes.Step 4Compute nodes access cached versions of the source data from the KNFSD File Cache proxy nodes by mounting the filesystem using NFS v3, v4.1 or v4.2. No client side modifications are required.### Two-tier Fan Out

This architecture diagram shows how to deploy a two-tier fan-out architecture of a Kernel NFS Daemon (KNFSD) File Cache NFS Caching Proxy to scale the presentation of a remote NFS filer to a fleet of compute nodes on AWS

[Download the architecture diagram](downloads/knfsd-file-cache-on-aws.pdf)Step 1Original source data to be accessed by compute nodes running in AWS is stored in a NFS filer hosted either in an on-premises data center or in an Amazon Virtual Private Cloud (Amazon VPC) in a different AWS region.Step 2Securely connect the remote facility to AWS using AWS Direct Connect or AWS Site-to-Site VPN for on-premises facilities. Use Inter-Region Peering to connect two VPCs across AWS regions.Step 3Deploy a first tier KNFSD File Cache proxy node to proxy and in-line cache the remote filer on an Amazon Elastic Cloud Compute (Amazon EC2) instance deployed in a private subnet in the same Availability Zone of the VPC hosting the compute nodes. Select an instance-type 2-8x more powerful than the second tier of KNFSD proxy nodes.Step 4To support high compute node counts, deploy an auto-scaling group of additional KNFSD File Cache proxy nodes to provide a second tier of caching. Use NFS v4.1+ to overcome file handle size limitations in NFS v3.Step 5Compute nodes access cached versions of the source data from the KNFSD File Cache proxy nodes by mounting the filesystem using NFS v4.1 or v4.2. No client side modifications are required.## Related content

- **KNFSD File Cache Sample code**: This sample code demonstrates a flexible, feature-rich, and customizable approach to deploy knfsd file cache

[Go to sample code](https://github.com/awslabs/knfsd-file-cache)

- **Introducing KNFSD File Cache: Extending Your NFS Storage into the Cloud**: Learn how KNFSD File Cache works under the hood, who it's built for, the benefits of running it on AWS, and how to deploy a production-ready autoscaling cluster with a single Terraform module; including customer testimonials from Wētā FX and ILM.

[View blog post](https://aws.amazon.com/blogs/media/introducing-knfsd-file-cache-extending-your-nfs-storage-into-the-cloud/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
