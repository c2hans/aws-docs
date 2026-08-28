---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-networkaccessanalyzer.html
---

# Network Access Analyzer events
<a name="events-ref-networkaccessanalyzer"></a>

Network Access Analyzer sends service events directly to EventBridge.

## Network Access Analyzer service events
<a name="events-ref-networkaccessanalyzer-events"></a>

Network Access Analyzer sends the following events directly to EventBridge:
+ Analysis Completed

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.networkaccessanalyzer

```
{
  "source": ["aws.networkaccessanalyzer"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.networkaccessanalyzer"],
  "detail-type": ["{{Analysis Completed}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
