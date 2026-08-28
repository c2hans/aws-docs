---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-datasync-discovery.html
---

# AWS DataSync Discovery events
<a name="events-ref-datasync-discovery"></a>

DataSync Discovery sends service events directly to EventBridge.

## DataSync Discovery service events
<a name="events-ref-datasync-discovery-events"></a>

DataSync Discovery sends the following events directly to EventBridge:
+ Discovery Job Expiration Soon
+ Discovery Job State Change
+ Storage System Connectivity Status Change

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.datasync-discovery

```
{
  "source": ["aws.datasync-discovery"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.datasync-discovery"],
  "detail-type": ["{{Discovery Job Expiration Soon}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
