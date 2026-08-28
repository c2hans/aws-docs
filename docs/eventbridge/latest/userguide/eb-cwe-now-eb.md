---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cwe-now-eb.html
---

# EventBridge is the evolution of Amazon CloudWatch Events
<a name="eb-cwe-now-eb"></a>

EventBridge was formerly called Amazon CloudWatch Events. The default event bus and the rules you created in CloudWatch Events also display in the EventBridge console. EventBridge uses the same CloudWatch Events API, so your code that uses the CloudWatch Events API stays the same.

EventBridge builds on the capabilities of CloudWatch Events with features such as partner events, Schema Registry, and EventBridge Pipes. New features added to EventBridge are not added to CloudWatch Events. For more information, see [What Is Amazon EventBridge?](eb-what-is.md).

All the features you're used to in CloudWatch Events are also present in EventBridge, including:
+ [Event buses in Amazon EventBridge](eb-event-bus.md)
+ [Rules in Amazon EventBridge](eb-rules.md)
+ [Events in Amazon EventBridge](eb-events.md)
+ [Events from AWS services](eb-events.md#eb-service-event)

EventBridge features that build on and expand the capabilities of events include:
+ [Receiving events from a SaaS partner with Amazon EventBridge](eb-saas.md)
+ [Amazon EventBridge Pipes](eb-pipes.md)
+ [Amazon EventBridge schemas](eb-schema.md)
+ [Amazon EventBridge Scheduler](using-eventbridge-scheduler.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
