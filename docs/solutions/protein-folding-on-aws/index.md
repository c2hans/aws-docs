---
source_url: https://docs.aws.amazon.com/solutions/protein-folding-on-aws/index.html
---

---
title: 'Guidance for Protein Folding on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/protein-folding-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Protein Folding on AWS

## Overview

This Guidance helps researchers run a diverse catalog of protein folding and design algorithms on AWS Batch. Knowing the physical structure of proteins is an important part of the drug discovery process. Machine learning (ML) algorithms significantly reduce the cost and time needed to generate usable protein structures. These systems have also inspired development of artificial intelligence (AI)-driven algorithms for de novo protein design and protein-ligand interaction analysis. This Guidance will allow researchers to quickly add support for new protein analysis algorithms while optimizing cost and maintaining performance.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/protein-folding-on-aws.pdf)

![Architecture diagram](/images/solutions/protein-folding-on-aws/images/protein-folding-on-aws-1.png)

1. **Step 1**: AWS CloudFormation deploys the infrastructure in your AWS account.
1. **Step 2**: AWS CodeBuild builds the containers necessary to run analysis algorithms, such as AlphaFold and OpenFold. All of the analysis algorithms are packaged as Docker containers and stored using Amazon Elastic Container Registry (Amazon ECR) in the deployment account. This helps ensure that all usage information remains private.
1. **Step 3**: AWS Lambda triggers the download of model artifacts and reference data to an Amazon FSx for Lustre file system.
1. **Step 4**: Define and submit analysis jobs from an Amazon SageMaker notebook instance or other Python environment.
1. **Step 5**: AWS Batch manages job scheduling and orchestration.
1. **Step 6**: Jobs run in general or accelerated compute environments based on the vCPU, memory, and GPU requirements.
1. **Step 7**: Jobs write outputs and results to an encrypted Amazon Simple Storage Service (Amazon S3) bucket.
1. **Step 8**: Users download job outputs to visualize the results or for downstream analysis.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/aws-batch-arch-for-protein-folding)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

Customers deploy architecture components using CloudFormation. Solution changes are tested and deployed using GitLab pipelines. Customers can submit jobs and process the results through a Python software development kit (SDK), including jobs from Jupyter notebooks. Jobs write all results and metrics to Amazon S3. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

All analysis jobs run within private subnets and use minimal AWS Identity and Access Management (IAM) policies to manage access to AWS services. All data is encrypted at rest and in transit. Amazon S3 data transfer occurs through a VPC endpoint. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Analysis algorithms are split into independent containers and Python classes for modular execution and updates. AWS Batch automatically provides job retry logic. Job inputs and outputs are stored in Amazon S3. Additionally, the CloudFormation template provisions an attached data repository for the FSx file system to rapidly restore reference data. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

Protein folding algorithms require large sequence databases for data preparation and can take several minutes or hours to finish. AWS Batch supports FSx for Lustre mounts and extended run times. Both AWS Batch and Amazon FSx for Lustre support HPC use cases, such as protein folding with high input/output (IO) requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

AWS Batch will automatically de-provision compute resources when jobs are finished. Customers can leverage Amazon Elastic Compute Cloud (Amazon EC2) Spot instances (which offer up to a 90% discount compared to On-Demand instances) and AWS Graviton-enabled instance types for some jobs. AWS Graviton instances are optimized for cloud workloads and can deliver up to 40% better price performance over comparable current generation x86-based instances. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

AWS Batch automatically scales compute resources to handle jobs in a managed queue. This architecture includes benchmarking results and default parameters to minimize hardware resources. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Metagenomi accelerates the search for cures to genetic diseases using AWS**: Predicting protein structures at scale using AWS BatchThis post demonstrates how to provision and use AWS Batch and other services to run AI-driven protein folding algorithms like RoseTTAFold.

[Metagenomi accelerates the search for cures to genetic diseases using AWS](https://www.youtube.com/watch?v=NS9P8Cuct8M)

[Read usage guidelines](/solutions/guidance-disclaimers/)
