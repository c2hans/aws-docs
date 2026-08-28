---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-wordpress/database-caching.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Database caching
<a name="database-caching"></a>

 Database caching can significantly reduce latency and increase throughput for read-heavy application workloads like WordPress. Application performance is improved by storing frequently accessed pieces of data in memory for low-latency access (for example, the results of I/O-intensive database queries). When a large percentage of the queries are served from the cache, the number of queries that need to hit the database is reduced, resulting in a lower cost associated with running the database.

 Although WordPress has limited caching capabilities out-of-the-box, a variety of plugins support integration with [Memcached](https://memcached.org/), a widely adopted memory object caching system. The W3 Total Cache plugin is a good example.

 In the simplest scenarios, you install Memcached on your web server and capture the result as a new snapshot. In this case, you are responsible for the administrative tasks associated with running a cache.

 Another option is to take advantage of a managed service such as [Amazon ElastiCache](https://aws.amazon.com/elasticache/) and avoid that operational burden. ElastiCache makes it easy to deploy, operate, and scale a distributed in-memory cache in the cloud. You can find information about how to connect to your ElastiCache cluster nodes in the [Amazon ElastiCache documentation](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/WhatIs.html).

 If you are using Lightsail and wish to access an ElastiCache cluster in your AWS account privately, you can do so by using VPC peering. For instructions to enable VPC peering, refer to [Set up Amazon VPC peering to work with AWS resources outside of Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-set-up-vpc-peering-with-aws-resources).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
