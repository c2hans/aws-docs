---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileSummary.html
---

# VoiceProfileSummary
<a name="API_voice-chime_VoiceProfileSummary"></a>

A high-level summary of a voice profile.

## Contents
<a name="API_voice-chime_VoiceProfileSummary_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-CreatedTimestamp"></a>
The time at which a voice profile summary was created.
Type: Timestamp
Required: No

 ** ExpirationTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-ExpirationTimestamp"></a>
Extends the life of the voice profile. You can use `UpdateVoiceProfile` to refresh an existing voice profile's voice print and extend the life of the summary.
Type: Timestamp
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-UpdatedTimestamp"></a>
The time at which a voice profile summary was last updated.
Type: Timestamp
Required: No

 ** VoiceProfileArn **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-VoiceProfileArn"></a>
The ARN of the voice profile in a voice profile summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** VoiceProfileDomainId **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-VoiceProfileDomainId"></a>
The ID of the voice profile domain in a voice profile summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** VoiceProfileId **   <a name="chimesdk-Type-voice-chime_VoiceProfileSummary-VoiceProfileId"></a>
The ID of the voice profile in a voice profile summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceProfileSummary)
