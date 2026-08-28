---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_PullRequestEvent.html
---

# PullRequestEvent
<a name="API_PullRequestEvent"></a>

Returns information about a pull request event.

## Contents
<a name="API_PullRequestEvent_Contents"></a>

 ** actorArn **   <a name="CodeCommit-Type-PullRequestEvent-actorArn"></a>
The Amazon Resource Name (ARN) of the user whose actions resulted in the event. Examples include updating the pull request with more commits or changing the status of a pull request.
Type: String
Required: No

 ** approvalRuleEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-approvalRuleEventMetadata"></a>
Information about a pull request event.
Type: [ApprovalRuleEventMetadata](API_ApprovalRuleEventMetadata.md) object
Required: No

 ** approvalRuleOverriddenEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-approvalRuleOverriddenEventMetadata"></a>
Information about an approval rule override event for a pull request.
Type: [ApprovalRuleOverriddenEventMetadata](API_ApprovalRuleOverriddenEventMetadata.md) object
Required: No

 ** approvalStateChangedEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-approvalStateChangedEventMetadata"></a>
Information about an approval state change for a pull request.
Type: [ApprovalStateChangedEventMetadata](API_ApprovalStateChangedEventMetadata.md) object
Required: No

 ** eventDate **   <a name="CodeCommit-Type-PullRequestEvent-eventDate"></a>
The day and time of the pull request event, in timestamp format.
Type: Timestamp
Required: No

 ** pullRequestCreatedEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestCreatedEventMetadata"></a>
Information about the source and destination branches for the pull request.
Type: [PullRequestCreatedEventMetadata](API_PullRequestCreatedEventMetadata.md) object
Required: No

 ** pullRequestEventType **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestEventType"></a>
The type of the pull request event (for example, a status change event (PULL\_REQUEST\_STATUS\_CHANGED) or update event (PULL\_REQUEST\_SOURCE\_REFERENCE\_UPDATED)).
Type: String
Valid Values: `PULL_REQUEST_CREATED | PULL_REQUEST_STATUS_CHANGED | PULL_REQUEST_SOURCE_REFERENCE_UPDATED | PULL_REQUEST_MERGE_STATE_CHANGED | PULL_REQUEST_APPROVAL_RULE_CREATED | PULL_REQUEST_APPROVAL_RULE_UPDATED | PULL_REQUEST_APPROVAL_RULE_DELETED | PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN | PULL_REQUEST_APPROVAL_STATE_CHANGED`
Required: No

 ** pullRequestId **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestId"></a>
The system-generated ID of the pull request.
Type: String
Required: No

 ** pullRequestMergedStateChangedEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestMergedStateChangedEventMetadata"></a>
Information about the change in mergability state for the pull request event.
Type: [PullRequestMergedStateChangedEventMetadata](API_PullRequestMergedStateChangedEventMetadata.md) object
Required: No

 ** pullRequestSourceReferenceUpdatedEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestSourceReferenceUpdatedEventMetadata"></a>
Information about the updated source branch for the pull request event.
Type: [PullRequestSourceReferenceUpdatedEventMetadata](API_PullRequestSourceReferenceUpdatedEventMetadata.md) object
Required: No

 ** pullRequestStatusChangedEventMetadata **   <a name="CodeCommit-Type-PullRequestEvent-pullRequestStatusChangedEventMetadata"></a>
Information about the change in status for the pull request event.
Type: [PullRequestStatusChangedEventMetadata](API_PullRequestStatusChangedEventMetadata.md) object
Required: No

## See Also
<a name="API_PullRequestEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/PullRequestEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/PullRequestEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/PullRequestEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
