---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_TextEvent.html
---

# TextEvent
<a name="API_TextEvent"></a>

Contains text content to be synthesized into speech.

## Contents
<a name="API_TextEvent_Contents"></a>

 ** Text **   <a name="polly-Type-TextEvent-Text"></a>
The text content to synthesize. If you specify `ssml` as the `TextType`, follow the SSML format for the input text.
Type: String
Required: Yes

 ** FlushStreamConfiguration **   <a name="polly-Type-TextEvent-FlushStreamConfiguration"></a>
Configuration for controlling when synthesized audio flushes to the output stream.
Type: [FlushStreamConfiguration](API_FlushStreamConfiguration.md) object
Required: No

 ** TextType **   <a name="polly-Type-TextEvent-TextType"></a>
Specifies whether the input text is plain text or SSML. Default: plain text.
Type: String
Valid Values: `ssml | text`
Required: No

## See Also
<a name="API_TextEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/TextEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/TextEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/TextEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Polly. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query polly` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
