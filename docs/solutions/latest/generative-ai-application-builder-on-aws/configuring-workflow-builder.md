---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/configuring-workflow-builder.html
---

# Configuring Workflow Builder
<a name="configuring-workflow-builder"></a>

Workflow Builder enables multi-agent orchestration through a supervisor agent that delegates work to specialized Agent Builder agents.

## Creating a workflow
<a name="creating-a-workflow"></a>

1. Navigate to the Deployment Dashboard

1. Select **Create Workflow Use Case**

1. Configure the supervisor agent:
   +  **Name**: Descriptive name for the workflow
   +  **Description**: Purpose and capabilities
   +  **System Prompt**: Instructions for agent delegation and coordination
   +  **Model**: Foundation model for the supervisor agent

 **Best practices for supervisor prompts:**
+ Clearly describe when to use each specialized agent
+ Include instructions for aggregating results from multiple agents
+ Define response formatting expectations
+ Set boundaries for delegation behavior

## Agent selection
<a name="agent-selection"></a>

Select Agent Builder agents to include as specialized agents:

1. Click **Add Agent** in the workflow configuration

1. Browse or search available Agent Builder agents

1. Review agent descriptions

1. Select agents to include in the workflow

 **Agent descriptions**

The supervisor agent uses agent descriptions to decide which agent to delegate to. Ensure descriptions clearly explain:
+ Agent’s specialized domain or capability
+ Types of tasks the agent handles
+ Input/output expectations

## Testing workflows
<a name="testing-workflows"></a>

After deployment:

1. Access the workflow through the Deployment Dashboard

1. Test with queries that require multiple agents

1. Monitor agent delegation in CloudWatch logs

1. Review response quality and delegation patterns

1. Adjust supervisor prompt if delegation is suboptimal

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
