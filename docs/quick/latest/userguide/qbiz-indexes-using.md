---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-using.html
---

# Using Amazon Q Business index knowledge bases
<a name="qbiz-indexes-using"></a>

Once created, Amazon Q Business index knowledge bases can be used in Amazon Quick just like any other knowledge base:

## Using in spaces
<a name="qbiz-indexes-in-spaces"></a>

Admins can add Amazon Q Business index knowledge bases to spaces:

1. Navigate to the space where you want to add the knowledge base.

1. Choose **Add resources**.

1. Select **Knowledge bases**.

1. Choose the Amazon Q Business index knowledge base from the list.

1. Choose **Add** to confirm.

## Using in output cards
<a name="qbiz-indexes-in-spaces-output"></a>

Admins can use Amazon Q Business index knowledge bases via Spaces in output cards.

## Using with agents
<a name="qbiz-indexes-in-agents"></a>

Admins can add Amazon Q Business index knowledge bases to custom agents:

1. Navigate to **Agents**.

1. Select an existing agent or create a new one.

1. In the agent configuration, choose **Add knowledge bases**.

1. Select the Amazon Q Business index knowledge base from the list.

1. Choose **Add** to confirm.

## Using with automations
<a name="qbiz-indexes-in-automations"></a>

Admins can add Amazon Q Business index knowledge bases to automations:

1. Navigate to **Automations**.

1. Select an existing automation or create a new one.

1. In the automation configuration, add a step that uses knowledge bases.

1. Select the Amazon Q Business index knowledge base from the list.

1. Configure the step and save the automation.

## Querying knowledge bases
<a name="qbiz-indexes-querying"></a>

Readers can query Amazon Q Business index knowledge bases through the Amazon Quick web application. However, a user will only be able to get a response from the Amazon Q Business index if they also have access to the Amazon Q Business application. To query the knowledge base:

1. Navigate to the Amazon Quick web application.

1. Select a space that contains the Amazon Q Business index knowledge base or use the default agent.

1. Enter your query in the chat interface.

1. View the response, which includes citations and clickable links to the source documents from the Amazon Q Business index.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
