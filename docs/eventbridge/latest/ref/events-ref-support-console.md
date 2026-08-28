---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-support-console.html
---

# AWS Support Center Console events
<a name="events-ref-support-console"></a>

Support Center Console sends service events to EventBridge via AWS CloudTrail.

## Support Center Console events delivered via AWS CloudTrail
<a name="event-ref-support-console-events-via-CT"></a>

AWS CloudTrail sends events originating from Support Center Console to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.support-console
+ `eventSource`: support-console.amazonaws.com

```
{
  "source": ["aws.support-console"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["support-console.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.support-console"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["support-console.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
