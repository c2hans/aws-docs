---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_PipelineExecution.html
---

# PipelineExecution
<a name="API_PipelineExecution"></a>

An execution of a pipeline.

## Contents
<a name="API_PipelineExecution_Contents"></a>

 ** CreatedBy **   <a name="sagemaker-Type-PipelineExecution-CreatedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** FailureReason **   <a name="sagemaker-Type-PipelineExecution-FailureReason"></a>
If the execution failed, a message describing why.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1300.
Pattern: `.*`
Required: No

 ** LastModifiedBy **   <a name="sagemaker-Type-PipelineExecution-LastModifiedBy"></a>
Information about the user who created or modified a SageMaker resource.
Type: [UserContext](API_UserContext.md) object
Required: No

 ** ParallelismConfiguration **   <a name="sagemaker-Type-PipelineExecution-ParallelismConfiguration"></a>
The parallelism configuration applied to the pipeline execution.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** PipelineArn **   <a name="sagemaker-Type-PipelineExecution-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline that was executed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*`
Required: No

 ** PipelineExecutionArn **   <a name="sagemaker-Type-PipelineExecution-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: No

 ** PipelineExecutionDescription **   <a name="sagemaker-Type-PipelineExecution-PipelineExecutionDescription"></a>
The description of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** PipelineExecutionDisplayName **   <a name="sagemaker-Type-PipelineExecution-PipelineExecutionDisplayName"></a>
The display name of the pipeline execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** PipelineExecutionStatus **   <a name="sagemaker-Type-PipelineExecution-PipelineExecutionStatus"></a>
The status of the pipeline status.
Type: String
Valid Values: `Executing | Stopping | Stopped | Failed | Succeeded`
Required: No

 ** PipelineExperimentConfig **   <a name="sagemaker-Type-PipelineExecution-PipelineExperimentConfig"></a>
Specifies the names of the experiment and trial created by a pipeline.
Type: [PipelineExperimentConfig](API_PipelineExperimentConfig.md) object
Required: No

 ** PipelineParameters **   <a name="sagemaker-Type-PipelineExecution-PipelineParameters"></a>
Contains a list of pipeline parameters. This list can be empty.
Type: Array of [Parameter](API_Parameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** PipelineVersionDisplayName **   <a name="sagemaker-Type-PipelineExecution-PipelineVersionDisplayName"></a>
The display name of the pipeline version that started this execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** PipelineVersionId **   <a name="sagemaker-Type-PipelineExecution-PipelineVersionId"></a>
The ID of the pipeline version that started this execution.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** SelectiveExecutionConfig **   <a name="sagemaker-Type-PipelineExecution-SelectiveExecutionConfig"></a>
The selective execution configuration applied to the pipeline run.
Type: [SelectiveExecutionConfig](API_SelectiveExecutionConfig.md) object
Required: No

## See Also
<a name="API_PipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/PipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/PipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/PipelineExecution)
