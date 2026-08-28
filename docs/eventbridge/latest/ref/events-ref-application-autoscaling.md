---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-application-autoscaling.html
---

# Application Auto Scaling events
<a name="events-ref-application-autoscaling"></a>

Application Auto Scaling sends service events directly to EventBridge.

## Application Auto Scaling service events
<a name="events-ref-application-autoscaling-events"></a>

Application Auto Scaling sends the following events directly to EventBridge:
+ Application Auto Scaling Scaling Activity State Change

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.application-autoscaling

```
{
  "source": ["aws.application-autoscaling"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.application-autoscaling"],
  "detail-type": ["{{Application Auto Scaling Scaling Activity State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
