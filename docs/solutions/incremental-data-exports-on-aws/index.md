---
source_url: https://docs.aws.amazon.com/solutions/incremental-data-exports-on-aws/index.html
---

---
title: 'Guidance for Incremental Data Exports on AWS'
canonical_url: https://docs.aws.amazon.com/solutions/incremental-data-exports-on-aws/
source: aws-documentation
generated_on: 2026-09-29
---

# Guidance for Incremental Data Exports on AWS

## Overview

This Guidance demonstrates a robust approach to incrementally export and maintain a centralized data repository reflecting ongoing changes in a distributed database. It shows how to establish a data pipeline that seamlessly captures and integrates incremental updates into an existing data store. The incremental process minimizes redundancy, enhances consistency, and improves access to accurate, up-to-date information. With more accurate data, you can make more informed, data-driven decisions.

## How it works

These technical details feature an architecture diagram to illustrate how to effectively use this solution. The architecture diagram shows the key components and their interactions, providing an overview of the architecture's structure and functionality step-by-step.

[Download the architecture diagram](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/solutions/approved/documents/architecture-diagrams/incremental-data-exports-on-aws.pdf)

![Architecture diagram](/images/solutions/incremental-data-exports-on-aws/images/incremental-data-exports-on-aws-1.png)

1. **Step 1**: Application traffic consistently adds, updates, and deletes items in an Amazon DynamoDB table.
1. **Step 2**: Perform a full export of your DynamoDB table. This will write the exported data into Amazon Simple Storage Service (Amazon S3) in JSON format.
1. **Step 3**: Create, prepare, and use Amazon EMR Serverless to read the full export of the DynamoDB table from Amazon S3. EMR Serverless will dynamically identify Iceberg table schema with the full set of columns that will map to all the unique attributes from your full DynamoDB exported dataset.
1. **Step 4**: Create AWS Glue Data Catalog to persist the Iceberg table meta store and query the table from Amazon Athena (or any Hive Meta store compatible query engine) using the same Glue Catalog.
1. **Step 5**: Use EMR Serverless to build the Iceberg table based on the full export of the DynamoDB table, and use the Iceberg table generated schema.
1. **Step 6**: Analysts can use an Athena query to verify that the Iceberg table is accessible and readable. This involves running a SELECT query on the Iceberg table through Athena to confirm that data can be retrieved successfully and accurately.
1. **Step 7**: Perform an incremental export of your DynamoDB table in JSON format. This will only export the changed data from the DynamoDB table since the last full or incremental export.
1. **Step 8**: Use EMR Serverless to update a previously created Iceberg table with the incremental export of the DynamoDB table data.
1. **Step 9**: Analysts will use the same Athena query to verify that the Iceberg table shows changed records. For example, if you've added or deleted items in the DynamoDB table after full export, the count should reflect this.
## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: Ready to deploy? Review the sample code on GitHub for detailed deployment instructions to deploy as-is or customize to fit your needs.

[Go to sample code](https://github.com/aws-solutions-library-samples/guidance-for-incremental-data-exports-on-aws)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

By offloading storage management to Amazon S3, you can concentrate on application development and analytics workflows without infrastructure overhead. Amazon S3 handles thousands of transactions per second, resulting in seamless upload and retrieval of data. This operational efficiency allows teams to optimize their core competencies while AWS manages the underlying storage infrastructure. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

DynamoDB, Amazon S3, and AWS Glue provide encryption, access controls, and audit logging, enabling users to meet security and compliance requirements. Athena and EMR Serverless inherit robust security features from their underlying services, helping to ensure data privacy and compliance. As AWS fully manages these services, security best practices are consistently implemented, reducing the burden of managing security measures. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

DynamoDB and Amazon S3 prioritize high availability through cross-Availability Zone replication and data redundancy within a Region, helping to maintain accessibility during failures or disruptions. Amazon S3 offers 99.999999999% durability, preventing data loss over time, while DynamoDB provides 99.999% availability and durability for tables. These fault-tolerant services employ redundant storage and distributed architectures, minimizing the impact of failures on data integrity and service availability. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

AWS Glue streamlines data discovery through its centralized metadata repository, reducing time spent locating and accessing datasets. It automatically scales resources to match extract, transform, load (ETL) job demands for optimal performance without manual intervention. AWS Glue's automated resource provisioning and efficient data cataloging contribute to high performance efficiency, allowing for seamless data processing and analytics workflows. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

EMR Serverless automatically provisions and releases resources based on job requirements, eliminating costs when jobs are not running. This consumption-based model is ideal for workloads with intermittent, short-duration processing followed by long idle periods. EMR Serverless optimizes costs by dynamically scaling resources to match demand, so that you only incur charges for the resources consumed and avoid unnecessary expenses during inactive periods. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

The serverless and scalable nature of AWS services like Amazon S3 and EMR Serverless optimizes compute and backend resource usage, effectively minimizing the environmental impact of your workloads. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

## Related content

- **Use Amazon DynamoDB incremental export to update Apache Iceberg tables**: This blog post demonstrates how to bulk process a series of full and incremental exports using Amazon EMR Serverless with Apache Spark to produce a single Apache Iceberg table representing the latest state of the DynamoDB table, which you will then be able to query using Amazon Athena.

[Use Amazon DynamoDB incremental export to update Apache Iceberg tables](https://aws.amazon.com/blogs/database/use-amazon-dynamodb-incremental-export-to-update-apache-iceberg-tables/)

[Read usage guidelines](/solutions/guidance-disclaimers/)
