---
source_url: https://docs.aws.amazon.com/solutions/deploying-high-performance-computing-clusters-on-aws/index.html
---

---
title: 'Guidance for Deploying High Performance Computing Clusters on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/deploying-high-performance-computing-clusters-on-aws/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Deploying High Performance Computing Clusters on AWS

Conforming high performance computing (HPC) workloads with NIST SP 800-223

## Overview

This Guidance demonstrates how to use infrastructure as code (IaC) templates to deploy secure and compliant high performance computing (HPC) workloads. The IaC templates automatically provision resources for a fully functional HPC environment that aligns with the security requirements of the National Institute of Standards and Technology (NIST) Special Publication (SP) 800-223. By offering a comprehensive suite of AWS services tailored for HPC, including high-performance processors, low-latency networking, and scalable storage options, this Guidance allows users to efficiently build and manage secure, compliant, and high performing compute environments.

## How it works

### Network, security and infrastructure deployment

This architecture diagram shows how to deploy this Guidance using AWS CloudFormation templates that provision networking resources, security, and storage components. The next tab shows how HPC resources are deployed using the AWS ParallelCluster CloudFormation stack.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-high-performance-computing-clusters-on-aws.pdf)Step 1Admins/DevOps users can deploy this architecture using a series of AWS CloudFormation templates. These templates provision networking resources, including Amazon Virtual Private Cloud (Amazon VPC) and subnets. The templates also provision resources for security and storage, such as Amazon Simple Storage Service (Amazon S3), Amazon Elastic File System (Amazon EFS), and Amazon FSx for Lustre. There are optional templates included to deploy a Slurm accounting database (DB) and a Microsoft Active Directory user directory.Step 2Four logical subnets (zones) are created, each in multiple Availability Zones (AZs), based on the target AWS Region. All required networking, networking access control list (ACLs), routes, and security resources are deployed. The four zones are: 1) Access Zone (public subnet), 2) Compute Zone, 3) Management Zone, and 4) Storage Zone (all private subnets).Step 3An Amazon RDS for MySQL instance is created that will be used as the Slurm Accounting Database. This is set up in a single zone, or can be modified to be multi-AZ if preferred. One AWS Directory Service user directory is created across two AZs.Step 4An Amazon EFS file system is created for shared cluster storage that is mounted in all of the deployed subnets for the Storage Zone. An FSx for Lustre file system is created that is used as a highly performant scratch file system in the preferred AZ.Step 5Two Amazon S3 buckets are created: one for campaign storage using Amazon S3 Intelligent-Tiering, and one for archival storage using Amazon S3 Glacier.Step 6Random passwords are generated for both the Slurm accounting database and the Directory Service that are stored securely in AWS Secrets Manager.### HPC cluster deployment

This architecture diagram shows how HPC resources are deployed using the AWS ParallelCluster CloudFormation stack. It references the network, storage, security, database, and user directory components from the previous tab.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deploying-high-performance-computing-clusters-on-aws.pdf)Step 1Admins/DevOps users use the AWS ParallelCluster AWS CloudFormation stack to deploy HPC resources. Resources can reference the network, storage, security, database, and user directory from the previously launched CloudFormation stacks.Step 2The AWS ParallelCluster CloudFormation template provisions a sample cluster configuration, which includes a head node deployed in a single Availability Zone within the Management zone. It also provisions a login node deployed in a single Availability Zone within the Access zone.Step 3The Slurm workload manager is deployed on the head node and used for managing the HPC workflow processes.Step 4The sample cluster configuration included creates two Slurm queues that provision compute nodes within the Compute zone. One queue uses compute-optimized Amazon Elastic Compute Cloud (Amazon EC2) instances, while the other queue utilizes GPU-accelerated Amazon EC2 instances.Step 5Users access this Guidance by establishing a connection to the deployed login node within the Access zone, utilizing either a NICE DCV, SSH, or an AWS Systems Manager Session Manager.Step 6Users authenticate to the log in node using a username and password stored in the AWS Managed Microsoft Active Directory.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-deploying-high-performance-computing-clusters-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

CloudFormation and AWS ParallelCluster support IaC practices for consistent, repeatable HPC deployments. Amazon CloudWatch provides monitoring and observability to assess cluster performance and health. Collectively, these services automate HPC deployments, supporting compliance and security and facilitating secure infrastructure management. This approach aligns with NIST SP 800-223 recommendations so you can implement best practices when managing complex HPC workloads on AWS. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

Amazon VPC enables network isolation and segmentation of HPC environments into distinct security zones (access, management, compute, and storage), aligning with NIST SP 800-223 recommendations. In addition, AWS services such as AWS Identity and Access Management (IAM), AWS Key Management Service (AWS KMS), and AWS CloudTrail directly address key security requirements. Specifically, IAM provides fine-grained access control implementing least privilege, AWS KMS offers data encryption at rest and in transit, and CloudTrail offers comprehensive API auditing. This multi-layered approach enables a zone-based security architecture with proper access controls, data protection, and comprehensive monitoring. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS ParallelCluster provides a framework for deploying and operating HPC clusters for consistent setup. Amazon EFS and FSx for Lustre offer optimized file systems for HPC workloads, while Amazon S3 stores campaign data and archives. Amazon Relational Database Service (Amazon RDS) manages the Slurm accounting database with automated backups, and AWS Auto Scaling adjusts capacity to maintain performance cost-effectively. These services address reliability concerns outlined in NIST SP 800-223 by providing robust data storage, supporting critical component availability, and enabling automatic scaling. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Amazon EC2 offers instance types optimized for various HPC workloads, including GPU-enabled instances for accelerated computing. FSx for Lustre provides a high performance file system designed for HPC, while AWS ParallelCluster automates HPC environment creation for efficient deployment and scaling. These services deliver the computational power, storage performance, and job scheduling capabilities essential for HPC workloads, allowing users to achieve optimal performance without managing complex infrastructure. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS ParallelCluster optimizes costs in HPC environments by automatically scaling compute resources based on workload demand and also by supporting Amazon EC2 Spot Instances for interruptible tasks. This dynamic adjustment can reduce costs by up to 90% compared to Amazon EC2 On-Demand Instances. Additionally, Amazon S3 Intelligent-Tiering automatically moves data to the most cost-effective access tier, optimizing storage costs for large HPC datasets. These services address the significant computational resource requirements of HPC systems by efficiently managing capacity and storage. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Amazon EC2 Auto Scaling and AWS ParallelCluster support sustainability in HPC environments by dynamically adjusting compute resources to match workload demands, minimizing idle resources. AWS Batch optimizes resource allocation for batch workloads, while Amazon S3 Intelligent-Tiering automatically moves data to appropriate storage tiers, reducing energy consumption for infrequently accessed data. Although NIST SP 800-223 does not explicitly focus on sustainability, these services align with its emphasis on efficient resource utilization. By using energy-efficient processors, matching resources to demand, and automating data management, these services minimize waste from overprovisioning—a common issue in traditional HPC environments. This approach not only reduces the environmental impact of HPC operations but also often leads to cost savings, demonstrating that sustainability and cost optimization can be complementary goals in cloud-based HPC. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
