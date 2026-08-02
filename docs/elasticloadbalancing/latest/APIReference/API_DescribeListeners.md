---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeListeners.html
---

# DescribeListeners
<a name="API_DescribeListeners"></a>

Describes the specified listeners or the listeners for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer. You must specify either a load balancer or one or more listeners.

For an HTTPS or TLS listener, the output includes the default certificate for the listener. To describe the certificate list for the listener, use [DescribeListenerCertificates](API_DescribeListenerCertificates.md).

## Request Parameters
<a name="API_DescribeListeners_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ListenerArns.member.N**
The Amazon Resource Names (ARN) of the listeners.
Type: Array of strings
Required: No

 ** LoadBalancerArn **
The Amazon Resource Name (ARN) of the load balancer.
Type: String
Required: No

 ** Marker **
The marker for the next set of results. (You received this marker from a previous call.)
Type: String
Required: No

 ** PageSize **
The maximum number of results to return with this call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 400.
Required: No

## Response Elements
<a name="API_DescribeListeners_ResponseElements"></a>

The following elements are returned by the service.

 **Listeners.member.N**
Information about the listeners.
Type: Array of [Listener](API_Listener.md) objects

 ** NextMarker **
If there are additional results, this is the marker for the next set of results. Otherwise, this is null.
Type: String

## Errors
<a name="API_DescribeListeners_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ListenerNotFound **
The specified listener does not exist.
HTTP Status Code: 400

 ** LoadBalancerNotFound **
The specified load balancer does not exist.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol is not supported.
HTTP Status Code: 400

## Examples
<a name="API_DescribeListeners_Examples"></a>

### Describe an HTTP listener
<a name="API_DescribeListeners_Example_1"></a>

This example describes the specified HTTP listener.

#### Sample Request
<a name="API_DescribeListeners_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeListeners
&ListenerArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeListeners_Example_1_Response"></a>

```
<DescribeListenersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeListenersResult>
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
  </DescribeListenersResult>
  <ResponseMetadata>
    <RequestId>18e470d3-f39c-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</DescribeListenersResponse>
```

### Describe an HTTPS listener
<a name="API_DescribeListeners_Example_2"></a>

This example describes the specified HTTPS listener.

#### Sample Request
<a name="API_DescribeListeners_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeListeners
&ListenerArns.member.1=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeListeners_Example_2_Response"></a>

```
<DescribeListenersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeListenersResult>
    <Listeners>
      <member>
        <Port>443</Port>
        <Protocol>HTTPS</Protocol>
        <LoadBalancerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</LoadBalancerArn>
        <ListenerArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2</ListenerArn>
        <DefaultActions>
          <member>
            <Type>forward</Type>
            <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
          </member>
        </DefaultActions>
        <SslPolicy>ELBSecurityPolicy-2016-08</SslPolicy>
        <Certificates>
          <member>
            <CertificateArn>arn:aws:acm:us-west-2:123456789012:certificate/68c11a12-39de-44dd-b329-fe64aEXAMPLE</CertificateArn>
          </member>
        </Certificates>
      </member>
    </Listeners>
  </DescribeListenersResult>
  <ResponseMetadata>
    <RequestId>18e470d3-f39c-11e5-a53c-67205c0d10fd</RequestId>
  </ResponseMetadata>
</DescribeListenersResponse>
```

### Describe the listeners for a load balancer
<a name="API_DescribeListeners_Example_3"></a>

This example describe the listeners for the specified load balancer.

#### Sample Request
<a name="API_DescribeListeners_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=DescribeListeners
&LoadBalancerArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeListeners_Example_3_Response"></a>

```
<DescribeLoadBalancersResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <DescribeListenersResult>
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
  </DescribeListenersResult>
  <ResponseMetadata>
    <RequestId>65a3a7ea-f39c-11e5-b543-9f2c3fbb9bee</RequestId>
  </ResponseMetadata>
</DescribeLoadBalancersResponse>
```

## See Also
<a name="API_DescribeListeners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/DescribeListeners)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/DescribeListeners)
