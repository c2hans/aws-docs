---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ChileAdditionalInfo.html
---

# ChileAdditionalInfo
<a name="API_taxSettings_ChileAdditionalInfo"></a>

 Additional tax information associated with your TRN in Chile.

## Contents
<a name="API_taxSettings_ChileAdditionalInfo_Contents"></a>

 ** businessActivity **   <a name="awscostmanagement-Type-taxSettings_ChileAdditionalInfo-businessActivity"></a>
 The business activity code of the taxpayer in Chile. This must be the activity code shown on your SII (Servicio de Impuestos Internos) tax profile. For the list of valid activity codes, see [SII activity codes](https://www.sii.cl/ayudas/ayudas_por_servicios/1956-codigos-1959.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\s\S]*`
Required: No

 ** documentType **   <a name="awscostmanagement-Type-taxSettings_ChileAdditionalInfo-documentType"></a>
 The type of tax document. For Chile, this can be `Invoice` or `Receipt`.
Type: String
Valid Values: `Invoice | Receipt`
Required: No

## See Also
<a name="API_taxSettings_ChileAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ChileAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ChileAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ChileAdditionalInfo)
