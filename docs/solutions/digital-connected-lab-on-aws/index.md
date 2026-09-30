---
source_url: https://docs.aws.amazon.com/solutions/digital-connected-lab-on-aws/index.html
---

---
title: 'Guidance for Digital Connected Lab on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/digital-connected-lab-on-aws/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Digital Connected Lab on AWS

## Overview

This Guidance helps you to connect life sciences data instruments and laboratory system files to the AWS Cloud, either through the internet or a direct connection with low latency. You can cut down on storage expenses for data that gets accessed less often or make it accessible for high-performance computing for genomics, imaging, and other intense workloads, all on AWS.

## How it works

This architecture diagram helps you learn how to connect file-based life sciences instruments and laboratory systems to the cloud and provide scalable data access and computing using Amazon Web Services (AWS).

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/digital-connected-lab-on-aws.pdf)

![Architecture diagram](/images/solutions/digital-connected-lab-on-aws/images/digital-connected-lab-on-aws-1.png)

1. **Step 1**: A lab technician runs an experiment or test, and results are written to a folder on an on-premises file server. An AWS DataSync task is set up to sync the data from local storage to a bucket in Amazon Simple Storage Service (Amazon S3).
1. **Step 2**: Data is transferred to the AWS Cloud either through the internet, or through a low-latency direct connection that avoids the internet, such as AWS Direct Connect.
1. **Step 3**: Electronic lab notebooks (ELN) and lab information management systems (LIMS) share experiment and test metadata bidirectionally with the AWS Cloud through events and APIs. Learn more about this integration in Guidance for a Laboratory Data Mesh on AWS.
1. **Step 4**: Partnering entities, like a contract research organization (CRO), can upload study results to Amazon S3 by using AWS Transfer Family for FTP, SFTP, or FTPS.
1. **Step 5**: You can optimize storage costs by writing instruments data to an S3 bucket configured for infrequent access. Identify your S3 storage access patterns to optimally configure your S3 bucket lifecycle policy and transfer data to Amazon S3 Glacier.
1. **Step 6**: Using Amazon FSx for Lustre, data is made accessible to high performance computing (HPC) on the Cloud for genomics, imaging, and other intensive workloads to provide a low millisecond-latency shared file system.
1. **Step 7**: Bioinformatics pipelines are orchestrated with AWS Step Functions, AWS HealthOmics, and AWS Batch for flexible CPU and GPU computing.
1. **Step 8**: Machine learning is conducted with an artificial intelligence and machine learning (AI/ML) toolkit that uses Amazon SageMaker for feature engineering, data labeling, model training, deployment and ML operations. Amazon Athena is used for flexible SQL queries.
1. **Step 9**: For researchers using on-premises applications for data analysis and reporting, they view and access data in Amazon S3 by using Network File System (NFS) or Server Message Block (SMB) through Amazon S3 File Gateway.
## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

As new data sources and partners arise, a variety of data transfer services can be used to adapt to these changing access patterns. For multi-site environments, S3 File Gateway can be used to transfer while you retain an on-site cache for other applications. Transfer Family lets partnering entities like CROs easily upload study results. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with AWS Identity and Access Management (IAM), so that each user is given only the permissions necessary to fulfill their job duties. We also suggest that you use at-rest encryption, and the services use in-flight encryption by default. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

DataSync leverages single or multiple VPC endpoints to ensure that if an Availability Zone is unavailable, the agent can reach another endpoint. DataSync is a scalable service that leverages sets of agents to move data. The tasks and agents can be scaled based on the demand of the amount of data that needs to be migrated. DataSync logs all events to Amazon CloudWatch. If a job fails, actions can be taken to better understand the issue and where the task is failing. Once the tasks are complete, post-processing jobs can be initiated to complete the next phase of the pipeline process. Amazon S3 provides a highly durable storage infrastructure designed for mission-critical and primary data storage. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

FSx for Lustre storage provides sub-millisecond latencies, up to hundreds of GBs/s of throughput, and millions of IOPS. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies that scale on-demand, you only pay for the resources you use. To further optimize cost, you can stop the notebook environments in SageMaker when they are not in use. If you don’t intend to use the Amazon QuickSight visualization dashboard, you can choose to not deploy it to save costs. Data Transfer charges are comprised of two main areas: DataSync, which is charged on a per GB transferred rate; and Direct Connect or VPN data transferred. Additionally, cross-Availability Zone charges might apply if VPC endpoints are used. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

CloudWatch metrics allow users to make data-driven decisions based on alerts and trends. By extensively using managed services and dynamic scaling, you minimize the environmental impact of the backend services. Most components are self-sustaining. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Building Digitally Connected Labs with AWS**: This post discusses the tools, best practices, and partners helping Life Sciences labs take full advantage of the scale and performance of AWS Cloud.

[Learn more](https://aws.amazon.com/blogs/industries/building-digitally-connected-labs-with-aws/)

- **Guidance for a Laboratory Data Mesh on AWS**: This Guidance demonstrates how to build a scientific data management system that integrates both laboratory instrument data and software with cloud data governance, data discovery, and bioinformatics pipelines, capturing key metadata events along the way.

[Learn more](https://aws.amazon.com/solutions/guidance/laboratory-data-mesh-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
