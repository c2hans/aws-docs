---
source_url: https://docs.aws.amazon.com/whitepapers/latest/database-caching-strategies-using-redis/database-challenges.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database challenges
<a name="database-challenges"></a>

 When you’re building distributed applications that require low latency and scalability, disk-based databases can pose a number of challenges. A few common ones include the following:
+  **Slow processing queries**: There are a number of query optimization techniques and schema designs that help boost query performance. However, the data retrieval speed from disk plus the added query processing times generally put your query response times in double-digit millisecond speeds, at best. This assumes that you have a steady load and your database is performing optimally.
+  **Cost to scale**: Whether the data is distributed in a disk-based NoSQL database or a vertically-scaled relational database, scaling for extremely high reads can be costly. It also can require several database read replicas to match what a single in-memory cache node can deliver in terms of requests per second.
+  **The need to simplify data access**: Although relational databases provide an excellent means to data model relationships, they aren’t optimal for data access. There are instances where your applications may want to access the data in a particular structure or view, to simplify data retrieval and increase application performance.

 Before implementing database caching, many architects and engineers spend great effort trying to extract as much performance as they can from their databases. However, there is a limit to the performance that you can achieve with a disk-based database, and it’s counterproductive to try to solve a problem with the wrong tools. For example, a large portion of the latency of your database query is dictated by the physics of retrieving data from disk.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
