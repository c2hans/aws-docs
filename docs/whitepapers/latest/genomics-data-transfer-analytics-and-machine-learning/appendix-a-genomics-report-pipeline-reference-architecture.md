---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-a-genomics-report-pipeline-reference-architecture.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix A: Genomics report pipeline reference architecture
<a name="appendix-a-genomics-report-pipeline-reference-architecture"></a>

 The following shows an example end-to-end genomics report pipeline architecture using the reference architectures described in this paper.

![Genomics report pipeline reference architecture](http://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/images/image6.png)

1.  A technician loads a genomic sample on a sequencer.

1.  The genomic sample is sequenced and written to a landing folder that is stored in a local on-premises storage system.

1.  An AWS DataSync sync task is preconfigured to sync the data from the parent directory of the landing folder on on-premises storage, to a bucket in Amazon S3.

1.  A run completion tracker script running as a cron job, starts a DataSync task run to transfer the run data to an Amazon S3 bucket. An inclusion filter can be used when running a DataSync task run, to only include a given run folder. Exclusion filters can be used to exclude files from data transfer. In addition, consider Incorporating a zero-bite file as a flag when uploading the data. Technicians can then indicate when a run has passed a manual QA check by placing an empty file in the data folder. Then, the watcher application will only trigger a sync task if the success file is present.

1.  DataSync transfers the data to Amazon S3.

1.  An Amazon CloudWatch Events is raised that uses an Amazon CloudWatch rule to launch an AWS Step Functions state machine.

1.  The state machine orchestrates secondary analysis and report generation tools which run in Docker containers using AWS Batch.

1.  Amazon S3 is used to store intermediate files for the state machine execution jobs.

1.  Optionally, the last tool in the state machine execution workflow uploads the report to the Laboratory Information Management System (LIMS).

1.  An additional step is added to run an AWS Glue workflow to convert the VCF to Apache Parquet, write the Parquet files to a data lake bucket in Amazon S3 and update the AWS Glue Data Catalog.

1.  A bioinformatic scientist works with the data in the Amazon S3 data lake using Amazon Athena via a Jupyter notebook, Amazon Athena console, AWS CLI, or an API. Jupyter notebooks can be launched from either Amazon SageMaker AI or AWS Glue. You can also use Amazon SageMaker AI to train machine learning models or do inference using data in your data lake.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
