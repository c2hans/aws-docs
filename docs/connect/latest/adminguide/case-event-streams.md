---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/case-event-streams.html
---

# Connect Customer Cases event streams
<a name="case-event-streams"></a>

Connect Customer Cases event streams provide you with near real-time updates when cases are created or modified within your Connect Customer Cases domain. The events published to the stream include these resource events:
+ Case created
+ Cases modified
+ Related items (Comments, Calls, Chats, Tasks) are added to a case

You can use the case event streams to integrate streams into your data lake solutions, create dashboards that display case performance metrics, implement business rules or automated actions based on case events, and configure alerting tools to trigger custom notifications of specific case activity.

**Topics**
+ [Set up case event streams](case-event-streams-enable.md)
+ [Allow Cases to send updates to conversational analytics rules](cases-rules-integration-onboarding.md)
+ [Case event payload and schema](case-event-streams-sample.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
