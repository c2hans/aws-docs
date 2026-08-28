---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationStatus.html
---

# CapacityReservationStatus
<a name="API_CapacityReservationStatus"></a>

Describes the availability of capacity for a Capacity Reservation.

## Contents
<a name="API_CapacityReservationStatus_Contents"></a>

 ** capacityReservationId **
The ID of the Capacity Reservation.
Type: String
Required: No

 ** totalAvailableCapacity **
The remaining capacity. Indicates the amount of resources that can be launched into the Capacity Reservation.
Type: Integer
Required: No

 ** totalCapacity **
The combined amount of `Available` and `Unavailable` capacity in the Capacity Reservation.
Type: Integer
Required: No

 ** totalUnavailableCapacity **
The used capacity. Indicates that the capacity is in use by resources that are running in the Capacity Reservation.
Type: Integer
Required: No

## See Also
<a name="API_CapacityReservationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
