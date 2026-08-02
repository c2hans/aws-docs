---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/aws-cloud-data-ingestion-patterns-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Cloud Data Ingestion Patterns and Practices
<a name="aws-cloud-data-ingestion-patterns-practices"></a>

Publication date: **July 23, 2021** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Today, many organizations want to gain further insight using the vast amount of data they generate or have access to. They may want to perform reporting, analytics and/or machine learning on that data and further integrate the results with other applications across the organization. More and more organizations have found it challenging to meet their needs with traditional on-premises data analytics solutions, and are looking at modernizing their data and analytics infrastructure by moving to cloud. However, before they can start analyzing the data, they need to ingest this data into cloud and use the right tool for the right job. This paper outlines the patterns, practices, and tools used by AWS customers when ingesting data into AWS Cloud using AWS services.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 As companies are dealing with massive surge in data being generated, collected and stored to support their business needs, users are expecting faster access to data to make better decisions quickly as changes occur. Such agility requires that they integrate terabytes to petabytes and sometimes exabytes of data, along with the data that was previously siloed, in order to get a complete view of their customers and business operations.

 To analyze these vast amounts of data and to cater to their end user’s needs, many companies create solutions like data lakes and data warehouses. They also have purpose-built data stores to cater to specific business applications and use cases—for example, relational database systems to cater to transactional systems for structured data or technologies like OpenSearch to perform log analytics and search operations.

 As customers use these data lakes and purpose-built stores, they often need to also move data between these systems. For example, moving data from the lake to purpose- built stores, from those stores to the lake, and between purpose-built stores.

 At re:Invent 2020, we walked through a new modern approach to called the [Modern Data architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/). This architecture is shown in the following diagram.

![A diagram depicting Modern Data architecture on AWS.](http://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/modern-data-architecture.png)

 As data in these data lakes and purpose-built stores continues to grow, it becomes harder to move all this data around. We call this *data gravity*.

 Data movement is a critical part of any system. To design a data ingestion pipeline, it is important to understand the requirements of data ingestion and choose the appropriate approach which meets performance, latency, scale, security, and governance needs.

 This whitepaper provides the patterns, practices and tools to consider in order to arrive at the most appropriate approach for data ingestion needs, with a focus on ingesting data from outside AWS to the AWS Cloud. This whitepaper is not a programming guide to handle data ingestion but is rather intended to be a guide for architects to understand the options available and provide guidance on what to consider when designing a data ingestion platform. It also guides you through various tools that are available to perform your data ingestion needs.

 The whitepaper is organized into several high-level sections which highlight the common patterns in the industry. For example, *homogeneous data ingestion* is a pattern where data is moved between similar data storage systems, like Microsoft SQL Server to Microsoft SQL Server or similar formats like Parquet to Parquet. This paper further breaks down different use cases for each pattern—for example, migration from on- premises system to AWS Cloud, scaling in the cloud for read-only workloads and reporting, or performing change data capture for continuous data ingestion into the analytics workflow.
