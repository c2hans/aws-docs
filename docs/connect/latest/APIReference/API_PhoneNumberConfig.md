---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_PhoneNumberConfig.html
---

# PhoneNumberConfig
<a name="API_PhoneNumberConfig"></a>

Configuration settings for phone type and phone number.

## Contents
<a name="API_PhoneNumberConfig_Contents"></a>

 ** Channel **   <a name="connect-Type-PhoneNumberConfig-Channel"></a>
The channel for this phone number configuration. **Only `VOICE` is supported for this data type.**
Type: String
Valid Values: `VOICE | CHAT | TASK | EMAIL`
Required: Yes

 ** PhoneType **   <a name="connect-Type-PhoneNumberConfig-PhoneType"></a>
The phone type. Valid values: SOFT\_PHONE, DESK\_PHONE.
Type: String
Valid Values: `SOFT_PHONE | DESK_PHONE`
Required: Yes

 ** PhoneNumber **   <a name="connect-Type-PhoneNumberConfig-PhoneNumber"></a>
The phone number for the user's desk phone.
Type: String
Pattern: `\+[1-9]\d{1,14}$`
Required: No

## See Also
<a name="API_PhoneNumberConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/PhoneNumberConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/PhoneNumberConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/PhoneNumberConfig)
