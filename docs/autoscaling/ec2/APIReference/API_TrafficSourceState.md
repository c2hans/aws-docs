---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TrafficSourceState.html
---

# TrafficSourceState
<a name="API_TrafficSourceState"></a>

Describes the state of a traffic source.

## Contents
<a name="API_TrafficSourceState_Contents"></a>

 ** Identifier **
The unique identifier of the traffic source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** State **
Describes the current state of a traffic source.
The state values are as follows:
+  `Adding` - The Auto Scaling instances are being registered with the load balancer or target group.
+  `Added` - All Auto Scaling instances are registered with the load balancer or target group.
+  `InService` - For an Elastic Load Balancing load balancer or target group, at least one Auto Scaling instance passed an `ELB` health check. For VPC Lattice, at least one Auto Scaling instance passed an `VPC_LATTICE` health check.
+  `Removing` - The Auto Scaling instances are being deregistered from the load balancer or target group. If connection draining (deregistration delay) is enabled, Elastic Load Balancing or VPC Lattice waits for in-flight requests to complete before deregistering the instances.
+  `Removed` - All Auto Scaling instances are deregistered from the load balancer or target group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** TrafficSource **
 *This member has been deprecated.*
This is replaced by `Identifier`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 511.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

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
<a name="API_TrafficSourceState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/TrafficSourceState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/TrafficSourceState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/TrafficSourceState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
