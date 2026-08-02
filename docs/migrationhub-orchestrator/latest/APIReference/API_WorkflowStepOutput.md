---
source_url: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_WorkflowStepOutput.html
---

# WorkflowStepOutput
<a name="API_WorkflowStepOutput"></a>

The output of a step.

## Contents
<a name="API_WorkflowStepOutput_Contents"></a>

 ** dataType **   <a name="migrationhuborchestrator-Type-WorkflowStepOutput-dataType"></a>
The data type of the output.
Type: String
Valid Values: `STRING | INTEGER | STRINGLIST | STRINGMAP`
Required: No

 ** name **   <a name="migrationhuborchestrator-Type-WorkflowStepOutput-name"></a>
The name of the step.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-a-zA-Z0-9_.+]+[-a-zA-Z0-9_.+ ]*`
Required: No

 ** required **   <a name="migrationhuborchestrator-Type-WorkflowStepOutput-required"></a>
Determine if an output is required from a step.
Type: Boolean
Required: No

 ** value **   <a name="migrationhuborchestrator-Type-WorkflowStepOutput-value"></a>
The value of the output.
Type: [WorkflowStepOutputUnion](API_WorkflowStepOutputUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_WorkflowStepOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhuborchestrator-2021-08-28/WorkflowStepOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhuborchestrator-2021-08-28/WorkflowStepOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhuborchestrator-2021-08-28/WorkflowStepOutput)
