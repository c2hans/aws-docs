---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfile.html
---

# VoiceProfile
<a name="API_voice-chime_VoiceProfile"></a>

The combination of a voice print and caller ID.

## Contents
<a name="API_voice-chime_VoiceProfile_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfile-CreatedTimestamp"></a>
The time at which the voice profile was created and enrolled.
Type: Timestamp
Required: No

 ** ExpirationTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfile-ExpirationTimestamp"></a>
The time at which a voice profile expires unless you re-enroll the caller via the `UpdateVoiceProfile` API.
Type: Timestamp
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfile-UpdatedTimestamp"></a>
The time at which the voice profile was last updated.
Type: Timestamp
Required: No

 ** VoiceProfileArn **   <a name="chimesdk-Type-voice-chime_VoiceProfile-VoiceProfileArn"></a>
The ARN of the voice profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** VoiceProfileDomainId **   <a name="chimesdk-Type-voice-chime_VoiceProfile-VoiceProfileDomainId"></a>
The ID of the domain that contains the voice profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** VoiceProfileId **   <a name="chimesdk-Type-voice-chime_VoiceProfile-VoiceProfileId"></a>
The ID of the voice profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
