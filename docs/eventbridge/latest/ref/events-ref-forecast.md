---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-forecast.html
---

# Amazon Forecast events
<a name="events-ref-forecast"></a>

Forecast sends service events directly to EventBridge, as well as via AWS CloudTrail.

## Forecast service events
<a name="events-ref-forecast-events"></a>

Forecast sends the following events directly to EventBridge:
+ Forecast Dataset Import Job State Change
+ Forecast Predictor Creation State Change
+ Forecast Predictor Deployment State Change
+ Forecast Export Job State Change
+ Forecast Forecast Creation State Change
+ Forecast Forecast Deletion State Change
+ Forecast Forecast Export Job State Change
+ Forecast Predictor Backtest Export Job State Change
+ Forecast Predictor Deletion State Change
+ Forecast Dataset Deletion State Change
+ Forecast Dataset Import Job Deletion State Change
+ Forecast Explainability Creation State Change
+ Forecast Explainability Export Job State Change
+ Forecast Explainability Deletion State Change
+ Forecast What-If Analysis Creation State Change
+ Forecast What-If Forecast Creation State Change
+ Forecast What-If Forecast Export Creation State Change
+ Forecast What-If Analysis Deletion State Change
+ Forecast What-If Forecast Deletion State Change
+ Forecast What-If Forecast Export Deletion State Change

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.forecast

```
{
  "source": ["aws.forecast"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.forecast"],
  "detail-type": ["{{Forecast Dataset Import Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## Forecast events delivered via AWS CloudTrail
<a name="event-ref-forecast-events-via-CT"></a>

AWS CloudTrail sends events originating from Forecast to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.forecast
+ `eventSource`: forecast.amazonaws.com

```
{
  "source": ["aws.forecast"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["forecast.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.forecast"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["forecast.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
