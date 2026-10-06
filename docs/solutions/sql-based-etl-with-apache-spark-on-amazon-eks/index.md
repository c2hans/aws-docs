---
source_url: https://docs.aws.amazon.com/solutions/sql-based-etl-with-apache-spark-on-amazon-eks/index.html
---

---
title: 'Guidance for SQL-Based ETL with Apache Spark on Amazon EKS'
canonical_url: https://docs.aws.amazon.com/solutions/sql-based-etl-with-apache-spark-on-amazon-eks/
source: aws-documentation
generated_on: 2026-10-05
---

# Guidance for SQL-Based ETL with Apache Spark on Amazon EKS

Unlock efficient data workflows and faster insights with a scalable, enterprise-grade extract, transform, and load (ETL) solution

## Overview

This Guidance helps address the gap between data consumption requirements and low-level data processing activities performed by common ETL practices. For organizations operating on SQL-based data management systems, adapting to modern data engineering practices can slow down the progress of harnessing powerful insights from their data. This Guidance provides a quality-aware design for increasing data process productivity through the open-source data framework Arc for a user-centered ETL approach. The Guidance accelerates interaction with ETL practices, fostering simplicity and raising the level of abstraction for unifying ETL activities in both batch and streaming. We also offer options for an optimal design using efficient compute instances (such as AWS Graviton Processors) that allow you to optimize the performance and cost of running ETL jobs at scale on Amazon EKS.

## How it works

This architecture diagram accelerates data processing with Apache Spark on Amazon EKS.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/sql-based-etl-with-apache-spark-on-amazon-eks.pdf)

![Architecture diagram](/images/solutions/sql-based-etl-with-apache-spark-on-amazon-eks/images/sql-based-etl-with-apache-spark-on-amazon-eks-1.png)

1. **Step 1**: Interact with ETL development and orchestration tools through Amazon CloudFront endpoints with Application Load Balancer origins, which provide secure connections between clients and ETL tools' endpoints.
1. **Step 2**: Develop, test, and schedule ETL jobs that process batch and stream data. The data traffic between ETL processes and data stores flows through Amazon Virtual Private Cloud (Amazon VPC) endpoints powered by AWS PrivateLink without leaving the AWS network.
1. **Step 3**: JupyterHub Integrated Development Environment (IDE), Argo Workflows, and Apache Spark Operator run as containers on an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. JupyterHub IDE can integrate with a source code repository (such as GitHub) to track ETL assets changes made by users. The assets include Jupyter notebook files and SQL scripts to be run with the Arc ETL framework.
1. **Step 4**: Update ETL assets in the source code repository, then upload to an Amazon Simple Storage Service (Amazon S3) bucket. The synchronization process can be implemented by an automated continuous integration and continuous deployment (CI/CD) pipeline initiated by updates in the source code repository or performed manually.
1. **Step 5**: You can optionally change Docker build source code uploaded from a code repository to the S3 ETL asset bucket. It activates an AWS CodeBuild and AWS CodePipeline CI/CD pipeline to automatically rebuild and push the Arc ETL Framework container image to an Amazon Elastic Container Registry (Amazon ECR) private registry.
1. **Step 6**: Schedule ETL jobs through Argo Workflows to run on an Amazon EKS cluster. These jobs automatically pull the Arc container image from Amazon ECR, download ETL assets from the artifact S3 bucket, and send application logs to Amazon CloudWatch. VPC endpoints secure access to all AWS services.
1. **Step 7**: As an authenticated user, you can interactively develop and test notebooks as ETL jobs in JupyterHub IDE, which automatically retrieves log-in credentials from AWS Secrets Manager to validate sign-in user requests.
1. **Step 8**: Access the ETL output data stored in the S3 bucket that supports the transactional data lake format. You can query the Delta Lake tables through Amazon Athena integrated with AWS Glue Data Catalog.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open implementation guide](https://aws-solutions-library-samples.github.io/compute/sql-based-etl-with-apache-spark-on-eks.html)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Within the Amazon EKS clusters, Amazon Elastic Compute Cloud (Amazon EC2) instances (X86_64 CPU, Graviton ARM64) act as compute nodes, running Guidance workloads. Spark jobs are executed on elastically provisioned Amazon EC2 Spot instances based on workload demands. CodeBuild and CodePipeline automate the GitOps process, building container images from Git code updates and pushing them to the Amazon ECR private registry. Argo Workflows schedules ETL jobs on Amazon EKS, automatically pulling the Arc Docker image from Amazon ECR, downloading ETL assets from the artifact S3 bucket, and sending application logs to CloudWatch. This automated deployment and execution of Data ETL jobs minimizes operational overhead and improves productivity. Further, the CI/CD pipeline using CodeBuild and CodePipeline helps ensure continuous improvement and development while securely storing the Guidance's Arc Docker image in Amazon ECR. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

The Amazon EKS cluster resources are deployed within an Amazon VPC, providing logical networking isolation from the public internet. Amazon VPC supports security features like VPC endpoint (keeping traffic within the AWS network), security groups, network access control lists (ACLs), and AWS Identity and Access Management (IAM) roles and policies for controlling inbound and outbound traffic and authorization. Amazon ECR image registry offers container-level security features such as vulnerability scanning. Amazon ECR and Amazon EKS follow Open Container Initiative (OCI) registry and Kubernetes API standards, incorporating strict security protocols. IAM provides access control for Amazon S3 application data, while AWS Key Management Service (AWS KMS) encrypts data at rest on Amazon S3. IAM Roles for Service Accounts (IRSA) on Amazon EKS clusters enables fine-grained access control for pods, enforcing role-based access control and limiting unauthorized Amazon S3 data access. Secrets Manager securely stores and manages credentials. CloudFront provides SSL-encoded secure entry points for Jupyter and Argo Workflows web tools. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Amazon EKS enables highly available topologies by deploying the Kubernetes Control and Compute Planes across multiple Availability Zones (AZs). This helps ensures continuous availability for data applications—even if an AZ experiences an interruption—resulting in a reliable multi-AZ EC2 instance deployment on Amazon EKS. For data storage, Amazon S3 provides high durability and availability, automatically replicating data objects across multiple AZs within a Region. Additionally, Amazon ECR hosts Docker images in a highly available and scalable architecture, reliably supporting container-based application deployment and increments. Amazon S3, Amazon EKS, and Amazon ECR are fully managed services designed for high service level agreements (SLAs) with reduced operational costs. They enable deployment of business-critical applications to meet high availability requirements. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The Amazon EKS cluster's Amazon EC2 compute nodes can dynamically scale up and down based on application workload. Graviton-based EC2 instances provide increased performance efficiency through custom-designed Arm-based processors, optimized hardware, and architectural enhancements. A decoupled compute-storage pattern (with input and output data stored in Amazon S3) enhances dynamic compute scaling efficiency. Data Catalog streamlines metadata management, seamlessly integrating with Athena for simplified metadata management and enhanced query performance. Data Catalog automates crawling and maintaining technical metadata for efficient data processing and querying. Athena offers fast querying against Amazon S3 data without moving it, further enhancing analytics workflow efficiency. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Amazon ECR is a managed service for securing and supporting container applications with a fixed monthly fee for storing and serving container images. Amazon EKS cluster compute nodes can scale up and down based on Spark workloads, offering cost-efficient Graviton and Spot instance types. Data Catalog provides a serverless, fully managed metadata repository, eliminating the need to set up and maintain a long-running metadata database and reducing operational overhead and costs. CodeBuild and CodePipeline automate the build and deploy of the Arc ETL Framework's Docker image in a serverless environment, eliminating the need for provisioning and managing build servers in addition to reducing infrastructure maintenance costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

This Guidance runs an Amazon EKS cluster with efficient compute types based on Graviton processors. Amazon ECR eliminates the need for custom hardware or physical server management. Data Catalog and Athena are serverless services, further reducing energy and environmental impact. Optimizing the Amazon EKS compute layer for large-scale Apache Spark workloads minimizes the environmental impact of analytics workloads. You have the flexibility to choose Arm-based processors based on performance needs and your sustainability priorities. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)
