---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/sus_sus_software_a6.html
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

### Implementation steps
<a name="implementation-steps"></a>
+  Analyze your data characteristics and access patterns to identify the correct configuration for your cloud resources. Key characteristics to consider include:
  +  **Data type:** structured, semi-structured, unstructured
  +  **Data growth:** bounded, unbounded
  +  **Data durability:** persistent, ephemeral, transient
  +  **Access patterns** reads or writes, update frequency, spiky, or consistent
+  Use architecture patterns that best support data access and storage patterns.
  + [ Patterns for enabling data persistence ](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/enabling-patterns.html)
  + [ Let’s Architect\! Modern data architectures ](https://aws.amazon.com/blogs/architecture/lets-architect-modern-data-architectures/)
  + [ Databases on AWS: The Right Tool for the Right Job ](https://www.youtube.com/watch?v=-pb-DkD6cWg)
+  Use technologies that work natively with compressed data.
  + [ Athena Compression Support file formats ](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html)
  + [ Format Options for ETL Inputs and Outputs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html)
  + [ Loading compressed data files from Amazon S3 with Amazon Redshift ](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html)
+  Use purpose-built [analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a) for data processing in your architecture. For detail on AWS purpose-built analytics services, see [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o).
+  Use the database engine that best supports your dominant query pattern. Manage your database indexes to ensure efficient querying. For further details, see [AWS Databases](https://aws.amazon.com/products/databases/) and [AWS re:Invent 2022 - Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0).
+  Select network protocols that reduce the amount of network capacity consumed in your architecture.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [COPY from columnar data formats with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html)
+  [Converting Your Input Record Format in Firehose](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)
+  [Improve query performance on Amazon Athena by Converting to Columnar Formats](https://docs.aws.amazon.com/athena/latest/ug/convert-to-columnar.html)
+  [Monitoring DB load with Performance Insights on Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html)
+  [Monitoring DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
+ [ Amazon S3 Intelligent-Tiering storage class ](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
+ [ Build a CQRS event store with Amazon DynamoDB ](https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/)

 **Related videos:**
+ [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U)
+ [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations ](https://www.youtube.com/watch?v=je6GCOZ22lI)
+ [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient ](https://www.youtube.com/watch?v=7-CB02rqiuw)
+ [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3 ](https://www.youtube.com/watch?v=RxgYNrXPOLw)
+ [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3 ](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
+ [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge ](https://www.youtube.com/watch?v=6X4lSPkn4ps)

 **Related examples:**
+ [AWS Purpose Built Databases Workshop ](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
+ [AWS Modern Data Architecture Immersion Day ](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
+ [ Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
