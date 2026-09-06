---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sus_sus_software_a6.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS03-BP05 Use software patterns and architectures that best support data access and storage patterns
<a name="sus_sus_software_a6"></a>

Understand how data is used within your workload, consumed by your users, transferred, and stored. Use software patterns and architectures that best support data access and storage to minimize the compute, networking, and storage resources required to support the workload.

 **Common anti-patterns:**
+  You assume that all workloads have similar data storage and access patterns.
+  You only use one tier of storage, assuming all workloads fit within that tier.
+  You assume that data access patterns will stay consistent over time.
+  Your architecture supports a potential high data access burst, which results in the resources remaining idle most of the time.

 **Benefits of establishing this best practice:** Selecting and optimizing your architecture based on data access and storage patterns will help decrease development complexity and increase overall utilization. Understanding when to use global tables, data partitioning, and caching will help you decrease operational overhead and scale based on your workload needs.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Use software and architecture patterns that aligns best to your data characteristics and access patterns. For example, use [modern data architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/) that allows you to use purpose-built services optimized for your unique analytics use cases. These architecture patterns allow for efficient data processing and reduce the resource usage.

 **Implementation steps**
+  Analyze your data characteristics and access patterns to identify the correct configuration for your cloud resources. Key characteristics to consider include:
  +  **Data type:** structured, semi-structured, unstructured
  +  **Data growth:** bounded, unbounded
  +  **Data durability:** persistent, ephemeral, transient
  +  **Access patterns** reads or writes, update frequency, spiky, or consistent
+  Use architecture patterns that best support data access and storage patterns.
  + [ Let’s Architect\! Modern data architectures ](https://aws.amazon.com/blogs/architecture/lets-architect-modern-data-architectures/)
  + [ Databases on AWS: The Right Tool for the Right Job ](https://www.youtube.com/watch?v=-pb-DkD6cWg)
+  Use technologies that work natively with compressed data.
+  Use purpose-built [analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a) for data processing in your architecture.
+  Use the database engine that best supports your dominant query pattern. Manage your database indexes to ensure efficient querying. For further details, see [AWS Databases](https://aws.amazon.com/products/databases/).
+  Select network protocols that reduce the amount of network capacity consumed in your architecture.

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
+ [ Amazon S3 Intelligent-Tiering storage class ](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)

 **Related videos:**
+ [ Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o)
