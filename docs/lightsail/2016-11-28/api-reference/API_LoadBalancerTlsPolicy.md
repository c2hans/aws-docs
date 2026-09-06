---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_LoadBalancerTlsPolicy.html
---

# LoadBalancerTlsPolicy
<a name="API_LoadBalancerTlsPolicy"></a>

Describes the TLS security policies that are available for Lightsail load balancers.

For more information about load balancer TLS security policies, see [Configuring TLS security policies on your Amazon Lightsail load balancers](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configure-load-balancer-tls-security-policy) in the *Amazon Lightsail Developer Guide*.

## Contents
<a name="API_LoadBalancerTlsPolicy_Contents"></a>

 ** ciphers **   <a name="Lightsail-Type-LoadBalancerTlsPolicy-ciphers"></a>
The ciphers used by the TLS security policy.
The ciphers are listed in order of preference.
Type: Array of strings
Required: No

 ** description **   <a name="Lightsail-Type-LoadBalancerTlsPolicy-description"></a>
The description of the TLS security policy.
Type: String
Required: No

 ** isDefault **   <a name="Lightsail-Type-LoadBalancerTlsPolicy-isDefault"></a>
A Boolean value that indicates whether the TLS security policy is the default.
Type: Boolean
Required: No

 ** name **   <a name="Lightsail-Type-LoadBalancerTlsPolicy-name"></a>
The name of the TLS security policy.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** protocols **   <a name="Lightsail-Type-LoadBalancerTlsPolicy-protocols"></a>
The protocols used in a given TLS security policy.
Type: Array of strings
Required: No

## See Also
<a name="API_LoadBalancerTlsPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/LoadBalancerTlsPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/LoadBalancerTlsPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/LoadBalancerTlsPolicy)
