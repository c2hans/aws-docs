---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-prerequisites.html
---

# Prerequisites
<a name="agentic-memory-prerequisites"></a>

To implement agentic memory with ElastiCache for Valkey, you need:

1. An AWS account with access to Amazon Bedrock, including Amazon Bedrock AgentCore Runtime and embedding models.

1. An ElastiCache cluster running Valkey 8.2 or later. Valkey 8.2 includes support for vector similarity search. For instructions on creating a cluster, see [Creating a cluster for Valkey or Redis OSS](Clusters.Create.md).

1. An Amazon Elastic Compute Cloud instance or other compute resource within the same Amazon VPC as your ElastiCache cluster.

1. Python 3.11 or later with the following packages:

   ```
   pip install strands-agents strands-agents-tools strands-agents-builder
   pip install mem0ai "mem0ai[vector_stores]"
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
