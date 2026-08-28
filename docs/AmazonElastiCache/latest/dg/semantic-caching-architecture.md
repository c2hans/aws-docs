---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/semantic-caching-architecture.html
---

# Solution architecture
<a name="semantic-caching-architecture"></a>

The following architecture implements a read-through semantic cache for an agent on Amazon Bedrock AgentCore. A request follows one of two paths:
+ **Cache hit** – If ElastiCache finds a prior query above the configured similarity threshold, AgentCore returns the cached answer immediately. This path invokes only the embedding model and does not require LLM inference. This path has millisecond-level end-to-end latency and does not incur LLM inference cost.
+ **Cache miss** – If no similar prior query is found, AgentCore invokes the LLM to generate a new answer and returns it to the user. The application then caches the prompt's embedding and answer in ElastiCache so that future similar prompts can be served from the cache.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
