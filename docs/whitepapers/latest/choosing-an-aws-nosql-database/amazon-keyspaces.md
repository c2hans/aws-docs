---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/amazon-keyspaces.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Keyspaces (for Apache Cassandra)
<a name="amazon-keyspaces"></a>

 [Amazon Keyspaces (for Apache Cassandra)](https://aws.amazon.com/keyspaces/) (Amazon Keyspaces) is a fully managed, Apache Cassandra-compatible database service. Some key features of Amazon Keyspaces include:
+  **Apache Cassandra compatibility** ‑— Full compatibility with Cassandra, allowing you to use your existing Cassandra applications and tools with minimal changes.
+  **Scalability** — Designed to handle millions of requests per second and terabytes of data, making it suitable for high-scale applications.
+ **Serverless** — Instead of deploying, managing, and maintaining storage and compute resources for your workload through nodes in a cluster, Amazon Keyspaces allocates storage and read/write throughput resources directly to tables.
+  **Global distribution** — Supports global distribution of data, allowing you to store and access data from multiple Regions, reducing latency and improving application performance.
+  **Monitoring and management** — Provides an easy-to-use, web-based console for monitoring and managing your database, as well as integration with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for metrics and alerts.
+  **Integration with other AWS services** — Integration with other AWS services such as Amazon S3, [Amazon Redshift](https://aws.amazon.com/pm/redshift), and [Amazon EMR](https://aws.amazon.com/emr/), making it easy to build data-driven applications.
+  **Highly available and secure** — Data is replicated automatically across multiple AWS Availability Zones using a replication factor of three. Amazon Keyspaces encrypts all customer data at rest by default, and is integrated with AWS IAM to help you manage access to your tables and data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
