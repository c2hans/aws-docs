---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_TargetDescription.html
---

# TargetDescription
<a name="API_TargetDescription"></a>

Information about a target.

## Contents
<a name="API_TargetDescription_Contents"></a>

 ** Id **
The ID of the target. If the target type of the target group is `instance`, specify an instance ID. If the target type is `ip`, specify an IP address. If the target type is `lambda`, specify the ARN of the Lambda function. If the target type is `alb`, specify the ARN of the Application Load Balancer target.
Type: String
Required: Yes

 ** AvailabilityZone **
An Availability Zone or `all`. This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer.
For Application Load Balancer target groups, the specified Availability Zone value is only applicable when cross-zone load balancing is off. Otherwise the parameter is ignored and treated as `all`.
This parameter is not supported if the target type of the target group is `instance` or `alb`.
If the target type is `ip` and the IP address is in a subnet of the VPC for the target group, the Availability Zone is automatically detected and this parameter is optional. If the IP address is outside the VPC, this parameter is required.
For Application Load Balancer target groups with cross-zone load balancing off, if the target type is `ip` and the IP address is outside of the VPC for the target group, this should be an Availability Zone inside the VPC for the target group.
If the target type is `lambda`, this parameter is optional and the only supported value is `all`.
Type: String
Required: No

 ** Port **
The port on which the target is listening. If the target group protocol is GENEVE, the supported port is 6081. If the target type is `alb`, the targeted Application Load Balancer must have at least one listener whose port matches the target group port. This parameter is not used if the target is a Lambda function.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** QuicServerId **
The server ID for the targets. This value is required if the protocol is `QUIC` or `TCP_QUIC` and can't be used with other protocols.
The ID consists of the `0x` prefix followed by 16 hexadecimal characters. Any letters must be lowercase. The value must be unique at the listener level. You can't modify the server ID for a registered target. You must deregister the target and then provide a new server ID when you register the target again.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_TargetDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/TargetDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/TargetDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/TargetDescription)
