---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetStepItem.html
---

# BatchGetStepItem
<a name="API_BatchGetStepItem"></a>

The details of a step returned in a batch get operation.

## Contents
<a name="API_BatchGetStepItem_Contents"></a>

 ** createdAt **   <a name="deadlinecloud-Type-BatchGetStepItem-createdAt"></a>
The date and time the resource was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="deadlinecloud-Type-BatchGetStepItem-createdBy"></a>
The user or system that created this resource.
Type: String
Required: Yes

 ** farmId **   <a name="deadlinecloud-Type-BatchGetStepItem-farmId"></a>
The farm ID of the step.
Type: String
Pattern: `farm-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-BatchGetStepItem-jobId"></a>
The job ID of the step.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** lifecycleStatus **   <a name="deadlinecloud-Type-BatchGetStepItem-lifecycleStatus"></a>
The life cycle status of the step.
Type: String
Valid Values: `CREATE_COMPLETE | UPDATE_IN_PROGRESS | UPDATE_FAILED | UPDATE_SUCCEEDED`
Required: Yes

 ** name **   <a name="deadlinecloud-Type-BatchGetStepItem-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** queueId **   <a name="deadlinecloud-Type-BatchGetStepItem-queueId"></a>
The queue ID of the step.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-BatchGetStepItem-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** taskRunStatus **   <a name="deadlinecloud-Type-BatchGetStepItem-taskRunStatus"></a>
The task run status for the step.
Type: String
Valid Values: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** taskRunStatusCounts **   <a name="deadlinecloud-Type-BatchGetStepItem-taskRunStatusCounts"></a>
The number of tasks for each run status for the step.
Type: String to integer map
Valid Keys: `PENDING | READY | ASSIGNED | STARTING | SCHEDULED | INTERRUPTING | RUNNING | SUSPENDED | CANCELED | FAILED | SUCCEEDED | NOT_COMPATIBLE`
Required: Yes

 ** dependencyCounts **   <a name="deadlinecloud-Type-BatchGetStepItem-dependencyCounts"></a>
The number of dependencies for the step.
Type: [DependencyCounts](API_DependencyCounts.md) object
Required: No

 ** description **   <a name="deadlinecloud-Type-BatchGetStepItem-description"></a>
The description of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** endedAt **   <a name="deadlinecloud-Type-BatchGetStepItem-endedAt"></a>
The date and time the resource ended running.
Type: Timestamp
Required: No

 ** lifecycleStatusMessage **   <a name="deadlinecloud-Type-BatchGetStepItem-lifecycleStatusMessage"></a>
A message that communicates the status of the life cycle.
Type: String
Required: No

 ** parameterSpace **   <a name="deadlinecloud-Type-BatchGetStepItem-parameterSpace"></a>
The parameter space for the step.
Type: [ParameterSpace](API_ParameterSpace.md) object
Required: No

 ** requiredCapabilities **   <a name="deadlinecloud-Type-BatchGetStepItem-requiredCapabilities"></a>
The required capabilities for the step.
Type: [StepRequiredCapabilities](API_StepRequiredCapabilities.md) object
Required: No

 ** startedAt **   <a name="deadlinecloud-Type-BatchGetStepItem-startedAt"></a>
The date and time the resource started running.
Type: Timestamp
Required: No

 ** targetTaskRunStatus **   <a name="deadlinecloud-Type-BatchGetStepItem-targetTaskRunStatus"></a>
The task status to start with on the step.
Type: String
Valid Values: `READY | FAILED | SUCCEEDED | CANCELED | SUSPENDED | PENDING`
Required: No

 ** taskFailureRetryCount **   <a name="deadlinecloud-Type-BatchGetStepItem-taskFailureRetryCount"></a>
The number of times that tasks failed and were retried.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.
Required: No

 ** updatedAt **   <a name="deadlinecloud-Type-BatchGetStepItem-updatedAt"></a>
The date and time the resource was updated.
Type: Timestamp
Required: No

 ** updatedBy **   <a name="deadlinecloud-Type-BatchGetStepItem-updatedBy"></a>
The user or system that updated this resource.
Type: String
Required: No

## See Also
<a name="API_BatchGetStepItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/BatchGetStepItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/BatchGetStepItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/BatchGetStepItem)
