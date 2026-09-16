---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StartPipelineExecution.html
---

# StartPipelineExecution
<a name="API_StartPipelineExecution"></a>

Starts a pipeline execution.

## Request Syntax
<a name="API_StartPipelineExecution_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "MlflowExperimentName": "{{string}}",
   "ParallelismConfiguration": {
      "MaxParallelExecutionSteps": {{number}}
   },
   "PipelineExecutionDescription": "{{string}}",
   "PipelineExecutionDisplayName": "{{string}}",
   "PipelineName": "{{string}}",
   "PipelineParameters": [
      {
         "Name": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "PipelineVersionId": {{number}},
   "SelectiveExecutionConfig": {
      "SelectedSteps": [
         {
            "StepName": "{{string}}"
         }
      ],
      "SourcePipelineExecutionArn": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_StartPipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: Yes

 ** [MlflowExperimentName](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-MlflowExperimentName"></a>
 The MLflow experiment name of the pipeline execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [ParallelismConfiguration](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-ParallelismConfiguration"></a>
This configuration, if specified, overrides the parallelism configuration of the parent pipeline for this specific run.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** [PipelineExecutionDescription](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-PipelineExecutionDescription"></a>
The description of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [PipelineExecutionDisplayName](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-PipelineExecutionDisplayName"></a>
The display name of the pipeline execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

 ** [PipelineName](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-PipelineName"></a>
The name or Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:([0-9]{12}|aws):pipeline/.*)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,255})`
Required: Yes

 ** [PipelineParameters](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-PipelineParameters"></a>
Contains a list of pipeline parameters. This list can be empty.
Type: Array of [Parameter](API_Parameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [PipelineVersionId](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-PipelineVersionId"></a>
The ID of the pipeline version to start execution from.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** [SelectiveExecutionConfig](#API_StartPipelineExecution_RequestSyntax) **   <a name="sagemaker-StartPipelineExecution-request-SelectiveExecutionConfig"></a>
The selective execution configuration applied to the pipeline run.
Type: [SelectiveExecutionConfig](API_SelectiveExecutionConfig.md) object
Required: No

## Response Syntax
<a name="API_StartPipelineExecution_ResponseSyntax"></a>

```
{
   "PipelineExecutionArn": "string"
}
```

## Response Elements
<a name="API_StartPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineExecutionArn](#API_StartPipelineExecution_ResponseSyntax) **   <a name="sagemaker-StartPipelineExecution-response-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`

## Errors
<a name="API_StartPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StartPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StartPipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StartPipelineExecution)
