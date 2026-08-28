---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-delete-event.html
---

# Delete an event
<a name="short-term-delete-event"></a>

The [DeleteEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteEvent.html) operation removes individual events from your AgentCore Memory. This operation helps maintain data privacy and relevance by letting you selectively remove specific events from a session while preserving the broader context and relationship structure within your application’s memory.

**Note**
These are manual deletion operations, and do not overlap with automatic deletion of events based on the `eventExpiryDuration` parameter set at the time of [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html) operation. Also deleting an event doesn’t remove the structured information derived out of it from the long term memory. For more information, see [DeleteMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteMemoryRecord.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
