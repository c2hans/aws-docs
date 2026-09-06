---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_VerifiedDestinationNumberInformation.html
---

# VerifiedDestinationNumberInformation
<a name="API_VerifiedDestinationNumberInformation"></a>

Provides information about the requested verified destintion phone number.

## Contents
<a name="API_VerifiedDestinationNumberInformation_Contents"></a>

 ** CreatedTimestamp **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-CreatedTimestamp"></a>
The time when the destination phone number was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DestinationPhoneNumber **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-DestinationPhoneNumber"></a>
The verified destination phone number, in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** Status **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-Status"></a>
The status of the verified destination phone number.
+  `PENDING`: The phone number hasn't been verified yet.
+  `VERIFIED`: The phone number is verified and can receive messages.
Type: String
Valid Values: `PENDING | VERIFIED | UNSUPPORTED`
Required: Yes

 ** VerifiedDestinationNumberArn **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-VerifiedDestinationNumberArn"></a>
The Amazon Resource Name (ARN) for the verified destination phone number.
Type: String
Required: Yes

 ** VerifiedDestinationNumberId **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-VerifiedDestinationNumberId"></a>
The unique identifier for the verified destination phone number.
Type: String
Required: Yes

 ** RcsAgentId **   <a name="pinpoint-Type-VerifiedDestinationNumberInformation-RcsAgentId"></a>
The unique identifier of the RCS agent associated with the verified destination number.
Type: String
Required: No

## See Also
<a name="API_VerifiedDestinationNumberInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/VerifiedDestinationNumberInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/VerifiedDestinationNumberInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/VerifiedDestinationNumberInformation)
