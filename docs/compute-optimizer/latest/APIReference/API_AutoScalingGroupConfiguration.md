---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupConfiguration.html
---

# AutoScalingGroupConfiguration
<a name="API_AutoScalingGroupConfiguration"></a>

Describes the configuration of an EC2 Auto Scaling group.

## Contents
<a name="API_AutoScalingGroupConfiguration_Contents"></a>

 ** allocationStrategy **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-allocationStrategy"></a>
 Describes the allocation strategy that the EC2 Auto Scaling group uses. This field is only available for EC2 Auto Scaling groups with mixed instance types.
Type: String
Valid Values: `Prioritized | LowestPrice`
Required: No

 ** desiredCapacity **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-desiredCapacity"></a>
The desired capacity, or number of instances, for the EC2 Auto Scaling group.
Type: Integer
Required: No

 ** estimatedInstanceHourReductionPercentage **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-estimatedInstanceHourReductionPercentage"></a>
 Describes the projected percentage reduction in instance hours after adopting the recommended configuration. This field is only available for EC2 Auto Scaling groups with scaling policies.
Type: Double
Required: No

 ** instanceType **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-instanceType"></a>
The instance type for the EC2 Auto Scaling group.
Type: String
Required: No

 ** maxSize **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-maxSize"></a>
The maximum size, or maximum number of instances, for the EC2 Auto Scaling group.
Type: Integer
Required: No

 ** minSize **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-minSize"></a>
The minimum size, or minimum number of instances, for the EC2 Auto Scaling group.
Type: Integer
Required: No

 ** mixedInstanceTypes **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-mixedInstanceTypes"></a>
 List the instance types within an EC2 Auto Scaling group that has mixed instance types.
Type: Array of strings
Required: No

 ** type **   <a name="computeoptimizer-Type-AutoScalingGroupConfiguration-type"></a>
 Describes whether the EC2 Auto Scaling group has a single instance type or a mixed instance type configuration.
Type: String
Valid Values: `SingleInstanceType | MixedInstanceTypes`
Required: No

## See Also
<a name="API_AutoScalingGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/AutoScalingGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/AutoScalingGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/AutoScalingGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
