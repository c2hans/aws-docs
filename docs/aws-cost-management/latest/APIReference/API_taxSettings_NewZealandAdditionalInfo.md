---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_NewZealandAdditionalInfo.html
---

# NewZealandAdditionalInfo

Contains additional tax information associated with your Tax Registration Number (TRN) in New Zealand, such as the Peppol ID used for electronic invoicing (e-invoicing).

## Contents
<a name="API_taxSettings_NewZealandAdditionalInfo_Contents"></a>

 ** peppolId **   <a name="awscostmanagement-Type-taxSettings_NewZealandAdditionalInfo-peppolId"></a>
The Peppol ID used for electronic invoicing (e-invoicing) in New Zealand. Must be your 13-digit New Zealand Business Number (NZBN), without the `0088` scheme prefix. Only accepted when the `sector` is `Government`.
Type: String
Pattern: `[0-9]{13}`
Required: No

## See Also
<a name="API_taxSettings_NewZealandAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/NewZealandAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/NewZealandAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/NewZealandAdditionalInfo)
