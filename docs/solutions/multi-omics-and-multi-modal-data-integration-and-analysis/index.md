---
source_url: https://docs.aws.amazon.com/solutions/multi-omics-and-multi-modal-data-integration-and-analysis/index.html
---

---
title: 'Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/multi-omics-and-multi-modal-data-integration-and-analysis/
source: aws-documentation
generated_on: 2026-10-08
---

# Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS

## Overview

This Guidance helps users prepare genomic, clinical, mutation, expression, and imaging data for large-scale analysis and perform interactive queries against a data lake. It includes infrastructure as code (IaC) automation, continuous integration and continuous delivery (CI/CD) for rapid iteration, an ingestion pipeline to store and transform the data, and notebooks and dashboards for interactive analysis. We also demonstrate how genomics variant and annotation data is stored and queried using AWS HealthOmics, Amazon Athena, and Amazon SageMaker notebooks. This Guidance was built in collaboration with [Bioteam](#Contributors) .

## How it works

### Architecture

Prepare genomic, clinical, mutation, expression and imaging data for large-scale analysis and query against a data lake.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.pdf?target=_blank)Step 1Ingest, format, and catalog data from The Cancer Genome Archive (TCGA). The raw data is pulled from the Registry of Open Data on AWS (RODA) through the TCGA API. The data is transformed in an AWS Glue extract, transform, and load (ETL) job and cataloged by an AWS Glue Crawler. This makes the data available for query in Athena.Step 2Data from The Cancer Imaging Atlas (TCIA) is ingested, formatted, and catalogued. The raw data is pulled from RODA through the TCIA API. The data is transformed in an AWS Glue ETL job and cataloged by an AWS Glue Crawler. Image locations can be queried and displayed using SageMaker Notebooks.Step 3VCF data from the One Thousand Genomes project, a sample VCF, and ClinVar Annotation VCF is ingested into Amazon Omics Variant and Annotation Stores and made available as tables in Lake Formation.Step 4Research scientists analyze the multi-modal data through a visual interface in QuickSight. The data is cached in a SPICE (Super-fast, Parallel, In-memory Calculation Engine) database, optimizing query performance.Step 5Data Scientists analyze the data with code using Jupyter notebooks provided through SageMaker Notebook environments.### CI/CD

Prepare genomic, clinical, mutation, expression and imaging data for large-scale analysis and query against a data lake.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/multi-omics-and-multi-modal-data-integration-and-analysis-on-aws.pdf#page=2?target=_blank)Step 1Create an AWS CodeBuild project containing the setup.sh script. This script creates the remaining AWS CloudFormation stacks, code repositories, and code.Step 2The landing zone (zone) stack creates the AWS CodeCommit pipe repository. After the landing zone (zone) stack completes its setup, the setup.sh script pushes source code to the CodeCommit pipe repository.Step 3The deployment pipeline (pipe) stack creates the CodeCommit code repository, an Amazon CloudWatch event, and the AWS CodePipeline code pipeline. After the deployment pipeline (pipe) stack completes its setup, the setup.sh script pushes source code to the CodeCommit code repository.Step 4The CodePipeline (code) pipeline deploys the codebase (genomics, imaging and omics) CloudFormation stacks. After the CodePipeline pipelines complete their setup, the resources deployed in your account include Amazon Simple Storage Service (Amazon S3) buckets for storing object access logs, build artifacts, and data in your data lake; CodeCommit repositories for source code; a CodeBuild project for building code artifacts; a CodePipeline pipeline for automating builds and deployment of resources; example AWS Glue jobs, crawlers, and a data catalog; and an Amazon SageMaker Jupyter notebook instance. An Amazon Omics Reference Store, Variant Store, and Annotation Store is provisioned, and a sample variant call file (VCF), a subset 1000 genomes VCF, and ClinVar Annotation VCF is ingested for analysis. Using AWS Lake Formation, a Data lake Admin can enable access of data in Omics Variant and Annotation Stores using Amazon Athena and SageMaker. An Amazon Omics Reference Store, Variant Store, and Annotation Store is provisioned to store publicly available variant and annotation data and make it available for query and analysis.Step 5The imaging stack creates a hyperlink to a CloudFormation quick start, which can be launched to deploy the Amazon QuickSight stack. The QuickSight stack creates Identity and Access Management (IAM) and QuickSight resources necessary to interactively explore the multi-omics dataset.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: This repository creates a scalable environment in AWS to prepare genomic, clinical, mutation, expression and imaging data for large-scale analysis and perform interactive queries against a data lake. The solution demonstrates how to 1) use HealthOmics Variant Store & Annotation Store to store genomic variant data and annotation data, 2) provision serverless data ingestion pipelines for multi-modal data preparation and cataloging, 3) visualize and explore clinical data through an interactive interface, and 4) run interactive analytic queries against a multi-modal data lake using Amazon Athena and Amazon SageMaker. A detailed guide is provided to experiment and use within your AWS account. Each stage of building the Guidance, including deployment, usage, and cleanup, is examined to prepare it for deployment. The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open the implementation guide](/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/welcome.html)
[Deploy sample code in the AWS Console](https://console.aws.amazon.com/cloudformation/home#/stacks/new?&templateURL=https://s3.amazonaws.com/solutions-reference/genomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena/latest/genomics-tertiary-analysis-and-data-lakes-using-aws-glue-and-amazon-athena.template)
[Open sample code on GitHub](https://github.com/awslabs/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance uses CodeBuild and CodePipeline to build, package and deploy everything needed in the solution to ingest and store Variant Call Files (VCFs) and work with multi-modal and multi-omic data from the datasets in The Cancer Genome Atlas (TCGA) and The Cancer Imaging Atlas (TCIA). Serverless genomics data ingestion and analysis is demonstrated using a fully managed service - Amazon Omics. Code changes made in the solution CodeCommit repository with be deployed through the provided CodePipeline deployment pipeline. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

This Guidance uses role based access with IAM and all buckets have encryption enabled, are private, and block public access. The data catalog in AWS Glue has encryption enabled and all meta data written by AWS Glue to Amazon S3 is encrypted. All roles are defined with least privileges and all communications between services stay within the customer account. Administrators can control Jupyter notebook, Amazon Omics Variant Stores’ data and AWS Glue Catalog data access is fully managed using Lake Formation, and Athena, SageMaker Notebook and QuickSight data access is managed through provided IAM roles. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

AWS Glue, Amazon S3, Amazon Omics, and Athena are all serverless and will scale data access performance as your data volume increases. AWS Glue provisions, configures, and scales the resources required to run your data integration jobs. Athena is serverless, so you can quickly query your data without having to set up and manage any servers or data warehouses. The QuickSight SPICE in-memory storage will scale your data exploration to thousands of users. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

By using serverless technologies, you only provision the exact resources you use. Each AWS Glue job will provision a Spark cluster on demand to transform data and de-provision the resources when done. If you choose to add new TCGA datasets, you can add new AWS Glue jobs and AWS Glue crawlers that will also prevision resources on-demand. Athena automatically executes queries in parallel, so most results come back within seconds. Amazon Omics optimizes variant query performance at scale by transforming files into Apache Parquet. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

By using serverless technologies that scale on demand, you pay only for the resources you use. To further optimize cost, you can stop the notebook environments in SageMaker when they are not in use. The QuickSight dashboard is also deployed through a separate CloudFormation template, so if you don’t intend to use the visualization dashboard, you can choose to not deploy it to save costs. Amazon Omics optimizes variant data storage cost at scale. Query costs are determined by the amount of data scanned by Athena and can be optimized by writing queries accordingly. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By extensively using managed services and dynamic scaling, you minimize the environmental impact of the backend services. A critical component for sustainability is to maximize the usage of notebook server instances. You should stop the notebook environments when not in use. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Multi-Modal Data Analysis with Health AI and ML Services on AWS**: This Guidance demonstrates how to set up an end-to-end framework to analyze multimodal healthcare and life sciences (HCLS) data.

[Learn More](https://aws.amazon.com/solutions/guidance/multi-modal-data-analysis-with-health-ai-and-ml-services-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
