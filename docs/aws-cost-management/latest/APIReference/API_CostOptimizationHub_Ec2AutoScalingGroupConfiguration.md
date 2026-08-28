---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2AutoScalingGroupConfiguration.html
---

# Ec2AutoScalingGroupConfiguration
<a name="API_CostOptimizationHub_Ec2AutoScalingGroupConfiguration"></a>

The EC2 Auto Scaling group configuration used for recommendations.

## Contents
<a name="API_CostOptimizationHub_Ec2AutoScalingGroupConfiguration_Contents"></a>

 ** allocationStrategy **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2AutoScalingGroupConfiguration-allocationStrategy"></a>
The strategy used for allocating instances, based on a predefined priority order or based on the lowest available price.
Type: String
Valid Values: `Prioritized | LowestPrice`
Required: No

 ** instance **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2AutoScalingGroupConfiguration-instance"></a>
Details about the instance for the EC2 Auto Scaling group with a single instance type.
Type: [InstanceConfiguration](API_CostOptimizationHub_InstanceConfiguration.md) object
Required: No

 ** mixedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2AutoScalingGroupConfiguration-mixedInstances"></a>
A list of instance types for an EC2 Auto Scaling group with mixed instance types.
Type: Array of [MixedInstanceConfiguration](API_CostOptimizationHub_MixedInstanceConfiguration.md) objects
Required: No

 ** type **   <a name="awscostmanagement-Type-CostOptimizationHub_Ec2AutoScalingGroupConfiguration-type"></a>
The type of EC2 Auto Scaling group, showing whether it consists of a single instance type or mixed instance types.
Type: String
Valid Values: `SingleInstanceType | MixedInstanceTypes`
Required: No

## See Also
<a name="API_CostOptimizationHub_Ec2AutoScalingGroupConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/Ec2AutoScalingGroupConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/Ec2AutoScalingGroupConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/Ec2AutoScalingGroupConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
