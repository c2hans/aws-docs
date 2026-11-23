---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_NorwayAdditionalInfo.html
---

# NorwayAdditionalInfo

Contains additional tax information associated with your Tax Registration Number (TRN) in Norway, such as the tax registration number type and the Peppol ID used for electronic invoicing (e-invoicing).

## Contents
<a name="API_taxSettings_NorwayAdditionalInfo_Contents"></a>

 ** peppolId **   <a name="awscostmanagement-Type-taxSettings_NorwayAdditionalInfo-peppolId"></a>
The Peppol ID used for electronic invoicing (e-invoicing) in Norway. Must be a valid 9-digit Norwegian Organisation Number, without the `0192` scheme prefix.
Type: String
Pattern: `[0-9]{9}`
Required: No

 ** taxRegistrationNumberType **   <a name="awscostmanagement-Type-taxSettings_NorwayAdditionalInfo-taxRegistrationNumberType"></a>
The tax registration number type in Norway.
Type: String
Valid Values: `TaxRegistrationNumber | LocalRegistrationNumber`
Required: No

## See Also
<a name="API_taxSettings_NorwayAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/NorwayAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/NorwayAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/NorwayAdditionalInfo)
