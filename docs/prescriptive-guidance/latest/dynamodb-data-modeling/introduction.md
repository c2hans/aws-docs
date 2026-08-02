---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/introduction.html
---

# Modeling data with Amazon DynamoDB
<a name="introduction"></a>

*Camilo Gonzalez, Moinul Al-Mamun, Satheish Kumar Chandraprakasam, and Santiago Segura, Amazon Web Services*

NoSQL databases provide flexible schemas for building modern applications. They are widely recognized for their ease of development, functionality, and performance at scale. Amazon DynamoDB provides fast and predictable performance with seamless scalability for NoSQL databases in the Amazon Web Services (AWS) Cloud. As a fully managed database service, DynamoDB helps you offload the administrative burdens of operating and scaling a distributed database. You don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling.

NoSQL schema design requires a different approach from traditional relational database management system (RDBMS) design. RDBMS data model focuses on the structure of data and its relationships with other data. NoSQL data modeling focuses on access patterns, or how the application is going to consume the data, so it stores the data in a way that supports straightforward query operations. For an RDBMS such as Microsoft SQL Server or IBM Db2, you can create a normalized data model without thinking much about access patterns. You can extend the data model to support your patterns and queries later.

This guide presents a data modeling process for using DynamoDB that provides functional requirements, performance, and effective costs. The guide is for database engineers who are planning to use DynamoDB as the operational database for their applications that are running on AWS. AWS Professional Services has used the recommended process to help enterprise companies with DynamoDB data modeling for different use cases and workloads.
