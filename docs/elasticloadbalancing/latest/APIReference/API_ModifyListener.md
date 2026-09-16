---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyListener.html
---

# ModifyListener
<a name="API_ModifyListener"></a>

Replaces the specified properties of the specified listener. Any properties that you do not specify remain unchanged.

Changing the protocol from HTTPS to HTTP, or from TLS to TCP, removes the security policy and default certificate properties. If you change the protocol from HTTP to HTTPS, or from TCP to TLS, you must add the security policy and default certificate properties.

To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.

## Request Parameters
<a name="API_ModifyListener_RequestParameters"></a>

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
To create a certificate list, use [AddListenerCertificates](API_AddListenerCertificates.md).
Type: Array of [Certificate](API_Certificate.md) objects
Required: No

 **DefaultActions.member.N**
The actions for the default rule.
Type: Array of [Action](API_Action.md) objects
Required: No

 ** ListenerArn **
The Amazon Resource Name (ARN) of the listener.
Type: String
Required: Yes

 ** MutualAuthentication **
[HTTPS listeners] The mutual authentication configuration information.
Type: [MutualAuthenticationAttributes](API_MutualAuthenticationAttributes.md) object
Required: No

 ** Port **
The port for connections from clients to the load balancer. You can't specify a port for a Gateway Load Balancer.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol for connections from clients to the load balancer. Application Load Balancers support the HTTP and HTTPS protocols. Network Load Balancers support the TCP, TLS, UDP, TCP\_UDP, QUIC, and TCP\_QUIC protocols. You can’t change the protocol to UDP, TCP\_UDP, QUIC, or TCP\_QUIC if dual-stack mode is enabled. You can't specify a protocol for a Gateway Load Balancer.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** SslPolicy **
[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.
For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html) in the *Application Load Balancers Guide* or [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html) in the *Network Load Balancers Guide*.
Type: String
Required: No

## Response Elements
<a name="API_ModifyListener_ResponseElements"></a>

The following element is returned by the service.

 **Listeners.member.N**
Information about the modified listener.
Type: Array of [Listener](API_Listener.md) objects

## Errors
<a name="API_ModifyListener_Errors"></a>

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

 ** ListenerNotFound **
The specified listener does not exist.
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
<a name="API_ModifyListener_Examples"></a>

### Change the default action
<a name="API_ModifyListener_Example_1"></a>

This example changes the default action for the specified listener.

#### Sample Request
<a name="API_ModifyListener_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyListener
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&DefaultActions.member.1.Type=forward
&DefaultActions.member.1.TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyListener_Example_1_Response"></a>

```
<ModifyListenerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyListenerResult>
    <Listeners>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Protocol>HTTP</Protocol>
        <Port>80</Port>
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f</TargetGroupArn>
          </member>
        </DefaultActions>
      </member>
    </Listeners>
  </ModifyListenerResult>
  <ResponseMetadata>
    <RequestId>9759b8df-f462-11e5-8a24-ffe2bf8623ae</RequestId>
  </ResponseMetadata>
</ModifyListenerResponse>
```

### Change the default certificate
<a name="API_ModifyListener_Example_2"></a>

This example changes the default certificate for the specified HTTPS listener.

#### Sample Request
<a name="API_ModifyListener_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyListener
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65
&Certificates.member.1.CertificateArn=arn:aws:iam::123456789012:server-certificate/my-new-server-cert
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyListener_Example_2_Response"></a>

```
<ModifyListenerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyListenerResult>
    <Listeners>
      <member>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <Protocol>HTTPS</Protocol>
        <Certificates>
          <member>
            <CertificateArn>arn:aws:iam::123456789012:server-certificate/my-new-server-cert</CertificateArn>
          </member>
        </Certificates>
        <Port>443</Port>
        <SslPolicy>ELBSecurityPolicy-2016-08</SslPolicy>
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </DefaultActions>
      </member>
    </Listeners>
  </ModifyListenerResult>
  <ResponseMetadata>
    <RequestId>3f72dcb2-f463-11e5-b95d-3b2c1831fc26</RequestId>
  </ResponseMetadata> </ModifyListenerResponse>
```

### Change the security policy
<a name="API_ModifyListener_Example_3"></a>

This example changes the security policy for the specified HTTPS listener.

#### Sample Request
<a name="API_ModifyListener_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyListener
&ListenerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65
&SslPolicy=ELBSecurityPolicy-2016-08
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyListener_Example_3_Response"></a>

```
<ModifyListenerResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyListenerResult>
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
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </DefaultActions>
      </member>
    </Listeners>
  </ModifyListenerResult>
  <ResponseMetadata>
    <RequestId>3f72dcb2-f463-11e5-b95d-3b2c1831fc26</RequestId>
  </ResponseMetadata>
</ModifyListenerResponse>
```

## See Also
<a name="API_ModifyListener_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyListener)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyListener)
