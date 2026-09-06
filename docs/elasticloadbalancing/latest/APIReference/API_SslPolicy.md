---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SslPolicy.html
---

# SslPolicy
<a name="API_SslPolicy"></a>

Information about a policy used for SSL negotiation.

## Contents
<a name="API_SslPolicy_Contents"></a>

 ** Ciphers.member.N **
The ciphers.
Type: Array of [Cipher](API_Cipher.md) objects
Required: No

 ** Name **
The name of the policy.
Type: String
Required: No

 ** SslProtocols.member.N **
The protocols.
Type: Array of strings
Required: No

 ** SupportedLoadBalancerTypes.member.N **
 The supported load balancers.
Type: Array of strings
Required: No

## See Also
<a name="API_SslPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SslPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SslPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SslPolicy)
