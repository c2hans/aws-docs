---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_UnitedArabEmiratesAdditionalInfo.html
---

# UnitedArabEmiratesAdditionalInfo

Contains additional tax information associated with your Tax Registration Number (TRN) in the United Arab Emirates, such as the TRN type and the Peppol ID used for electronic invoicing (e-invoicing).

## Contents
<a name="API_taxSettings_UnitedArabEmiratesAdditionalInfo_Contents"></a>

 ** emiratesId **   <a name="awscostmanagement-Type-taxSettings_UnitedArabEmiratesAdditionalInfo-emiratesId"></a>
Your Emirates ID. Optional. Must be in the format `784-YYYY-NNNNNNN-N`.
Type: String
Pattern: `784-[0-9]{4}-[0-9]{7}-[0-9]`
Required: No

 ** peppolId **   <a name="awscostmanagement-Type-taxSettings_UnitedArabEmiratesAdditionalInfo-peppolId"></a>
The Peppol ID used for electronic invoicing (e-invoicing) in the United Arab Emirates. Optional. Must be a 10-digit number.
Type: String
Pattern: `[0-9]{10}`
Required: No

 ** taxRegistrationNumberType **   <a name="awscostmanagement-Type-taxSettings_UnitedArabEmiratesAdditionalInfo-taxRegistrationNumberType"></a>
The type of your TRN in the United Arab Emirates. Valid values are `VATTaxRegistrationNumber` and `LocalTaxRegistrationNumber` (Corporate Tax). This field must be provided.
Type: String
Valid Values: `VATTaxRegistrationNumber | LocalTaxRegistrationNumber`
Required: No

 ** tradeLicenseNumber **   <a name="awscostmanagement-Type-taxSettings_UnitedArabEmiratesAdditionalInfo-tradeLicenseNumber"></a>
Your trade license number in the United Arab Emirates. Optional. Must be a 10-digit number.
Type: String
Pattern: `[0-9]{10}`
Required: No

## See Also
<a name="API_taxSettings_UnitedArabEmiratesAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/UnitedArabEmiratesAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/UnitedArabEmiratesAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/UnitedArabEmiratesAdditionalInfo)
