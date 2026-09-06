---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_ApiPassthrough.html
---

# ApiPassthrough
<a name="API_ApiPassthrough"></a>

Contains X.509 certificate information to be placed in an issued certificate. An `APIPassthrough` or `APICSRPassthrough` template variant must be selected, or else this parameter is ignored.

If conflicting or duplicate certificate information is supplied from other sources, AWS Private CA applies [order of operation rules](https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations) to determine what information is used.

## Contents
<a name="API_ApiPassthrough_Contents"></a>

 ** Extensions **   <a name="privateca-Type-ApiPassthrough-Extensions"></a>
Specifies X.509 extension information for a certificate.
Type: [Extensions](API_Extensions.md) object
Required: No

 ** Subject **   <a name="privateca-Type-ApiPassthrough-Subject"></a>
Contains information about the certificate subject. The `Subject` field in the certificate identifies the entity that owns or controls the public key in the certificate. The entity can be a user, computer, device, or service. The `Subject `must contain an X.500 distinguished name (DN). A DN is a sequence of relative distinguished names (RDNs). The RDNs are separated by commas in the certificate.
Type: [ASN1Subject](API_ASN1Subject.md) object
Required: No

## See Also
<a name="API_ApiPassthrough_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/ApiPassthrough)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/ApiPassthrough)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/ApiPassthrough)
