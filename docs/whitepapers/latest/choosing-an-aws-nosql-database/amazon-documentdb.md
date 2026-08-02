---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/amazon-documentdb.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon DocumentDB (with MongoDB compatibility)
<a name="amazon-documentdb"></a>

 [Amazon DocumentDB (with MongoDB compatibility)](https://aws.amazon.com/documentdb/) (Amazon DocumentDB) is a fully managed, scalable, and highly available document database service. It is designed to be compatible with the [MongoDB](https://www.mongodb.com/) API, allowing you to use existing MongoDB applications and tools with Amazon DocumentDB.

 DocumentDB supports a range of use cases, such as content management systems, e-commerce applications, and mobile backends. It allows you to store and retrieve JSON-like documents, with support for complex queries, indexing, and aggregation. It also supports transactions, allowing you to group multiple write operations into a single atomic unit of work.

 Some of the key features of Amazon DocumentDB include:
+  **Compatibility** — DocumentDB is compatible with existing MongoDB drivers and tools, and applications can be used with DocumentDB with little or no change.
+  **Scalability** — [DocumentDB Elastic Clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-using-elastic-clusters.html) scale within minutes to handle millions of reads and writes with petabytes of storage capacity, helping you cost-effectively meet the needs of your most demanding document workloads.
+  **Flexibility** — Supports a flexible data model that allows you to store and retrieve JSON-like documents with varying structure and complexity. This makes it well-suited for a wide range of use cases, such as content management, user profiles, product catalogs, and more.
+  **Durability** — Designed to provide high durability and availability for your data. It provides automatic backup and recovery, point-in-time recovery, and data replication across multiple Availability Zones for high availability and disaster recovery (DR). DocumentDB automatically backs up your data and transaction logs to Amazon S3, which is designed for 99.999999999% durability. This helps ensure that your data is protected against data loss or corruption, even in the event of a disaster or outage.
+  **Global clusters** — [DocumentDB global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters.html) provides disaster recovery from Region-wide outages and enables low-latency global reads.
+  **Integration with other AWS services** — You can integrate with [AWS Glue](https://aws.amazon.com/glue/) to import and export data from and to DocumentDB to other AWS services such as [Amazon S3](https://aws.amazon.com/s3/), [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/).
