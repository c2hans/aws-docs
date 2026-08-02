---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileDomain.html
---

# VoiceProfileDomain
<a name="API_voice-chime_VoiceProfileDomain"></a>

A collection of voice profiles.

## Contents
<a name="API_voice-chime_VoiceProfileDomain_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-CreatedTimestamp"></a>
The time at which the voice profile domain was created.
Type: Timestamp
Required: No

 ** Description **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-Description"></a>
The description of the voice profile domain.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-Name"></a>
The name of the voice profile domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** ServerSideEncryptionConfiguration **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-ServerSideEncryptionConfiguration"></a>
A structure that contains the configuration settings for server-side encryption.
Type: [ServerSideEncryptionConfiguration](API_voice-chime_ServerSideEncryptionConfiguration.md) object
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-UpdatedTimestamp"></a>
The time at which the voice profile was last updated.
Type: Timestamp
Required: No

 ** VoiceProfileDomainArn **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-VoiceProfileDomainArn"></a>
The voice profile domain's Amazon Resource Number (ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** VoiceProfileDomainId **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomain-VoiceProfileDomainId"></a>
The ID of the voice profile domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceProfileDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceProfileDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceProfileDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceProfileDomain)
