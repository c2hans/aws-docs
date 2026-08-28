---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-entityresolution.html
---

# AWS Entity Resolution events
<a name="events-ref-entityresolution"></a>

AWS Entity Resolution sends service events to EventBridge via AWS CloudTrail.

## AWS Entity Resolution events delivered via AWS CloudTrail
<a name="event-ref-entityresolution-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Entity Resolution to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.entityresolution
+ `eventSource`: entityresolution.amazonaws.com

```
{
  "source": ["aws.entityresolution"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["entityresolution.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.entityresolution"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["entityresolution.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
