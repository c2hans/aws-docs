---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-connect.html
---

# Amazon Connect Customer events
<a name="events-ref-connect"></a>

Connect Customer sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Connect Customer service events
<a name="events-ref-connect-events"></a>

Connect Customer sends the following events directly to EventBridge:
+ Contact Lens Analysis State Change
+ Rule for Contact Lens Post Call Matched
+ Rule for Contact Lens Realtime Matched
+ Contact Lens Realtime Rules Matched
+ Contact Lens Post Call Rules Matched
+ Amazon Connect Rules Action Execution Failed
+ Contact Lens Post Chat Rules Matched
+ Contact Lens After Chat Work Rules Matched
+ Contact Lens After Call Work Rules Matched
+ Contact Lens Email Rules Matched
+ Contact Lens Evaluation Rules Matched
+ Contact Lens Realtime Chat Rules Matched
+ Metrics Rules Matched
+ Contact Lens Automated Evaluation Submission Failed
+ Contact Lens Evaluation Export Failed
+ Amazon Connect Contact Event

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.connect

```
{
  "source": ["aws.connect"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.connect"],
  "detail-type": ["{{Contact Lens Analysis State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Connect Customer events delivered via AWS CloudTrail
<a name="event-ref-connect-events-via-CT"></a>

AWS CloudTrail sends events originating from Connect Customer to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.connect
+ `eventSource`: connect.amazonaws.com

```
{
  "source": ["aws.connect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["connect.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.connect"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["connect.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
