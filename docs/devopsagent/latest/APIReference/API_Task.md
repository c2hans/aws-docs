---
source_url: https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_Task.html
---

# Task
<a name="API_Task"></a>

Represents a backlog task with all its properties and metadata

## Contents
<a name="API_Task_Contents"></a>

 ** agentSpaceId **   <a name="devopsagent-Type-Task-agentSpaceId"></a>
The unique identifier for the agent space containing this task
Type: String
Required: Yes

 ** createdAt **   <a name="devopsagent-Type-Task-createdAt"></a>
Timestamp when this task was created
Type: Timestamp
Required: Yes

 ** priority **   <a name="devopsagent-Type-Task-priority"></a>
The priority level of this task
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | MINIMAL`
Required: Yes

 ** status **   <a name="devopsagent-Type-Task-status"></a>
The current status of this task
Type: String
Valid Values: `PENDING_TRIAGE | LINKED | PENDING_START | IN_PROGRESS | PENDING_CUSTOMER_APPROVAL | COMPLETED | FAILED | TIMED_OUT | CANCELED | SKIPPED | WAITING`
Required: Yes

 ** taskId **   <a name="devopsagent-Type-Task-taskId"></a>
The unique identifier for this task
Type: String
Required: Yes

 ** taskType **   <a name="devopsagent-Type-Task-taskType"></a>
The type of this task
Type: String
Valid Values: `INVESTIGATION | EVALUATION | RELEASE_READINESS_REVIEW | RELEASE_TESTING`
Required: Yes

 ** title **   <a name="devopsagent-Type-Task-title"></a>
The title of the task
Type: String
Required: Yes

 ** updatedAt **   <a name="devopsagent-Type-Task-updatedAt"></a>
Timestamp when this task was last updated
Type: Timestamp
Required: Yes

 ** version **   <a name="devopsagent-Type-Task-version"></a>
Version number for optimistic locking
Type: Integer
Required: Yes

 ** description **   <a name="devopsagent-Type-Task-description"></a>
Optional detailed description of the task
Type: String
Required: No

 ** executionId **   <a name="devopsagent-Type-Task-executionId"></a>
The execution ID associated with this task, if any
Type: String
Required: No

 ** hasLinkedTasks **   <a name="devopsagent-Type-Task-hasLinkedTasks"></a>
Indicates if this task has other tasks linked to it
Type: Boolean
Required: No

 ** metadata **   <a name="devopsagent-Type-Task-metadata"></a>
Optional metadata for the task
Type: JSON value
Required: No

 ** primaryTaskId **   <a name="devopsagent-Type-Task-primaryTaskId"></a>
The task ID of the primary investigation this task is linked to
Type: String
Required: No

 ** reference **   <a name="devopsagent-Type-Task-reference"></a>
Optional reference information linking this task to external systems
Type: [ReferenceOutput](API_ReferenceOutput.md) object
Required: No

 ** statusReason **   <a name="devopsagent-Type-Task-statusReason"></a>
Explanation for why the task status was changed (e.g., linked reason)
Type: String
Required: No

 ** supportMetadata **   <a name="devopsagent-Type-Task-supportMetadata"></a>
Optional support metadata for the task
Type: JSON value
Required: No

## See Also
<a name="API_Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-agent-2026-01-01/Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-agent-2026-01-01/Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-agent-2026-01-01/Task)
