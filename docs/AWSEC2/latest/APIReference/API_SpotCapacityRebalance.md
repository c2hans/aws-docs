---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotCapacityRebalance.html
---

# SpotCapacityRebalance
<a name="API_SpotCapacityRebalance"></a>

The Spot Instance replacement strategy to use when Amazon EC2 emits a signal that your Spot Instance is at an elevated risk of being interrupted. For more information, see [Capacity rebalancing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-capacity-rebalance.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_SpotCapacityRebalance_Contents"></a>

 ** ReplacementStrategy ** (request), ** replacementStrategy ** (response)
The replacement strategy to use. Only available for fleets of type `maintain`.
 `launch` - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet. Spot Fleet does not terminate the instances that receive a rebalance notification. You can terminate the old instances, or you can leave them running. You are charged for all instances while they are running.
 `launch-before-terminate` - Spot Fleet launches a new replacement Spot Instance when a rebalance notification is emitted for an existing Spot Instance in the fleet, and then, after a delay that you specify (in `TerminationDelay`), terminates the instances that received a rebalance notification.
Type: String
Valid Values: `launch | launch-before-terminate`
Required: No

 ** TerminationDelay ** (request), ** terminationDelay ** (response)
The amount of time (in seconds) that Amazon EC2 waits before terminating the old Spot Instance after launching a new replacement Spot Instance.
Required when `ReplacementStrategy` is set to `launch-before-terminate`.
Not valid when `ReplacementStrategy` is set to `launch`.
Valid values: Minimum value of `120` seconds. Maximum value of `7200` seconds.
Type: Integer
Required: No

## See Also
<a name="API_SpotCapacityRebalance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotCapacityRebalance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotCapacityRebalance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotCapacityRebalance)
