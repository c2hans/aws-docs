---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BrazilAdditionalInfo.html
---

# BrazilAdditionalInfo
<a name="API_taxSettings_BrazilAdditionalInfo"></a>

Additional tax information associated with your TRN in Brazil.

## Contents
<a name="API_taxSettings_BrazilAdditionalInfo_Contents"></a>

 ** ccmCode **   <a name="awscostmanagement-Type-taxSettings_BrazilAdditionalInfo-ccmCode"></a>
The Cadastro de Contribuintes Mobiliários (CCM) code for your TRN in Brazil. This only applies for a CNPJ tax type for the São Paulo municipality.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\d+`
Required: No

 ** legalNatureCode **   <a name="awscostmanagement-Type-taxSettings_BrazilAdditionalInfo-legalNatureCode"></a>
Legal nature of business, based on your TRN in Brazil. This only applies for a CNPJ tax type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `\d+`
Required: No

## See Also
<a name="API_taxSettings_BrazilAdditionalInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/BrazilAdditionalInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/BrazilAdditionalInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/BrazilAdditionalInfo)
