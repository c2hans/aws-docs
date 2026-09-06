---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CountryLaunchStatusInformation.html
---

# CountryLaunchStatusInformation
<a name="API_CountryLaunchStatusInformation"></a>

Contains per-country launch status details for an RCS agent.

## Contents
<a name="API_CountryLaunchStatusInformation_Contents"></a>

 ** CarrierStatus **   <a name="pinpoint-Type-CountryLaunchStatusInformation-CarrierStatus"></a>
An array of CarrierStatusInformation objects containing carrier-level launch status details.
Type: Array of [CarrierStatusInformation](API_CarrierStatusInformation.md) objects
Required: Yes

 ** IsoCountryCode **   <a name="pinpoint-Type-CountryLaunchStatusInformation-IsoCountryCode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
Type: String
Length Constraints: Fixed length of 2.
Pattern: `[A-Z]{2}`
Required: Yes

 ** RegistrationId **   <a name="pinpoint-Type-CountryLaunchStatusInformation-RegistrationId"></a>
The unique identifier of the registration associated with this country launch.
Type: String
Required: Yes

 ** Status **   <a name="pinpoint-Type-CountryLaunchStatusInformation-Status"></a>
The launch status for this country.
Type: String
Valid Values: `CREATED | PENDING | PARTIAL | ACTIVE | REJECTED`
Required: Yes

 ** RcsPlatformId **   <a name="pinpoint-Type-CountryLaunchStatusInformation-RcsPlatformId"></a>
The RCS platform identifier for this country.
Type: String
Required: No

## See Also
<a name="API_CountryLaunchStatusInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CountryLaunchStatusInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CountryLaunchStatusInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CountryLaunchStatusInformation)
