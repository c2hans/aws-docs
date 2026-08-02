---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_CustomExtension.html
---

# CustomExtension
<a name="API_CustomExtension"></a>

Specifies the X.509 extension information for a certificate.

Extensions present in `CustomExtensions` follow the `ApiPassthrough` [template rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations).

## Contents
<a name="API_CustomExtension_Contents"></a>

 ** ObjectIdentifier **   <a name="privateca-Type-CustomExtension-ObjectIdentifier"></a>

Specifies the object identifier (OID) of the X.509 extension. For more information, see the [Global OID reference database.](https://oidref.com/2.5.29)
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: Yes

 ** Value **   <a name="privateca-Type-CustomExtension-Value"></a>

Specifies the base64-encoded value of the X.509 extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?`
Required: Yes

 ** Critical **   <a name="privateca-Type-CustomExtension-Critical"></a>

Specifies the critical flag of the X.509 extension.
Type: Boolean
Required: No

## See Also
<a name="API_CustomExtension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/CustomExtension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/CustomExtension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/CustomExtension)
