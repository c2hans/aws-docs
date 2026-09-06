---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementByAcceptingInvitationTaskSummary.html
---

# ListEngagementByAcceptingInvitationTaskSummary
<a name="API_ListEngagementByAcceptingInvitationTaskSummary"></a>

 Specifies a subset of fields associated with tasks related to accepting an engagement invitation.

## Contents
<a name="API_ListEngagementByAcceptingInvitationTaskSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EngagementInvitationId **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-EngagementInvitationId"></a>
 The unique identifier of the engagement invitation that was accepted.
Type: String
Pattern: `engi-[0-9,a-z]{13}`
Required: No

 ** Message **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-Message"></a>
 Detailed message describing the failure and possible recovery steps.
Type: String
Required: No

 ** OpportunityId **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-OpportunityId"></a>
 Unique identifier of opportunity that was created.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** ReasonCode **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-ReasonCode"></a>
 A code pointing to the specific reason for the failure.
Type: String
Valid Values: `InvitationAccessDenied | InvitationValidationFailed | EngagementAccessDenied | OpportunityAccessDenied | ResourceSnapshotJobAccessDenied | ResourceSnapshotJobValidationFailed | ResourceSnapshotJobConflict | EngagementValidationFailed | EngagementConflict | OpportunitySubmissionFailed | EngagementInvitationConflict | InternalError | OpportunityValidationFailed | OpportunityConflict | ResourceSnapshotAccessDenied | ResourceSnapshotValidationFailed | ResourceSnapshotConflict | ServiceQuotaExceeded | RequestThrottled | ContextNotFound | CustomerProjectContextNotPermitted | DisqualifiedLeadNotPermitted`
Required: No

 ** ResourceSnapshotJobId **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-ResourceSnapshotJobId"></a>
 Unique identifier of the resource snapshot job that was created.
Type: String
Pattern: `job-[0-9a-z]{13}`
Required: No

 ** StartTime **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-StartTime"></a>
 Task start timestamp.
Type: Timestamp
Required: No

 ** TaskArn **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-TaskArn"></a>
 The Amazon Resource Name (ARN) that uniquely identifies the task.
Type: String
Pattern: `arn:.*`
Required: No

 ** TaskId **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-TaskId"></a>
 Unique identifier of the task.
Type: String
Pattern: `.*task-[0-9a-z]{13}`
Required: No

 ** TaskStatus **   <a name="AWSPartnerCentral-Type-ListEngagementByAcceptingInvitationTaskSummary-TaskStatus"></a>
 Status of the task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_ListEngagementByAcceptingInvitationTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementByAcceptingInvitationTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementByAcceptingInvitationTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementByAcceptingInvitationTaskSummary)
