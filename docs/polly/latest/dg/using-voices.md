---
source_url: https://docs.aws.amazon.com/polly/latest/dg/using-voices.html
---

# Choosing a voice engine
<a name="using-voices"></a>

You can access Amazon Polly voices through the Amazon Polly console or AWS CLI.

**To choose a voice engine on the console**

1. Open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. From the Amazon Polly console, choose the desired voice engine.

1. Choose the desired voice from the voice drop-down menu.

1. Generate TTS audio with text of your choice.

To choose a voice engine in the AWS CLI, specify the `Engine` and `VoiceId` in the `SyntheszieSpeech` or `StartSpeechSynthesisTask` API operations. For some examples, see the [quick-start code samples](https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html) and the [Python examples](https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
