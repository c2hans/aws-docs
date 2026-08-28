---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_view_metrics_export.html
---

# Viewing Amazon S3 Storage Lens metrics using a data export
<a name="storage_lens_view_metrics_export"></a>

Amazon S3 Storage Lens metrics are generated daily in CSV or Apache Parquet-formatted metrics export files and placed in an S3 general purpose bucket in your account. From there, you can ingest the metrics export into the analytics tools of your choice, such as Amazon Quick and Amazon Athena, where you can analyze storage usage and activity trends. You can also send daily metric exports to an AWS-managed S3 table bucket for immediate querying, using AWS analytics services or third-party tools.

**Topics**
+ [Using an AWS KMS key to encrypt your metrics exports](storage_lens_encrypt_permissions.md)
+ [What is an S3 Storage Lens export manifest?](storage_lens_whatis_metrics_export_manifest.md)
+ [Understanding the Amazon S3 Storage Lens export schemas](storage_lens_understanding_metrics_export_schema.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
