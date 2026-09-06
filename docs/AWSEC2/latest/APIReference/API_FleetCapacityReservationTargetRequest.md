---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetCapacityReservationTargetRequest.html
---

# FleetCapacityReservationTargetRequest
<a name="API_FleetCapacityReservationTargetRequest"></a>

Describes the target Capacity Reservations or Capacity Reservation Resource Groups for an EC2 Fleet that launches into reserved capacity. You can specify Capacity Reservation IDs or a Capacity Reservation Resource Group ARN, but not both.

## Contents
<a name="API_FleetCapacityReservationTargetRequest_Contents"></a>

 ** CapacityReservationId.N **
The IDs of the Capacity Reservations in which to launch the instances.
Type: Array of strings
Required: No

 ** CapacityReservationResourceGroupArn.N **
The ARNs of the Capacity Reservation Resource Groups in which to launch the instances.
Type: Array of strings
Required: No

## See Also
<a name="API_FleetCapacityReservationTargetRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetCapacityReservationTargetRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetCapacityReservationTargetRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetCapacityReservationTargetRequest)
