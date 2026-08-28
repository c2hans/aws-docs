---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ListOpportunityFromEngagementTaskSummary.html
---

# ListOpportunityFromEngagementTaskSummary
<a name="API_ListOpportunityFromEngagementTaskSummary"></a>

Provides a summary of a task related to creating an opportunity from an engagement. This structure contains key information about the task's status, associated identifiers, and any failure details for opportunity creation processes.

## Contents
<a name="API_ListOpportunityFromEngagementTaskSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ContextId **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-ContextId"></a>
The unique identifier of the engagement context associated with the opportunity creation task. This links the task to specific contextual information within the engagement.
Type: String
Pattern: `[1-9][0-9]*`
Required: No

 ** EngagementId **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-EngagementId"></a>
The unique identifier of the engagement from which the opportunity is being created. This field helps track the source of the opportunity creation task.
Type: String
Pattern: `eng-[0-9a-z]{14}`
Required: No

 ** Message **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-Message"></a>
A detailed message providing additional information about the task, especially useful in case of failures. This field may contain error details or other relevant information about the task's execution.
Type: String
Required: No

 ** OpportunityId **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-OpportunityId"></a>
The unique identifier of the opportunity created as a result of the task. This field is populated when the task is completed successfully.
Type: String
Pattern: `O[0-9]{1,19}`
Required: No

 ** ReasonCode **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-ReasonCode"></a>
A code indicating the specific reason for a task failure. This field is populated when the task status is FAILED and provides a categorized reason for the failure.
Type: String
Valid Values: `InvitationAccessDenied | InvitationValidationFailed | EngagementAccessDenied | OpportunityAccessDenied | ResourceSnapshotJobAccessDenied | ResourceSnapshotJobValidationFailed | ResourceSnapshotJobConflict | EngagementValidationFailed | EngagementConflict | OpportunitySubmissionFailed | EngagementInvitationConflict | InternalError | OpportunityValidationFailed | OpportunityConflict | ResourceSnapshotAccessDenied | ResourceSnapshotValidationFailed | ResourceSnapshotConflict | ServiceQuotaExceeded | RequestThrottled | ContextNotFound | CustomerProjectContextNotPermitted | DisqualifiedLeadNotPermitted`
Required: No

 ** ResourceSnapshotJobId **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-ResourceSnapshotJobId"></a>
The identifier of the resource snapshot job associated with this task, if a snapshot was created as part of the opportunity creation process.
Type: String
Pattern: `job-[0-9a-z]{13}`
Required: No

 ** StartTime **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-StartTime"></a>
The timestamp indicating when the task was initiated, in RFC 3339 format.
Type: Timestamp
Required: No

 ** TaskArn **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-TaskArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the task within AWS. This ARN can be used for referencing the task in other AWS services or APIs.
Type: String
Pattern: `arn:.*`
Required: No

 ** TaskId **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-TaskId"></a>
The unique identifier of the task for creating an opportunity from an engagement.
Type: String
Pattern: `.*task-[0-9a-z]{13}`
Required: No

 ** TaskStatus **   <a name="AWSPartnerCentral-Type-ListOpportunityFromEngagementTaskSummary-TaskStatus"></a>
The current status of the task. Valid values are COMPLETE, INPROGRESS, or FAILED.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_ListOpportunityFromEngagementTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ListOpportunityFromEngagementTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
