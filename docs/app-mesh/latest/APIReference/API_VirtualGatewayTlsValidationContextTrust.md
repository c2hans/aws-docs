---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayTlsValidationContextTrust.html
---

# VirtualGatewayTlsValidationContextTrust
<a name="API_VirtualGatewayTlsValidationContextTrust"></a>

An object that represents a Transport Layer Security (TLS) validation context trust.

## Contents
<a name="API_VirtualGatewayTlsValidationContextTrust_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** acm **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-acm"></a>
A reference to an object that represents a Transport Layer Security (TLS) validation context trust for an AWS Certificate Manager certificate.
Type: [VirtualGatewayTlsValidationContextAcmTrust](API_VirtualGatewayTlsValidationContextAcmTrust.md) object
Required: No

 ** file **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-file"></a>
An object that represents a Transport Layer Security (TLS) validation context trust for a local file.
Type: [VirtualGatewayTlsValidationContextFileTrust](API_VirtualGatewayTlsValidationContextFileTrust.md) object
Required: No

 ** sds **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextTrust-sds"></a>
A reference to an object that represents a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.
Type: [VirtualGatewayTlsValidationContextSdsTrust](API_VirtualGatewayTlsValidationContextSdsTrust.md) object
Required: No

## See Also
<a name="API_VirtualGatewayTlsValidationContextTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayTlsValidationContextTrust)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
