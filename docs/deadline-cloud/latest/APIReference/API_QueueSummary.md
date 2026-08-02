---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_QueueSummary.html
---

# QueueSummary
<a name="API_QueueSummary"></a>

The details of a queue summary.

## Contents
<a name="API_QueueSummary_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-QueueSummary-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-QueueSummary-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** defaultBudgetAction **   <a name="deadlinecloud-Type-QueueSummary-defaultBudgetAction"></a>
The default action taken on a queue summary if a budget wasn't configured.
Type: String
Valid Values: `NONE | STOP_SCHEDULING_AND_COMPLETE_TASKS | STOP_SCHEDULING_AND_CANCEL_TASKS`
Required: Yes

 ** displayName **   <a name="deadlinecloud-Type-QueueSummary-displayName"></a>
The display name of the queue summary to update.
This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-QueueSummary-farmId"></a>
The farm ID.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-QueueSummary-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** status **   <a name="deadlinecloud-Type-QueueSummary-status"></a>
That status of the queue.
Type: String
Valid Values: `IDLE | SCHEDULING | SCHEDULING_BLOCKED`
Required: Yes

 ** blockedReason **   <a name="deadlinecloud-Type-QueueSummary-blockedReason"></a>
The reason the queue is blocked, if applicable.
Type: String
Valid Values: `NO_BUDGET_CONFIGURED | BUDGET_THRESHOLD_REACHED`
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-QueueSummary-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-QueueSummary-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_QueueSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/QueueSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/QueueSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/QueueSummary)
