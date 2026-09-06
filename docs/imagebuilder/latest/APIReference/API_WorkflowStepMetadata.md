---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowStepMetadata.html
---

# WorkflowStepMetadata
<a name="API_WorkflowStepMetadata"></a>

Runtime details and status for the workflow step.

## Contents
<a name="API_WorkflowStepMetadata_Contents"></a>

 ** action **   <a name="imagebuilder-Type-WorkflowStepMetadata-action"></a>
The step action name.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`
Required: No

 ** description **   <a name="imagebuilder-Type-WorkflowStepMetadata-description"></a>
Description of the workflow step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** endTime **   <a name="imagebuilder-Type-WorkflowStepMetadata-endTime"></a>
The timestamp when the workflow step finished.
Type: String
Required: No

 ** inputs **   <a name="imagebuilder-Type-WorkflowStepMetadata-inputs"></a>
Input parameters that Image Builder provides for the workflow step.
Type: String
Required: No

 ** message **   <a name="imagebuilder-Type-WorkflowStepMetadata-message"></a>
Detailed output message that the workflow step provides at runtime.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** name **   <a name="imagebuilder-Type-WorkflowStepMetadata-name"></a>
The name of the workflow step.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`
Required: No

 ** outputs **   <a name="imagebuilder-Type-WorkflowStepMetadata-outputs"></a>
The file names that the workflow step created as output for this runtime instance of the workflow.
Type: String
Required: No

 ** rollbackStatus **   <a name="imagebuilder-Type-WorkflowStepMetadata-rollbackStatus"></a>
Reports on the rollback status of the step, if applicable.
Type: String
Valid Values: `RUNNING | COMPLETED | SKIPPED | FAILED`
Required: No

 ** startTime **   <a name="imagebuilder-Type-WorkflowStepMetadata-startTime"></a>
The timestamp when the workflow step started.
Type: String
Required: No

 ** status **   <a name="imagebuilder-Type-WorkflowStepMetadata-status"></a>
Runtime status for the workflow step.
Type: String
Valid Values: `PENDING | SKIPPED | RUNNING | COMPLETED | FAILED | CANCELLED`
Required: No

 ** stepExecutionId **   <a name="imagebuilder-Type-WorkflowStepMetadata-stepExecutionId"></a>
A unique identifier for the workflow step, assigned at runtime.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_WorkflowStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowStepMetadata)
