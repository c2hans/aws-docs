---
source_url: https://docs.aws.amazon.com/whitepapers/latest/choosing-an-aws-nosql-database/considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Considerations
<a name="considerations"></a>

## Best practices and limitations
<a name="best-practices-and-limitations"></a>
+  For implementation best practices and limitations, refer to the AWS documentation for the respective [database service](https://docs.aws.amazon.com/index.html?nc2=h_ql_doc_do_v).
+  If your use cases use relatively static schemas, perform complex table lookups, require accessing data across multiple keys and might experience high service throughputs it might be a better fit for [Amazon RDS](https://aws.amazon.com/pm/rds/?p=ft&c=db&z=3) offerings.

## Some customer journeys and lessons learned
<a name="some-customer-journeys-and-lessons-learned"></a>
+  [Amazon DynamoDB on Production: FinBox’s Compilation of Lessons Learned in a Year](https://aws.amazon.com/blogs/startups/what-finbox-learned-using-dynamodb/)
+  Refer to this [case study](https://aws.amazon.com/solutions/case-studies/mcafee-dynamodb-case-study/) to learn how McAfee’s use case of migrating from Microsoft SQL server to DynamoDB to power their next generation messaging platform to drive ecommerce business
+  Watch this [video](https://aws.amazon.com/documentdb/customers/fulfillment-by-amazon/) on why Amazon Fulfillment choose Amazon DocumentDB to power their inventory authority platform (IAP), considerations for performance and scale, and some learnings from their experience
+  Watch this [video](https://aws.amazon.com/documentdb/customers/finra/) to hear about [FINRA](https://www.finra.org/#/)’s story on how they modernized their data collection platform used by FINRA customers from a relational database using XML to Amazon DocumentDB.
+  [Idea to product: PricewaterhouseCoopers launches Check-In within three months on Amazon Keyspaces](https://aws.amazon.com/blogs/database/idea-to-product-pwc-launches-check-in-within-three-months-on-amazon-keyspaces/)
+  Watch this [video](https://www.youtube.com/watch?v=QEKDpToureQ) to learn about the key features of ElastiCache (Redis OSS) and dive deep into how Groupon uses ElastiCache for deal curation.
+  [Blog post](https://aws.amazon.com/blogs/database/how-near-reduced-latency-by-four-times-and-achieved-99-9-uptime-by-migrating-to-amazon-elasticache/) on how [Near](https://near.com/) was able to reduce latency by four times and achieve 99.9% uptime of its critical RTB platform applications by moving to ElastiCache.
+  [LexisNexis](https://www.lexisnexis.com/en-us/gateway.page) presentation on [using graph to store relationships between legal documents](https://youtu.be/9ZXxFKEvMgs) using [Amazon Neptune](https://aws.amazon.com/neptune/).
+  [Cox Automotive](https://www.coxautoinc.com/) presentation on [using graph to store relationships between user identities on their web platforms](https://www.youtube.com/watch?v=I7_b1xkQ7Dc) to power marketing and advertising.

## References
<a name="references"></a>
+  [Scale and performance characteristics of Timestream](https://aws.amazon.com/blogs/database/deriving-real-time-insights-over-petabytes-of-time-series-data-with-amazon-timestream/) – Deriving near real-time insights over petabytes of time series data with Amazon Timestream.
+  This [blog post](https://aws.amazon.com/blogs/database/ramping-up-on-amazon-documentdb-with-mongodb-compatibility/) provides you with a quick summary and set of resources for common topics so you can quickly ramp up on Amazon DocumentDB.
+  This [blog post](https://aws.amazon.com/blogs/database/improved-performance-for-lightweight-transactions-with-amazon-keyspaces/) provides improved performance characteristics of Amazon Keyspaces, lightweight transactions API, advanced design patterns, and operational best practices.
+  AWS Online Tech Talks: [ElasticCache](https://www.youtube.com/watch?v=OeCzNhsV1OY) best practices
+  [Getting started](https://aws.amazon.com/blogs/database/graph-your-aws-resources-with-amazon-neptune/) with Amazon Neptune by creating a graph of all of your AWS resources.
+  [How to migrate an application](https://aws.amazon.com/blogs/database/migrate-an-application-from-using-gridfs-to-using-amazon-s3-and-amazon-documentdb-with-mongodb-compatibility/) from using [GridFS](https://www.mongodb.com/docs/manual/core/gridfs/) to using Amazon S3 and Amazon DocumentDB.
+  Graph data model lets you traverse through relationships without requiring joins and indexes. For more information, refer to the ["How Do I Know I Need an Amazon Neptune Graph Database?”](https://www.youtube.com/watch?v=nNZcl_cVzhE) video.
+  Graph data model lets you traverse through relationships without requiring joins and indexes. For more information, refer to ["How Do I Know I Need an Amazon Neptune Graph Database?”](https://www.youtube.com/watch?v=nNZcl_cVzhE).
+  Complex data models (such as arrays, nested fields, and deep relationships) let you consider a wider range of application needs. For more information, refer to the “[When to use DocumentDB vs DynamoDB](https://aws.amazon.com/documentdb/resources/video-documentdb-twitch/)” video.
+  DynamoDB provides extreme scale for certain data access patterns. For more information, refer to “[How to determine if Amazon DynamoDB is appropriate for your needs](https://aws.amazon.com/blogs/database/how-to-determine-if-amazon-dynamodb-is-appropriate-for-your-needs-and-then-plan-your-migration/)”.
+  Refer to this [tech talk](https://www.youtube.com/watch?v=PK-LLTn2hVY) to learn about DocumentDB use cases, and how Amazon DocumentDB cluster architecture provides better performance, scalability, and availability.
+  Amazon MemoryDB is a durable, in-memory database for workloads that require an ultra-fast Redis-compatible primary database. If you require sub-millisecond performance and need to add persistence and durability, consider using MemoryDB rather than in-memory cache for Redis. Refer to this [*tech talk*](https://www.youtube.com/watch?v=Jbq_XZMZEKY) to learn about Amazon MemoryDB.

### Developer references
<a name="developer-references"></a>
+  [Why purpose-built database?](https://aws.amazon.com/getting-started/hands-on/purpose-built-databases/why-purpose-built-databases/) This hands-on tutorial will help you get an idea of how AWS NoSQL databases can help run your specific workloads.

### Training and guidance
<a name="training-and-guidance"></a>
+  To ensure that development teams were comfortable with transitioning to Amazon, it essential to train the teams on AWS NoSQL databases and cloud-based design patterns (tech talks, [workshops](https://workshops.aws/), and [Immersion Days](https://immersionday.com/).)
