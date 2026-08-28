---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_ClientPolicyTls.html
---

# ClientPolicyTls
<a name="API_ClientPolicyTls"></a>

A reference to an object that represents a Transport Layer Security (TLS) client policy.

## Contents
<a name="API_ClientPolicyTls_Contents"></a>

 ** validation **   <a name="appmesh-Type-ClientPolicyTls-validation"></a>
A reference to an object that represents a TLS validation context.
Type: [TlsValidationContext](API_TlsValidationContext.md) object
Required: Yes

 ** certificate **   <a name="appmesh-Type-ClientPolicyTls-certificate"></a>
A reference to an object that represents a client's TLS certificate.
Type: [ClientTlsCertificate](API_ClientTlsCertificate.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** enforce **   <a name="appmesh-Type-ClientPolicyTls-enforce"></a>
Whether the policy is enforced. The default is `True`, if a value isn't specified.
Type: Boolean
Required: No

 ** ports **   <a name="appmesh-Type-ClientPolicyTls-ports"></a>
One or more ports that the policy is enforced for.
Type: Array of integers
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_ClientPolicyTls_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/ClientPolicyTls)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/ClientPolicyTls)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/ClientPolicyTls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
