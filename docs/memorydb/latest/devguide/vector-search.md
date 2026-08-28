---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search.html
---

# Vector search
<a name="vector-search"></a>

Vector search for MemoryDB extends the functionality of MemoryDB. Vector search can be used in conjunction with existing MemoryDB functionality. Applications that do not use vector search are unaffected by its presence. Vector search is available in all Regions that MemoryDB is available.

Vector search for simplifies your application architecture while delivering high-speed vector search. Vector search for MemoryDB is ideal for use cases where peak performance and scale are the most important selection criteria. You can use your existing MemoryDB data, or a Valkey or Redis OSS API, to build machine learning and generative AI use cases. This includes retrieval-augmented generation, anomaly detection, document retrieval, and real-time recommendations.

As of 6/26/2024, AWS MemoryDB delivers the fastest vector search performance at the highest recall rates among popular vector databases on AWS.

**Topics**
+ [Vector search overview](vector-search-overview.md)
+ [Use cases](vector-search-examples.md)
+ [Vector search features and limits](vector-search-limits.md)
+ [Create a cluster enabled for vector search](vector-search-cluster.md)
+ [Vector search commands](vector-search-commands.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
