---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-delete.html
---

# Delete session summaries
<a name="agents-memory-delete"></a>

To delete session summaries, send a [DeleteAgentMemory](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteAgentMemory.html) request (see link for request and response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt).

The following fields are required:

| Field | Short description |
| --- | --- |
| agentId | The identifier of the agent. |
| agentAliasId | The identifier of the agent alias. |

The following field is optional.

| Field | Short description |
| --- | --- |
| memoryId | The identifier of the memory that has the session summaries |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
