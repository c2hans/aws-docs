---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_Listener.html
---

# Listener
<a name="API_Listener"></a>

Information about a listener.

## Contents
<a name="API_Listener_Contents"></a>

 ** AlpnPolicy.member.N **
[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.
Type: Array of strings
Required: No

 ** Certificates.member.N **
[HTTPS or TLS listener] The default certificate for the listener.
Type: Array of [Certificate](API_Certificate.md) objects
Required: No

 ** DefaultActions.member.N **
The default actions for the listener.
Type: Array of [Action](API_Action.md) objects
Required: No

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** MutualAuthentication **
The mutual authentication configuration information.
Type: [MutualAuthenticationAttributes](API_MutualAuthenticationAttributes.md) object
Required: No

 ** Port **
The port on which the load balancer is listening.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol for connections from clients to the load balancer.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** SslPolicy **
[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.
Type: String
Required: No

## See Also
<a name="API_Listener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/Listener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/Listener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/Listener)
