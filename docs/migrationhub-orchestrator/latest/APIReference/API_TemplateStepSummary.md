---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TemplateStepSummary.html
---

# TemplateStepSummary
<a name="API_TemplateStepSummary"></a>

The summary of the step.

## Contents
<a name="API_TemplateStepSummary_Contents"></a>

 ** id **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-id"></a>
The ID of the step.
Type: String
Required: No

 ** name **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-name"></a>
The name of the step.
Type: String
Required: No

 ** next **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-next"></a>
The next step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** owner **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-owner"></a>
The owner of the step.
Type: String
Valid Values: `AWS_MANAGED | CUSTOM`
Required: No

 ** previous **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-previous"></a>
The previous step.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** stepActionType **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-stepActionType"></a>
The action type of the step. You must run and update the status of a manual step for the workflow to continue after the completion of the step.
Type: String
Valid Values: `MANUAL | AUTOMATED`
Required: No

 ** stepGroupId **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-stepGroupId"></a>
The ID of the step group.
Type: String
Required: No

 ** targetType **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-targetType"></a>
The servers on which to run the script.
Type: String
Valid Values: `SINGLE | ALL | NONE`
Required: No

 ** templateId **   <a name="migrationhuborchestrator-Type-TemplateStepSummary-templateId"></a>
The ID of the template.
Type: String
Required: No

## See Also
<a name="API_TemplateStepSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/TemplateStepSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/TemplateStepSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/TemplateStepSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Migration Hub Orchestrator. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-orchestrator` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
