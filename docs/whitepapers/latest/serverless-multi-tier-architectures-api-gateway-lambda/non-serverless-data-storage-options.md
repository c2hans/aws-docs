---
source_url: https://docs.aws.amazon.com/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/non-serverless-data-storage-options.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Non-serverless data storage options
<a name="non-serverless-data-storage-options"></a>

 [Amazon Relational Database Service](https://aws.amazon.com/rds) (Amazon RDS) is a managed web service that makes it easier to set up, operate, and scale a relational database using any of the available engines (Amazon Aurora, PostgreSQL, MySQL, MariaDB, Oracle, and Microsoft SQL Server) and running on several different database instance types that are optimized for memory, performance, or I/O.

 [Amazon Redshift](https://aws.amazon.com/redshift) is a fully managed, petabyte-scale data warehouse service in the cloud.

 [Amazon ElastiCache](https://aws.amazon.com/elasticache) is a fully managed deployment of Redis or Memcached. Seamlessly deploy, run, and scale popular open source compatible in-memory data stores.

 [Amazon Neptune](https://aws.amazon.com/neptune) is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. Neptune supports popular graph models - property graphs and W3C Resource Description Framework (RDF) - and their respective query languages, enabling you to easily build queries that efficiently navigate highly connected datasets.

 [Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads.

 Finally, you can also use data stores running independently on Amazon EC2 as the data tier of a multi-tier application

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
