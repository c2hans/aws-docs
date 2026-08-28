---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewayListenerTlsValidationContext.html
---

# VirtualGatewayListenerTlsValidationContext
<a name="API_VirtualGatewayListenerTlsValidationContext"></a>

An object that represents a virtual gateway's listener's Transport Layer Security (TLS) validation context.

## Contents
<a name="API_VirtualGatewayListenerTlsValidationContext_Contents"></a>

 ** trust **   <a name="appmesh-Type-VirtualGatewayListenerTlsValidationContext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
Type: [VirtualGatewayListenerTlsValidationContextTrust](API_VirtualGatewayListenerTlsValidationContextTrust.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** subjectAlternativeNames **   <a name="appmesh-Type-VirtualGatewayListenerTlsValidationContext-subjectAlternativeNames"></a>
A reference to an object that represents the SANs for a virtual gateway listener's Transport Layer Security (TLS) validation context.
Type: [SubjectAlternativeNames](API_SubjectAlternativeNames.md) object
Required: No

## See Also
<a name="API_VirtualGatewayListenerTlsValidationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewayListenerTlsValidationContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
