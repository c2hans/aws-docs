---
source_url: https://docs.aws.amazon.com/nova/latest/userguide/prompting-speech.html
---

# Amazon Nova Sonic prompting best practices
<a name="prompting-speech"></a>

**Note**
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

The Amazon Nova Sonic model requires a different prompting approach than standard text-based models. When you craft prompts for speech-to-speech models, it's important to understand that the *system prompt* steers the model's output style and lexical choice. It can't be used to change speech attributes such as accent and pitch. The model decides those speech characteristics based on the context of the conversation.

The key distinction is that the output is speech audio, instead of written text. This means you should optimize content for auditory comprehension rather than for reading comprehension. Your prompts should guide the model to generate text that will be naturally converted to speech. Focus on conversational flow and clarity when heard rather than when read.

**Topics**
+ [System prompt authoring guidelines and examples](prompting-speech-speech.md)
+ [Best practices for the Amazon Nova Sonic system prompt](prompting-speech-best-practices.md)
+ [Example custom system prompts](prompting-speech-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
