---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-serverlessrepo.html
---

# AWS Serverless Application Repository events
<a name="events-ref-serverlessrepo"></a>

AWS Serverless Application Repository sends service events to EventBridge via AWS CloudTrail.

## AWS Serverless Application Repository events delivered via AWS CloudTrail
<a name="event-ref-serverlessrepo-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Serverless Application Repository to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.serverlessrepo
+ `eventSource`: serverlessrepo.amazonaws.com

```
{
  "source": ["aws.serverlessrepo"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["serverlessrepo.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.serverlessrepo"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["serverlessrepo.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
