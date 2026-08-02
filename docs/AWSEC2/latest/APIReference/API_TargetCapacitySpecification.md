---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TargetCapacitySpecification.html
---

# TargetCapacitySpecification
<a name="API_TargetCapacitySpecification"></a>

The number of units to request. You can choose to set the target capacity in terms of instances or a performance characteristic that is important to your application workload, such as vCPUs, memory, or I/O. If the request type is `maintain`, you can specify a target capacity of 0 and add capacity later.

You can use the On-Demand Instance `MaxTotalPrice` parameter, the Spot Instance `MaxTotalPrice`, or both to ensure that your fleet cost does not exceed your budget. If you set a maximum price per hour for the On-Demand Instances and Spot Instances in your request, EC2 Fleet will launch instances until it reaches the maximum amount that you're willing to pay. When the maximum amount you're willing to pay is reached, the fleet stops launching instances even if it hasn’t met the target capacity. The `MaxTotalPrice` parameters are located in [OnDemandOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OnDemandOptions.html) and [SpotOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotOptions).

## Contents
<a name="API_TargetCapacitySpecification_Contents"></a>

 ** defaultTargetCapacityType **
The default target capacity type.
Type: String
Valid Values: `spot | on-demand | capacity-block | reserved-capacity`
Required: No

 ** onDemandTargetCapacity **
The number of On-Demand units to request. If you specify a target capacity for Spot units, you cannot specify a target capacity for On-Demand units.
Type: Integer
Required: No

 ** spotTargetCapacity **
The maximum number of Spot units to launch. If you specify a target capacity for On-Demand units, you cannot specify a target capacity for Spot units.
Type: Integer
Required: No

 ** targetCapacityUnitType **
The unit for the target capacity.
Type: String
Valid Values: `vcpu | memory-mib | units`
Required: No

 ** totalTargetCapacity **
The number of units to request, filled the default target capacity type.
Type: Integer
Required: No

## See Also
<a name="API_TargetCapacitySpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TargetCapacitySpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TargetCapacitySpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TargetCapacitySpecification)
