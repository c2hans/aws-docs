---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TrafficSourceIdentifier.html
---

# TrafficSourceIdentifier
<a name="API_TrafficSourceIdentifier"></a>

Identifying information for a traffic source.

## Contents
<a name="API_TrafficSourceIdentifier_Contents"></a>

 ** Identifier **
Identifies the traffic source.
For Application Load Balancers, Gateway Load Balancers, Network Load Balancers, and VPC Lattice, this will be the Amazon Resource Name (ARN) for a target group in this account and Region. For Classic Load Balancers, this will be the name of the Classic Load Balancer in this account and Region.
For example:
+ Application Load Balancer ARN: `arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/1234567890123456`
+ Classic Load Balancer name: `my-classic-load-balancer`
+ VPC Lattice ARN: `arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-1234567890123456`
To get the ARN of a target group for a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer, or the name of a Classic Load Balancer, use the Elastic Load Balancing [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) and [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operations.
To get the ARN of a target group for VPC Lattice, use the VPC Lattice [GetTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetTargetGroup.html) API operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Type **
Provides additional context for the value of `Identifier`.
The following lists the valid values:
+  `elb` if `Identifier` is the name of a Classic Load Balancer.
+  `elbv2` if `Identifier` is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.
+  `vpc-lattice` if `Identifier` is the ARN of a VPC Lattice target group.
Required if the identifier is the name of a Classic Load Balancer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_TrafficSourceIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TrafficSourceIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TrafficSourceIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TrafficSourceIdentifier)
