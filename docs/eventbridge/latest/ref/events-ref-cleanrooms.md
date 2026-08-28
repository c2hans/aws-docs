---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-cleanrooms.html
---

# AWS Clean Rooms events
<a name="events-ref-cleanrooms"></a>

AWS Clean Rooms sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Clean Rooms service events
<a name="events-ref-cleanrooms-events"></a>

AWS Clean Rooms sends the following events directly to EventBridge:
+ Collaboration Created
+ Collaboration Updated
+ Membership Created
+ Membership Updated
+ Membership Deleted
+ Protected Job Submitted
+ Protected Job Started
+ Protected Job Cancelling
+ Protected Job Cancelled
+ Protected Job Succeeded
+ Protected Job Failed
+ Protected Query Submitted
+ Protected Query Started
+ Protected Query Cancelling
+ Protected Query Cancelled
+ Protected Query Succeeded
+ Protected Query Failed
+ Protected Query Timed Out

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.cleanrooms

```
{
  "source": ["aws.cleanrooms"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["{{Collaboration Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Clean Rooms events delivered via AWS CloudTrail
<a name="event-ref-cleanrooms-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Clean Rooms to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.cleanrooms
+ `eventSource`: cleanrooms.amazonaws.com

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cleanrooms.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.cleanrooms"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["cleanrooms.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
