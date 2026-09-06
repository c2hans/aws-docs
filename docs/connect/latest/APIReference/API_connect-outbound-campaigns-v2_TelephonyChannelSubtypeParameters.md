---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters.html
---

# TelephonyChannelSubtypeParameters
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters"></a>

The overridden telephony parameters for an outbound request of a campaign.

## Contents
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters_Contents"></a>

 ** attributes **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters-attributes"></a>
Attributes for the outbound request.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 32767.
Key Pattern: `[a-zA-Z0-9\-_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Value Pattern: `.*`
Required: Yes

 ** destinationPhoneNumber **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters-destinationPhoneNumber"></a>
The destination phone number.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20.
Pattern: `[\d\-+]*`
Required: Yes

 ** answerMachineDetectionConfig **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters-answerMachineDetectionConfig"></a>
The answering machine detection configuration for the outbound request.
Type: [AnswerMachineDetectionConfig](API_connect-outbound-campaigns-v2_AnswerMachineDetectionConfig.md) object
Required: No

 ** connectSourcePhoneNumber **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters-connectSourcePhoneNumber"></a>
The Connect Customer source phone number for the outbound request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** ringTimeout **   <a name="connect-Type-connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters-ringTimeout"></a>
The ring timeout for this specific outbound call. Overrides the default ring timeout configuration if specified.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 60.
Required: No

## See Also
<a name="API_connect-outbound-campaigns-v2_TelephonyChannelSubtypeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcampaignsv2-2024-04-23/TelephonyChannelSubtypeParameters)
