---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecutionStepMetadata.html
---

# PipelineExecutionStepMetadata
<a name="API_PipelineExecutionStepMetadata"></a>

Metadata for a step execution.

## Contents
<a name="API_PipelineExecutionStepMetadata_Contents"></a>

 ** AutoMLJob **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-AutoMLJob"></a>
The Amazon Resource Name (ARN) of the AutoML job that was run by this step.
Type: [AutoMLJobStepMetadata](API_AutoMLJobStepMetadata.md) object
Required: No

 ** BedrockCustomModel **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-BedrockCustomModel"></a>
 The metadata of the Amazon Bedrock custom model used in the pipeline execution step.
Type: [BedrockCustomModelMetadata](API_BedrockCustomModelMetadata.md) object
Required: No

 ** BedrockCustomModelDeployment **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-BedrockCustomModelDeployment"></a>
 The metadata of the Amazon Bedrock custom model deployment used in pipeline execution step.
Type: [BedrockCustomModelDeploymentMetadata](API_BedrockCustomModelDeploymentMetadata.md) object
Required: No

 ** BedrockModelImport **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-BedrockModelImport"></a>
 The metadata of Amazon Bedrock model import used in pipeline execution step.
Type: [BedrockModelImportMetadata](API_BedrockModelImportMetadata.md) object
Required: No

 ** BedrockProvisionedModelThroughput **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-BedrockProvisionedModelThroughput"></a>
 The metadata of the Amazon Bedrock provisioned model throughput used in the pipeline execution step.
Type: [BedrockProvisionedModelThroughputMetadata](API_BedrockProvisionedModelThroughputMetadata.md) object
Required: No

 ** Callback **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Callback"></a>
The URL of the Amazon SQS queue used by this step execution, the pipeline generated token, and a list of output parameters.
Type: [CallbackStepMetadata](API_CallbackStepMetadata.md) object
Required: No

 ** ClarifyCheck **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-ClarifyCheck"></a>
Container for the metadata for a Clarify check step. The configurations and outcomes of the check step execution. This includes:
+ The type of the check conducted,
+ The Amazon S3 URIs of baseline constraints and statistics files to be used for the drift check.
+ The Amazon S3 URIs of newly calculated baseline constraints and statistics.
+ The model package group name provided.
+ The Amazon S3 URI of the violation report if violations detected.
+ The Amazon Resource Name (ARN) of check processing job initiated by the step execution.
+ The boolean flags indicating if the drift check is skipped.
+ If step property `BaselineUsedForDriftCheck` is set the same as `CalculatedBaseline`.
Type: [ClarifyCheckStepMetadata](API_ClarifyCheckStepMetadata.md) object
Required: No

 ** Condition **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Condition"></a>
The outcome of the condition evaluation that was run by this step execution.
Type: [ConditionStepMetadata](API_ConditionStepMetadata.md) object
Required: No

 ** EMR **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-EMR"></a>
The configurations and outcomes of an Amazon EMR step execution.
Type: [EMRStepMetadata](API_EMRStepMetadata.md) object
Required: No

 ** Endpoint **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Endpoint"></a>
The endpoint that was invoked during this step execution.
Type: [EndpointStepMetadata](API_EndpointStepMetadata.md) object
Required: No

 ** EndpointConfig **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-EndpointConfig"></a>
The endpoint configuration used to create an endpoint during this step execution.
Type: [EndpointConfigStepMetadata](API_EndpointConfigStepMetadata.md) object
Required: No

 ** Fail **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Fail"></a>
The configurations and outcomes of a Fail step execution.
Type: [FailStepMetadata](API_FailStepMetadata.md) object
Required: No

 ** InferenceComponent **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-InferenceComponent"></a>
 The metadata of the inference component used in pipeline execution step.
Type: [InferenceComponentMetadata](API_InferenceComponentMetadata.md) object
Required: No

 ** Job **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Job"></a>
The metadata for a SageMaker job used in a pipeline execution step.
Type: [JobStepMetadata](API_JobStepMetadata.md) object
Required: No

 ** Lambda **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Lambda"></a>
The Amazon Resource Name (ARN) of the Lambda function that was run by this step execution and a list of output parameters.
Type: [LambdaStepMetadata](API_LambdaStepMetadata.md) object
Required: No

 ** Lineage **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Lineage"></a>
 The metadata of the lineage used in pipeline execution step.
Type: [LineageMetadata](API_LineageMetadata.md) object
Required: No

 ** Model **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-Model"></a>
The Amazon Resource Name (ARN) of the model that was created by this step execution.
Type: [ModelStepMetadata](API_ModelStepMetadata.md) object
Required: No

 ** ProcessingJob **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-ProcessingJob"></a>
The Amazon Resource Name (ARN) of the processing job that was run by this step execution.
Type: [ProcessingJobStepMetadata](API_ProcessingJobStepMetadata.md) object
Required: No

 ** QualityCheck **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-QualityCheck"></a>
The configurations and outcomes of the check step execution. This includes:
+ The type of the check conducted.
+ The Amazon S3 URIs of baseline constraints and statistics files to be used for the drift check.
+ The Amazon S3 URIs of newly calculated baseline constraints and statistics.
+ The model package group name provided.
+ The Amazon S3 URI of the violation report if violations detected.
+ The Amazon Resource Name (ARN) of check processing job initiated by the step execution.
+ The Boolean flags indicating if the drift check is skipped.
+ If step property `BaselineUsedForDriftCheck` is set the same as `CalculatedBaseline`.
Type: [QualityCheckStepMetadata](API_QualityCheckStepMetadata.md) object
Required: No

 ** RegisterModel **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-RegisterModel"></a>
The Amazon Resource Name (ARN) of the model package that the model was registered to by this step execution.
Type: [RegisterModelStepMetadata](API_RegisterModelStepMetadata.md) object
Required: No

 ** TrainingJob **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-TrainingJob"></a>
The Amazon Resource Name (ARN) of the training job that was run by this step execution.
Type: [TrainingJobStepMetadata](API_TrainingJobStepMetadata.md) object
Required: No

 ** TransformJob **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-TransformJob"></a>
The Amazon Resource Name (ARN) of the transform job that was run by this step execution.
Type: [TransformJobStepMetadata](API_TransformJobStepMetadata.md) object
Required: No

 ** TuningJob **   <a name="sagemaker-Type-PipelineExecutionStepMetadata-TuningJob"></a>
The Amazon Resource Name (ARN) of the tuning job that was run by this step execution.
Type: [TuningJobStepMetaData](API_TuningJobStepMetaData.md) object
Required: No

## See Also
<a name="API_PipelineExecutionStepMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineExecutionStepMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineExecutionStepMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineExecutionStepMetadata)
