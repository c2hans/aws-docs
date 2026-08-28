---
source_url: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rule-retry-policy.html
---

# How EventBridge retries delivering events
<a name="eb-rule-retry-policy"></a>

Sometimes an [event](eb-events.md) isn't successfully delivered to the [target](eb-targets.md) specified in a [rule](eb-rules.md). This can happen, for example:
+ If the target resource is unavailable
+ Due to network conditions

When an event isn't successfully delivered to a target because of retriable errors, EventBridge retries sending the event. You set the length of time it tries, and number of retry attempts in the **Retry policy** settings for the target. By default, EventBridge retries sending the event for 24 hours and up to 185 times with an [exponential back off and *jitter*](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/), or randomized delay.

If an event isn't delivered after all retry attempts are exhausted, the event is dropped and EventBridge doesn't continue to process it.

To avoid losing events after they fail to be delivered to a target, configure a dead-letter queue (DLQ) to receive all failed events. For more information, see [Using dead-letter queues to process undelivered events in EventBridge](eb-rule-dlq.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EventBridge. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eventbridge` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
