---
source_url: https://docs.aws.amazon.com/solutions/scalable-cryo-em-on-aws-parallel-computing-service-pcs/index.html
---

---
title: 'Guidance for Scalable Cryo-EM on AWS Parallel Computing Service (PCS)'
canonical_url: https://docs.aws.amazon.com/solutions/scalable-cryo-em-on-aws-parallel-computing-service-pcs/
source: aws-documentation
generated_on: 2026-10-01
---

# Guidance for Scalable Cryo-EM on AWS Parallel Computing Service (PCS)

## Overview

This guidance shows how to deploy a secure, high-performance Cryo-EM analysis environment on AWS ParallelCluster Service, enabling research organizations to accelerate molecular structure determination. By combining CryoSPARC software with flexible CPU/GPU compute options, high-throughput FSx storage, and automated Slurm job management, researchers can efficiently process large-scale Cryo-EM datasets through a secure web interface. The solution streamlines deployment while providing the computational power and storage performance needed for advanced structural biology research.

## Benefits

### Accelerate scientific discoveries

Deploy purpose-built high-performance computing infrastructure for Cryo-EM research without managing complex hardware. Researchers can focus on breakthrough science while AWS PCS automatically provisions the right compute resources for each processing stage.

### Optimize research costs

Scale computing resources dynamically based on workload demands with purpose-designed instance groups for CPU and GPU processing. Pay only for the computational power you need when you need it, eliminating idle infrastructure costs during research cycles.

### Streamline data workflows

Access high-throughput storage with FSx for Lustre and EFS to efficiently process and store large microscopy datasets. The integrated storage solution provides researchers with seamless data management from initial capture through processing to long-term archival in S3.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/scalable-cryo-em-on-aws-parallel-computing-service-pcs.pdf)

![Architecture diagram](/images/solutions/scalable-cryo-em-on-aws-parallel-computing-service-pcs/images/scalable-cryo-em-on-aws-parallel-computing-service-pcs-1.png)

1. **Step 1**: The admin user initiates SSH/SSM connection to the login node, a statically-provisioned Amazon Elastic Compute Cloud (Amazon EC2) instance in the public subnet. The login node is part of the AWS Parallel Computing Service (Amazon PCS) cluster.
1. **Step 2**: The Slurm controller for the cluster is in an Amazon Virtual Private Cloud (Amazon VPC).
1. **Step 3**: CryoSPARC is installed on a shared file system mounted to both the login node and compute nodes. Installing the software includes downloading the installation script, applying the license key, and initializing the server.
1. **Step 4**: User access configuration involves creating CryoSPARC user accounts and establishing secure SSH tunneling. The web interface is configured for remote access, allowing researchers to interact with the platform through their browsers securely.
1. **Step 5**: The storage configuration uses Amazon FSx for Lustre at 250 MB/s/TiB throughput with Amazon Simple Storage Service (Amazon S3) Data Repository Association for Cryo-EM data storage. Amazon FSx mounts to /shared for processing while Amazon Elastic File System (Amazon EFS) mounts to /home for user data.
1. **Step 6**: The Slurm controller manages three AWS PCS queues (cpu, single-gpu, multi-gpu) mapped to their corresponding compute node groups in the private subnet. CPU groups use c5a.8xlarge instances, single-GPU uses g6.4xlarge instances, and multi-GPU uses g6.48xlarge instances. The queues map to compute node groups and lanes in the CryoSPARC Web UI. Users submit jobs to lanes, and Slurm routes jobs to queues and directs workloads to Amazon EC2 instance types for resource allocation and job processing.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-scalable-cryo-em-on-aws-parallel-computing-service)

[Read usage guidelines](/solutions/guidance-disclaimers/)
