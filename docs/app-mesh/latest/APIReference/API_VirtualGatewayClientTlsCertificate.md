---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayClientTlsCertificate.html
---

# VirtualGatewayClientTlsCertificate
<a name="API_VirtualGatewayClientTlsCertificate"></a>

An object that represents the virtual gateway's client's Transport Layer Security (TLS) certificate.

## Contents
<a name="API_VirtualGatewayClientTlsCertificate_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** file **   <a name="appmesh-Type-VirtualGatewayClientTlsCertificate-file"></a>
An object that represents a local file certificate. The certificate must meet specific requirements and you must have proxy authorization enabled. For more information, see [ Transport Layer Security (TLS) ](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html).
Type: [VirtualGatewayListenerTlsFileCertificate](API_VirtualGatewayListenerTlsFileCertificate.md) object
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayClientTlsCertificate-sds"></a>
A reference to an object that represents a virtual gateway's client's Secret Discovery Service certificate.
Type: [VirtualGatewayListenerTlsSdsCertificate](API_VirtualGatewayListenerTlsSdsCertificate.md) object
Required: No

## See Also
<a name="API_VirtualGatewayClientTlsCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayClientTlsCertificate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
