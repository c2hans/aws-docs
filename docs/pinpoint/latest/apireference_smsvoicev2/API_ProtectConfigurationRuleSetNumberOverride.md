---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ProtectConfigurationRuleSetNumberOverride.html
---

# ProtectConfigurationRuleSetNumberOverride
<a name="API_ProtectConfigurationRuleSetNumberOverride"></a>

Provides details on phone number rule overrides for a protect configuration.

## Contents
<a name="API_ProtectConfigurationRuleSetNumberOverride_Contents"></a>

 ** Action **   <a name="pinpoint-Type-ProtectConfigurationRuleSetNumberOverride-Action"></a>
The action for the rule to perform of either blocking or allowing messages to the destination phone number.
Type: String
Valid Values: `ALLOW | BLOCK`
Required: Yes

 ** CreatedTimestamp **   <a name="pinpoint-Type-ProtectConfigurationRuleSetNumberOverride-CreatedTimestamp"></a>
The time when the rule was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** DestinationPhoneNumber **   <a name="pinpoint-Type-ProtectConfigurationRuleSetNumberOverride-DestinationPhoneNumber"></a>
The destination phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: Yes

 ** ExpirationTimestamp **   <a name="pinpoint-Type-ProtectConfigurationRuleSetNumberOverride-ExpirationTimestamp"></a>
The time the rule will expire at. If `ExpirationTimestamp` is not set then the rule will not expire.
Type: Timestamp
Required: No

 ** IsoCountryCode **   <a name="pinpoint-Type-ProtectConfigurationRuleSetNumberOverride-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

## See Also
<a name="API_ProtectConfigurationRuleSetNumberOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationRuleSetNumberOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ProtectConfigurationRuleSetNumberOverride)
