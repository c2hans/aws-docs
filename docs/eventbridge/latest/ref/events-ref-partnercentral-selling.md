---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-partnercentral-selling.html
---

# AWS Partner Central Selling events
<a name="events-ref-partnercentral-selling"></a>

Partner Central Selling sends service events directly to EventBridge.

## Partner Central Selling service events
<a name="events-ref-partnercentral-selling-events"></a>

Partner Central Selling sends the following events directly to EventBridge:
+ Opportunity Created
+ Opportunity Updated
+ Opportunity Accepted
+ Opportunity Rejected
+ Engagement Invitation Created
+ Engagement Invitation Accepted
+ Engagement Invitation Rejected
+ Engagement Invitation Expired
+ Engagement Member Joined
+ Resource Snapshot Created
+ Engagement Member Added
+ Engagement Resource Snapshot Created

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.partnercentral-selling

```
{
  "source": ["aws.partnercentral-selling"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.partnercentral-selling"],
  "detail-type": ["{{Opportunity Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
