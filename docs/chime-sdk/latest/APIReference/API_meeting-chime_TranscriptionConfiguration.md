---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TranscriptionConfiguration.html
---

# TranscriptionConfiguration
<a name="API_meeting-chime_TranscriptionConfiguration"></a>

The configuration for the current transcription operation. Must contain `EngineTranscribeSettings` or `EngineTranscribeMedicalSettings`.

## Contents
<a name="API_meeting-chime_TranscriptionConfiguration_Contents"></a>

 ** EngineTranscribeMedicalSettings **   <a name="chimesdk-Type-meeting-chime_TranscriptionConfiguration-EngineTranscribeMedicalSettings"></a>
The transcription configuration settings passed to Amazon Transcribe Medical.
Type: [EngineTranscribeMedicalSettings](API_meeting-chime_EngineTranscribeMedicalSettings.md) object
Required: No

 ** EngineTranscribeSettings **   <a name="chimesdk-Type-meeting-chime_TranscriptionConfiguration-EngineTranscribeSettings"></a>
The transcription configuration settings passed to Amazon Transcribe.
Type: [EngineTranscribeSettings](API_meeting-chime_EngineTranscribeSettings.md) object
Required: No

## See Also
<a name="API_meeting-chime_TranscriptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/TranscriptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/TranscriptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/TranscriptionConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
