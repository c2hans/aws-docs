---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CapacityReservation.html
---

# CapacityReservation
<a name="API_CapacityReservation"></a>

A reservation for a specified number of data processing units (DPUs). When a reservation is initially created, it has no DPUs. Athena allocates DPUs until the allocated amount equals the requested amount.

## Contents
<a name="API_CapacityReservation_Contents"></a>

 ** AllocatedDpus **   <a name="athena-Type-CapacityReservation-AllocatedDpus"></a>
The number of data processing units currently allocated.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** CreationTime **   <a name="athena-Type-CapacityReservation-CreationTime"></a>
The time in UTC epoch millis when the capacity reservation was created.
Type: Timestamp
Required: Yes

 ** Name **   <a name="athena-Type-CapacityReservation-Name"></a>
The name of the capacity reservation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._-]+`
Required: Yes

 ** Status **   <a name="athena-Type-CapacityReservation-Status"></a>
The status of the capacity reservation.
Type: String
Valid Values: `PENDING | ACTIVE | CANCELLING | CANCELLED | FAILED | UPDATE_PENDING`
Required: Yes

 ** TargetDpus **   <a name="athena-Type-CapacityReservation-TargetDpus"></a>
The number of data processing units requested.
Type: Integer
Valid Range: Minimum value of 4.
Required: Yes

 ** LastAllocation **   <a name="athena-Type-CapacityReservation-LastAllocation"></a>
Contains the submission time of a single allocation request for a capacity reservation and the most recent status of the attempted allocation.
Type: [CapacityAllocation](API_CapacityAllocation.md) object
Required: No

 ** LastSuccessfulAllocationTime **   <a name="athena-Type-CapacityReservation-LastSuccessfulAllocationTime"></a>
The time of the most recent capacity allocation that succeeded.
Type: Timestamp
Required: No

## See Also
<a name="API_CapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CapacityReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
