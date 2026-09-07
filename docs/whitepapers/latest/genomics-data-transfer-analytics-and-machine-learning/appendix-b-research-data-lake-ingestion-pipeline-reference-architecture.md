---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-b-research-data-lake-ingestion-pipeline-reference-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix B: Research data lake ingestion pipeline reference architecture
<a name="appendix-b-research-data-lake-ingestion-pipeline-reference-architecture"></a>

 The following reference architecture shows an example end-to-end research data lake data ingestion AWS Glue pipeline using the data lake reference architectures described in this paper. The AWS Glue workflows enable you to construct data pipelines using extract, transform, and load (ETL) functions, crawlers, and triggers.

![Data pipeline using AWS Glue workflows](https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/images/image7.png)

1.  An AWS Glue trigger is run either on-demand or on a schedule.

1.  The dataset is first copied to a quarantine bucket to be scanned for personal health information (PHI) or viruses.

1.  A trigger then launches Glue Python shell jobs that make REST calls to Personal Health Information (PHI) and virus scanning services that scan the dataset which resides in the Amazon S3 quarantine bucket. A quality control (QC) process is run to confirm that the data is in the agreed upon format and schema.

1.  If the dataset passes the scans and QC validation, the data is copied to a pre-curated bucket where the dataset resides without changes.

1.  The dataset is then copied to a curated bucket where it is reorganized and filtered based on the study or research project.

1.  A trigger then launches jobs to update a research project dashboard, a research portal database, extract transform, and load (ETL) processes to transform the data and write it to the data lake in Apache Parquet format. AWS Glue crawlers crawl the data, infer the schema, and update the AWS Glue meta data catalog. The data is made available for query using big data query engines such as Amazon Athena. Data governance is managed with Identity and Access Management (IAM) or with AWS Lake Formation.
