---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/omni-investigations.html
---

# Investigations

An investigation finds the root cause of an issue. Start one when an alert fires or you see an anomaly on a chart and want to know why. With CloudWatch Omni, you can investigate with its own root cause analysis or with a connected investigation agent. This topic explains where you can start an investigation and which investigation agents you can connect.

## Start an investigation
<a name="omni-investigations-start-an-investigation"></a>

Wherever you see an **Investigate** action in CloudWatch Omni, you can start an investigation from it. You can start an investigation from the following places:
+ From an alert, choose the alert's **Investigate** action, or turn on **Auto-trigger an investigation with your agent** in the alert's create or edit form. For more information about investigating a firing alert, see [Investigate a firing alert](omni-alerts.md#omni-alerts-investigate-a-firing-alert).
+ From a chart, select an anomalous range or open the chart's menu, and choose **Investigate this signal**. The investigation starts from the chart's service or query.
+ From a service page, start the investigation from the service. For more information about monitoring a service, see [Monitor a service](omni-monitor-a-service.md).
+ From a failed agent run, choose **Investigate** on the run when your space is connected to the AWS DevOps Agent. For more information about agent runs, see [Agent traces](omni-agent-traces.md).
+ From a thread, describe the symptom and ask Omni to investigate. If more than one investigator is available, Omni asks which one to use and remembers your choice. For more information about the Omni agent, see [Ask the Omni agent](omni-ask-the-omni-agent.md).
+ From a thread, enter `/investigation new <description of issue>` to start an investigation with the command.

## Investigation agents
<a name="omni-investigations-investigation-agents"></a>

By connecting an investigation agent, you can hand root cause analysis to a tool your team already trusts. You can review the agent's findings in the investigation in CloudWatch Omni. Connect an agent to your space to investigate with it:
+ [Investigate with the AWS DevOps Agent](omni-investigate-with-the-aws-devops-agent.md)
+ [Investigate with AWS Partner agents](omni-investigate-with-partner-agents.md), including [Investigate with ResolveAI](omni-investigate-with-resolve-ai.md)
