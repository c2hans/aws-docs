---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CapacityReservationSpecification.html
---

# CapacityReservationSpecification
<a name="API_CapacityReservationSpecification"></a>

 Describes the Capacity Reservation preference and targeting options. If you specify `open` or `none` for `CapacityReservationPreference`, do not specify a `CapacityReservationTarget`.

## Contents
<a name="API_CapacityReservationSpecification_Contents"></a>

 ** CapacityReservationPreference **
 The capacity reservation preference. The following options are available:
+  `capacity-reservations-only` - Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation resource group. If capacity isn't available, instances will fail to launch.
+  `capacity-reservations-first` - Auto Scaling will try to launch instances into a Capacity Reservation or Capacity Reservation resource group first. If capacity isn't available, instances will run in On-Demand capacity.
+  `none` - Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity.
+  `default` - Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.
Type: String
Valid Values: `capacity-reservations-only | capacity-reservations-first | none | default`
Required: No

 ** CapacityReservationTarget **
 Describes a target Capacity Reservation or Capacity Reservation resource group.
Type: [CapacityReservationTarget](API_CapacityReservationTarget.md) object
Required: No

## See Also
<a name="API_CapacityReservationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/CapacityReservationSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/CapacityReservationSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/CapacityReservationSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
