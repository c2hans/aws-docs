---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/network-type-best-practices.html
---

# IPv6 client examples for Valkey, Memcached, and Redis OSS
<a name="network-type-best-practices"></a>

ElastiCache is compatible with Valkey, Memcached, and Redis OSS. This means that clients which support IPv6 connections should be able to connect to IPv6 enabled ElastiCache for Memcached clusters. There are some caveats worth noting when interacting with IPv6 enabled resources.

You can view the [Best practices for Valkey and Redis clients](https://aws.amazon.com/blogs/database/best-practices-redis-clients-and-amazon-elasticache-for-redis/) blog post on the AWS Database Blog for recommendations on configuring Valkey and Redis OSS clients for ElastiCache resources.

Following are best practices for interacting with IPv6 enabled ElastiCache resources with commonly used open-source client libraries.

## Validated clients with Valkey and Redis OSS
<a name="network-type-validated-clients-redis"></a>

ElastiCache is compatible with Valkey and open-source Redis OSS. This means that Valkey and open source Redis OSS clients that support IPv6 connections should be able to connect to IPv6 enabled ElastiCache for Redis OSS clusters. In addition, several of the most popular Python and Java clients have been specifically tested and validated to work with all supported network type configurations (IPv4 only, IPv6 only, and Dual Stack)

The following clients have specifically been validated to work with all supported network type configurations for Valkey and Redis OSS.

Validated Clients:
+ [Redis Py ()](https://github.com/redis/redis-py) – [4.1.2](https://github.com/redis/redis-py/tree/v4.1.2)
+ [Lettuce](https://lettuce.io/) – [Version: 6.1.6.RELEASE](https://github.com/lettuce-io/lettuce-core/tree/6.1.6.RELEASE)
+ [Jedis](https://github.com/redis/jedis) – [Version: 3.6.0](https://github.com/redis/jedis/tree/jedis-3.6.0)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
