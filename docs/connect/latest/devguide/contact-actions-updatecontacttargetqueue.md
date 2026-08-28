---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/contact-actions-updatecontacttargetqueue.html
---

# UpdateContactTargetQueue
<a name="contact-actions-updatecontacttargetqueue"></a>

Sets the contact's TargetQueue. This is the queue is used by all other instructions that check a queue implicitly, and for TransferContactToQueue.

## Parameter object
<a name="updatecontacttargetqueue-parameter"></a>

```
{
  "QueueId": [Optional] A queue ID or queue ARN. If AgentId is specified, this may not be specified. This must be either defined fully statically or as a single valid JSONPath identifier.
  "AgentId": [Optional] An agent ID or agent ARN, representing an agent queue. If QueueId is specified, this may not be specified. This must be either defined fully statically or as a single valid JSONPath identifier.
}
```

## Results and conditions
<a name="updatecontacttargetqueue-results"></a>

None.

## Errors
<a name="updatecontacttargetqueue-errors"></a>
+ NoMatchingError - if no other Error matches.

## Restrictions
<a name="updatecontacttargetqueue-restrictions"></a>

This action is supported only in inbound contact flows and transfer flows. It is not supported in whisper flows, hold flows, or customer queue flows.

## Corresponding block in the UI
<a name="updatecontacttargetqueue-ui"></a>

[Set working queue](https://docs.aws.amazon.com/connect/latest/adminguide/set-working-queue.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
