---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/BestPractices.Clients.Redis.ServerTimeout.html
---

# Configure a server-side idle timeout (Valkey and Redis OSS)
<a name="BestPractices.Clients.Redis.ServerTimeout"></a>

We have observed cases when a customer's application has a high number of idle clients connected, but isn't actively sending commands. In such scenarios, you can exhaust all 65,000 connections with a high number of idle clients. To avoid such scenarios, configure the timeout setting appropriately on the server via [Valkey and Redis OSS parameters](ParameterGroups.Engine.md#ParameterGroups.Redis). This ensures that the server actively disconnects idle clients to avoid an increase in the number of connections. This setting is not available on serverless caches.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
