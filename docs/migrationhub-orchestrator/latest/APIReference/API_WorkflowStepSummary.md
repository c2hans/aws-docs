---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepSummary.html
---

# WorkflowStepSummary
<a name="API_WorkflowStepSummary"></a>

The summary of the step in a migration workflow.

## Contents
<a name="API_WorkflowStepSummary_Contents"></a>

 ** description **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-description"></a>
The description of the step.
Type: String
Required: No

 ** name **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-name"></a>
The name of the step.
Type: String
Required: No

 ** next **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** noOfSrvCompleted **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-noOfSrvCompleted"></a>
The number of servers that have been migrated.
Type: Integer
Required: No

 ** noOfSrvFailed **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-noOfSrvFailed"></a>
The number of servers that have failed to migrate.
Type: Integer
Required: No

 ** owner **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-owner"></a>
The owner of the step.
Type: String
Valid Values: `AWS_MANAGED | CUSTOM`
Required: No

 ** previous **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** scriptLocation **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-scriptLocation"></a>
The location of the script.
Type: String
Required: No

 ** status **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-status"></a>
The status of the step.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | SKIPPED | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | USER_ATTENTION_REQUIRED`
Required: No

 ** statusMessage **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-statusMessage"></a>
The status message of the migration workflow.
Type: String
Required: No

 ** stepActionType **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`
Required: No

 ** stepId **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-stepId"></a>
The ID of the step.
Type: String
Required: No

 ** totalNoOfSrv **   <a name="migrationhuborchestrator-Type-WorkflowStepSummary-totalNoOfSrv"></a>
The total number of servers that have been migrated.
Type: Integer
Required: No

## See Also
<a name="API_WorkflowStepSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/WorkflowStepSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/WorkflowStepSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/WorkflowStepSummary)
