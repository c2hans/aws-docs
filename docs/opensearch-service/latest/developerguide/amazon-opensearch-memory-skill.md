---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/amazon-opensearch-memory-skill.html
---

# amazon-opensearch-memory skill

`amazon-opensearch-memory` is a skill in the Agent Toolkit for AWS that helps your AI coding agent integrate an application with Amazon OpenSearch Memory. With the skill, the agent can create a space, write conversation turns as events, and search the memories that OpenSearch Memory extracts from them. A skill is a curated package of instructions and reference material that helps an agent complete a task correctly. The agent loads the skill when your request names OpenSearch Memory, an OpenSearch Memory space, or the `aws opensearchmemory` commands.

For how the service works, see [What is Amazon OpenSearch Memory?](memory.md).

## Capabilities
<a name="opensearch-memory-skill-capabilities"></a>

The skill covers the following tasks.

### Spaces and memory strategies
<a name="opensearch-memory-skill-spaces"></a>

Create a space, add or change its memory strategies (`SEMANTIC`, `SUMMARY`, and `CUSTOM`), set event and memory retention, and delete a space.

```
Create an OpenSearch Memory space for my agent that extracts user facts and session summaries
```

### Events and memories
<a name="opensearch-memory-skill-events"></a>

Write conversation turns as events, read events back, write or update memories directly, and delete an end user's data.

```
Write this conversation turn for user-42 to my OpenSearch Memory space
```

### Search
<a name="opensearch-memory-skill-search"></a>

Search or list memories, build a search query, and filter results by time or metadata.

```
Search my OpenSearch Memory space for what user-42 said about where they live
```

### Access control and encryption
<a name="opensearch-memory-skill-security-tasks"></a>

Write IAM policies, isolate end users from each other, and use a customer managed AWS KMS key for a space.

```
What IAM policy lets a read-only agent search memories in one OpenSearch Memory space but not write to it?
```

### Troubleshooting
<a name="opensearch-memory-skill-troubleshooting"></a>

Diagnose errors such as `ResourceNotFoundException` after a space reports `ACTIVE`, `ConflictException` while a space is `UPDATING`, or `ValidationException` on a search query, and find out why memories don't appear in search results.

```
I wrote events to my OpenSearch Memory space, but searching memories returns nothing
```

## How the agent gets the skill
<a name="opensearch-memory-skill-delivery"></a>

The skill is delivered through the Agent Toolkit for AWS. You have two options:
+ **Discover it at runtime through the AWS MCP Server.** With the AWS MCP Server configured (see [Set up the AWS MCP Server](aws-mcp-server.md)), your agent finds the skill on demand using the server's `search_documentation` tool and loads it with `retrieve_skill` – no local install required.
+ **Install it with the AWS CLI.** The following command installs the skill to the AI coding agents that the Agent Toolkit for AWS detects on your system. This command requires AWS CLI version 2.35.0 or later. For more information, see [AWS CLI](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html) in the Agent Toolkit for AWS documentation.

  ```bash
  aws agent-toolkit add-skill --skill-name amazon-opensearch-memory
  ```

The source of the skill is in the [Agent Toolkit for AWS repository](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills/amazon-opensearch-memory) on GitHub.

## Using the skill with and without the AWS MCP Server
<a name="opensearch-memory-skill-with-without-mcp"></a>

The skill is designed to run with the AWS MCP Server, which provides authenticated API access and sandboxed script execution. Where the AWS MCP Server is available, the agent uses its `run_script` tool to run OpenSearch Memory operations. For setup, see [Set up the AWS MCP Server](aws-mcp-server.md).

The skill also works without the AWS MCP Server. Every operation in the skill runs with the AWS CLI alone (for example, `aws opensearchmemory create-space` or `aws opensearchmemory search-memories`). The skill includes instructions that work with both approaches.

## Prerequisites
<a name="opensearch-memory-skill-prerequisites"></a>
+ An AI coding agent that supports the Agent Toolkit for AWS (such as Claude Code or Codex).
+ AWS credentials configured with permission for the OpenSearch Memory operations you intend to run. See [Identity and Access Management for Amazon OpenSearch Memory](security-iam-memory.md).
+ An AWS Region where OpenSearch Memory is available. See [Supported AWS Regions](memory-how-it-works.md#memory-regions).
+ To run the skill without the AWS MCP Server, AWS CLI version 2.40.4 or later, the first version that includes the `aws opensearchmemory` commands.
+ For the recommended setup, the AWS MCP Server. See [Set up the AWS MCP Server](aws-mcp-server.md).

## Security considerations
<a name="opensearch-memory-skill-security"></a>

When the agent runs OpenSearch Memory operations, it acts with the credentials you provide. Anything those credentials are authorized to do, the agent can trigger on your behalf.
+ Use least-privilege credentials. Grant only the `osm:` actions the agent needs, scoped to specific space ARNs. For a read-only agent, grant only read actions such as `osm:SearchMemories`, `osm:GetMemory`, and `osm:ListMemories`.
+ Isolate end users. Use one actor ID per end user, and restrict principals with the `osm:actorId` condition key. See [Identity and Access Management for Amazon OpenSearch Memory](security-iam-memory.md).
+ Require explicit confirmation before the agent deletes a space, a memory, or an event. Deletions are permanent.
+ Don't put secrets or credentials in events, memories, or metadata.
+ Review tool output. MCP tool responses, including the events and memories the agent reads, are returned to the language model as context. Avoid running operations against spaces that contain sensitive data you don't want exposed to your model provider.
