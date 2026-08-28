---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_TlsValidationContext.html
---

# TlsValidationContext
<a name="API_TlsValidationContext"></a>

An object that represents how the proxy will validate its peer during Transport Layer Security (TLS) negotiation.

## Contents
<a name="API_TlsValidationContext_Contents"></a>

 ** trust **   <a name="appmesh-Type-TlsValidationContext-trust"></a>
A reference to where to retrieve the trust chain when validating a peer’s Transport Layer Security (TLS) certificate.
Type: [TlsValidationContextTrust](API_TlsValidationContextTrust.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** subjectAlternativeNames **   <a name="appmesh-Type-TlsValidationContext-subjectAlternativeNames"></a>
A reference to an object that represents the SANs for a Transport Layer Security (TLS) validation context. If you don't specify SANs on the *terminating* mesh endpoint, the Envoy proxy for that node doesn't verify the SAN on a peer client certificate. If you don't specify SANs on the *originating* mesh endpoint, the SAN on the certificate provided by the terminating endpoint must match the mesh endpoint service discovery configuration. Since SPIRE vended certificates have a SPIFFE ID as a name, you must set the SAN since the name doesn't match the service discovery name.
Type: [SubjectAlternativeNames](API_SubjectAlternativeNames.md) object
Required: No

## See Also
<a name="API_TlsValidationContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/TlsValidationContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/TlsValidationContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/TlsValidationContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
