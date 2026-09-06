---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CustomAttribute.html
---

# CustomAttribute
<a name="API_CustomAttribute"></a>

Defines the X.500 relative distinguished name (RDN).

## Contents
<a name="API_CustomAttribute_Contents"></a>

 ** ObjectIdentifier **   <a name="privateca-Type-CustomAttribute-ObjectIdentifier"></a>
Specifies the object identifier (OID) of the attribute type of the relative distinguished name (RDN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: Yes

 ** Value **   <a name="privateca-Type-CustomAttribute-Value"></a>

Specifies the attribute value of relative distinguished name (RDN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_CustomAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CustomAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CustomAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CustomAttribute)
