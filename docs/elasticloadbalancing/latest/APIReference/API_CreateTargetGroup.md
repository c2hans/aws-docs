---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_CreateTargetGroup.html
---

# CreateTargetGroup
<a name="API_CreateTargetGroup"></a>

Creates a target group.

To register targets with the target group, use [RegisterTargets](API_RegisterTargets.md). To update the health check settings for the target group, use [ModifyTargetGroup](API_ModifyTargetGroup.md). To monitor the health of targets in the target group, use [DescribeTargetHealth](API_DescribeTargetHealth.md).

To route traffic to the targets in a target group, specify the target group in an action using [CreateListener](API_CreateListener.md) or [CreateRule](API_CreateRule.md).

To delete a target group, use [DeleteTargetGroup](API_DeleteTargetGroup.md).

For more information, see the following:
+  [Target groups for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)
+  [Target groups for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html)
+  [Target groups for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/target-groups.html)

This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple target groups with the same settings, each call succeeds.

## Request Parameters
<a name="API_CreateTargetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HealthCheckEnabled **
Indicates whether health checks are enabled. If the target type is `lambda`, health checks are disabled by default but can be enabled. If the target type is `instance`, `ip`, or `alb`, health checks are always enabled and can't be disabled.
Type: Boolean
Required: No

 ** HealthCheckIntervalSeconds **
The approximate amount of time, in seconds, between health checks of an individual target. The range is 5-300. If the target group protocol is TCP, TLS, UDP, TCP\_UDP, QUIC, TCP\_QUIC, HTTP or HTTPS, the default is 30 seconds. If the target group protocol is GENEVE, the default is 10 seconds. If the target type is `lambda`, the default is 35 seconds.
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
The port the load balancer uses when performing health checks on targets. If the protocol is HTTP, HTTPS, TCP, TLS, UDP, TCP\_UDP, QUIC, or TCP\_QUIC the default is `traffic-port`, which is the port on which each target receives traffic from the load balancer. If the protocol is GENEVE, the default is port 80.
Type: String
Required: No

 ** HealthCheckProtocol **
The protocol the load balancer uses when performing health checks on targets. For Application Load Balancers, the default is HTTP. For Network Load Balancers and Gateway Load Balancers, the default is TCP. The TCP protocol is not supported for health checks if the protocol of the target group is HTTP or HTTPS. The GENEVE, TLS, UDP, TCP\_UDP, QUIC, and TCP\_QUIC protocols are not supported for health checks.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** HealthCheckTimeoutSeconds **
The amount of time, in seconds, during which no response from a target means a failed health check. The range is 2–120 seconds. For target groups with a protocol of HTTP, the default is 6 seconds. For target groups with a protocol of TCP, TLS or HTTPS, the default is 10 seconds. For target groups with a protocol of GENEVE, the default is 5 seconds. If the target type is `lambda`, the default is 30 seconds.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 120.
Required: No

 ** HealthyThresholdCount **
The number of consecutive health check successes required before considering a target healthy. The range is 2-10. If the target group protocol is TCP, TCP\_UDP, UDP, TLS, HTTP or HTTPS, the default is 5. For target groups with a protocol of GENEVE, the default is 5. If the target type is `lambda`, the default is 5.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** IpAddressType **
The IP address type. The default value is `ipv4`.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** Matcher **
[HTTP/HTTPS health checks] The HTTP or gRPC codes to use when checking for a successful response from a target. For target groups with a protocol of TCP, TCP\_UDP, UDP, QUIC, TCP\_QUIC, or TLS the range is 200-599. For target groups with a protocol of HTTP or HTTPS, the range is 200-499. For target groups with a protocol of GENEVE, the range is 200-399.
Type: [Matcher](API_Matcher.md) object
Required: No

 ** Name **
The name of the target group.
This name must be unique per region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.
Type: String
Required: Yes

 ** Port **
The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target. If the target is a Lambda function, this parameter does not apply. If the protocol is GENEVE, the supported port is 6081.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol to use for routing traffic to the targets. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, TCP\_UDP, QUIC, or TCP\_QUIC. For Gateway Load Balancers, the supported protocol is GENEVE. A TCP\_UDP listener must be associated with a TCP\_UDP target group. A TCP\_QUIC listener must be associated with a TCP\_QUIC target group. If the target is a Lambda function, this parameter does not apply.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** ProtocolVersion **
[HTTP/HTTPS protocol] The protocol version. Specify `GRPC` to send requests to targets using gRPC. Specify `HTTP2` to send requests to targets using HTTP/2. The default is `HTTP1`, which sends requests to targets using HTTP/1.1.
Type: String
Required: No

 **Tags.member.N**
The tags to assign to the target group.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** TargetControlPort **
The port on which the target control agent and application load balancer exchange management traffic for the target optimizer feature.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** TargetType **
The type of target that you must specify when registering targets with this target group. You can't specify targets for a target group using more than one target type.
+  `instance` - Register targets by instance ID. This is the default value.
+  `ip` - Register targets by IP address. You can specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify publicly routable IP addresses.
+  `lambda` - Register a single Lambda function as a target.
+  `alb` - Register a single Application Load Balancer as a target.
Type: String
Valid Values: `instance | ip | lambda | alb`
Required: No

 ** UnhealthyThresholdCount **
The number of consecutive health check failures required before considering a target unhealthy. The range is 2-10. If the target group protocol is TCP, TCP\_UDP, UDP, TLS, QUIC, TCP\_QUIC, HTTP or HTTPS, the default is 2. For target groups with a protocol of GENEVE, the default is 2. If the target type is `lambda`, the default is 5.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** VpcId **
The identifier of the virtual private cloud (VPC). If the target is a Lambda function, this parameter does not apply. Otherwise, this parameter is required.
Type: String
Required: No

## Response Elements
<a name="API_CreateTargetGroup_ResponseElements"></a>

The following element is returned by the service.

 **TargetGroups.member.N**
Information about the target group.
Type: Array of [TargetGroup](API_TargetGroup.md) objects

## Errors
<a name="API_CreateTargetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateTargetGroupName **
A target group with the specified name already exists.
HTTP Status Code: 400

 ** InvalidConfigurationRequest **
The requested configuration is not valid.
HTTP Status Code: 400

 ** TooManyTags **
You've reached the limit on the number of tags for this resource.
HTTP Status Code: 400

 ** TooManyTargetGroups **
You've reached the limit on the number of target groups for your AWS account.
HTTP Status Code: 400

## Examples
<a name="API_CreateTargetGroup_Examples"></a>

### Create a target group to route traffic to instances registered by instance ID
<a name="API_CreateTargetGroup_Example_1"></a>

This example creates a target group for an Application Load Balancer that you can use to route traffic to instances using HTTP on port 80. You register the instances by instance ID. This target group uses the default health check settings.

#### Sample Request
<a name="API_CreateTargetGroup_Example_1_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateTargetGroup
&Name=my-targets
&Protocol=HTTP
&Port=80
&VpcId=vpc-3ac0fb5f
&TargetType=instance
&Version=2015-12-01
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTargetGroup_Example_1_Response"></a>

```
<CreateTargetGroupResponse xmlns="http://elasticloadbalancing.amazonaws.com/doc/2015-12-01/">
  <CreateTargetGroupResult>
    <TargetGroups>
      <member>
        <TargetGroupArn>arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067</TargetGroupArn>
        <HealthCheckTimeoutSeconds>5</HealthCheckTimeoutSeconds>
        <HealthCheckPort>traffic-port</HealthCheckPort>
        <Matcher>
          <HttpCode>200</HttpCode>
        </Matcher>
        <TargetGroupName>my-targets</TargetGroupName>
        <HealthCheckProtocol>HTTP</HealthCheckProtocol>
        <HealthCheckPath>/</HealthCheckPath>
        <Protocol>HTTP</Protocol>
        <Port>80</Port>
        <VpcId>vpc-3ac0fb5f</VpcId>
        <HealthyThresholdCount>5</HealthyThresholdCount>
        <HealthCheckIntervalSeconds>30</HealthCheckIntervalSeconds>
        <UnhealthyThresholdCount>2</UnhealthyThresholdCount>
      </member>
    </TargetGroups>
  </CreateTargetGroupResult>
  <ResponseMetadata>
    <RequestId>b83fe90e-f2d5-11e5-b95d-3b2c1831fc26</RequestId>
  </ResponseMetadata>
</CreateTargetGroupResponse>
```

### Create a target group to route traffic to IP addresses
<a name="API_CreateTargetGroup_Example_2"></a>

This example creates a target group for a Network Load Balancer that you can use to route traffic to IP addresses using TCP on port 80. This target group uses the default health check settings.

#### Sample Request
<a name="API_CreateTargetGroup_Example_2_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateTargetGroup
&Name=my-ip-targets
&Protocol=TCP
&Port=80
&VpcId=vpc-09e5e2c5ef7e38ae7
&TargetType=ip
&Version=2015-12-01
&AUTHPARAMS
```

### Create a target group to route traffic to a Lambda function
<a name="API_CreateTargetGroup_Example_3"></a>

This example creates a target group for an Application Load Balancer that you can use to route traffic to a Lambda function. This target group uses the default health check settings. For more information, see [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html) in the *Application Load Balancers Guide*.

#### Sample Request
<a name="API_CreateTargetGroup_Example_3_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateTargetGroup
&Name=my-lambda-target
&TargetType=lambda
&Version=2015-12-01
&AUTHPARAMS
```

### Create a target group for your Gateway Load Balancer
<a name="API_CreateTargetGroup_Example_4"></a>

This example creates a target group for a Gateway Load Balancer. The protocol must be GENEVE and the port must be 6081.

#### Sample Request
<a name="API_CreateTargetGroup_Example_4_Request"></a>

```
https://elasticloadbalancing.amazonaws.com/?Action=CreateTargetGroup
&Name=my-appliance-targets
&Protocol=GENEVE
&Port=6081
&VpcId=vpc-09e5e2c5ef7e38ae7
&TargetType=ip
&Version=2015-12-01
&AUTHPARAMS
```

## See Also
<a name="API_CreateTargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/CreateTargetGroup)
