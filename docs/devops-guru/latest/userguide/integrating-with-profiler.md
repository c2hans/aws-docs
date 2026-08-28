---
source_url: https://docs.aws.amazon.com/devops-guru/latest/userguide/integrating-with-profiler.html
---

# Integrating with CodeGuru Profiler
<a name="integrating-with-profiler"></a>

This section provides an overview of how Amazon DevOps Guru integrates with Amazon CodeGuru Profiler. You can view recommendations from CodeGuru Profiler as insights in the DevOps Guru console.

Amazon DevOps Guru integrates with Amazon CodeGuru Profiler with an EventBridge managed rule. CodeGuru Profiler sends events to EventBridge. The managed rule routes events that are sent with the default event bus. Each inbound event from CodeGuru Profiler is a proactive anomaly report. For more information, see [Working with EventBridge with CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-eventbridge.html).

DevOps Guru supports inbound events with EventBridge. An event indicates a change in a recommendation that DevOps Guru identified. CodeGuru Profiler sends a heartbeat event every 24 hours to show the continuity of the event. Events carry CodeGuru Profiler recommendation information as well as metadata for your compute resources. For information on an event lifecycle, see [Amazon EventBridge Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html).

When you set up DevOps Guru, DevOps Guru creates the EventBridge Managed Rule in your account that routes events from another service. This rule routes to DevOps Guru. Notifications are sent when there is an inbound event.

An event bus receives events from a source such as DevOps Guru and routes them to rules associated with that event bus. For more information on event buses, see [Event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html).

For information on some of the parameters, see [Amazon EventBridge events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html).

To receive CodeGuru Profiler insights in DevOps Guru, you must have the following.
+ CodeGuru Profiler must be enabled. For information on enabling CodeGuru Profiler, see [Setting up CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/setting-up.html).
+ DevOps Guru must be enabled. For information on enabling DevOps Guru, see [Enable DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/getting-started-enable-service.html).
+ The same resources must be monitored in the same Region in both CodeGuru Profiler and DevOps Guru.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
