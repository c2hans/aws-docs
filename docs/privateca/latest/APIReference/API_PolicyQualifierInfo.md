---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_PolicyQualifierInfo.html
---

# PolicyQualifierInfo
<a name="API_PolicyQualifierInfo"></a>

Modifies the `CertPolicyId` of a `PolicyInformation` object with a qualifier. AWS Private CA supports the certification practice statement (CPS) qualifier.

## Contents
<a name="API_PolicyQualifierInfo_Contents"></a>

 ** PolicyQualifierId **   <a name="privateca-Type-PolicyQualifierInfo-PolicyQualifierId"></a>
Identifies the qualifier modifying a `CertPolicyId`.
Type: String
Valid Values: `CPS`
Required: Yes

 ** Qualifier **   <a name="privateca-Type-PolicyQualifierInfo-Qualifier"></a>
Defines the qualifier type. AWS Private CA supports the use of a URI for a CPS qualifier in this field.
Type: [Qualifier](API_Qualifier.md) object
Required: Yes

## See Also
<a name="API_PolicyQualifierInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/PolicyQualifierInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/PolicyQualifierInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/PolicyQualifierInfo)
