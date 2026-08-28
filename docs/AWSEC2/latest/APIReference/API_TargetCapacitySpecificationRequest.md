---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TargetCapacitySpecificationRequest.html
---

# TargetCapacitySpecificationRequest
<a name="API_TargetCapacitySpecificationRequest"></a>

The number of units to request. You can choose to set the target capacity as the number of instances. Or you can set the target capacity to a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.

You can use the On-Demand Instance `MaxTotalPrice` parameter, the Spot Instance `MaxTotalPrice` parameter, or both parameters to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, EC2 Fleet will launch instances until it reaches the maximum amount that you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn't met the target capacity. The `MaxTotalPrice` parameters are located in [OnDemandOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OnDemandOptionsRequest) and [SpotOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotOptionsRequest).

## Contents
<a name="API_TargetCapacitySpecificationRequest_Contents"></a>

 ** TotalTargetCapacity **
The number of units to request, filled using the default target capacity type.
Type: Integer
Required: Yes

 ** DefaultTargetCapacityType **
The default target capacity type.
Type: String
Valid Values: `spot | on-demand | capacity-block | reserved-capacity`
Required: No

 ** OnDemandTargetCapacity **
The number of On-Demand units to request.
Type: Integer
Required: No

 ** SpotTargetCapacity **
The number of Spot units to request.
Type: Integer
Required: No

 ** TargetCapacityUnitType **
The unit for the target capacity. You can specify this parameter only when using attributed-based instance type selection.
Default: `units` (the number of instances)
Type: String
Valid Values: `vcpu | memory-mib | units`
Required: No

## See Also
<a name="API_TargetCapacitySpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TargetCapacitySpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TargetCapacitySpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TargetCapacitySpecificationRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
