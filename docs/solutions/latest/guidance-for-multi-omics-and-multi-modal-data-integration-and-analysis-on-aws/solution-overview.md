---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/solution-overview.html
---

# Prepare genomic, clinical, mutation, expression, and imaging data for large-scale analysis and perform interactive queries against a data lake
<a name="solution-overview"></a>

Publication date: *July 2020 ([last update](revisions.md): January 2023)*

 This guidance creates a scalable environment in AWS to prepare genomic, clinical, mutation, expression and imaging data for large-scale analysis and perform interactive queries against a data lake. This guidance demonstrates how to:

1. Provision [Amazon Omics](https://aws.amazon.com/omics/) resources to ingest, store and query genomics data.

1. Provision serverless data ingestion pipelines for multi-modal data preparation and cataloging.

1. Visualize and explore clinical data through an interactive interface.

1. Run interactive analytic queries against a multi-modal data lake using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/APIReference/Welcome.html) and an [Amazon SageMaker AI notebook instance](https://aws.amazon.com/sagemaker/notebooks/?sc_icampaign=pac_sagemaker-studio-notebooks&sc_ichannel=ha&sc_icontent=awssm-12090_pac&sc_iplace=2up&trk=2d328222-41dd-4782-8641-e5572b05846a%7Eha_awssm-12090_pac).

## 1. Provision Amazon Omics resources to ingest, store, and query genomics data
<a name="provision-amazon-omics"></a>

This guidance uses [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/) and [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to build, package, and deploy Amazon Omics resources: Reference store, Variant store and Annotation store. And Variant Call Files (VCFs). These resources are ingested and stored in a query ready format in the Variant and Annotation stores.

## 2. Provision serverless data ingestion pipelines for multi-modal data preparation and cataloging
<a name="provision-serverless-data-ingestion-pipelines-for-multi-modal-data-preparation-and-cataloging"></a>

### The Cancer Genome Atlas (TCGA) dataset ingestion
<a name="ingestion-cancer-genome-atlas-dataset"></a>

 For multi-modal data ingestion, the guidance retrieves public data from [The Cancer Genome Atlas (TCGA)](https://portal.gdc.cancer.gov/) and [The Cancer Imaging Archive (TCIA)](https://www.cancerimagingarchive.net/) using a set of [AWS Glue](https://aws.amazon.com/glue/) jobs. The retrieved data sets are parsed, filtered, and stored in the data lake bucket in Parquet format. The guidance also provides several AWS Glue crawlers, which catalog and infer the schema of the downloaded data sets.

 Once all the detailed data sets have been retrieved, another AWS Glue job invokes [Amazon Athena](https://aws.amazon.com/athena/) to summarize the data sets, store the results in Parquet format, and register the results as a Glue data catalog table in a single query operation. An AWS Glue workflow is provided to coordinate and sequence the multiple Glue jobs and crawlers created by the guidance.

 The `TCGAWorkflow` [AWS Glue](https://aws.amazon.com/glue/) workflow is provided to prepare the data. It invokes and sequences the AWS Glue jobs that extract, translate, and load (ETL) data from TCG and TCIA into Amazon S3; the AWS Glue crawlers, which register the data sets in the AWS Glue data catalog; and the final AWS Glue job, which creates a summary of the data sets through invoking an Amazon Athena query.

### Ingestion of genomic datasets – 1000 Genomes Project and ClinVar
<a name="ingestion-genomic-datasets-1000-genomes-project-and-clinvar"></a>

During setup, annotation data from [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) (in VCF format), an example VCF file, and a subset of the [1000 Genomes Project](https://www.genome.gov/27528684/1000-genomes-project) dataset (in VCF format) are copied into the data lake bucket. An Amazon Omics reference store and variant store are configured. The example VCF along with the 1000 Genomes subset VCF are ingested into the variant store and made available for query. In addition, the ClinVar VCF is ingested into the Amazon Omics annotation store and made available for query similar to data in the variant store. A separate Athena database is configured to provide access to the variant and annotation store data using Athena.

## 3. Visualize and explore clinical data through an interactive interface
<a name="visualize-and-explore-clinical-data-through-an-interactive-interface"></a>

 An [Quick](https://aws.amazon.com/quicksight/) dataset is provisioned to provide users an interactive, drag-and-drop interface to explore clinical data. The dataset retrieves data from [Amazon Athena](https://aws.amazon.com/athena/), joining the clinical table with the summary table to facilitate visualization of data availability and interactive cohort generation. The guidance includes detailed instructions for building your own visual queries on the data, and guidance on sharing the resulting analysis with other users.

## 4. Run interactive analytic queries against a multi-modal data lake
<a name="run-interactive-analytic-queries-against-a-multi-modal-data-lake"></a>

**Note**
PyAthena is a Python [DB API 2.0 (PEP 249)](https://www.python.org/dev/peps/pep-0249/) compliant client for [Amazon Athena](https://docs.aws.amazon.com/athena/latest/APIReference/Welcome.html). PyDICOM is a Python library which can be used to read, modify, and write DICOM image files.

 An [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) notebook instance is provisioned with several example Jupyter notebooks that demonstrates how to work with data in a multi-modal data lake.

### The Cancer Genome Atlas (TCGA) dataset
<a name="cancer-genome-atlas-dataset"></a>

 The TCGA notebook uses Amazon Athena to construct a cohort of lung cancer patients from TCGA based on clinical and tumor mutation data to analyze signals in gene expression data. A subset of the identified patients having image data are retrieved and visualized within the notebook. This is done using a sequence of queries submitted by the PyAthena driver and image data retrieved and parsed using PyDICOM.

### The 1000 Genomes Project dataset
<a name="genomic-datasets-1000-genomes-project-and-clinvar"></a>

 The 1000 Genomes Project notebook uses Amazon Athena to identify genomic variants related to drug response for a given cohort of individuals. The below query is run against data in the data lake using the PyAthena driver to:

1. Filter by samples in a subpopulation.

1. Aggregate variant frequencies for the subpopulation-of-interest.

1. Join on the ClinVar dataset.

1. Filter by variants that have been implicated in drug-response.

1. Order by highest frequency variants. The query can also be run in the Amazon Athena console.

   ```
   SELECT  count(*)/cast(numsamples AS DOUBLE) AS genotypefrequency
       ,cv.attributes['RS'] as rs_id
       ,cv.attributes['CLNDN'] as clinvar_disease_name
       ,cv.attributes['CLNSIG'] as clinical_significance
       ,sv.contigname
       ,sv.start
       ,sv."end"
       ,sv.referenceallele
       ,sv.alternatealleles
       ,sv.calls
           FROM {variant_table_name} sv
           CROSS JOIN
               (SELECT count(1) AS numsamples
               FROM
                   (SELECT DISTINCT vs.sampleid
                   FROM {variant_table_name} vs
                   WHERE vs.sampleid LIKE 'NA12%'))
           JOIN {annotation_table_name} cv
           ON sv.contigname = cv.contigname
               AND sv.start = cv.start
               AND sv."end" = cv."end"
               AND sv.referenceallele = cv.referenceallele
               AND sv.alternatealleles = cv.alternatealleles
               AND cv.attributes['CLNSIG'] LIKE '%response%'
               AND sv.sampleid LIKE 'NA12%'
           GROUP BY  sv.contigname
                     ,sv.start
                     ,sv."end"
                     ,sv.referenceallele
                     ,sv.alternatealleles
                     ,sv.calls
                     ,cv.attributes['RS']
                     ,cv.attributes['CLNDN']
                     ,cv.attributes['CLNSIG']
                     ,numsamples
           ORDER BY genotypefrequency DESC LIMIT 50
   ```

## Continuous integration and continuous delivery (CI/CD)
<a name="coninuous-integration-continuous-delivery"></a>

The guidance includes [continuous integration](https://aws.amazon.com/devops/continuous-integration/) and [continuous delivery](https://aws.amazon.com/devops/continuous-delivery/) (CI/CD) using [AWS CodeCommit](https://aws.amazon.com/codecommit/) source code repositories and [AWS CodePipeline](https://aws.amazon.com/codepipeline/) for building and deploying updates to the data preparation jobs, crawlers, data analysis notebooks, and the data lake infrastructure. This guidance fully leverages [infrastructure as code](https://d1.awsstatic.com/whitepapers/DevOps/infrastructure-as-code.pdf?did=wp_card&trk=wp_card) principles and best practices that allow you to rapidly evolve the guidance. After deployment, you can modify the guidance to fit your particular needs, for example, by adding new data preparation jobs and crawlers. Each change is tracked by the CI/CD pipeline, facilitating change control management, rollbacks, and auditing.

This implementation guide describes architectural considerations and configuration steps for deploying the Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS in the Amazon Web Services (AWS) Cloud. It includes links to an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template that launches and configures the AWS services required to deploy this guidance using AWS best practices for security and availability.

The guide is intended for IT infrastructure architects, administrators, data scientists, software engineers, and DevOps professionals who have practical experience architecting in the AWS Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
