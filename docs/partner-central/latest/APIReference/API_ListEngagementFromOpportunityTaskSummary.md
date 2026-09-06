---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListEngagementFromOpportunityTaskSummary.html
---

# ListEngagementFromOpportunityTaskSummary
<a name="API_ListEngagementFromOpportunityTaskSummary"></a>

 Provides a summary of a task related to creating an engagement from an opportunity. This structure contains key information about the task's status, associated identifiers, and any failure details.

## Contents
<a name="API_ListEngagementFromOpportunityTaskSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** EngagementId **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-EngagementId"></a>
 The unique identifier of the engagement created as a result of the task. This field is populated when the task is completed successfully.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** EngagementInvitationId **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-EngagementInvitationId"></a>
The unique identifier of the Engagement Invitation.
Type: String
Pattern: `engi-[0-9,a-z]{13}`
Required: No

 ** Message **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-Message"></a>
 A detailed message providing additional information about the task, especially useful in case of failures. This field may contain error details or other relevant information about the task's execution
Type: String
Required: No

 ** OpportunityId **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-OpportunityId"></a>
 The unique identifier of the original Opportunity from which the Engagement is being created. This field helps track the source of the Engagement creation task.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** ReasonCode **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-ReasonCode"></a>
 A code indicating the specific reason for a task failure. This field is populated when the task status is FAILED and provides a categorized reason for the failure.
Type: String
Valid Values: `InvitationAccessDenied | InvitationValidationFailed | EngagementAccessDenied | OpportunityAccessDenied | ResourceSnapshotJobAccessDenied | ResourceSnapshotJobValidationFailed | ResourceSnapshotJobConflict | EngagementValidationFailed | EngagementConflict | OpportunitySubmissionFailed | EngagementInvitationConflict | InternalError | OpportunityValidationFailed | OpportunityConflict | ResourceSnapshotAccessDenied | ResourceSnapshotValidationFailed | ResourceSnapshotConflict | ServiceQuotaExceeded | RequestThrottled | ContextNotFound | CustomerProjectContextNotPermitted | DisqualifiedLeadNotPermitted`
Required: No

 ** ResourceSnapshotJobId **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-ResourceSnapshotJobId"></a>
 The identifier of the resource snapshot job associated with this task, if a snapshot was created as part of the Engagement creation process.
Type: String
Pattern: `job-[0-9a-z]{13}`
Required: No

 ** StartTime **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-StartTime"></a>
 The timestamp indicating when the task was initiated, in RFC 3339 5.6 date-time format.
Type: Timestamp
Required: No

 ** TaskArn **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-TaskArn"></a>
 The Amazon Resource Name (ARN) uniquely identifying this task within AWS. This ARN can be used for referencing the task in other AWS services or APIs.
Type: String
Pattern: `arn:.*`
Required: No

 ** TaskId **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-TaskId"></a>
 A unique identifier for a specific task.
Type: String
Pattern: `.*task-[0-9a-z]{13}`
Required: No

 ** TaskStatus **   <a name="AWSPartnerCentral-Type-ListEngagementFromOpportunityTaskSummary-TaskStatus"></a>
 The current status of the task.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_ListEngagementFromOpportunityTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListEngagementFromOpportunityTaskSummary)
