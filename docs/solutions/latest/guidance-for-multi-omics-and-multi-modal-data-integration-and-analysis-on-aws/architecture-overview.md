---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

 The following diagram describes the overall data lake architecture; how data is ingested, curated, cataloged, and queried.

![Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS data lake architecture](http://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/images/multi-omics-data-lake-diagram.png)

 This guidance demonstrates how to ingest common multi-omics data sets into a centralized data lake and work with that data using Amazon Athena and Jupyter notebooks. There are example ingestion pipelines for clinical, mutation, gene expression, and copy number data (TCGA), and imaging metadata (TCIA). An Amazon Omics Reference Store, Variant Store and Annotation Store are also created for genomic variant calls data (1000 Genomes), annotation data (ClinVar) and an example individual Variant Call File (VCF) data.

## The Cancer Genome Atlas (TCGA) dataset
<a name="arch-cancer-genome-atlas-dataset"></a>

 A set of data from two specific projects (Lung Adenocarcinoma, LUAD and Lung Squamous Cell Carcinoma, LUSC) is retrieved from The Cancer Genome Atlas (TCGA) during setup. The dataset, originally in raw formats direct from TCGA, is parsed and stored in Apache Parquet format and partitioned by project ID. The `tcga-clin`, `tcga-cnv`, `tcga-exp`, and `tcga-mut` crawlers are provided to crawl the datasets, infer the data schemas, and add tables to the guidance AWS Glue data catalog.

 Imaging metadata from the same two projects (TCGA-LUAD and TCGA-LUSC) is retrieved from The Cancer Imaging Archive (TCIA) during deployment. The dataset is parsed and stored in Apache Parquet format and partitioned by project ID. The `tcga-img` crawler is provided to crawl the dataset, infer the data schemas, and add tables to the guidance AWS Glue data catalog.

 A summary table stores counts of the number of TCGA and TCIA data records available for each patient in the dataset. This summary table is computed via an AWS Glue job, which invokes an Amazon Athena query, saving the results in Apache Parquet format. The `tcga-sum` crawler is provided to crawl the dataset, infer the data schemas, and add tables to the guidance AWS Glue data catalog.

## Genomics datasets – 1000 Genomes Project and ClinVar
<a name="arch-genomic-datasets-1000-genomes-project-and-clinvar"></a>

 A portion of the 1000 Genomes Project dataset (Chromosome 22) is copied into the data lake bucket during setup. An automated step is initiated to ingest this Variant Call File (VCF) into the pre-created Amazon Omics Variant store.

 A ClinVar VCF is copied into the data lake bucket during deployment. An automated step is initiated to ingest this VCF into the pre-created Amazon Omics Annotation store.

 An example VCF is copied into the data lake bucket during setup. An automated step is initiated to ingest this VCF into the pre-created Amazon Omics Variant store.

The creation of Amazon Omics Variant and Annotation stores automatically shares these stores as [AWS Lake Formation](https://aws.amazon.com/lake-formation/) tables. With a few steps run by a Data lake Administrator, this data is made available in the AWS Glue data catalog for query using Athena.

 Deploying this guidance with the default parameters builds the following environment in the AWS Cloud.

![AWS Cloud environment built after deploying this guidance with default parameters](http://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/images/multi-omics-diagram.png)

 The AWS CloudFormation template creates six CloudFormation stacks in your AWS account including a `setup` stack to install the guidance. The other stacks include a landing zone (`zone`) stack containing the common resources and artifacts, a deployment pipeline (`pipe`) stack defining the guidance's CI/CD pipeline, and three codebase (`genomics`, `imaging`, and `omics`) stacks providing the ETL scripts, jobs, crawlers, Omics resources, a data catalog, and notebook resources. The installation also includes a seventh CloudFormation stack that can be launched via a quick start link to set up the QuickSight resources (`quicksight`).

1.  The setup stack creates an [AWS CodeBuild](https://aws.amazon.com/codebuild/) project containing the setup.sh script. This script creates the remaining CloudFormation stacks and provides the source code for both the AWS CodeCommit pipe repository and the code repository.

1.  The landing zone (zone) stack creates the CodeCommit pipe repository. After the landing zone (zone) stack completes its setup, the setup.sh script pushes source code to the CodeCommit pipe repository.

1.  The deployment pipeline (pipe) stack creates the CodeCommit code repository, an [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) event, and the CodePipeline code pipeline. After the deployment pipeline (pipe) stack completes its setup, the setup.sh script pushes source code to the CodeCommit code repository.

1.  The CodePipeline (code) pipeline deploys the codebase (genomics, imaging, and omics) CloudFormation stacks. After the AWS CodePipeline pipelines complete their setup, the resources deployed in your account include [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets for storing object access logs, build artifacts, and data in your data lake; CodeCommit repositories for source code; an AWS CodeBuild project for building code artifacts (for example, third-party libraries used for data processing); an AWS CodePipeline pipeline for automating builds and deployment of resources; example AWS Glue jobs, crawlers, and a data catalog; and an Amazon SageMaker AI Jupyter notebook instance. An Amazon Omics Reference Store, Variant Store and Annotation store is provisioned and an example VCF, 1000 Genomes subset VCF and ClinVar annotation VCF are loaded into the solution for analysis using Amazon Athena.

1.  The imaging stack creates a hyperlink to a CloudFormation quick start, which can be launched to deploy the QuickSight (quicksight) stack. The QuickSight stack creates IAM and QuickSight resources necessary to interactively explore the multi-omics dataset.

 The example code includes the resources needed to prepare data for large-scale analysis and perform interactive queries against a multi-omics data lake.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
