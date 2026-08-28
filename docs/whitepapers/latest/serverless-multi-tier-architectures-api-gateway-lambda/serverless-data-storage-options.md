---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/serverless-data-storage-options.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Serverless data storage options
<a name="serverless-data-storage-options"></a>

 [Amazon S3](https://aws.amazon.com/s3) is an object storage service that offers industry-leading scalability, data availability, security, and performance.

 [Amazon Aurora](https://aws.amazon.com/rds/aurora/) is a MySQL-compatible and PostgreSQL-compatible relational database built for the cloud, that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open-source databases. Aurora offers both serverless and traditional usage models.

 [Amazon DynamoDB](https://aws.amazon.com/dynamodb) is a key-value and document database that delivers single-digit millisecond performance at any scale. It is a fully managed, serverless, multi-region, multi-active, durable database with built-in security, backup and restore, and in-memory caching for internet-scale applications.

 [Amazon Timestream](https://aws.amazon.com/timestream) is a fast, scalable, fully managed time series database service for IoT and operational applications that makes it simple to store and analyze trillions of events per day at 1/10th the cost of relational databases. Driven by the rise of IoT devices, IT systems, and smart industrial machines, time-series data—data that measures how things change over time—is one of the fastest growing data types.

 [Amazon Quantum Ledger Database](https://aws.amazon.com/qldb) (Amazon QLDB) is a fully managed ledger database that provides a transparent, immutable, and cryptographically verifiable transaction log owned by a central trusted authority. Amazon QLDB tracks each and every application data change and maintains a complete and verifiable history of changes over time.

 [Amazon Keyspaces](https://aws.amazon.com/keyspaces) (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra–compatible database service. With Amazon Keyspaces, you can run your Cassandra workloads on AWS using the same Cassandra application code and developer tools that you use today. You don’t have to provision, patch, or manage servers, and you don’t have to install, maintain, or operate software. Amazon Keyspaces is serverless, so you pay for only the resources you use and the service can automatically scale tables up and down in response to application traffic.

[Amazon Elastic File System ](https://aws.amazon.com/efs) (Amazon EFS) provides a simple, serverless, set-and-forget, elastic file system that lets you share file data without provisioning or managing storage. It can be used with AWS Cloud services and on-premises resources, and is built to scale on demand to petabytes without disrupting applications. With Amazon EFS, you can grow and shrink your file systems automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth. Amazon EFS can be mounted with Lambda function which makes it a viable file storage option for APIs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
