---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AbbreviatedExecution.html
---

# AbbreviatedExecution
<a name="API_AbbreviatedExecution"></a>

A summarized representation of a plan execution. This structure contains key information about an execution without all the detailed step data.

## Contents
<a name="API_AbbreviatedExecution_Contents"></a>

 ** executionAction **   <a name="regionswitch-Type-AbbreviatedExecution-executionAction"></a>
The plan execution action. Valid values are `activate`, to activate an AWS Region, or `deactivate`, to deactivate a Region.
Type: String
Valid Values: `activate | deactivate | postRecovery`
Required: Yes

 ** executionId **   <a name="regionswitch-Type-AbbreviatedExecution-executionId"></a>
The execution identifier of a plan execution.
Type: String
Required: Yes

 ** executionRegion **   <a name="regionswitch-Type-AbbreviatedExecution-executionRegion"></a>
The AWS Region for a plan execution.
Type: String
Required: Yes

 ** executionState **   <a name="regionswitch-Type-AbbreviatedExecution-executionState"></a>
The plan execution state. Provides the state of a plan execution, for example, In Progress or Paused by Operator.
Type: String
Valid Values: `inProgress | pausedByFailedStep | pausedByOperator | completed | completedWithExceptions | canceled | planExecutionTimedOut | pendingManualApproval | failed | pending | completedMonitoringApplicationHealth`
Required: Yes

 ** mode **   <a name="regionswitch-Type-AbbreviatedExecution-mode"></a>
The plan execution mode. Valid values are `graceful`, for graceful executions, or `ungraceful`, for ungraceful executions.
Type: String
Valid Values: `graceful | ungraceful`
Required: Yes

 ** planArn **   <a name="regionswitch-Type-AbbreviatedExecution-planArn"></a>
The Amazon Resource Name (ARN) of the plan.
Type: String
Pattern: `arn:aws[a-zA-Z-]*:arc-region-switch::[0-9]{12}:plan/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,30}[a-zA-Z0-9])?):([a-z0-9]{6})`
Required: Yes

 ** startTime **   <a name="regionswitch-Type-AbbreviatedExecution-startTime"></a>
The timestamp when the plan execution was started.
Type: Timestamp
Required: Yes

 ** actualRecoveryTime **   <a name="regionswitch-Type-AbbreviatedExecution-actualRecoveryTime"></a>
The actual recovery time that Region switch calculates for a plan execution. Actual recovery time includes the time for the plan to run added to the time elapsed until the application health alarms that you've specified are healthy again.
Type: String
Pattern: `P(?!$)(\d+Y)?(\d+M)?(\d+D)?(T(?=\d)(\d+H)?(\d+M)?(\d+S)?)?`
Required: No

 ** comment **   <a name="regionswitch-Type-AbbreviatedExecution-comment"></a>
An optional comment about the plan execution.
Type: String
Required: No

 ** endTime **   <a name="regionswitch-Type-AbbreviatedExecution-endTime"></a>
The timestamp when the plan execution was ended.
Type: Timestamp
Required: No

 ** recoveryExecutionId **   <a name="regionswitch-Type-AbbreviatedExecution-recoveryExecutionId"></a>
The unique identifier of the most recent recovery execution. Required when starting a post-recovery execution.
Type: String
Required: No

 ** updatedAt **   <a name="regionswitch-Type-AbbreviatedExecution-updatedAt"></a>
The timestamp when the plan execution was last updated.
Type: Timestamp
Required: No

 ** version **   <a name="regionswitch-Type-AbbreviatedExecution-version"></a>
The version for the plan.
Type: String
Required: No

## See Also
<a name="API_AbbreviatedExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/AbbreviatedExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/AbbreviatedExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/AbbreviatedExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query arc-region-switch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
