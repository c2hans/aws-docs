---
source_url: https://docs.aws.amazon.com/solutions/migrating-tabular-data-from-amazon-s3-to-s3-tables/index.html
---

---
title: 'Guidance for Migrating Tabular Data from Amazon S3 to S3 Tables'
canonical_url: https://docs.aws.amazon.com/solutions/migrating-tabular-data-from-amazon-s3-to-s3-tables/
source: aws-documentation
generated_on: 2026-10-07
---

# Guidance for Migrating Tabular Data from Amazon S3 to S3 Tables

## Overview

This Guidance demonstrates how to migrate tabular data from Amazon Simple Storage Service (Amazon S3) general purpose buckets to Amazon S3 Tables, purpose-built storage for tabular data. S3 Tables introduces a new bucket type, S3 table bucket, that stores fully managed Apache Iceberg tables to deliver up to three times faster query performance and up to ten times higher transactions per second compared to storing Iceberg tables in Amazon S3 general purpose buckets. The Guidance sets up an automated migration process for moving Apache Iceberg and Apache Hive tables registered in AWS Glue Data Catalog and stored in Amazon S3 general purpose buckets to Amazon S3 table buckets using AWS Step Functions and Amazon EMR with Apache Spark. With built-in support for Apache Iceberg, you can query tabular data in S3 table buckets with popular query engines including Amazon Athena, Amazon Redshift, and Apache Spark.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/migrating-tabular-data-from-amazon-s3-to-s3-tables.pdf)

![Architecture diagram](/images/solutions/migrating-tabular-data-from-amazon-s3-to-s3-tables/images/migrating-tabular-data-from-amazon-s3-to-s3-tables-1.png)

1. **Step 1**: The user deploys this solution using AWS CloudFormation by creating a stack through the AWS Management Console.
1. **Step 2**: CloudFormation deploys resources including AWS Lambda, AWS Identity and Access Management (IAM), custom resources, AWS Step Functions, and a PySpark Script.
1. **Step 3**: The CheckResourceExists Lambda function checks for the existence of a source Amazon Simple Storage Service (Amazon S3) bucket and the AWS Glue table for migration.
1. **Step 4**: The EMRLogS3Bucket Amazon S3 bucket is created by CloudFormation to store the Amazon EMR cluster logs, as well as the PySpark script for the Apache Spark on Amazon EMR jobs.
1. **Step 5**: The EMREC2StateMachine Step Functions task is manually invoked by the user to orchestrate the creation of an Amazon EMR cluster and the execution of an Apache Spark job.
1. **Step 6**: The Apache Spark jobs running on the Amazon EMR cluster use the Create Table As Select (CTAS) functionality to migrate data from the source AWS Glue table and source Amazon S3 bucket to the target Amazon S3 table bucket.
1. **Step 7**: Upon completion of the migration workflow, the EMREC2StateMachine Step Functions task sends a notification email to the user by Amazon Simple Notification Service (Amazon SNS).
1. **Step 8**: The Amazon EMR cluster is terminated by the EMREC2StateMachine Step Functions task.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Deploy this Guidance**

[Sample code](https://github.com/aws-solutions-library-samples/guidance-for-migrating-tabular-data-from-amazon-s3-to-s3-tables)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By using CloudFormation, you gain automated deployment and comprehensive visibility into all created AWS resources and their deployment status. To enhance monitoring and alerting, Lambda functions store invocation and operational events in Amazon CloudWatch Logs, while Amazon SNS sends email notifications about the migration workflow's status. These services collectively enable robust auditing and monitoring of S3 Tables. S3 Tables provide automated compaction and unreferenced file cleanup. This combination of services helps ensure optimal performance, facilitates troubleshooting, and minimizes operational overhead, allowing you to maintain excellence in your data management operations. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

S3 Tables and IAM work together to provide robust security measures. They offer identity-based and resource-based fine-grained access controls so that only authorized users and processes can interact with your data. Data protection is enhanced through encryption at rest and in transit, safeguarding your information throughout the migration process and beyond. IAM is designed for precise control over who can access AWS resources and what actions they can perform, enabling you to maintain strict compliance requirements. By implementing these security features, you can prevent unauthorized access to table data, protect sensitive information, and ensure that your migration process adheres to your organization's security policies and regulatory standards. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

Lambda automatically scales to handle increasing concurrent requests across multiple Availability Zones (AZs) for high availability. Amazon SNS delivers messages across AZs, while Amazon S3 provides durable, multi-AZ storage for logs. S3 Tables offer automated maintenance, support for concurrent operations, and inherit the durability of Amazon S3. Step Functions contributes retry and catch mechanisms for workflow management. AWS Glue Tables provide a serverless way to organize related data. These services collectively support consistent performance, data durability, and automated maintenance throughout the migration, minimizing manual intervention and maximizing reliability of your data operations. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

S3 Tables deliver the same durability, availability, scalability, and performance characteristics as S3 itself, and automatically optimizes storage to maximize query performance and to minimize cost. Step Functions enhances efficiency by breaking workflows into smaller, manageable tasks and orchestrating them to reduce overall processing time and resource utilization. AWS Glue Tables contribute with their schema-on-read capability, enabling flexible and efficient querying of large datasets. Collectively, these services deliver improved object data storage, query throughput, and transaction processing for analytics workloads compared to traditional Amazon S3 buckets. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Lambda provides serverless compute, enabling cost-effective scaling for multiple parallel invocations without the need for provisioned infrastructure. Amazon S3 offers reliable, low-cost object storage, while Amazon SNS delivers messages to multiple subscribers efficiently. S3 Tables significantly reduce operational costs through automated compaction, snapshot management, and cleanup of unreferenced files. This automation eliminates the need for you to build and maintain costly compute clusters for table optimization, a process that traditionally requires skilled development teams and complex systems. Furthermore, this Guidance combines cost-effective storage with scalable compute and orchestration, while S3 Tables keep Apache Iceberg tables performant without additional infrastructure costs. This approach not only optimizes expenses but also improves reliability and lowers the barrier to entry for modern analytics. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Lambda, a serverless compute service, provisions resources on-demand, reducing energy consumption by eliminating idle infrastructure. Similarly, Amazon SNS offers serverless messaging, efficiently delivering messages between applications and subscribers without maintaining always-on servers. Amazon S3 Tables further contribute to sustainability by optimizing storage layout through compaction and removing unnecessary data through automated maintenance. This approach significantly reduces the storage footprint required for data persistence. By using these serverless and storage-efficient services, your migration process not only becomes more cost-effective but also aligns with environmental sustainability goals, demonstrating a commitment to responsible resource usage in cloud operations. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Build a managed transactional data lake with Amazon S3 Tables**: This blog post provides an overview of S3 Tables, and an example of how to build a transactional data lake with S3 Tables using Apache Spark on Amazon EMR.

[Learn more](https://aws.amazon.com/blogs/storage/build-a-managed-transactional-data-lake-with-amazon-s3-tables/)

- **How Amazon S3 Tables use compaction to improve query performance by up to 3 times**: This blog post demonstrates how Amazon S3 Tables use compaction to improve query performance by up to 3 times, optimizing data organization for more efficient analytics processing on S3.

[Learn more](https://aws.amazon.com/blogs/storage/how-amazon-s3-tables-use-compaction-to-improve-query-performance-by-up-to-3-times/)

- **New Amazon S3 Tables: Storage optimized for analytics workloads**: This blog post demonstrates how the new Amazon S3 Tables feature optimizes analytics workloads, improving performance and reducing costs for data queries on S3.

[Learn more](https://aws.amazon.com/blogs/aws/new-amazon-s3-tables-storage-optimized-for-analytics-workloads/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
