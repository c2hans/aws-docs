---
source_url: https://docs.aws.amazon.com/polly/latest/dg/using-speechmarks.html
---

# Speech mark types
<a name="using-speechmarks"></a>

You request speech marks using the [SpeechMarkTypes](https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisTask.html#polly-StartSpeechSynthesisTask-request-SpeechMarkTypes) option for either the [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html) or [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisTask.html) commands. You specify the metadata elements that you want to return from your input text. You can request as many as four types of metadata but you must specify at least one per request. No audio output is generated with the request.

In the AWS CLI, for example:

```
--speech-mark-types='["sentence", "word", "viseme", "ssml"]'
```

Amazon Polly generates speech marks using the following elements:
+  **sentence** – Indicates a sentence element in the input text.
+  **word** – Indicates a word element in the text.
+  **viseme** – Describes the face and mouth movements corresponding to each phoneme being spoken. For more information, see [Visemes and Amazon Polly](viseme.md).
+  **ssml** – Describes a <mark> element from the SSML input text. For more information, see [Generating speech from SSML documents](ssml.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
