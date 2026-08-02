---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_OriginationIdentityMetadata.html
---

# OriginationIdentityMetadata
<a name="API_OriginationIdentityMetadata"></a>

The metadata for an origination identity associated with a pool.

## Contents
<a name="API_OriginationIdentityMetadata_Contents"></a>

 ** IsoCountryCode **   <a name="pinpoint-Type-OriginationIdentityMetadata-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region. This field is optional and may not be present for origination identity types that are not country-specific, such as RCS agents.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** NumberCapabilities **   <a name="pinpoint-Type-OriginationIdentityMetadata-NumberCapabilities"></a>
Describes if the origination identity can be used for text messages, voice calls or both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SMS | VOICE | MMS | RCS`
Required: Yes

 ** OriginationIdentity **   <a name="pinpoint-Type-OriginationIdentityMetadata-OriginationIdentity"></a>
The unique identifier of the origination identity.
Type: String
Required: Yes

 ** OriginationIdentityArn **   <a name="pinpoint-Type-OriginationIdentityMetadata-OriginationIdentityArn"></a>
The Amazon Resource Name (ARN) associated with the origination identity.
Type: String
Required: Yes

 ** PhoneNumber **   <a name="pinpoint-Type-OriginationIdentityMetadata-PhoneNumber"></a>
The phone number in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: No

## See Also
<a name="API_OriginationIdentityMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/OriginationIdentityMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/OriginationIdentityMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/OriginationIdentityMetadata)
