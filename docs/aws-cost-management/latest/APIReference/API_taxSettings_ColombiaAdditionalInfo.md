---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ColombiaAdditionalInfo.html
---

# ColombiaAdditionalInfo
<a name="API_taxSettings_ColombiaAdditionalInfo"></a>

Contains additional tax information associated with your Tax Registration Number (TRN) in Colombia, derived from your Registro Único Tributario (RUT) document.

## Contents
<a name="API_taxSettings_ColombiaAdditionalInfo_Contents"></a>

 ** issueDate **   <a name="awscostmanagement-Type-taxSettings_ColombiaAdditionalInfo-issueDate"></a>
The issue date of the RUT document from Box 61, in `YYYY-MM-DD` format.
Type: String
Pattern: `(\d{4}-(0[0-9]|1[0-2])-([0-2][0-9]|3[0-1]))`
Required: No

 ** responsibilityCodes **   <a name="awscostmanagement-Type-taxSettings_ColombiaAdditionalInfo-responsibilityCodes"></a>
The DIAN fiscal responsibility codes from Box 53 of the RUT document (for example, `48` for value-added tax (VAT) responsibility).
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 26 items.
Pattern: `\d{2}`
Required: No

 ** taxpayerTypeCode **   <a name="awscostmanagement-Type-taxSettings_ColombiaAdditionalInfo-taxpayerTypeCode"></a>
The taxpayer category from Box 24 of the RUT document (`1` for a legal entity, `2` for a natural person).
Type: String
Pattern: `\d{1}`
Required: No

## See Also
<a name="API_taxSettings_ColombiaAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ColombiaAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ColombiaAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ColombiaAdditionalInfo)
