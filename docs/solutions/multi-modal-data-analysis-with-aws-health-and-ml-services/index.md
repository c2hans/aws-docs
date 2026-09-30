---
source_url: https://docs.aws.amazon.com/solutions/multi-modal-data-analysis-with-aws-health-and-ml-services/index.html
---

---
title: 'Guidance for Multi-Modal Data Analysis with AWS Health and ML Services'
canonical_url: https://docs.aws.amazon.com/solutions/multi-modal-data-analysis-with-aws-health-and-ml-services/
source: aws-documentation
generated_on: 2026-09-30
---

# Guidance for Multi-Modal Data Analysis with AWS Health and ML Services

## Overview

This Guidance demonstrates how to set up an end-to-end framework to analyze multimodal healthcare and life sciences (HCLS) data. It analyzes this data using purpose-built health care and life sciences services (such as AWS HealthOmics, AWS HealthLake, AWS HealthImaging) and machine learning (ML) and analytics services (such as Amazon SageMaker, Amazon Athena, and Amazon QuickSight). It ingests raw HCLS data formats like variant call format (VCF), Fast Healthcare Interoperability Resources (FHIR), and Digital Imaging and Communications in Medicine (DICOM), and provides a zero-extract, transform, load (ETL) architecture to customers who want to run their data analysis at scale on AWS. The architectures shows how to store, transform, and analyze linked genomic, clinical, and medical imaging data of patients. The effectiveness of the Guidance is demonstrated on a coherent synthetic patient dataset with multiple disease scenarios, released by MITRE and available on [AWS Registry of Open Data](https://registry.opendata.aws/synthea-coherent-data/) . It then trains an ML model for predicting patient outcomes. It also includes an interactive dashboard for visualizing summary statistics of data and ML model reports that can be customized based on the user persona.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/multi-modal-data-analysis-with-aws-health-and-ml-services.pdf)

![Architecture diagram](/images/solutions/multi-modal-data-analysis-with-aws-health-and-ml-services/images/multi-modal-data-analysis-with-aws-health-and-ml-services-1.png)

1. **Step 1**: Ingest genomic data from Amazon Simple Storage Service (Amazon S3) or Registry of Open Data on AWS (RODA) to AWS HealthOmics. Use HealthOmics Reference store for reference genome data, such as FastAll (FASTA), and HealthOmics Sequence store for sequence data, such as FASTQ, Binary Alignment Map (BAM), and Compressed Reference-oriented Alignment Map (CRAM). Use HealthOmics Variant store for VCF files and HealthOmics Annotation store for annotation files. To run private or Ready2Run workflows, use HealthOmics Workflows.
1. **Step 2**: Ingest FHIR data to AWS HealthLake.
1. **Step 3**: Ingest DICOM images to AWS HealthImaging and read into insight toolkit (ITK) image object in-memory through API calls.
1. **Step 4**: View tables from HealthOmics and HealthLake as resources in AWS Lake Formation.
1. **Step 5**: Query the tables with Amazon Athena.
1. **Step 6**: Generate brain masking with the Medical Open Network for AI (MONAI) segmentation model. Use Amazon SageMaker Preprocessing to parallelize radiomic feature computation for each image representation.
1. **Step 7**: Build visualization dashboards with Amazon QuickSight.
1. **Step 8**: Store the multimodal feature set in Amazon SageMaker Feature Store.
1. **Step 9**: Build and train ML models on multimodal features with SageMaker AutoGluon-Tabular.
1. **Step 10**: Deploy the model as an endpoint for real-time inference.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-multi-modal-data-analysis-with-aws-health-and-ml-services)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

HealthOmics integrates with Amazon EventBridge and provides notifications for actions like Variant or Annotation store creation and delete in addition to start and completion of data import jobs. You can overlay rules and handling targets onto this Guidance to monitor and respond to any incidents that may occur, such as repeated import failures. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

HealthImaging enforces the use of AWS Key Management Service (AWS KMS) encryption as it will not allow the creation of an unencrypted datastore. In addition to this, encryption at rest and transit are supported by HealthOmics, HealthLake, Amazon SageMaker, Athena, QuickSight, Lake Formation, and Amazon S3. This Guidance uses AWS-owned keys, but customers are able to bring their own keys if needed. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

When deploying this Guidance in an environment with pre-existing HealthOmics resources, you should be aware of HealthOmics Analytics quotas. This Guidance creates 1 Variant store and 1 Annotation store. By default, HealthOmics has a limit of 10 Variant stores and 10 Annotation stores. There are also default limits on the number of import jobs to HealthOmics Analytics stores and the file sizes they can handle. The default limit is 5 concurrent Variant or Annotation store import jobs. This Guidance uses 1 Variant import job and 1 Annotation import job. Variant import jobs have a default limit of 1,000 sources, each with a limit of 20 GB. The example variant data used by this Guidance consists of about 800 Variant files, each about 1 GB. Annotation import jobs have a default limit of 1 source, each with a limit of 20 GB in size. The example annotation data in this Guidance is a single file that is about 10 GB. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The data in HealthLake is automatically available through Lake Formation. This allows customers to create organizational units (OUs) of users and then grant row and column-level access to those users depending on their data access requirements. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

HealthLake automatically transforms the clinical data stored in your data catalog to run SQL queries on the data. This eliminates the need for exporting data and paying for data transfer costs for HealthLake data. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

By establishing a centralized data lake for all modalities, this Guidance removes the need to create redundant data. Data stores provided by HealthLake, HealthOmics, and HealthImaging become the single source of truth for each of their respective data types. Lake Formation can govern and filter each data type to provide users with the appropriate access to data without duplication. Similarly, you can create common database constructs, such as “views” in Athena to support multiple analysis use cases without data replication. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS**: This Guidance helps users prepare genomic, clinical, mutation, expression, and imaging data for large-scale analysis and perform interactive queries against a data lake.

[Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS](https://aws.amazon.com/solutions/guidance/multi-modal-data-analysis-with-health-ai-and-ml-services-on-aws/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
