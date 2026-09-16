---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateListener.html
---

# CreateListener
<a name="API_CreateListener"></a>

Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

To update a listener, use [ModifyListener](API_ModifyListener.md). When you are finished with a listener, you can delete it using [DeleteListener](API_DeleteListener.md). If you are finished with both the listener and the load balancer, you can delete them both using [DeleteLoadBalancer](API_DeleteLoadBalancer.md).

For more information, see the following:
+  [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)
+  [Listeners for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html)
+  [Listeners for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html)

This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.

## Request Parameters
<a name="API_CreateListener_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **AlpnPolicy.member.N**
[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:
+  `HTTP1Only`
+  `HTTP2Only`
+  `HTTP2Optional`
+  `HTTP2Preferred`
+  `None`
For more information, see [ALPN policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html#alpn-policies) in the *Network Load Balancers Guide*.
Type: Array of strings
Required: No

 **Certificates.member.N**
[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set `CertificateArn` to the certificate ARN but do not set `IsDefault`.
To create a certificate list for the listener, use [AddListenerCertificates](API_AddListenerCertificates.md).
Type: Array of [Certificate](API_Certificate.md) objects
Required: No

 **DefaultActions.member.N**
The actions for the default rule.
Type: Array of [Action](API_Action.md) objects
Required: Yes

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: Yes

 ** MutualAuthentication **
[HTTPS listeners] The mutual authentication configuration information.
Type: [MutualAuthenticationAttributes](API_MutualAuthenticationAttributes.md) object
Required: No

 ** Port **
The port on which the load balancer is listening. You can't specify a port for a Gateway Load Balancer.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP\_UDP, QUIC, and TCP\_QUIC. You can’t specify the UDP, TCP\_UDP, QUIC, or TCP\_QUIC protocol if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** SslPolicy **
[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.
For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html) in the *Application Load Balancers Guide* and [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) in the *Network Load Balancers Guide*.
Type: String
Required: No

 **Tags.member.N**
The tags to assign to the listener.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Elements
<a name="API_CreateListener_ResponseElements"></a>

The following element is returned by the service.

 **Listeners.member.N**
Information about the listener.
Type: Array of [Listener](API_Listener.md) objects

## Errors
<a name="API_CreateListener_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ALPNPolicyNotFound **
The specified ALPN policy is not supported.
HTTP Status Code: 400

 ** CertificateNotFound **
The specified certificate does not exist.
HTTP Status Code: 400

 ** DuplicateListener **
A listener with the specified port already exists.
HTTP Status Code: 400

 ** IncompatibleProtocols **
The specified configuration is not valid with this protocol.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** InvalidLoadBalancerAction **
The requested action is not valid.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** SSLPolicyNotFound **
The specified SSL policy does not exist.
HTTP Status Code: 400

 ** TargetGroupAssociationLimit **
You've reached the limit on the number of load balancers per target group.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

 ** TooManyActions **
You've reached the limit on the number of actions per rule.
HTTP Status Code: 400

 ** TooManyCertificates **
You've reached the limit on the number of certificates per load balancer.
HTTP Status Code: 400

 ** TooManyListeners **
You've reached the limit on the number of listeners per load balancer.
HTTP Status Code: 400

 ** TooManyRegistrationsForTargetId **
You've reached the limit on the number of times a target can be registered with a load balancer.
HTTP Status Code: 400

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TooManyTargets **
You've reached the limit on the number of targets.
HTTP Status Code: 400

 ** TooManyUniqueTargetGroupsPerLoadBalancer **
You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.
HTTP Status Code: 400

 ** TrustStoreNotFound **
The specified trust store does not exist.
HTTP Status Code: 400

 ** TrustStoreNotReady **
The specified trust store is not active.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol is not supported.
HTTP Status Code: 400

## Examples
<a name="API_CreateListener_Examples"></a>

### Create an HTTP listener
<a name="API_CreateListener_Example_1"></a>

This example creates an HTTP listener for the specified Application Load Balancer that forwards requests to the specified target group.

#### Sample Request
<a name="API_CreateListener_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Protocol=HTTP
&Port=80
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateListener_Example_1_Response"></a>

```
<CreateListenerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateListenerResult>
    <Listeners>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Protocol>HTTP</Protocol>
        <Port>80</Port>
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </DefaultActions>
      </member>
    </Listeners>
  </CreateListenerResult>
  <ResponseMetadata>
    <RequestId>883c84bb-f387-11e5-ae48-cff02092876b</RequestId>
  </ResponseMetadata>
</CreateListenerResponse>
```

### Create an HTTPS listener
<a name="API_CreateListener_Example_2"></a>

This example creates an HTTPS listener for the specified Application Load Balancer that forwards requests to the specified target group. Note that you must specify a default certificate for an HTTPS listener. You can create and manage your certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).

#### Sample Request
<a name="API_CreateListener_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188
&Protocol=HTTPS
&Port=443
&Certificates.member.1.CertificateArn=arn:aws:iam::123456789012:server-certificate/my-server-cert
&SslPolicy=ELBSecurityPolicy-2016-08
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateListener_Example_2_Response"></a>

```
<CreateListenerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateListenerResult>
    <Listeners>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Protocol>HTTPS</Protocol>
        <Certificates>
          <member>
            <CertificateArn>arn:aws:iam::123456789012:server-certificate/my-server-cert</CertificateArn>
          </member>
        </Certificates>
        <Port>443</Port>
        <SslPolicy>ELBSecurityPolicy-2016-08</SslPolicy>
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </DefaultActions>
      </member>
    </Listeners>
  </CreateListenerResult>
  <ResponseMetadata>
    <RequestId>97f1bb38-f390-11e5-b95d-3b2c1831fc26</RequestId>
  </ResponseMetadata>
</CreateListenerResponse>
```

### Create a TCP listener
<a name="API_CreateListener_Example_3"></a>

This example creates a TCP listener for the specified Network Load Balancer that forwards requests to the specified target group.

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/2d7b630a7815dda2
&Protocol=TCP
&Port=80
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-targets/b7fce90c666d892a
&Version=2015-12-01
&AUTHPARAMS
```

### Create a TLS listener
<a name="API_CreateListener_Example_4"></a>

This example creates a TLS listener for the specified Network Load Balancer that forwards requests to the specified target group.

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/2d7b630a7815dda2
&Protocol=TLS
&Port=443
&Certificates.member.1.CertificateArn=arn:aws:acm::123456789012:server-certificate/my-server-cert
&SslPolicy=ELBSecurityPolicy-2016-08
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tls-targets/b7fce90c666d892a
&Version=2015-12-01
&AUTHPARAMS
```

### Create a UDP listener
<a name="API_CreateListener_Example_5"></a>

This example creates a UDP listener for the specified Network Load Balancer that forwards requests to the specified target group.

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/2d7b630a7815dda2
&Protocol=UDP
&Port=53
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-udp-targets/b7fce90c666d892a
&Version=2015-12-01
&AUTHPARAMS
```

### Create a TCP\_UDP listener
<a name="API_CreateListener_Example_6"></a>

This example creates a TCP\_UDP listener for the specified Network Load Balancer that forwards requests to the specified target group. The target group must use the TCP\_UDP protocol.

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/2d7b630a7815dda2
&Protocol=TCP_UDP
&Port=80
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-udp-targets/b7fce90c666d892a
&Version=2015-12-01
&AUTHPARAMS
```

### Create a listener for your Gateway Load Balancer
<a name="API_CreateListener_Example_7"></a>

This example creates a listener for the specified Gateway Load Balancer that forwards requests to the specified target group. You can't specify a port or protocol.

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateListener
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/gwy/my-gateway-load-balancer/2d7b630a7815dda2
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-appliance-targets/b7fce90c666d892a
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/CreateListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/CreateListener)
