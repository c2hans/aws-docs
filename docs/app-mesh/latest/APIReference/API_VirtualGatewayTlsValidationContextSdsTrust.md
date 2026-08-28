---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayTlsValidationContextSdsTrust.html
---

# VirtualGatewayTlsValidationContextSdsTrust
<a name="API_VirtualGatewayTlsValidationContextSdsTrust"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) Secret Discovery Service validation context trust. The proxy must be configured with a local SDS provider via a Unix Domain Socket. See App Mesh [TLS documentation](https://docs.aws.amazon.com/app-mesh/latest/userguide/tls.html) for more info.

## Contents
<a name="API_VirtualGatewayTlsValidationContextSdsTrust_Contents"></a>

 ** secretName **   <a name="appmesh-Type-VirtualGatewayTlsValidationContextSdsTrust-secretName"></a>
A reference to an object that represents the name of the secret for a virtual gateway's Transport Layer Security (TLS) Secret Discovery Service validation context trust.
Type: String
Required: Yes

## See Also
<a name="API_VirtualGatewayTlsValidationContextSdsTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayTlsValidationContextSdsTrust)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
