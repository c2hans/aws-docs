---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/voice-for-audio-prompts.html
---

# Choose the text-to-speech voice and language for audio prompts in Connect Customer
<a name="voice-for-audio-prompts"></a>

You select the text-to-speech voice and language in the [Set voice](set-voice.md) block.

You can also use SSML in Amazon Lex bots to modify the voice used by a chat bot when interacting with your customers. For more information about using SSML in Amazon Lex bots, see [Managing Messages](https://docs.aws.amazon.com/lex/latest/dg/howitworks-manage-prompts.html#msg-prompts-response) and [Managing Conversation Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html#special-response) in the Amazon Lex Developer Guide.

**Tip**
If you enter text that isn't supported for the Amazon Polly voice you are using, it won't be played. However, any other supported text in the prompt will be played. For a list of supported languages, see [Languages Supported by Amazon Polly](https://docs.aws.amazon.com/polly/latest/dg/SupportedLanguage.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
