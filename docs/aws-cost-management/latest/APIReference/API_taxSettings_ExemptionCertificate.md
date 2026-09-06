---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ExemptionCertificate.html
---

# ExemptionCertificate
<a name="API_taxSettings_ExemptionCertificate"></a>

The exemption certificate.

## Contents
<a name="API_taxSettings_ExemptionCertificate_Contents"></a>

 ** documentFile **   <a name="awscostmanagement-Type-taxSettings_ExemptionCertificate-documentFile"></a>
The exemption certificate file content.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 4194304.
Required: Yes

 ** documentName **   <a name="awscostmanagement-Type-taxSettings_ExemptionCertificate-documentName"></a>
The exemption certificate file name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `([A-Za-z0-9_.-]+)\.([pP][dD][fF]|[jJ][pP][gG]|[pP][nN][gG])`
Required: Yes

## See Also
<a name="API_taxSettings_ExemptionCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/taxsettings-2018-05-10/ExemptionCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/taxsettings-2018-05-10/ExemptionCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/taxsettings-2018-05-10/ExemptionCertificate)
