---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_StartSpeechSynthesisStreamActionStream.html
---

# StartSpeechSynthesisStreamActionStream
<a name="API_StartSpeechSynthesisStreamActionStream"></a>

Inbound event stream for sending input and control events to manage bidirectional speech synthesis.

## Contents
<a name="API_StartSpeechSynthesisStreamActionStream_Contents"></a>

 ** CloseStreamEvent **   <a name="polly-Type-StartSpeechSynthesisStreamActionStream-CloseStreamEvent"></a>
An event indicating the end of the input stream.
Type: [CloseStreamEvent](API_CloseStreamEvent.md) object
Required: No

 ** TextEvent **   <a name="polly-Type-StartSpeechSynthesisStreamActionStream-TextEvent"></a>
A text event containing content to be synthesized.
Type: [TextEvent](API_TextEvent.md) object
Required: No

## See Also
<a name="API_StartSpeechSynthesisStreamActionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStreamActionStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStreamActionStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStreamActionStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
