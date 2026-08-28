---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-emr.html
---

# Amazon EMR events
<a name="events-ref-emr"></a>

Amazon EMR sends service events directly to EventBridge.

## Amazon EMR service events
<a name="events-ref-emr-events"></a>

Amazon EMR sends the following events directly to EventBridge:
+ EMR Auto Scaling Policy State Change
+ EMR Step Status Change
+ EMR Cluster State Change
+ EMR Instance Group State Change
+ EMR Instance Fleet State Change
+ EMR Instance Group Status Notification
+ EMR Instance Fleet Status Notification
+ EMR Configuration Error
+ EMR Application Health State Change
+ EMR Managed Scaling Action
+ EMR Instance Fleet Resize
+ EMR Instance Group Resize
+ EMR Instance Fleet Cluster Start
+ EMR Instance Group Cluster Start
+ EMR Unhealthy Node Replacement
+ EMR Instance Fleet Provisioning
+ EMR Instance Group Provisioning
+ EMR Instance Fleet Termination
+ EMR Instance Group Termination
+ EMR Instance Fleet Update

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.emr

```
{
  "source": ["aws.emr"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.emr"],
  "detail-type": ["{{EMR Auto Scaling Policy State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
