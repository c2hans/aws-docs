---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalAlternative.html
---

# MedicalAlternative
<a name="API_streaming_MedicalAlternative"></a>

A list of possible alternative transcriptions for the input audio. Each alternative may contain one or more of `Items`, `Entities`, or `Transcript`.

## Contents
<a name="API_streaming_MedicalAlternative_Contents"></a>

 ** Entities **   <a name="transcribe-Type-streaming_MedicalAlternative-Entities"></a>
Contains entities identified as personal health information (PHI) in your transcription output.
Type: Array of [MedicalEntity](API_streaming_MedicalEntity.md) objects
Required: No

 ** Items **   <a name="transcribe-Type-streaming_MedicalAlternative-Items"></a>
Contains words, phrases, or punctuation marks in your transcription output.
Type: Array of [MedicalItem](API_streaming_MedicalItem.md) objects
Required: No

 ** Transcript **   <a name="transcribe-Type-streaming_MedicalAlternative-Transcript"></a>
Contains transcribed text.
Type: String
Required: No

## See Also
<a name="API_streaming_MedicalAlternative_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-streaming-2017-10-26/MedicalAlternative)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-streaming-2017-10-26/MedicalAlternative)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-streaming-2017-10-26/MedicalAlternative)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Transcribe. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transcribe` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
