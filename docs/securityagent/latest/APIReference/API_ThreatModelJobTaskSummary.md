---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatModelJobTaskSummary.html
---

# ThreatModelJobTaskSummary
<a name="API_ThreatModelJobTaskSummary"></a>

Contains summary information about a threat model job task.

## Contents
<a name="API_ThreatModelJobTaskSummary_Contents"></a>

 ** taskId **   <a name="securityagent-Type-ThreatModelJobTaskSummary-taskId"></a>
The unique identifier of the task.
Type: String
Required: Yes

 ** agentSpaceId **   <a name="securityagent-Type-ThreatModelJobTaskSummary-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-ThreatModelJobTaskSummary-createdAt"></a>
The date and time the task was created, in UTC format.
Type: Timestamp
Required: No

 ** executionStatus **   <a name="securityagent-Type-ThreatModelJobTaskSummary-executionStatus"></a>
The current execution status of the task.
Type: String
Valid Values: `IN_PROGRESS | ABORTED | COMPLETED | INTERNAL_ERROR | FAILED`
Required: No

 ** threatModelId **   <a name="securityagent-Type-ThreatModelJobTaskSummary-threatModelId"></a>
The unique identifier of the threat model associated with the task.
Type: String
Required: No

 ** threatModelJobId **   <a name="securityagent-Type-ThreatModelJobTaskSummary-threatModelJobId"></a>
The unique identifier of the threat model job that contains the task.
Type: String
Required: No

 ** title **   <a name="securityagent-Type-ThreatModelJobTaskSummary-title"></a>
The title of the task.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatModelJobTaskSummary-updatedAt"></a>
The date and time the task was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ThreatModelJobTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatModelJobTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatModelJobTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatModelJobTaskSummary)
