---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_TaskFilter.html
---

# TaskFilter
<a name="API_TaskFilter"></a>

Filter criteria for listing backlog tasks, supporting time range, priority, status, and type filters.

## Contents
<a name="API_TaskFilter_Contents"></a>

 ** createdAfter **   <a name="devopsagent-Type-TaskFilter-createdAfter"></a>
Filter for tasks created after this timestamp inclusive
Type: Timestamp
Required: No

 ** createdBefore **   <a name="devopsagent-Type-TaskFilter-createdBefore"></a>
Filter for tasks created before this timestamp exclusive
Type: Timestamp
Required: No

 ** primaryTaskId **   <a name="devopsagent-Type-TaskFilter-primaryTaskId"></a>
Filter by primary task ID to get linked tasks
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: No

 ** priority **   <a name="devopsagent-Type-TaskFilter-priority"></a>
Filter by priority (single value only)
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | MINIMAL`
Required: No

 ** status **   <a name="devopsagent-Type-TaskFilter-status"></a>
Filter by status (single value only)
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `PENDING_TRIAGE | LINKED | PENDING_START | IN_PROGRESS | PENDING_CUSTOMER_APPROVAL | COMPLETED | FAILED | TIMED_OUT | CANCELED | SKIPPED | WAITING`
Required: No

 ** taskType **   <a name="devopsagent-Type-TaskFilter-taskType"></a>
Filter by task type (single value only)
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `INVESTIGATION | EVALUATION | RELEASE_READINESS_REVIEW | RELEASE_TESTING`
Required: No

## See Also
<a name="API_TaskFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/TaskFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/TaskFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/TaskFilter)
