---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/automate-research-quick-flows.html
---

# Automating research with Quick Flows
<a name="automate-research-quick-flows"></a>

Amazon Quick Research can be integrated into Quick Flows to automate your research workflows. This allows you to standardize research processes, schedule recurring research reports, and share proven research methods across your organization.

## When to use research in Quick Flows
<a name="when-to-use-research-in-flows"></a>

Consider using Quick Research as a flow step when you need to:
+ **Standardize research processes** across your team by creating reusable workflows
+ **Schedule automated research** that runs at specific times (like every Monday 8am)
+ **Trigger downstream actions** based on research findings, such as updating records in Salesforce or creating tasks in Jira

## Getting started
<a name="getting-started-research-flows"></a>

To add Quick Research as a step in your flows, you'll configure a research agent that defines your research objective, selects data sources, and optionally accepts user inputs. The research results can then be used to drive subsequent actions in your workflow.

For detailed instructions, see [Research](ai-response-steps.md#research-step).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
