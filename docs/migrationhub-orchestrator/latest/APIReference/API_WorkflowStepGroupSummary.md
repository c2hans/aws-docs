---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepGroupSummary.html
---

# WorkflowStepGroupSummary
<a name="API_WorkflowStepGroupSummary"></a>

The summary of a step group in a workflow.

## Contents
<a name="API_WorkflowStepGroupSummary_Contents"></a>

 ** id **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-id"></a>
The ID of the step group.
Type: String
Required: No

 ** name **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-name"></a>
The name of the step group.
Type: String
Required: No

 ** next **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-next"></a>
The next step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** owner **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-owner"></a>
The owner of the step group.
Type: String
Valid Values: `AWS_MANAGED | CUSTOM`
Required: No

 ** previous **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-previous"></a>
The previous step group.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** status **   <a name="migrationhuborchestrator-Type-WorkflowStepGroupSummary-status"></a>
The status of the step group.
Type: String
Valid Values: `AWAITING_DEPENDENCIES | READY | IN_PROGRESS | COMPLETED | FAILED | PAUSED | PAUSING | USER_ATTENTION_REQUIRED`
Required: No

## See Also
<a name="API_WorkflowStepGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/WorkflowStepGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/WorkflowStepGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/WorkflowStepGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
