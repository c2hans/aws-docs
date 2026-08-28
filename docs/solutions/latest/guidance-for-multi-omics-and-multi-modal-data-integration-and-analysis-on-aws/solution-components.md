---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/solution-components.html
---

# Components
<a name="solution-components"></a>

## CI/CD pipeline
<a name="cicd-pipeline"></a>

 A complete continuous integration and continuous deployment (CI/CD) pipeline is created when you launch the guidance. This pipeline is built using AWS CodeCommit as the source code, AWS CodeBuild projects to build the guidance’s artifacts (for example, hail.jar), and an AWS CodePipeline pipeline to run a build project and automate deployment (using AWS CloudFormation) after the updated source code is published.

 The AWS resources that compose the CI/CD pipeline are defined in the `Pipe/template_cfn.yml` file. Changes to the guidance requiring new artifacts to be built require an update to the CI/CD pipeline definition.

## Demonstration datasets
<a name="solution-demonstration-datasets"></a>

 This guidance copies the following datasets into your data lake bucket.
+  **The Cancer Genome Atlas, Lung Adenocarcinoma and Lung Squamous Cell Carcinoma (TCGA-LUAD and TCGA-LUSC)** – Two public cancer studies consisting of clinical, mutation, gene expression, and copy number data, partitioned by study ID and in Apache Parquet format. These studies are retrieved directly from The Cancer Genome Atlas (TCGA) APIs via a set of AWS Glue jobs. These datasets are used as the basis of cohort exploration and selection.
+  **The Cancer Imaging Archive, Lung Adenocarcinoma and Lung Squamous Cell Carcinoma (TCIA)** – Imaging metadata for subjects in the TCGA studies listed above, partitioned by study ID and in Apache Parquet format. This metadata is retrieved directly from The Cancer Imaging Archive (TCIA) APIs via an AWS Glue job. This dataset can be used to filter patients by availability of imaging data, as well as retrieve individual images for high-level exploration.
+  **1000 Genomes, Chromosome 22 (genome)** – A portion of the 1000 genomes public dataset of human genomic variant data in VCF format. This dataset is used as our cohort dataset for creating the drug response report.
+  **ClinVar (annotation)** – The public dataset that aggregates information about genomic variation and its relationship to human health. We use the VCF format to be used with Amazon Omics Variant Store.
+  **Individual Sample Variants (sample)** – An individual sample Variant Call File (VCF) dataset used to demonstrate queryability with Athena.

## AWS Glue jobs
<a name="aws-glue-jobs"></a>

 This guidance creates the following AWS Glue jobs:
+  **Clinical, Cnv, Expression, and Mutation** – Retrieves data from TCGA, filters and transforms it to Apache Parquet format, and writes the resulting files to the data lake. For each of the four data types, there are two jobs, one for each of the two source TCGA projects (LUAD and LUSC). For a total of 8 jobs.
+  **ImagingMetadata** – Retrieves imaging metadata from The Cancer Imaging Archive (TCIA), transforms them to Apache Parquet format, and writes the resulting files to the data lake. There is one job for each of the two source TCGA projects (LUAD and LUSC).
+  **TcgaSummary** – Invokes Amazon Athena to generate a new database table containing summary metrics over all of the TCGA and TCIA data tables, saving the results in Apache Parquet format within the data lake, and registering the table with the Glue data catalog.

## AWS Glue crawlers
<a name="aws-glue-crawlers"></a>

 This guidance creates the following AWS Glue crawlers:
+  **tcga-clin** – Creates/Updates the `clinical_patient` and other clinical tables in the AWS Glue data catalog to reflect the data schema of the TCGA clinical data in the data lake.
+  **tcga-cnv** - Creates/Updates the `tcga_cnv` table in the AWS Glue data catalog to reflect the data schema of the TCGA copy number data in the data lake.
+  **tcga-exp** – Creates/Updates the `expression_tcga_luad` and `expression_tcga_lusc` tables in the AWS Glue data catalog to reflect the data schema of the TCGA expression data in the data lake.
+  **tcga-mut** – Creates/Updates the `tcga_mutation` table in the AWS Glue data catalog to reflect the data schema of the TCGA mutation data in the data lake.
+  **tcga-img** – Creates/Updates the `tcia_patients` and `tcia_image_series` tables in the AWS Glue data catalog to reflect the data schema of the TCIA image metadata in the data lake.
+  **tcga-sum** – Creates/Updates the `tcga_summary` table in the AWS Glue data catalog to reflect the data schema of the TCGA summary data in the data lake.

## AWS Glue workflow
<a name="aws-glue-workflow"></a>

 This guidance creates an AWS Glue workflow which sequences and coordinates the AWS Glue jobs and crawlers as part of the TCGA and TCIA data sets. For each TCGA data type and for the TCIA data, two Glue jobs are invoked, followed by a trigger that signals the corresponding Glue crawler to run. Once all Glue crawlers are complete, the `TcgaSummary` job is invoked to create the summary table.

## AWS Glue data catalog
<a name="aws-glue-data-catalog"></a>

 This guidance creates an AWS Glue data catalog with a `genomicsanalysis` database that contains all the tables used by this guidance. AWS Glue is configured to encrypt the metadata stored in the data catalog, data files stored in Amazon S3 buckets, and all logs stored in Amazon CloudWatch.

## SageMaker AI notebook instance
<a name="sagemaker-notebook-instance"></a>

 This guidance creates an Amazon SageMaker AI notebook instance that demonstrates how to use AWS Glue and Amazon Athena to identify variants related to drug response.

## Amazon S3 buckets
<a name="amazon-s3-buckets"></a>

 This guidance creates the following Amazon S3 buckets. Each bucket has encryption and logging activated:
+  **Data Lake Bucket** – Stores genomic variant and ClinVar variant annotation data.
+  **Resources Bucket** – Stores notebooks and shell scripts.
+  **Build Bucket** – Stores build artifacts deployed through the pipeline.
+  **Logs Bucket –** Stores S3 access logs related to the three buckets listed above.

## QuickSight dataset
<a name="quicksight-dataset"></a>

 This solution creates an Quick dataset derived from the Amazon Athena `clinical_patient` and `tcga_summary` tables, joined by the patient ID field, and filtered for key columns. The dataset is shared with the guidance owner and available for creating interactive analyses on clinical data. Before using QuickSight to explore the data in this guidance, sign up for an Quick subscription. For details, refer to [Signing up for an Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html) in the *Quick User Guide*.

## Amazon Omics
<a name="amazon-omics"></a>

 This solution creates the following Amazon Omics resources:
+ **Reference Store ** – A data store for the storage of reference genomes in FASTA format.
+ **Variant Store ** – A data store that stores variant data at a population scale in VCF format.
+ **Annotation Store ** – A data store that stores annotation data in VCF, GFF3 and TSV/CSV formats downstream queryability.
+ In addition, the example datasets (1000 Genomes, example VCF and ClinVar VCF) are ingested into these stores as part of the solution setup.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
