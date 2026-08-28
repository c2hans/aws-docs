---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/short-term-get-event.html
---

# Get an event
<a name="short-term-get-event"></a>

The [GetEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetEvent.html) API retrieves a specific raw event by its identifier from short-term memory in AgentCore Memory. This API requires you to specify the `memoryId` , `actorId` , `sessionId` , and `eventId` as path parameters in the request URL.

```
import boto3

data_client = boto3.client('bedrock-agentcore')

response = data_client.get_event(
    memoryId="your-memory-id",
    actorId="your-actor-id",
    sessionId="your-session-id",
    eventId="your-event-id"
)

event = response['event']
print(f"Event ID: {event['eventId']}")
print(f"Timestamp: {event['eventTimestamp']}")
print(f"Payload: {event['payload']}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
