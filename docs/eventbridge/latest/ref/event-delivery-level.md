---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/event-delivery-level.html
---

# Delivery level for AWS service events
<a name="event-delivery-level"></a>

Each AWS service that generates events sends them to EventBridge as either *best effort* or *durable* delivery attempts.
+ *Best effort delivery* means that the service attempts to send all events to EventBridge, but in some rare cases an event might not be delivered.
+ *Durable delivery* means the service will successfully attempt to deliver events to EventBridge at least once.

Once a valid event is delivered to EventBridge, EventBridge matches it against rules and then follows the retry policy and any dead-letter queue specified for the event target(s). For more information, see [Retrying event delivery](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html) in the *EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
