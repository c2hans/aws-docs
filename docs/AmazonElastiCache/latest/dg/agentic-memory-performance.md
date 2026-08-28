---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-performance.html
---

# Performance benefits
<a name="agentic-memory-performance"></a>

The following table summarizes the performance improvements observed in testing with a memory-enabled agent versus a stateless agent:

| Metric | Without memory | With memory | Improvement |
| --- | --- | --- | --- |
| Tool calls per request | 3 | 0 (memory retrieval) | Eliminated redundant tool calls |
| Token usage | \~70,000 | \~6,300 | 12x reduction |
| Response time | 9.25 seconds | 2 seconds | 3x\+ faster |
| Memory lookup latency | N/A | Sub-millisecond | Valkey in-memory performance |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
