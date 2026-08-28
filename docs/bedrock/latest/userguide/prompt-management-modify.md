---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-modify.html
---

# Modify a prompt using Prompt management
<a name="prompt-management-modify"></a>

To learn how to modify prompts using Prompt management, choose the tab for your preferred method, and then follow the steps:

------
#### [ Console ]

**To modify a prompt**

1. Sign in to the AWS Management Console with an IAM identity that has permissions to use the Amazon Bedrock console. Then, open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock).

1. Select **Prompt management** from the left navigation pane. Then, choose a prompt in the **Prompts** section.

1. To edit the **Name** or **Description** of the prompt, choose **Edit** in the **Overview** section. After you make your edits, choose **Save**.

1. To modify the prompt and its configurations, choose **Edit in prompt builder**

1. To learn about the parts of the prompt that you can modify, see [Create a prompt using Prompt management](prompt-management-create.md).

------
#### [ API ]

To modify a prompt, send an [UpdatePrompt](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdatePrompt.html) request with an [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). Include both fields that you want to maintain and fields that you want to change.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
