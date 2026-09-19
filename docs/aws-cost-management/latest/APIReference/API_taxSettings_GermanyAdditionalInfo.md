---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GermanyAdditionalInfo.html
---

# GermanyAdditionalInfo
<a name="API_taxSettings_GermanyAdditionalInfo"></a>

Contains additional tax information associated with your Tax Registration Number (TRN) in Germany, such as the economic identification number and Steuernummer.

## Contents
<a name="API_taxSettings_GermanyAdditionalInfo_Contents"></a>

 ** economicIdentificationNumber **   <a name="awscostmanagement-Type-taxSettings_GermanyAdditionalInfo-economicIdentificationNumber"></a>
The economic identification number (Wirtschafts-Identifikationsnummer, or W-IdNr) in Germany.
Type: String
Pattern: `DE[0-9]{9}`
Required: No

 ** steuernummer **   <a name="awscostmanagement-Type-taxSettings_GermanyAdditionalInfo-steuernummer"></a>
The Steuernummer (tax number issued by the local tax office) in Germany.
Type: String
Pattern: `((10|11|21|22|23|24|26|27|28|30|31|32|40|41)[0-9]{11}|[59][0-9]{12})`
Required: No

## See Also
<a name="API_taxSettings_GermanyAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/GermanyAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/GermanyAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/GermanyAdditionalInfo)
