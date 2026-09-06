---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ExtendedKeyUsage.html
---

# ExtendedKeyUsage
<a name="API_ExtendedKeyUsage"></a>

Specifies additional purposes for which the certified public key may be used other than basic purposes indicated in the `KeyUsage` extension.

## Contents
<a name="API_ExtendedKeyUsage_Contents"></a>

 ** ExtendedKeyUsageObjectIdentifier **   <a name="privateca-Type-ExtendedKeyUsage-ExtendedKeyUsageObjectIdentifier"></a>
Specifies a custom `ExtendedKeyUsage` with an object identifier (OID).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `([0-2])\.([0-9]|([0-3][0-9]))((\.([0-9]+)){0,126})`
Required: No

 ** ExtendedKeyUsageType **   <a name="privateca-Type-ExtendedKeyUsage-ExtendedKeyUsageType"></a>
Specifies a standard `ExtendedKeyUsage` as defined as in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12).
Type: String
Valid Values: `SERVER_AUTH | CLIENT_AUTH | CODE_SIGNING | EMAIL_PROTECTION | TIME_STAMPING | OCSP_SIGNING | SMART_CARD_LOGIN | DOCUMENT_SIGNING | CERTIFICATE_TRANSPARENCY`
Required: No

## See Also
<a name="API_ExtendedKeyUsage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ExtendedKeyUsage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ExtendedKeyUsage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ExtendedKeyUsage)
