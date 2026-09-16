---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdatePipelineExecution.html
---

# UpdatePipelineExecution
<a name="API_UpdatePipelineExecution"></a>

Updates a pipeline execution.

## Request Syntax
<a name="API_UpdatePipelineExecution_RequestSyntax"></a>

```
{
   "ParallelismConfiguration": {
      "MaxParallelExecutionSteps": {{number}}
   },
   "PipelineExecutionArn": "{{string}}",
   "PipelineExecutionDescription": "{{string}}",
   "PipelineExecutionDisplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdatePipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ParallelismConfiguration](#API_UpdatePipelineExecution_RequestSyntax) **   <a name="sagemaker-UpdatePipelineExecution-request-ParallelismConfiguration"></a>
This configuration, if specified, overrides the parallelism configuration of the parent pipeline for this specific run.
Type: [ParallelismConfiguration](API_ParallelismConfiguration.md) object
Required: No

 ** [PipelineExecutionArn](#API_UpdatePipelineExecution_RequestSyntax) **   <a name="sagemaker-UpdatePipelineExecution-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: Yes

 ** [PipelineExecutionDescription](#API_UpdatePipelineExecution_RequestSyntax) **   <a name="sagemaker-UpdatePipelineExecution-request-PipelineExecutionDescription"></a>
The description of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3072.
Pattern: `.*`
Required: No

 ** [PipelineExecutionDisplayName](#API_UpdatePipelineExecution_RequestSyntax) **   <a name="sagemaker-UpdatePipelineExecution-request-PipelineExecutionDisplayName"></a>
The display name of the pipeline execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 82.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,81}`
Required: No

## Response Syntax
<a name="API_UpdatePipelineExecution_ResponseSyntax"></a>

```
{
   "PipelineExecutionArn": "string"
}
```

## Response Elements
<a name="API_UpdatePipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineExecutionArn](#API_UpdatePipelineExecution_ResponseSyntax) **   <a name="sagemaker-UpdatePipelineExecution-response-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the updated pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`

## Errors
<a name="API_UpdatePipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdatePipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdatePipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdatePipelineExecution)
