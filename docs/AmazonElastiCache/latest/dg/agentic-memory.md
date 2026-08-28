---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory.html
---

# Using Amazon ElastiCache for Valkey for agentic memory
<a name="agentic-memory"></a>

Agentic AI applications use external tools, APIs, and multi-step reasoning to complete complex tasks. However, by default, agents don't retain memory between conversations, which limits their ability to provide personalized responses or maintain context across sessions. Amazon ElastiCache for Valkey provides the high-performance, low-latency infrastructure that agentic memory systems require to store, retrieve, and manage persistent memory for AI agents.

This topic explains how to use ElastiCache for Valkey as the storage layer for agentic memory, covering the concepts, architecture, implementation, and best practices for building memory-enabled AI agents.

**Note**
To build agent memory on ElastiCache with AI agents, visit the [Agent tools for ElastiCache](AgentTools.md) page to install the ElastiCache Skill and Valkey MCP server. They provide knowledge as well as tools to create agent memory workflows.

**Topics**
+ [Overview of agentic memory](agentic-memory-overview.md)
+ [Types of agentic memory](agentic-memory-types.md)
+ [Why ElastiCache for Valkey for agentic memory](agentic-memory-why-elasticache.md)
+ [Solution architecture](agentic-memory-architecture.md)
+ [Prerequisites](agentic-memory-prerequisites.md)
+ [Setting up ElastiCache for Valkey as a vector store for agentic memory](agentic-memory-setup.md)
+ [Performance benefits](agentic-memory-performance.md)
+ [Best practices](agentic-memory-best-practices.md)
+ [Related resources](agentic-memory-related-resources.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
