---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TrafficMirrorTarget.html
---

# TrafficMirrorTarget
<a name="API_TrafficMirrorTarget"></a>

Describes a Traffic Mirror target.

## Contents
<a name="API_TrafficMirrorTarget_Contents"></a>

 ** description **
Information about the Traffic Mirror target.
Type: String
Required: No

 ** gatewayLoadBalancerEndpointId **
The ID of the Gateway Load Balancer endpoint.
Type: String
Required: No

 ** networkInterfaceId **
The network interface ID that is attached to the target.
Type: String
Required: No

 ** networkLoadBalancerArn **
The Amazon Resource Name (ARN) of the Network Load Balancer.
Type: String
Required: No

 ** ownerId **
The ID of the account that owns the Traffic Mirror target.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the Traffic Mirror target.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** trafficMirrorTargetId **
The ID of the Traffic Mirror target.
Type: String
Required: No

 ** type **
The type of Traffic Mirror target.
Type: String
Valid Values: `network-interface | network-load-balancer | gateway-load-balancer-endpoint`
Required: No

## See Also
<a name="API_TrafficMirrorTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TrafficMirrorTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TrafficMirrorTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TrafficMirrorTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
