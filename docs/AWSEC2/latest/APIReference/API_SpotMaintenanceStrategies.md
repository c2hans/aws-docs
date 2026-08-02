---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMaintenanceStrategies.html
---

# SpotMaintenanceStrategies
<a name="API_SpotMaintenanceStrategies"></a>

The strategies for managing your Spot Instances that are at an elevated risk of being interrupted.

## Contents
<a name="API_SpotMaintenanceStrategies_Contents"></a>

 ** CapacityRebalance ** (request), ** capacityRebalance ** (response)
The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see [Capacity rebalancing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html) in the *Amazon EC2 User Guide*.
Type: [SpotCapacityRebalance](API_SpotCapacityRebalance.md) object
Required: No

## See Also
<a name="API_SpotMaintenanceStrategies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotMaintenanceStrategies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotMaintenanceStrategies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotMaintenanceStrategies)
