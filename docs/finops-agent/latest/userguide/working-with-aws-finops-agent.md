---
source_url: https://docs.aws.amazon.com/finops-agent/latest/userguide/working-with-aws-finops-agent.html
---

AWS FinOps Agent is in preview release and is subject to change.

# Working with AWS FinOps Agent
<a name="working-with-aws-finops-agent"></a>

After your agent is created, you interact with it through chat in the web application. This chapter describes what you can do with the agent and how to operationalize it. Start with the use cases to see what the agent can do from chat, then set up an automated workflow that runs without manual triage. The remaining topics cover the task queue and automations, teaching the agent about your business through context files and memory, and enabling Jira and Slack.

The [use cases](chatting-with-finops-agent.md) show what the agent can do from a single conversation: ask about costs, investigate anomalies, surface optimization recommendations, and generate reports. Any of these can run on a schedule or in response to an event. For a complete hands-off example, [event-triggered cost anomaly investigation](automated-anomaly-response.md) connects a AWS Cost Anomaly Detection trigger, an investigation, and a Slack destination into one workflow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS FinOps Agent (preview). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finops-agent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
