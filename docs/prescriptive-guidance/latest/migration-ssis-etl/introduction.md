---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-ssis-etl/introduction.html
---

# Migrating SSIS ETL jobs to AWS
<a name="introduction"></a>

*Durga Prasad and Harpreet Singh, Amazon Web Services*

Amazon Web Services (AWS) provides services for developing and running extract, transform, and load (ETL) or extract, load, and transform (ELT) jobs and big data workloads. Microsoft SQL Server Integration Services (SSIS) is an on-premises ETL tool that has a graphical interface for building ETL jobs. Depending on the target state architecture, you can use the AWS Glue graphical interface or the Apache Spark framework with Python libraries to build ETL jobs in the AWS Cloud.

This guide describes the steps for migrating SSIS ETL/ELT jobs from on premises to AWS. It discusses migration phases, best practices, and recommendations to reduce the migration effort and improve the experience. The information is applicable to any target AWS architecture.

The guide is for program or project managers, product owners, solution architects, and developers who are:
+ Migrating from SSIS to AWS for various reasons, such as modernization or cost savings.
+ Primarily using AWS services for ETL and big data workloads.
+ Looking for a cloud-based solution to take advantage of a serverless model and flexible pricing.

## Targeted business outcomes
<a name="business-outcomes"></a>

Migrating your SSIS jobs to the AWS Cloud helps you achieve these primary outcomes:
+ Modernize existing on-premises ETL processes in a cost-effective way
+ Respond to the information needs of the organization faster
+ Merge existing processes and retire unused processes to reduce maintenance and operational overhead
+ Build a foundation to meet your organization's future data requirements

## Attachments
<a name="attachments-ae5b08b7-f641-4524-9650-6ac5a0f71dd9"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
