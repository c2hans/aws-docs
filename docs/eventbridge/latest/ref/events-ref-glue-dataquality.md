---
source_url: https://docs.aws.amazon.com/eventbridge/latest/ref/events-ref-glue-dataquality.html
---

# AWS Glue Data Quality events
<a name="events-ref-glue-dataquality"></a>

AWS Glue Data Quality sends service events directly to EventBridge.

## AWS Glue Data Quality service events
<a name="events-ref-glue-dataquality-events"></a>

AWS Glue Data Quality sends the following events directly to EventBridge:
+ Glue Job State Change
+ Glue Catalog State Change
+ Glue Crawler State Change
+ Glue Scheduled Crawler Invocation Failure
+ Glue Job Run Status
+ Glue Crawler Table Change
+ Glue Data Catalog Database State Change
+ Glue Data Catalog Table State Change
+ Glue Statistics Task Started
+ Glue Statistics Task Succeeded
+ Glue Statistics Task Failed
+ Glue Auto Statistics Invocation Failure
+ Glue Scheduled Statistics Invocation Failure
+ Data Quality Task State Change
+ Data Quality Evaluation Results Available
+ Entity Metering Event
+ Auto debug metadata key shared from Orca

*Delivery type*: [ Best effort ](event-delivery-level.md)

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.glue-dataquality

```
{
  "source": ["aws.glue-dataquality"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.glue-dataquality"],
  "detail-type": ["{{Glue Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
