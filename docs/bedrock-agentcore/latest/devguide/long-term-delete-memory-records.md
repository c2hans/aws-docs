---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-delete-memory-records.html
---

# Delete memory records
<a name="long-term-delete-memory-records"></a>

The [DeleteMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteMemoryRecord.html) API removes individual memory records from your AgentCore Memory, giving you control over what information persists in your application’s memory. This API helps maintain data hygiene by letting selective removal of outdated, sensitive, or irrelevant information while preserving the rest of your memory context.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
