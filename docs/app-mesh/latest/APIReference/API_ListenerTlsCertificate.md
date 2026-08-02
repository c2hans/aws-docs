---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListenerTlsCertificate.html
---

# ListenerTlsCertificate
<a name="API_ListenerTlsCertificate"></a>

An object that represents a listener's Transport Layer Security (TLS) certificate.

## Contents
<a name="API_ListenerTlsCertificate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acm **   <a name="appmesh-Type-ListenerTlsCertificate-acm"></a>
A reference to an object that represents an AWS Certificate Manager certificate.
Type: [ListenerTlsAcmCertificate](API_ListenerTlsAcmCertificate.md) object
Required: No

 ** file **   <a name="appmesh-Type-ListenerTlsCertificate-file"></a>
A reference to an object that represents a local file certificate.
Type: [ListenerTlsFileCertificate](API_ListenerTlsFileCertificate.md) object
Required: No

 ** sds **   <a name="appmesh-Type-ListenerTlsCertificate-sds"></a>
A reference to an object that represents a listener's Secret Discovery Service certificate.
Type: [ListenerTlsSdsCertificate](API_ListenerTlsSdsCertificate.md) object
Required: No

## See Also
<a name="API_ListenerTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTlsCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTlsCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTlsCertificate)
