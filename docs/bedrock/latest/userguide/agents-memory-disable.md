---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-memory-disable.html
---

# Disable agent memory
<a name="agents-memory-disable"></a>

You can disable memory for your agent at any time. You cannot access memory sessions after you disable memory for your agent.

**Note**
If you enable memory for the agent and do not specify `memoryId` when you invoke the agent, agent will not store that specific turn in the memory.

To learn how to disable memory, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To disable memory for your agent,**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. Select **Agents** from the left navigation pane. Then, choose an agent in the **Agents** section.

1. Choose **Edit in Agent Builder**

1. In the **Memory** section, choose **Disable**.

------
#### [ API ]

To disable memory, send a [UpdateAgent](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateAgent.html) request (see link for request and response formats and field details) with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). Send the request without specifying the `memoryConfiguration` structure. This will disassociate the memory from the agent.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
