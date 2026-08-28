---
source_url: https://docs.aws.amazon.com/lexv2/latest/dg/bedrock-agent-intent-level.html
---

# Enable Bedrock Agent Intent by adding a built-in intent to your bot
<a name="bedrock-agent-intent-level"></a>

You can enable Bedrock Agent Intent by adding a built-in intent to your Amazon Lex V2 bot.

**Note**
You must first activate the Bedrock Agent Intent feature on the Generative AI panel in order to activate the feature for individual bots.

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at https://console.aws.amazon.com/lexv2/home.

1. In the navigation pane under **Bots**, select the bot you want to use for the Bedrock Agent Intent.

1. Under All languages, select **English (US**) to expand the list.

1. Select **Add intent** and choose **Use built-in intent** from the dropdown menu.

1. For more details about configurations for the AMAZON.BedrockAgentIntent, see [AMAZON.BedrockAgentIntent](built-in-intent-bedrockagent.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
