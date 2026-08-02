---
source_url: https://docs.aws.amazon.com/databases-on-aws-how-to-choose/index.html
---

# Choosing an AWS database service

Determine which AWS databases are the best fit for your organization.

## Overview of AWS database services

AWS oﬀers a growing number of database options (15+) with diverse data models to support a variety of workloads.

These include relational, key-value, document, in-memory, graph, time series, vector, and wide-column databases that help organizations:

- Process millions of transactions per second with consistent performance
- Store and retrieve data with microsecond latency for real-time applications
- Manage core business processes securely with enterprise-grade reliability
- Power AI applications with domain-specific knowledge through vector capabilities

Choosing the right database, or multiple databases, requires you to make a series of decisions based on your organizational needs. This page helps you ask the right questions, provides a clear path for implementation, and helps you migrate from your existing database.

**Note:** This page focuses on databases that are suitable for online transaction processing (OLTP) applications. To store and analyze massive amounts of data quickly and efficiently, a requirement that is typically met by an online analytical processing (OLAP) application, AWS offers Amazon Redshift. Amazon Redshift is a fully managed, cloud-based data warehousing service that handles large-scale analytics workloads.

## Key concepts

There are two high-level categories of AWS OLTP databases—relational and non-relational. **Relational** The AWS relational database family includes eight popular engines for Amazon Aurora and Amazon Relational Database Service. The Aurora engines include Amazon Aurora PostgreSQL-Compatible Edition, Amazon Aurora MySQL-Compatible Edition, or Amazon Aurora DSQL. The Amazon RDS engines include PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, and Db2. These databases store data in tabular format with rows and columns, allowing you to link tables to gain deeper insights into interconnected data points. **Non-relational** Non-relational databases use a variety of data models for accessing and managing data. These include key-value, document, caching, in-memory, graph, time series, and wide-column data models. They’re optimized for applications requiring large data volumes, low latency, and flexible data models by relaxing some data consistency restrictions.

- **Reduced operational overhead**: The services are designed to accommodate various data characteristics and operational requirements. AWS databases support different data models (relational, semi-structured, time series, etc.) and access patterns while allowing customers to choose between self-hosted or fully managed options. The managed services remove the burden of routine database administration tasks, enabling teams to focus on value-adding activities like schema design and query optimization.

[Get started: Operate and optimize relational databases](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-database-migration/optimization-phase.html)

- **Enterprise-grade reliability**: AWS database services prioritize enterprise-grade resiliency, performance, and security features. The platforms offer comprehensive backup and recovery options, support for high-concurrency transactions, multi-region deployment capabilities, and in-memory caching solutions for microsecond response times. Security is implemented through a shared responsibility model, with AWS managing security of the cloud infrastructure while customers maintain control over their data security, authentication, and compliance requirements.

[Learn more: Security and resiliency built into AWS databases](https://aws.amazon.com/products/databases/secure-and-resilient/)

- **Migration flexibility and cost control**: AWS database services offer flexible migration strategies to help customers transition to the cloud based on their specific needs. Organizations can choose to simply rehost their existing databases on EC2 instances for a quick migration, change platforms to managed services like Amazon RDS, or refactor their applications to use cloud-native solutions like Aurora or purpose-built NoSQL databases. For maximum flexibility and cost optimization, AWS also provides serverless database options that automatically scale with demand and follow a pay-for-use model.

[Blog post: Select the right database and database migration plan for your workloads](https://aws.amazon.com/blogs/architecture/selecting-the-right-database-and-database-migration-plan-for-your-workloads/)

## Use cases

Solve your most challenging data problems, from scaling to millions of users, to powering AI with your domain-specific data.

### Internet-scale applications

These applications can handle 100 million or more requests per second over hundreds of terabytes of data. They automatically scale vertically and horizontally to provide flexibility for your workloads. Learn about [data modeling for an internet-scale online transactional system using Amazon DynamoDB](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-capabilities-enhance-data-processing-and-retrieval/)

[Amazon DynamoDB](/dynamodb)
[Amazon Aurora](/rds)
[Amazon ElastiCache](/elasticache)

### Vector databases and vector search for use with generative AI applications

Whatever database service you use will likely contain a wealth of domain-specific data (such as financial records, health records, genomic data, and supply chain information). This data can provide you with a unique and valuable perspective on your business and the broader industry that you work within. For generative AI usage, the domain-specific data you plan to use for semantic context must be encoded as a set of elements, each expressed internally as a *vector*. This contextually relevant data typically comes from your internal databases, data lakes, or unstructured data or document stores - the data stores that host your domain-specific data or knowledge. These data stores are generically called knowledge bases. [Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) is the process for retrieving facts from these knowledge bases to ground [large language models (LLMs)](https://aws.amazon.com/what-is/large-language-model/) with up-to-date, accurate, and insightful data. AWS has added vector capabilities to AWS database and search services so you can store vector datasets where your data is, simplify your application architecture, and use tried, tested, and familiar tools. A vector database, or vector data store, simply means a database with vector capabilities. Such a database can also provide additional enhancements to the ways you use your data with generative AI. Learn more about how AWS [has added vector capabilities to AWS database and search services](https://aws.amazon.com/blogs/database/the-role-of-vector-datastores-in-generative-ai-applications/)

[Amazon Neptune](/neptune)
[Amazon MemoryDB](/memorydb)
[Amazon DocumentDB (with MongoDB compatibility)](/documentdb)
[Amazon Relational Database Service](/rds)
[Amazon Aurora](/rds)
[Amazon DynamoDB](/dynamodb)
[Amazon Keyspaces](/keyspaces)
[Amazon Timestream](/timestream)

### Real-time applications

Real-time applications such as caching, session stores, gaming leaderboards, ride hailing, ad targeting, and real-time analytics need microsecond latency and high throughput to support a trillion or more requests per second. Learn about [building real-time applications with ElastiCache](https://aws.amazon.com/blogs/database/building-a-real-time-gaming-leaderboard-with-amazon-elasticache-for-redis/)

[Amazon DynamoDB](/dynamodb)
[Amazon ElastiCache](/elasticache)

### Enterprise applications

Enterprise applications manage core business processes (such as sales, billing, customer service, and human resources) and line-of-business processes (such as a reservation system at a hotel chain or a risk-management system at an insurance company). These applications need databases that are fast, scalable, secure, available, and reliable. Learn about [building data-driven applications using AWS databases ElastiCache](https://d1.awsstatic.com/psc-digital/2024/gc-600/database-mod-apps/Building-modern-applications-using-AWS-databases.pdf)

[Amazon Aurora](/rds)
[Amazon Relational Database Service](/rds)

## Compare services

This table highlights the type of data that each database is optimized to handle. Use it to help determine the database that is the best fit for your use case.

| Data model | When would you use it? | What is it optimized for? | Related database engines and services |
| --- | --- | --- | --- |
| Relational | Use when you're migrating or modernizing an on-premises relational workload, or if your workload has less predictable query patterns. | Optimized for structured data that is stored in tables, rows, and columns. Relational databases support complex queries through joins. | [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) <br> [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) |
| Key-value | Use for workloads such as session stores or shopping carts. Key-value databases can scale to large amounts of data and extremely high throughput of requests, while servicing millions of simultaneous users through distributed processing and storage. | Optimized to provide a serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale. | [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) |
| In-memory | Use Amazon ElastiCache when you need a caching layer to improve read performance. Use Amazon MemoryDB when you need full data persistence, but still need sub-millisecond read latencies. | Optimized to support microsecond reads and sub-millisecond writes. MemoryDB supports microsecond reads and single-digit millisecond writes. ElastiCache is an ephemeral cache, while MemoryDB is an in-memory database. | [Amazon ElastiCache](https://docs.aws.amazon.com/elasticache/) <br> [Amazon MemoryDB](https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb.html) |
| Document | Use when you want to store JSON-like documents with rich querying abilities across the fields of the documents. | Optimized for storing semi-structured data as documents with multilayered attributes. | [Amazon DocumentDB (with MongoDB compatibility)](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html) |
| Wide-column | Use when you need to migrate your on-premises Apache Cassandra workloads, or when you need to process data at high speeds for applications that require single-digit millisecond latency. | Optimized for workloads that require heavy reads/writes and high throughput, coupled with low latency and linear scalability. | [Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html) |
| Graph | Use when you have to model complex networks of objects, such as social networks, fraud detection, and recommendation engine use cases. | Optimized for traversing and evaluating large numbers of relationships, and identifying patterns with minimal latency. | [Amazon Neptune](https://docs.aws.amazon.com/neptune/) |
| Time series | Use when you have a large amount of time series data, potentially from a number of sources, such as Internet of Things (IoT) data, application metrics, and asset tracking. | Optimized for storing and querying data that is associated with timestamps and trend lines. | [Amazon Timestream](https://docs.aws.amazon.com/timestream/) |

## Start building

This section helps you learn more about the database service or services that you've chosen, and how to get started with them. The database you've chosen might not satisfy all of your requirements perfectly, so it's important to consider your needs and workload requirements carefully. Prioritize based on the considerations covered in this guide, your own specific requirements, and the requirements for which you have some ﬂexibility. This will help you make eﬀective trade-oﬀs and lead to the best possible outcome for your needs. Also consider that, usually, you can cover your application requirements with a mix of best-fit databases. By building a solution with multiple database types, you can use the strengths that each type provides. For example, in an e-commerce use case, you might use Amazon DocumentDB (for product catalogs and user proﬁles) for the ﬂexibility that is provided by semi-structured data, but then combine it with the low, predictable latency provided by DynamoDB (for when your users are browsing your product catalog). You might also add Aurora for inventory and order processing, where a relational data model and transaction support are needed. To help you learn more about each of the available AWS database services, we have provided a pathway to explore how each of the services work. The following section provides links to in-depth documentation, hands-on tutorials, and resources to help you get started.

### Amazon Aurora

**Getting started with Amazon Aurora**

This guide includes tutorials and covers more advanced Aurora concepts and procedures, such as the different kinds of endpoints and how to scale Aurora clusters up and down.

[Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

**Use Amazon Aurora global databases**

Get started using Aurora global databases. This guide outlines the supported engines and AWS Regions availability for Aurora global databases with Aurora MySQL and Aurora PostgreSQL.

[Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html)

### Amazon Relational Database Service

**Getting started with Amazon Relational Database Service**

Create and connect to a DB instance using Amazon RDS. You learn to create a DB instance that uses DB2, MariaDB, MySQL, Microsoft SQL Server, Oracle, or PostgreSQL.

[Explore the guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)

**Create and connect to a PostgreSQL database**

Create an environment to run your PostgreSQL database (this environment is called a DB instance), connect to the database, and delete the DB instance.

[Get started with the tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html)

**Create a web server and an Amazon RDS DB instance**

Learn how to install an Apache web server with PHP and create a MySQL database. The web server runs on an Amazon EC2 instance using Amazon Linux. The MySQL database is a MySQL DB instance.

[Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/create-mysql-db/)

### Amazon DocumentDB (with MongoDB compatibility)

**Getting started with Amazon DocumentDB (with MongoDB compatibility)**

We help you get started using Amazon DocumentDB in just four steps. This guide uses AWS CloudShell to connect and query your cluster using the MongoDB shell directly from the AWS Management Console.

[Explore the guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html)

**Setting up a document database with Amazon DocumentDB**

This tutorial helps you to get started connecting to your Amazon DocumentDB cluster from your AWS CloudShell environment with a MongoDB shell, and then run a few queries.

[Get started with the tutorial](https://aws.amazon.com/getting-started/hands-on/getting-started-amazon-documentdb-with-aws-cloud9/)

**Best practices for working with Amazon DocumentDB**

Learn best practices for working with Amazon DocumentDB, along with the basic operational guidelines when working with it.

[Explore the guide](https://docs.aws.amazon.com/documentdb/latest/developerguide/best_practices.html)

**Assessing MongoDB compatibility**

Use the Amazon DocumentDB compatibility tool to help you assess the compatibility of a MongoDB application by using the application's source code or MongoDB server profile logs.

[Use the tool](https://github.com/awslabs/amazon-documentdb-tools/tree/master/compat-tool)

### Amazon DynamoDB

**What is Amazon DynamoDB?**

This guide explains how you can use this fully managed NoSQL database service to offload the administrative burdens of operating and scaling a distributed database (including hardware provisioning, setup and configuration, replication, software patching, and cluster scaling).

[Explore the guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)

**Getting started with DynamoDB and the AWS SDKs**

We help you get started with DynamoDB and the AWS SDKs. This guide includes hands-on tutorials that show you how to run code examples in DynamoDB.

[Explore the guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStartedDynamoDB.html)

**Create and query a NoSQL table with DynamoDB**

Use these hands-on tutorials to get started with DynamoDB and the AWS SDKs. You can run the code examples on either the downloadable version of DynamoDB or the DynamoDB web service.

[Get started with the tutorials](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)

**Create a DynamoDB table**

Use the Amazon DocumentDB compatibility tool to help you assess the compatibility of a MongoDB application by using the application's source code or MongoDB server profile logs.

[Get started with the tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-1.html)

### Amazon ElastiCache

**Documentation for ElastiCache**

Explore the full set of ElastiCache documentation, including user guides as well as specific AWS CLI and API references.

[Explore the guides](https://docs.aws.amazon.com/elasticache/)

**Getting started with ElastiCache**

Learn how to create, grant access to, connect to, and delete a Valkey (cluster mode disabled) cluster using the ElastiCache console.

[Get started with the tutorial](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/GettingStarted.html)

### Amazon MemoryDB

**Getting started with Amazon MemoryDB**

We guide you through the steps to create, grant access to, connect to, and delete a MemoryDB cluster using the MemoryDB console.

[Use the guide](https://docs.aws.amazon.com/memorydb/latest/devguide/getting-started.html)

**Get started with Amazon MemoryDB for Valkey**

Get an overview of MemoryDB for Valkey, its benefits, and how you can upgrade your MemoryDB for Redis OSS database to MemoryDB for Valkey database.

[Read the blog post](https://aws.amazon.com/blogs/database/get-started-with-amazon-memorydb-for-valkey/)

**Integrating MemoryDB with Java-based Lambda**

We discuss some of the common use cases for the data store, MemoryDB, which is built to provide durability and faster reads and writes.

[Read the blog post](https://aws.amazon.com/blogs/compute/integrating-amazon-memorydb-for-redis-with-java-based-aws-lambda/)

### Amazon Keyspaces

**Getting started with Amazon Keyspaces (for Apache Cassandra)**

This guide is for those who are new to Apache Cassandra and Amazon Keyspaces (for Apache Cassandra). It walks you through installing all the programs and drivers that you need to successfully use Amazon Keyspaces.

[Explore the guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.html)

**Beginner course for using Amazon Keyspaces (for Apache Cassandra)**

Learn the benefits, typical use cases, and technical concepts of Amazon Keyspaces. You can try the service through the sample code provided or the interactive tool in the AWS Management Console.

[Take the course (requires sign-in)](https://skillbuilder.aws/learn/KHGZNGWXKV/getting-started-with-amazon-keyspaces/MXK17GET8G)

### Amazon Neptune

**Getting started with Amazon Neptune**

We help you get started using Amazon Neptune, a fully managed graph database service. This guide shows you how to create a Neptune database.

[Explore the guide](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-setup.html)

**Using knowledge graphs to build GraphRAG applications with Amazon Bedrock and Amazon Neptune**

Build GraphRAG applications using Amazon Bedrock and Amazon Neptune with LlamaIndex framework.

[Read the blog post](https://aws.amazon.com/blogs/database/using-knowledge-graphs-to-build-graphrag-applications-with-amazon-bedrock-and-amazon-neptune/)

### Amazon Timestream

**Getting started with Amazon Timestream**

We help you get started with Amazon Timestream. This guide provides instructions for setting up a fully functional sample application.

[Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started.html)

**Best practices with Amazon Timestream**

We explore best practices, including the practices that relate to data modeling, security, configuration, data ingestion, queries, client applications, and supported integrations.

[Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/best-practices.html)

**Accessing Amazon Timestream using the AWS SDKs**

Learn how to access Amazon Timestream using the AWS SDKs in the language of your choice: Java, Go, Python, Node.js, or .NET.

[Explore the guide](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started-sdks.html)

**Understanding time-series data and why it matters**

Explore the nature of time-series data, its presence across different types of industries and various use cases it enables.

[Read the blog post](https://aws.amazon.com/blogs/database/understanding-time-series-data-and-why-it-matters/)

## Resources

- **Learn**: [Hands-on tutorials](https://aws.amazon.com/getting-started/hands-on/) [Solution architect resources](https://aws.amazon.com/architecture/databases/) [Professional development courses](https://skillbuilder.aws/search?searchText=introduction-to-building-with-aws-databases) [Startup resources](https://aws.amazon.com/startups/learn/maximizing-performance-with-aws-databases) [Decision maker resources](https://aws.amazon.com/free/database/)
- **Build**: [Explore reference architecture diagrams](https://aws.amazon.com/architecture/) [Explore whitepapers](https://aws.amazon.com/whitepapers/) [Explore vetted solutions](https://aws.amazon.com/solutions/databases/)
- **Discover**: [Getting started with AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) [Using AWS Schema Conversion Tool](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html) [Selecting the right database and database migration plan for your workloads](https://aws.amazon.com/blogs/architecture/selecting-the-right-database-and-database-migration-plan-for-your-workloads/)

---
