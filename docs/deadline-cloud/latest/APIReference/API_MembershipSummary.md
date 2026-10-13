---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_MembershipSummary.html
---

# MembershipSummary
<a name="API_MembershipSummary"></a>

A membership record for a principal on a single Deadline Cloud resource. The summary identifies the resource that the principal is a member of and the principal's membership level for that resource.

## Contents
<a name="API_MembershipSummary_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** farm **   <a name="deadlinecloud-Type-MembershipSummary-farm"></a>
A membership on a farm.
Type: [FarmMember](API_FarmMember.md) object
Required: No

 ** fleet **   <a name="deadlinecloud-Type-MembershipSummary-fleet"></a>
A membership on a fleet.
Type: [FleetMember](API_FleetMember.md) object
Required: No

 ** job **   <a name="deadlinecloud-Type-MembershipSummary-job"></a>
A membership on a job.
Type: [JobMember](API_JobMember.md) object
Required: No

 ** queue **   <a name="deadlinecloud-Type-MembershipSummary-queue"></a>
A membership on a queue.
Type: [QueueMember](API_QueueMember.md) object
Required: No

## See Also
<a name="API_MembershipSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/MembershipSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/MembershipSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/MembershipSummary)
