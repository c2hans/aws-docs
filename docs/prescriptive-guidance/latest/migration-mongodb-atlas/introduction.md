---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-mongodb-atlas/introduction.html
---

# Migrating to MongoDB Atlas on AWS
<a name="introduction"></a>

*Battulga Purevragchaa and Igor Alekseev, Amazon Web Services*

*Babu Srinivasan, MongoDB*

This guide describes the architecture, tools, considerations, and use cases for migrating from an on-premises relational, legacy, or other type of database to MongoDB Atlas in the AWS Cloud. Source relational databases include Oracle Database, SQL Server, MySQL, PostgreSQL, and other databases such as Sybase and IBM Db2. You can also migrate from databases such as Azure Cosmos DB, Apache Cassandra, Couchbase, and Redis. For step-by-step instructions, see the following patterns on the AWS Prescriptive Guidance website:
+ [Migrate a self-hosted MongoDB environment to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-self-hosted-mongodb-environment-to-mongodb-atlas-on-the-aws-cloud.html)
+ [Migrate a relational database to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-relational-database-to-mongodb-atlas.html)
+ [Stream data from IBM Db2, SAP, Sybase, and other databases to MongoDB Atlas on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/stream-data-from-ibm-db2-to-mongodb-atlas.html)

## Overview
<a name="overview"></a>

MongoDB Atlas is a developer data platform that provides a document model database built on a scale-out architecture for developers who build scalable web and business applications. Development teams use MongoDB for the following reasons:
+ **Flexible data model** – MongoDB is document-oriented, so it supports dynamic and nested data without restrictive schemas. This makes it easier for developers to represent complex or changing data.
+ **High performance** – MongoDB provides high throughput and low latency with native indexing, in-memory computing, and other optimizations. This is critical for modern applications.
+ **Scalability** – MongoDB scales horizontally on commodity hardware with built-in sharding and replication. This makes it easy to scale from hundreds to millions of operations per second without compromising high availability.
+ **Robust and unified queries** – MongoDB supports flexible ad-hoc queries, indexing, and aggregation. It performs well without extensive tuning and enables a wide range of query patterns.
+ **Ease of use** – MongoDB provides a developer-friendly experience with JSON-like documents, rich drivers for many languages, and extensive documentation and community. It's easy for teams to get productive quickly.
+ **Resilience and high availability** – MongoDB Atlas is designed with resilience and high availability in mind. Its database replica sets consist of primary and secondary members, ensuring automatic failover to a secondary member in the event of a disruption in the primary member. Atlas is trusted by organizations of all sizes to support mission-critical workloads.

Other features include indexing on nested fields, atomicity, consistency, isolation, durability (ACID) transactions, and geospatial queries. MongoDB Atlas also supports:
+ A single view that aggregates data from multiple sources.
+ Real-time data analysis.
+ Internet of Things (IoT) applications.
+ Scalable mobile applications.
+ Catalogs of database assets, entities, and metadata that simplify data storage, data retrieval, and schema changes.
+ Ability to store and manage any type of content.
+ Ability to offload mainframe applications to modern platforms.
+ Database support for gaming applications.
+ Reduced complexity for working with time series data.
+ Generative artificial intelligence (AI) use cases with MongoDB Atlas Vector Search.

For more use cases, see the [MongoDB website](https://www.mongodb.com/use-cases).

## MongoDB Atlas on AWS
<a name="atlas-on-aws"></a>

MongoDB Atlas on AWS is a fully managed database as a service (DBaaS) that is highly available, performant at a global scale, and compliant with demanding security and privacy standards in cost-effective ways. Here are some notable benefits:
+ Global footprint – AWS has a global footprint, that includes data centers in regions all around the world. This makes it easy to deploy your MongoDB Atlas clusters close to your users, which can improve performance and reduce latency.
+ Security – MongoDB Atlas supports SAML 2.0 authentication through integration with AWS IAM Identity Center. It also lets customers centralize access management to Atlas by supporting single sign-on (SSO) by using corporate directory credentials.
+ Cost optimization – AWS provides cost optimization tools that help you save money by analyzing your database usage patterns and identifying opportunities to optimize your spending. You can also user AWS Reserved Instances and other savings plans to get significant discounts on your MongoDB Enterprise Advanced clusters.
+ Backup and disaster recovery – AWS provides a full range of backup and disaster recovery capabilities that help protect your data in the event of a disaster. MongoDB Atlas on AWS provides continuous backups, point-in-time restores, and cross-Region replication to help make sure that your data is always safe and recoverable.
+ Seamless integrations – Integrations with other AWS services are seamless with MongoDB Atlas.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
