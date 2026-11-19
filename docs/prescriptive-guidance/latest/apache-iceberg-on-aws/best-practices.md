---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/best-practices.html
---

# Best practices for optimizing Iceberg workloads

Iceberg is a table format that's designed to simplify data lake management and enhance workload performance. Different use cases might prioritize different aspects such as cost, read performance, write performance, or data retention, so Iceberg offers configuration options to manage these trade-offs. This section provides insights for optimizing and fine-tuning your Iceberg workloads to meet your requirements.

## Applies to both hosting options
<a name="applies-to-hosting-options"></a>

The guidance in this section applies to both **self-managed Iceberg on Amazon S3** and **Amazon S3 Tables** except where explicitly called out.

## In this section
<a name="in-this-section"></a>
+ [General best practices](best-practices-general.md)
+ [Optimizing read and write performance](optimizing-read-and-write-performance.md)
+ [Optimizing storage](best-practices-storage.md)
+ [Maintaining Iceberg tables](maintaining-iceberg-tables.md) — the three execution options for Iceberg maintenance on AWS:
  + [Self-managed maintenance with Apache Spark procedures](self-managed-maintenance.md)
  + [Maintenance with the AWS Glue Data Catalog table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md)
  + [Maintenance in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md)
+ [Handling concurrency](handling-write-concurrency.md)
