---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationAssociationMetadata.html
---

# RegistrationAssociationMetadata
<a name="API_RegistrationAssociationMetadata"></a>

Metadata for the origination identity that is associated with the registration.

## Contents
<a name="API_RegistrationAssociationMetadata_Contents"></a>

 ** ResourceArn **   <a name="pinpoint-Type-RegistrationAssociationMetadata-ResourceArn"></a>
The Amazon Resource Name (ARN) of the origination identity that is associated with the registration.
Type: String
Required: Yes

 ** ResourceId **   <a name="pinpoint-Type-RegistrationAssociationMetadata-ResourceId"></a>
The unique identifier for the origination identity. For example this could be a **PhoneNumberId** or **SenderId**.
Type: String
Required: Yes

 ** ResourceType **   <a name="pinpoint-Type-RegistrationAssociationMetadata-ResourceType"></a>
The origination identity type.
Type: String
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-RegistrationAssociationMetadata-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: No

 ** PhoneNumber **   <a name="pinpoint-Type-RegistrationAssociationMetadata-PhoneNumber"></a>
The phone number associated with the registration in E.164 format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+?[1-9][0-9]{1,18}`
Required: No

## See Also
<a name="API_RegistrationAssociationMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationAssociationMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationAssociationMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationAssociationMetadata)
