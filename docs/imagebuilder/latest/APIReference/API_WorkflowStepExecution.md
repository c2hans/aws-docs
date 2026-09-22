---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowStepExecution.html
---

# WorkflowStepExecution
<a name="API_WorkflowStepExecution"></a>

Contains runtime details for a workflow step that has paused at a `WaitForAction` step, and is waiting for you to send an action.

## Contents
<a name="API_WorkflowStepExecution_Contents"></a>

 ** action **   <a name="imagebuilder-Type-WorkflowStepExecution-action"></a>
The name of the step action.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`
Required: No

 ** imageBuildVersionArn **   <a name="imagebuilder-Type-WorkflowStepExecution-imageBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the image build version that ran the workflow.
Type: String
Pattern: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):image/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** name **   <a name="imagebuilder-Type-WorkflowStepExecution-name"></a>
The name of the workflow step.
Type: String
Pattern: `^[A-Za-z][A-Za-z0-9-_]{1,99}$`
Required: No

 ** startTime **   <a name="imagebuilder-Type-WorkflowStepExecution-startTime"></a>
The timestamp when the workflow step started.
Type: String
Required: No

 ** stepExecutionId **   <a name="imagebuilder-Type-WorkflowStepExecution-stepExecutionId"></a>
Uniquely identifies the workflow step that ran for the associated image build version.
Type: String
Pattern: `^step-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** workflowBuildVersionArn **   <a name="imagebuilder-Type-WorkflowStepExecution-workflowBuildVersionArn"></a>
The Amazon Resource Name (ARN) of the workflow resource that ran.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/[0-9]+\.[0-9]+\.[0-9]+/[0-9]+$`
Required: No

 ** workflowExecutionId **   <a name="imagebuilder-Type-WorkflowStepExecution-workflowExecutionId"></a>
Uniquely identifies the runtime instance of the workflow that contains the workflow step that ran for the associated image build version.
Type: String
Pattern: `^wf-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

## See Also
<a name="API_WorkflowStepExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowStepExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowStepExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowStepExecution)
