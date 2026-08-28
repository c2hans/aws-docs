---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-social-messaging.html
---

# AWS End User Messaging Social events
<a name="events-ref-social-messaging"></a>

End User Messaging Social sends service events directly to EventBridge.

## End User Messaging Social service events
<a name="events-ref-social-messaging-events"></a>

End User Messaging Social sends the following events directly to EventBridge:
+ WhatsApp Message Sent
+ WhatsApp Message Delivered
+ WhatsApp Message Read
+ WhatsApp Message Failed
+ WhatsApp Message Undeliverable
+ WhatsApp Message Received
+ WhatsApp Unknown Notification Received
+ WhatsApp Message Handover Succeeded
+ WhatsApp Message Handover Failed

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.social-messaging

```
{
  "source": ["aws.social-messaging"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.social-messaging"],
  "detail-type": ["{{WhatsApp Message Sent}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
