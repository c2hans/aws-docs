---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CallDetails.html
---

# CallDetails
<a name="API_voice-chime_CallDetails"></a>

The details of an Amazon Chime SDK Voice Connector call.

## Contents
<a name="API_voice-chime_CallDetails_Contents"></a>

 ** IsCaller **   <a name="chimesdk-Type-voice-chime_CallDetails-IsCaller"></a>
Identifies a person as the caller or the callee.
Type: Boolean
Required: No

 ** TransactionId **   <a name="chimesdk-Type-voice-chime_CallDetails-TransactionId"></a>
The transaction ID of a Voice Connector call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** VoiceConnectorId **   <a name="chimesdk-Type-voice-chime_CallDetails-VoiceConnectorId"></a>
The Voice Connector ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_voice-chime_CallDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-voice-2022-08-03/CallDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-voice-2022-08-03/CallDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-voice-2022-08-03/CallDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
