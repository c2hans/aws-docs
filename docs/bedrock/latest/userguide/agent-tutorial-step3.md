---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/agent-tutorial-step3.html
---

# Step 3: Test the agent
<a name="agent-tutorial-step3"></a>

In this procedure, you'll test the working draft of your agent using the built-in testing interface in the Amazon Bedrock console. You'll send natural language queries asking for the current date and time, and observe how the agent processes these requests, invokes your Lambda function, and returns formatted responses. This testing step allows you to verify that your agent correctly understands user intent, properly calls the Lambda function, and presents the information in a user-friendly way.

For more information, see [Test and troubleshoot agent behavior](agents-test.md).

**To test the agent**

1. In the Amazon Bedrock console, open the agent that you created in [Step 2: Create an Amazon Bedrock agent](agent-tutorial-step2.md)

1. Choose **Test** to open the **Test** panel.

1. In the **Alias** dropdown, select the alias **TestAlias: Working draft**.

1. In the chat interface, enter a prompt that would trigger one of your agent's actions, such as:
   + **What time is it?**
   + **Can you tell me today's date?**

1. The agent will process your prompt, invoke the Lambda function if necessary, and return a response.

1. (Optional) Choose **Show trace** to see the [trace](trace-events.md) steps for the prompt that you sent to the model. In the trace you should see the reasoning that the model uses to determine when to call the Lambda function to get the date and time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
