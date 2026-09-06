---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleetError.html
---

# CreateFleetError
<a name="API_CreateFleetError"></a>

Describes the instances that could not be launched by the fleet.

## Contents
<a name="API_CreateFleetError_Contents"></a>

 ** errorCode **
The error code that indicates why the instance could not be launched. For more information about error codes, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html).
Type: String
Required: No

 ** errorMessage **
The error message that describes why the instance could not be launched. For more information about error messages, see [Error codes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html).
Type: String
Required: No

 ** launchTemplateAndOverrides **
The launch templates and overrides that were used for launching the instances. The values that you specify in the Overrides replace the values in the launch template.
Type: [LaunchTemplateAndOverridesResponse](API_LaunchTemplateAndOverridesResponse.md) object
Required: No

 ** lifecycle **
Indicates if the instance that could not be launched was a Spot, On-Demand, Capacity Block for ML, or interruptible Capacity Reservation instance. If you are using `ReservedCapacityOptions` with `on-demand-capacity-reservation` in the `ReservationTypes` list, the value can also be `on-demand-capacity-reservation`.
Type: String
Valid Values: `spot | on-demand | interruptible-capacity-reservation | capacity-block`
Required: No

## See Also
<a name="API_CreateFleetError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateFleetError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateFleetError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateFleetError)
