---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatModelJobTask.html
---

# ThreatModelJobTask
<a name="API_ThreatModelJobTask"></a>

Represents an individual task within a threat model job.

## Contents
<a name="API_ThreatModelJobTask_Contents"></a>

 ** taskId **   <a name="securityagent-Type-ThreatModelJobTask-taskId"></a>
The unique identifier of the task.
Type: String
Required: Yes

 ** agentSpaceId **   <a name="securityagent-Type-ThreatModelJobTask-agentSpaceId"></a>
The unique identifier of the agent space.
Type: String
Required: No

 ** createdAt **   <a name="securityagent-Type-ThreatModelJobTask-createdAt"></a>
The date and time the task was created, in UTC format.
Type: Timestamp
Required: No

 ** description **   <a name="securityagent-Type-ThreatModelJobTask-description"></a>
A description of the task.
Type: String
Required: No

 ** executionStatus **   <a name="securityagent-Type-ThreatModelJobTask-executionStatus"></a>
The current execution status of the task.
Type: String
Valid Values: `IN_PROGRESS | ABORTED | COMPLETED | INTERNAL_ERROR | FAILED`
Required: No

 ** logsLocation **   <a name="securityagent-Type-ThreatModelJobTask-logsLocation"></a>
The location of the task execution logs.
Type: [LogLocation](API_LogLocation.md) object
Required: No

 ** threatModelId **   <a name="securityagent-Type-ThreatModelJobTask-threatModelId"></a>
The unique identifier of the threat model associated with the task.
Type: String
Required: No

 ** threatModelJobId **   <a name="securityagent-Type-ThreatModelJobTask-threatModelJobId"></a>
The unique identifier of the threat model job that contains the task.
Type: String
Required: No

 ** title **   <a name="securityagent-Type-ThreatModelJobTask-title"></a>
The title of the task.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatModelJobTask-updatedAt"></a>
The date and time the task was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ThreatModelJobTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatModelJobTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatModelJobTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatModelJobTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
