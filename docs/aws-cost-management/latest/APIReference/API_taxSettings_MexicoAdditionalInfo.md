---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_MexicoAdditionalInfo.html
---

# MexicoAdditionalInfo
<a name="API_taxSettings_MexicoAdditionalInfo"></a>

Contains additional tax information associated with your Tax Registration Number (TRN) in Mexico, such as the SAT tax regime and CFDI usage code.

## Contents
<a name="API_taxSettings_MexicoAdditionalInfo_Contents"></a>

 ** cfdiUsageCode **   <a name="awscostmanagement-Type-taxSettings_MexicoAdditionalInfo-cfdiUsageCode"></a>
The SAT CFDI usage code that identifies the purpose of the invoice in Mexico (for example, `G01` for goods acquisition, `S01` for no tax effects).
Type: String
Pattern: `[A-Z]{1,2}\d{2}`
Required: No

 ** taxRegime **   <a name="awscostmanagement-Type-taxSettings_MexicoAdditionalInfo-taxRegime"></a>
The SAT-assigned tax regime code for your business in Mexico. Must be a 3-digit number (for example, `601` for General de Ley Personas Morales).
Type: String
Pattern: `\d{3}`
Required: No

 ** taxRegimeFullName **   <a name="awscostmanagement-Type-taxSettings_MexicoAdditionalInfo-taxRegimeFullName"></a>
The full name of the SAT tax regime associated with your business in Mexico.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Required: No

## See Also
<a name="API_taxSettings_MexicoAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/MexicoAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/MexicoAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/MexicoAdditionalInfo)
