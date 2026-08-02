---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_LaunchTemplateCapacityReservationSpecificationResponse.html
---

# LaunchTemplateCapacityReservationSpecificationResponse
<a name="API_LaunchTemplateCapacityReservationSpecificationResponse"></a>

Information about the Capacity Reservation targeting option.

## Contents
<a name="API_LaunchTemplateCapacityReservationSpecificationResponse_Contents"></a>

 ** capacityReservationPreference **
Indicates the instance's Capacity Reservation preferences. Possible preferences include:
+  `open` - The instance can run in any `open` Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
+  `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs in On-Demand capacity.
Type: String
Valid Values: `capacity-reservations-only | open | none`
Required: No

 ** capacityReservationTarget **
Information about the target Capacity Reservation or Capacity Reservation group.
Type: [CapacityReservationTargetResponse](API_CapacityReservationTargetResponse.md) object
Required: No

## See Also
<a name="API_LaunchTemplateCapacityReservationSpecificationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/LaunchTemplateCapacityReservationSpecificationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/LaunchTemplateCapacityReservationSpecificationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/LaunchTemplateCapacityReservationSpecificationResponse)
