---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InterruptibleCapacityAllocation.html
---

# InterruptibleCapacityAllocation
<a name="API_InterruptibleCapacityAllocation"></a>

 Represents the allocation of capacity from a source reservation to an interruptible reservation, tracking current and target instance counts for allocation management.

## Contents
<a name="API_InterruptibleCapacityAllocation_Contents"></a>

 ** instanceCount **
 The current number of instances allocated to the interruptible reservation.
Type: Integer
Required: No

 ** interruptibleCapacityReservationId **
 The ID of the interruptible Capacity Reservation created from the allocation.
Type: String
Required: No

 ** interruptionType **
 The type of interruption policy applied to the interruptible reservation.
Type: String
Valid Values: `adhoc`
Required: No

 ** status **
 The current status of the allocation (updating during reclamation, active when complete).
Type: String
Valid Values: `pending | active | updating | canceling | canceled | failed`
Required: No

 ** targetInstanceCount **
 After your modify request, the requested number of instances allocated to interruptible reservation.
Type: Integer
Required: No

## See Also
<a name="API_InterruptibleCapacityAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InterruptibleCapacityAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InterruptibleCapacityAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InterruptibleCapacityAllocation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
