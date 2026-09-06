---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/storage-solutions-for-.net-applications-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Storage Solutions for .NET Applications on AWS
<a name="storage-solutions-for-.net-applications-on-aws"></a>

Most applications need various storage requirements, such as relational or NoSQL databases, flat files, object storage, block storage, or various types of in-memory cache tiers. .NET applications are no exception and depending on their functionalities, may require one or more of these solutions.

AWS includes a number of purpose-built relational database services, such as [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), [Amazon Aurora](https://aws.amazon.com/rds/aurora/), and [Amazon Redshift](https://aws.amazon.com/redshift/), the fastest growing cloud data warehouse service. Amazon RDS supports popular open-source engines (MySQL, PostgreSQL, and MariaDB), as well as commercial engines (Microsoft SQL Server and Oracle). You can run these or any other engine on Amazon EC2 instances.

There are a number of specialized databases, including [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for key-value and document storage, [Amazon Neptune](https://aws.amazon.com/neptune/) for graph data, [Amazon Quantum Ledger Database](https://aws.amazon.com/qldb/), and [Amazon Managed Blockchain](https://aws.amazon.com/managed-blockchain/).

.NET applications can use [Amazon S3](https://aws.amazon.com/s3/) for object storage, and [Amazon EFS](https://aws.amazon.com/efs/) for Linux-based shared file systems, or [Amazon FSx for Windows](https://aws.amazon.com/fsx/windows/) file shares.

Finally, [Amazon Elastic Block Storage](https://aws.amazon.com/ebs/) is an easy to use, high performance block storage service designed for use with Amazon EC2 for both throughput and transaction intensive workloads at any scale.

You can build extremely high-performance .NET applications using elasticity and flexibility of managed AWS services for in-memory caching, such as [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/), [Redis](https://redis.io/), [Memcached](https://memcached.org/), or [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/).
