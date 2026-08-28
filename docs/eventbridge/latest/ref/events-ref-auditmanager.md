---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-auditmanager.html
---

# AWS Audit Manager events
<a name="events-ref-auditmanager"></a>

Audit Manager sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Audit Manager service events
<a name="events-ref-auditmanager-events"></a>

Audit Manager sends the following events directly to EventBridge:
+ Assessment Created
+ Assessment Updated
+ Assessment Deleted
+ Assessment ControlSet Delegation Created
+ Assessment ControlSet Under Review
+ Assessment ControlSet Reviewed
+ Assessment Control Reviewed
+ Daily Assessment Evidence Collected
+ Assessment Report Created
+ Assessment Report Failed
+ Custom Framework Created
+ Custom Framework Updated
+ Custom Framework Deleted
+ Framework Share Created
+ Framework Share Accepted
+ Framework Share Declined
+ Framework Share Revoked
+ Framework Share Expired
+ Custom Control Created
+ Custom Control Updated
+ Custom Control Deleted

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.auditmanager

```
{
  "source": ["aws.auditmanager"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["{{Assessment Created}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Audit Manager events delivered via AWS CloudTrail
<a name="event-ref-auditmanager-events-via-CT"></a>

AWS CloudTrail sends events originating from Audit Manager to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.auditmanager
+ `eventSource`: auditmanager.amazonaws.com

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["auditmanager.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.auditmanager"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["auditmanager.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
