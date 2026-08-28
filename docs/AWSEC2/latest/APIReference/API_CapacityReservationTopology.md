---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationTopology.html
---

# CapacityReservationTopology
<a name="API_CapacityReservationTopology"></a>

Information about the Capacity Reservation topology.

## Contents
<a name="API_CapacityReservationTopology_Contents"></a>

 ** availabilityZone **
The name of the Availability Zone or Local Zone that the Capacity Reservation is in.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone or Local Zone that the Capacity Reservation is in.
Type: String
Required: No

 ** capacityBlockId **
The ID of the Capacity Block. This parameter is only supported for UltraServer instances and identifies instances within the UltraServer domain.
Type: String
Required: No

 ** capacityReservationId **
The ID of the Capacity Reservation.
Type: String
Required: No

 ** groupName **
The name of the placement group that the Capacity Reservation is in.
Type: String
Required: No

 ** instanceType **
The instance type.
Type: String
Required: No

 ** NetworkNodeSet.N **
The network nodes. The nodes are hashed based on your account. Capacity Reservations from different accounts running under the same server will return a different hashed list of strings.
The value is `null` or empty if:
+ The instance type is not supported.
+ The Capacity Reservation is in a state other than `active` or `pending`.
Type: Array of strings
Required: No

 ** state **
The current state of the Capacity Reservation. For the list of possible states, see [DescribeCapacityReservations](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html).
Type: String
Required: No

## See Also
<a name="API_CapacityReservationTopology_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationTopology)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationTopology)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationTopology)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
