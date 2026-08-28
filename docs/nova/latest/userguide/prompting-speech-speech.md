---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech-speech.html
---

# System prompt authoring guidelines and examples
<a name="prompting-speech-speech"></a>

**Note**
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

The *system prompt* determines the personality, style, and content of your conversational assistant. While you can't control voice parameters directly, you can influence how natural and engaging the spoken interaction feels through the content generated. Here's a recommended baseline:

`You are a friend. You and the user will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation.`

The following examples describe how you can use the system prompt to affect the output of the speech-to-speech model.

**Example: Controlling response length**
You can also adjust the verbosity of the conversational model by adding specific instructions about length. For example, you can provide a prompt that is chatty with limits:

`You are a friend. You and the user will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios.`

Alternatively, you can provide a prompt that allows for more detailed responses:

`You are a friend. You and the user will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Provide thorough, detailed explanations when the topic requires it, though still maintaining a natural conversational flow.`

**Example: Conversational Bot**
You can guide the model to communicate in a more natural, human-like manner during turn-based conversations by adding below instructions:

`As the agent, you'll be part of a spoken conversation with the user, following a sequence of user, agent, user, agent turns. When it's your turn to speak respond with a human touch, adding emotions, wit, playfulness, and empathy where it fits. Use simple, engaging, and helpful language.`

Your prompt would look like:

`You are a friend. You and the user will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. As the agent, you'll be part of a spoken conversation with the user, following a sequence of user, agent, user, agent turns. When it's your turn to speak respond with a human touch, adding emotions, wit, playfulness, and empathy where it fits. Use simple, engaging, and helpful language.`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
