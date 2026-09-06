---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetGroup.html
---

# TargetGroup
<a name="API_TargetGroup"></a>

Information about a target group.

## Contents
<a name="API_TargetGroup_Contents"></a>

 ** HealthCheckEnabled **
Indicates whether health checks are enabled.
Type: Boolean
Required: No

 ** HealthCheckIntervalSeconds **
The approximate amount of time, in seconds, between health checks of an individual target.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** HealthCheckPath **
The destination for health checks on the targets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** HealthCheckPort **
The port to use to connect with the target.
Type: String
Required: No

 ** HealthCheckProtocol **
The protocol to use to connect with the target. The GENEVE, TLS, UDP, and TCP\_UDP protocols are not supported for health checks.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** HealthCheckTimeoutSeconds **
The amount of time, in seconds, during which no response means a failed health check.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 120.
Required: No

 ** HealthyThresholdCount **
The number of consecutive health checks successes required before considering an unhealthy target healthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** IpAddressType **
The IP address type. The default value is `ipv4`.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** LoadBalancerArns.member.N **
The Amazon Resource Name (ARN) of the load balancer that routes traffic to this target group. You can use each target group with only one load balancer.
Type: Array of strings
Required: No

 ** Matcher **
The HTTP or gRPC codes to use when checking for a successful response from a target.
Type: [Matcher](API_Matcher.md) object
Required: No

 ** Port **
The port on which the targets are listening. This parameter is not used if the target is a Lambda function.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** Protocol **
The protocol to use for routing traffic to the targets.
Type: String
Valid Values: `HTTP | HTTPS | TCP | TLS | UDP | TCP_UDP | GENEVE | QUIC | TCP_QUIC`
Required: No

 ** ProtocolVersion **
[HTTP/HTTPS protocol] The protocol version. The possible values are `GRPC`, `HTTP1`, and `HTTP2`.
Type: String
Required: No

 ** TargetControlPort **
The port on which the target control agent and application load balancer exchange management traffic for the target optimizer feature.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** TargetGroupArn **
The Amazon Resource Name (ARN) of the target group.
Type: String
Required: No

 ** TargetGroupName **
The name of the target group.
Type: String
Required: No

 ** TargetType **
The type of target that you must specify when registering targets with this target group. The possible values are `instance` (register targets by instance ID), `ip` (register targets by IP address), `lambda` (register a single Lambda function as a target), or `alb` (register a single Application Load Balancer as a target).
Type: String
Valid Values: `instance | ip | lambda | alb`
Required: No

 ** UnhealthyThresholdCount **
The number of consecutive health check failures required before considering the target unhealthy.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 10.
Required: No

 ** VpcId **
The ID of the VPC for the targets.
Type: String
Required: No

## See Also
<a name="API_TargetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TargetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TargetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TargetGroup)
