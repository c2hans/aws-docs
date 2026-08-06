---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/understanding-amazon-nosql-data-stores.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Understanding Amazon NoSQL data stores
<a name="understanding-amazon-nosql-data-stores"></a>

 AWS provides the broadest selection of managed NoSQL databases, allowing you to save, grow, and innovate faster. With Amazon NoSQL databases, you get high performance, enterprise-grade security, automatic, and instant scalability. The following table lists some of the AWS managed NoSQL database services offered, and their key characteristics:

 *Table 1 — AWS database service comparison *

|  AWS database service  |  Use cases  |  Strengths  |  Security  |  Performance  |  Cross-Region resiliency  |
| --- | --- | --- | --- | --- | --- |
| Amazon DocumentDB (with MongoDB compatibility)**\***+  Mid TB range <br />+  Data format: JSCO, BSON, XML <br />+  NoSQL type: document <br />+  Consistency: strong/eventual  | User profile/personalization, catalogs, mobile, and content management, retail and marketing (for example, tracking customers who purchase similar items) | Flexible schema and indexing, ad hoc queries on any attributes, including nested attributes | Capability to enable data encryption at rest and in transit | Millions of requests per second with millisecond latency | DocumentDB Global clusters |
|  Amazon DynamoDB**\*** +   High TB range  <br />+   Data format: JSON, BSON, or XML  <br />+   NoSQL type: key-value, document  <br />+   Consistency: strong/eventual   |  +   User preferences  <br />+   Session management  <br />+   Shopping cart  <br />+   Product catalog  <br />+   High-traffic web apps  <br />+   Near real-time bidding    |  +   Performance at scale  <br />+   Serverless  <br />+   Simple data model    | Encrypts all data at rest by default, row/column level security | Single digit millisecond at any scale, In-memory acceleration with DynamoDB (DAX) for low latency access to eventually consistent data  | Global tables  |
| Amazon Keyspaces (for Apache Cassandra)+   Data format: JSON  <br />+   NoSQL type: wide column  <br />+   Consistency: one, local\_one, local-quorum   |  High scalable apps for: +   Equipment maintenance  <br />+   Fleet management  <br />+   Route optimization   |  +   Extreme write speeds with relatively less velocity reads  <br />+  Being serverless, allocates storage and read/write throughput directly to tables   |  +  Tables are encrypted by default <br />+  Capability to enable data encryption at rest and in transit   |  Single digit millisecond response at any scale  | [Multi-Region Replication](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication.html) |
|  Amazon Neptune**\*** +   Mid TB range  <br />+   Data format: Germalin, RDF, open Cypher  <br />+   NoSQL type: graph  <br />+   Consistency: immediate consistency   |  +   Recommendations  <br />+   Social patterns  <br />+   relationship traversal  <br />+   Fraud detection  <br />+   Risk assessment    |  +   Highly connected data is locally indexed and purpose-built to answer questions about relationships  <br />+   Optimized for efficient storage and retrieval    | Capability to enable data encryption at rest and in transit |  High throughput, low latency  |  +   Cross-Region snapshot  <br />+   Neptune streams to replicate data between cross-Region clusters    |
|  Amazon Timestream**\*** +   NoSQL type: TimeSeries  <br />+   Consistency: eventual   |  +   Server metrics  <br />+   Application performance monitoring  <br />+   Network data  <br />+   IoT apps  <br />+   Sensor data  <br />+   Events  <br />+   Clicks  <br />+   Financial forecasting  <br />+   Many other types of analytics data    |  Analytics over time series data  |  Encrypts all data by default  | Capable of ingesting trillions of events daily. The adaptive SQL query engine provides rapid point-in-time queries with its in-memory store, and fast analytical queries through its magnetic store |  Cross-Region backup |
|  Amazon ElastiCache (Memcached)+   Low TB range  <br />+   NoSQL type: in-memory, key-value   |  +   Caching repeat requests  <br />+   Sticky sessions (to store session state)    |  +   Simple caching model  <br />+   Multi-threaded performance    | Capability to enable data encryption at rest and in transit |  Sub-millisecond response time  |  N/A |
|  Amazon ElastiCache (Redis OSS) +   Low TB range  <br />+   NoSQL type: in-memory, key-value    |  +   Gaming leaderboards  <br />+   Geospatial applications    |  +   Complex data structures  <br />+   Sorting and ranking  <br />+   Pub/sub messaging  <br />+   Geospatial capabilities    | Capability to enable data encryption at rest and in transit |  Sub-millisecond response time  |  Global datastores  |
|  Amazon MemoryDB +   NoSQL type: in-memory, database  <br />+   Consistency: strong/eventual   |  +   High concurrency  <br />+   Streaming media  <br />+   Data feeds    |  +   Durable database  <br />+   Complex data structures    | Capability to enable data encryption at rest and in transit |  Microsecond read and single-digit millisecond write latency  |  Cross-Region snapshot |

**\*** ACID compliant

**Topics**
+ [Amazon DynamoDB](amazon-dynamodb.md)
+ [Amazon Keyspaces (for Apache Cassandra)](amazon-keyspaces.md)
+ [Amazon Neptune](amazon-neptune.md)
+ [Amazon Timestream](amazon-timestream.md)
+ [Amazon ElastiCache](amazon-elasticache.md)
+ [Amazon DocumentDB (with MongoDB compatibility)](amazon-documentdb.md)
+ [Amazon MemoryDB](amazon-memorydb-for-redis.md)
