---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/decision-making.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Decision making
<a name="decision-making"></a>

 This section outlines a decision framework you can use to help you determine which AWS-managed NoSQL database service, or combination of database services would fit your workload needs best.

 While there is no simple formula you can follow that is comprehensive enough to apply generally, there are a few important questions related to your application that should be answered during the selection process:

**What type of data is your application planning to persist (such as JSON structures, telemetry data, image files, geospatial data)?**

 Different databases allow you to access stored data differently. If you plan to store unstructured data such as images or encoded payloads, you need a data store that can store and retrieve the entire unstructured binary payload fast, but may need a rich set of data access features to introspect the unstructured data.

 Conversely, a catalog system needs a richer feature set to access data based on patterns, but also allow for flexibility to expand the set of attributes collected for each item in the catalog. These capabilities may be more important than the absolute fastest way to retrieve data access.

 **What performance requirements and service-level commitments have you made to your end users (for example, a service level agreement that guarantees microsecond or millisecond-level response latency for queries)?**

 If your workload requires extremely high read performance with a response time measured in microseconds rather than single-digit milliseconds, then you may consider using in-memory [caching](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Strategies.html) solutions alongside your database, or a database that supports in-memory data access.

 Also consider how predictable your performance needs to be. A database such as Amazon DynamoDB can deliver consistent, predictable response latencies to reads and writes, but it does so because it supports a small number of query patterns that have a known cost. It’s a great fit for point queries accessing one or a very small number of records at high frequency.

 If your data access patterns require accessing a variable or unpredictable number of records or volume of data, your performance will also have more variability. Consider also that modern architectures are implemented using decoupled microservices, each with different date access requirements, compounding the end-to-end latency or performance of the end user request.

 **What are your resiliency requirements?**

 Workloads with high availability requirements (such as mission-critical applications that can’t tolerate any downtime) can span multiple Regions to provide further resiliency in case a specific AWS region becomes unreachable. For example, you can use [DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/) to deploy globally across supported Regions and read or write to the local copies of the tables concurrently. Amazon DocumentDB also supports multiple Regions through [Amazon DocumentDB global clusters](https://docs.aws.amazon.com/documentdb/latest/developerguide/global-clusters.html), but you can only write in the primary Region cluster.

 After you address these questions, you can use the following decision tree for further direction on how to narrow down your choices. The decision tree covers two scenarios:

1.  If you’re already using a NoSQL database on premises and would like to consider migrating to a fully managed scalable, highly available AWS NoSQL database service, start your review of our decision tree at Step 1.

1.  If you want to modernize your application and are considering a NoSQL database, you can use the decision tree to choose the most appropriate AWS-managed NoSQL database service for your use case based on your requirements by starting at Step 2, You can start eith the data model that is appropriate for your use case.

![Decision tree flowchart for selecting AWS database services based on data model and use case.](http://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/images/decision-tree2.png)
