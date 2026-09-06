---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecutionStep.html
---

# PipelineExecutionStep
<a name="API_PipelineExecutionStep"></a>

An execution of a step in a pipeline.

## Contents
<a name="API_PipelineExecutionStep_Contents"></a>

 ** AttemptCount **   <a name="sagemaker-Type-PipelineExecutionStep-AttemptCount"></a>
The current attempt of the execution step. For more information, see [Retry Policy for SageMaker Pipelines steps](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-retry-policy.html).
Type: Integer
Required: No

 ** CacheHitResult **   <a name="sagemaker-Type-PipelineExecutionStep-CacheHitResult"></a>
If this pipeline execution step was cached, details on the cache hit.
Type: [CacheHitResult](API_CacheHitResult.md) object
Required: No

 ** EndTime **   <a name="sagemaker-Type-PipelineExecutionStep-EndTime"></a>
The time that the step stopped executing.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-PipelineExecutionStep-FailureReason"></a>
The reason why the step failed execution. This is only returned if the step failed its execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Metadata **   <a name="sagemaker-Type-PipelineExecutionStep-Metadata"></a>
Metadata to run the pipeline step.
Type: [PipelineExecutionStepMetadata](API_PipelineExecutionStepMetadata.md) object
Required: No

 ** SelectiveExecutionResult **   <a name="sagemaker-Type-PipelineExecutionStep-SelectiveExecutionResult"></a>
The ARN from an execution of the current pipeline from which results are reused for this step.
Type: [SelectiveExecutionResult](API_SelectiveExecutionResult.md) object
Required: No

 ** StartTime **   <a name="sagemaker-Type-PipelineExecutionStep-StartTime"></a>
The time that the step started executing.
Type: Timestamp
Required: No

 ** StepDescription **   <a name="sagemaker-Type-PipelineExecutionStep-StepDescription"></a>
The description of the step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** StepDisplayName **   <a name="sagemaker-Type-PipelineExecutionStep-StepDisplayName"></a>
The display name of the step.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** StepName **   <a name="sagemaker-Type-PipelineExecutionStep-StepName"></a>
The name of the step that is executed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[A-Za-z0-9\-_]*`
Required: No

 ** StepStatus **   <a name="sagemaker-Type-PipelineExecutionStep-StepStatus"></a>
The status of the step execution.
Type: String
Valid Values: `Starting | Executing | Stopping | Stopped | Failed | Succeeded`
Required: No

## See Also
<a name="API_PipelineExecutionStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineExecutionStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineExecutionStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineExecutionStep)
