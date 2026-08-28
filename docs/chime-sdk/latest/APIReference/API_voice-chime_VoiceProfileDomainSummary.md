---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_VoiceProfileDomainSummary.html
---

# VoiceProfileDomainSummary
<a name="API_voice-chime_VoiceProfileDomainSummary"></a>

A high-level overview of a voice profile domain.

## Contents
<a name="API_voice-chime_VoiceProfileDomainSummary_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-CreatedTimestamp"></a>
The time at which the voice profile domain summary was created.
Type: Timestamp
Required: No

 ** Description **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-Description"></a>
Describes the voice profile domain summary.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Name **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-Name"></a>
The name of the voice profile domain summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9 _.-]+`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-UpdatedTimestamp"></a>
The time at which the voice profile domain summary was last updated.
Type: Timestamp
Required: No

 ** VoiceProfileDomainArn **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-VoiceProfileDomainArn"></a>
The ARN of a voice profile in a voice profile domain summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** VoiceProfileDomainId **   <a name="chimesdk-Type-voice-chime_VoiceProfileDomainSummary-VoiceProfileDomainId"></a>
The ID of the voice profile domain summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_VoiceProfileDomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/VoiceProfileDomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/VoiceProfileDomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/VoiceProfileDomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
