---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_AccessMethod.html
---

# AccessMethod
<a name="API_AccessMethod"></a>

Describes the type and format of extension access. Only one of `CustomObjectIdentifier` or `AccessMethodType` may be provided. Providing both results in `InvalidArgsException`.

## Contents
<a name="API_AccessMethod_Contents"></a>

 ** AccessMethodType **   <a name="privateca-Type-AccessMethod-AccessMethodType"></a>
Specifies the `AccessMethod`.
Type: String
Valid Values: `CA_REPOSITORY | RESOURCE_PKI_MANIFEST | RESOURCE_PKI_NOTIFY`
Required: No

 ** CustomObjectIdentifier **   <a name="privateca-Type-AccessMethod-CustomObjectIdentifier"></a>
An object identifier (OID) specifying the `AccessMethod`. The OID must satisfy the regular expression shown below. For more information, see NIST's definition of [Object Identifier (OID)](https://csrc.nist.gov/glossary/term/Object_Identifier).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: No

## See Also
<a name="API_AccessMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/AccessMethod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/AccessMethod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/AccessMethod)
