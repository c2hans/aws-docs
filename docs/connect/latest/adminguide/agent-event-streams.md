---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/agent-event-streams.html
---

# Connect Customer agent event streams
<a name="agent-event-streams"></a>

Connect Customer agent event streams are Amazon Kinesis data streams that provide you with near real-time reporting of agent activity within your Connect Customer instance. The events published to the stream include these CCP events:
+ Agent login
+ Agent logout
+ Agent connects with a contact
+ Agent status change, such as to Available to handle contacts, or on Break or at Training.

You can use the agent event streams to create dashboards that display agent information and events, integrate streams into workforce management (WFM) solutions, and configure alerting tools to trigger custom notifications of specific agent activity. Agent event streams help you manage agent staffing and efficiency.

**Topics**
+ [Enable agent event streams to report agent activity in Connect Customer](agent-event-streams-enable.md)
+ [Sample agent event stream in Connect Customer](sample-agent-event-stream.md)
+ [Determine the contact center agent's ACW (After Contact Work) time](determine-acw-time.md)
+ [Agent event streams data model in Connect Customer](agent-event-stream-model.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
