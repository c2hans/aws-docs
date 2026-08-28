---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_software_a6.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP05 Use software patterns and architectures that best support data access and storage patterns
<a name="sus_sus_software_a6"></a>

 Understand how data is used within your workload, consumed by your users, transferred, and stored. Select technologies to minimize data processing and storage requirements.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Analyze your data access and storage patterns.
+  Store data files in efficient file formats such as Parquet to prevent unnecessary processing (for example, when running analytics) and to reduce the total storage provisioned.
+  Use technologies that work natively with compressed data.
+  Use the database engine that best supports your dominant query pattern.
+  Manage your database indexes to ensure index designs support efficient query execution.
+  Select network protocols that reduce the amount of network capacity consumed.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Athena Compression Support file formats](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html)
+  [COPY from columnar data formats with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html)
+  [Converting Your Input Record Format in Firehose](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)
+  [Format Options for ETL Inputs and Outputs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html)
+  [Improve query performance on Amazon Athena by Converting to Columnar Formats](https://docs.aws.amazon.com/athena/latest/ug/convert-to-columnar.html)
+  [Loading compressed data files from Amazon S3 with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html)
+  [Monitoring DB load with Performance Insights on Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html)
+  [Monitoring DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
+  [AWS IoT FleetWise](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-iot-fleetwise-transferring-vehicle-data-cloud/)

 **Related videos:**
+  [Building Sustainably on AWS](https://www.youtube.com/watch?v=ARAitMSIxc8)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
