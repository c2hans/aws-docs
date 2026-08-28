---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_QueueLimitAssociationSummary.html
---

# QueueLimitAssociationSummary
<a name="API_QueueLimitAssociationSummary"></a>

Provides information about the association between a queue and a limit.

## Contents
<a name="API_QueueLimitAssociationSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-createdAt"></a>
The Unix timestamp of the date and time that the association was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-createdBy"></a>
The user identifier of the person that created the association.
Type: String
Required: Yes

 ** limitId **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-limitId"></a>
The unique identifier of the limit in the association.
Type: String
Pattern: `limit-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-queueId"></a>
The unique identifier of the queue in the association.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-status"></a>
The status of task scheduling in the queue-limit association.
+  `ACTIVE` - Association is active.
+  `STOP_LIMIT_USAGE_AND_COMPLETE_TASKS` - Association has stopped scheduling new tasks and is completing current tasks.
+  `STOP_LIMIT_USAGE_AND_CANCEL_TASKS` - Association has stopped scheduling new tasks and is canceling current tasks.
+  `STOPPED` - Association has been stopped.
Type: String
Valid Values: `ACTIVE | STOP_LIMIT_USAGE_AND_COMPLETE_TASKS | STOP_LIMIT_USAGE_AND_CANCEL_TASKS | STOPPED`
Required: Yes

 ** updatedAt **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-updatedAt"></a>
The Unix timestamp of the date and time that the association was last updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-QueueLimitAssociationSummary-updatedBy"></a>
The user identifier of the person that updated the association.
Type: String
Required: No

## See Also
<a name="API_QueueLimitAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueLimitAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueLimitAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueLimitAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
