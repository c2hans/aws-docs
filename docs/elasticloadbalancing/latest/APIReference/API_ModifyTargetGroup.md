---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyTargetGroup.html
---

# ModifyTargetGroup
<a name="API_ModifyTargetGroup"></a>

Modifies the health checks used when evaluating the health state of the targets in the specified target group.

To monitor the health of the targets, use [DescribeTargetHealth](API_DescribeTargetHealth.md).

## Request Parameters
<a name="API_ModifyTargetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HealthCheckEnabled **
Indicates whether health checks are enabled. If the target type is `lambda`, health checks are disabled by default but can be enabled. If the target type is `instance`, `ip`, or `alb`, health checks are always enabled and can't be disabled.
Type: Boolean
Required: No

 ** HealthCheckIntervalSeconds **
The approximate amount of time, in seconds, between health checks of an individual target.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** HealthCheckPath **
[HTTP/HTTPS health checks] The destination for health checks on the targets.
[HTTP1 or HTTP2 protocol version] The ping path. The default is /.
[GRPC protocol version] The path of a custom health check method with the format /package.service/method. The default is /AWS.ALB/healthcheck.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** HealthCheckPort **
The port the load balancer uses when performing health checks on targets.
Type: String
Required: No

 ** HealthCheckProtocol **
The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. It is supported for health checks only if the protocol of the target group is TCP, TLS, UDP, or TCP\_UDP. The GENEVE, TLS, UDP, TCP\_UDP, QUIC, and TCP\_QUIC protocols are not supported for health checks.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** HealthCheckTimeoutSeconds **
[HTTP/HTTPS health checks] The amount of time, in seconds, during which no response means a failed health check.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 120.
Required: No

 ** HealthyThresholdCount **
The number of consecutive health checks successes required before considering an unhealthy target healthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** Matcher **
[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP\_UDP, UDP or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.
Type: [Matcher](API_Matcher.md) object
Required: No

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: Yes

 ** UnhealthyThresholdCount **
The number of consecutive health check failures required before considering the target unhealthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

## Response Elements
<a name="API_ModifyTargetGroup_ResponseElements"></a>

The following element is returned by the service.

 **TargetGroups.member.N**
Information about the modified target group.
Type: Array of [TargetGroup](API_TargetGroup.md) objects

## Errors
<a name="API_ModifyTargetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

## Examples
<a name="API_ModifyTargetGroup_Examples"></a>

### Modify the health check configuration for a target group
<a name="API_ModifyTargetGroup_Example_1"></a>

This example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group.

#### Sample Request
<a name="API_ModifyTargetGroup_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=ModifyTargetGroup
&TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f
&HealthCheckProtocol=HTTPS
&HealthCheckPort=443
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyTargetGroup_Example_1_Response"></a>

```
<ModifyTargetGroupResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <ModifyTargetGroupResult>
    <TargetGroups>
      <member>
        <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f</TargetGroupArn>
        <HealthCheckTimeoutSeconds>5</HealthCheckTimeoutSeconds>
        <HealthCheckPort>443</HealthCheckPort>
        <Matcher>
          <HttpCode>200</HttpCode>
        </Matcher>
        <TargetGroupName>my-https-targets</TargetGroupName>
        <HealthCheckProtocol>HTTPS</HealthCheckProtocol>
        <Protocol>HTTPS</Protocol>
        <Port>443</Port>
        <HealthyThresholdCount>5</HealthyThresholdCount>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <HealthCheckIntervalSeconds>30</HealthCheckIntervalSeconds>
        <LoadBalancerArns>
          <member>arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188</member>
        </LoadBalancerArns>
        <UnhealthyThresholdCount>2</UnhealthyThresholdCount>
      </member>
    </TargetGroups>
  </ModifyTargetGroupResult>
  <ResponseMetadata>
    <RequestId>8525b334-f466-11e5-aa04-33bf366f62e2</RequestId>
  </ResponseMetadata>
</ModifyTargetGroupResponse>
```

## See Also
<a name="API_ModifyTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyTargetGroup)
