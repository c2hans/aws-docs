---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/connect-eventbridge-events.html
---

# EventBridge events emitted by Connect Customer
<a name="connect-eventbridge-events"></a>

Connect Customer emits a variety of events related to the contact center, including but not limited to the following types of events:
+  [Contact events](contact-events.md) - contact (voice calls, chat, and task) events.
+ [Rule events](contact-lens-rules-eventbridge-event.md) - create rules that generate EventBridge events.
+ [Performance evaluation events](performance-evaluation-events.md) - monitor failures for automated evaluations and S3 exports of evaluations.
+ [Screen recording events](track-screen-recording-status.md) - events for tracking agent screen recording status.
+ [Voice ID events](voiceid-event-schema.md) - events for every transaction: enrollment, authentication, or detection of fraudsters in a watchlist. Events are sent to the EventBridge default event bus.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
