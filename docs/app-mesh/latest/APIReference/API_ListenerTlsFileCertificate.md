---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ListenerTlsFileCertificate.html
---

# ListenerTlsFileCertificate
<a name="API_ListenerTlsFileCertificate"></a>

An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [Transport Layer Security (TLS)](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html#virtual-node-tls-prerequisites).

## Contents
<a name="API_ListenerTlsFileCertificate_Contents"></a>

 ** certificateChain **   <a name="appmesh-Type-ListenerTlsFileCertificate-certificateChain"></a>
The certificate chain for the certificate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** privateKey **   <a name="appmesh-Type-ListenerTlsFileCertificate-privateKey"></a>
The private key for a certificate stored on the file system of the virtual node that the proxy is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_ListenerTlsFileCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ListenerTlsFileCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ListenerTlsFileCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ListenerTlsFileCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
