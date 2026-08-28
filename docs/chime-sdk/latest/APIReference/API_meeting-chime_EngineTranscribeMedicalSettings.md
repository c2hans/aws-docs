---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_EngineTranscribeMedicalSettings.html
---

# EngineTranscribeMedicalSettings
<a name="API_meeting-chime_EngineTranscribeMedicalSettings"></a>

Settings specific to the Amazon Transcribe Medical engine.

## Contents
<a name="API_meeting-chime_EngineTranscribeMedicalSettings_Contents"></a>

 ** LanguageCode **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-LanguageCode"></a>
The language code specified for the Amazon Transcribe Medical engine.
Type: String
Valid Values: `en-US`
Required: Yes

 ** Specialty **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-Specialty"></a>
The specialty specified for the Amazon Transcribe Medical engine.
Type: String
Valid Values: `PRIMARYCARE | CARDIOLOGY | NEUROLOGY | ONCOLOGY | RADIOLOGY | UROLOGY`
Required: Yes

 ** Type **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-Type"></a>
The type of transcription.
Type: String
Valid Values: `CONVERSATION | DICTATION`
Required: Yes

 ** ContentIdentificationType **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-ContentIdentificationType"></a>
Set this field to `PHI` to identify personal health information in the transcription output.
Type: String
Valid Values: `PHI`
Required: No

 ** Region **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-Region"></a>
The AWS Region passed to Amazon Transcribe Medical. If you don't specify a Region, Amazon Chime uses the meeting's Region.
Type: String
Valid Values: `us-east-1 | us-east-2 | us-west-2 | ap-southeast-2 | ca-central-1 | eu-west-1 | auto`
Required: No

 ** VocabularyName **   <a name="chimesdk-Type-meeting-chime_EngineTranscribeMedicalSettings-VocabularyName"></a>
The name of the vocabulary passed to Amazon Transcribe Medical.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

## See Also
<a name="API_meeting-chime_EngineTranscribeMedicalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-meetings-2021-07-15/EngineTranscribeMedicalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-meetings-2021-07-15/EngineTranscribeMedicalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-meetings-2021-07-15/EngineTranscribeMedicalSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
