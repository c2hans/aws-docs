---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetectMitigationActionsTaskSummary.html
---

# DetectMitigationActionsTaskSummary
<a name="API_DetectMitigationActionsTaskSummary"></a>

 The summary of the mitigation action tasks.

## Contents
<a name="API_DetectMitigationActionsTaskSummary_Contents"></a>

 ** actionsDefinition **   <a name="iot-Type-DetectMitigationActionsTaskSummary-actionsDefinition"></a>
 The definition of the actions.
Type: Array of [MitigationAction](API_MitigationAction.md) objects
Required: No

 ** onlyActiveViolationsIncluded **   <a name="iot-Type-DetectMitigationActionsTaskSummary-onlyActiveViolationsIncluded"></a>
 Includes only active violations.
Type: Boolean
Required: No

 ** suppressedAlertsIncluded **   <a name="iot-Type-DetectMitigationActionsTaskSummary-suppressedAlertsIncluded"></a>
 Includes suppressed alerts.
Type: Boolean
Required: No

 ** target **   <a name="iot-Type-DetectMitigationActionsTaskSummary-target"></a>
 Specifies the ML Detect findings to which the mitigation actions are applied.
Type: [DetectMitigationActionsTaskTarget](API_DetectMitigationActionsTaskTarget.md) object
Required: No

 ** taskEndTime **   <a name="iot-Type-DetectMitigationActionsTaskSummary-taskEndTime"></a>
 The date the task ended.
Type: Timestamp
Required: No

 ** taskId **   <a name="iot-Type-DetectMitigationActionsTaskSummary-taskId"></a>
 The unique identifier of the task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** taskStartTime **   <a name="iot-Type-DetectMitigationActionsTaskSummary-taskStartTime"></a>
 The date the task started.
Type: Timestamp
Required: No

 ** taskStatistics **   <a name="iot-Type-DetectMitigationActionsTaskSummary-taskStatistics"></a>
 The statistics of a mitigation action task.
Type: [DetectMitigationActionsTaskStatistics](API_DetectMitigationActionsTaskStatistics.md) object
Required: No

 ** taskStatus **   <a name="iot-Type-DetectMitigationActionsTaskSummary-taskStatus"></a>
 The status of the task.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | CANCELED`
Required: No

 ** violationEventOccurrenceRange **   <a name="iot-Type-DetectMitigationActionsTaskSummary-violationEventOccurrenceRange"></a>
 Specifies the time period of which violation events occurred between.
Type: [ViolationEventOccurrenceRange](API_ViolationEventOccurrenceRange.md) object
Required: No

## See Also
<a name="API_DetectMitigationActionsTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetectMitigationActionsTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetectMitigationActionsTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetectMitigationActionsTaskSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
