---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopPipelineExecution.html
---

# StopPipelineExecution
<a name="API_StopPipelineExecution"></a>

Stops a pipeline execution.

 **Callback Step**

A pipeline execution won't stop while a callback step is running. When you call `StopPipelineExecution` on a pipeline execution with a running callback step, SageMaker Pipelines sends an additional Amazon SQS message to the specified SQS queue. The body of the SQS message contains a "Status" field which is set to "Stopping".

You should add logic to your Amazon SQS message consumer to take any needed action (for example, resource cleanup) upon receipt of the message followed by a call to `SendPipelineExecutionStepSuccess` or `SendPipelineExecutionStepFailure`.

Only when SageMaker Pipelines receives one of these calls will it stop the pipeline execution.

 **Lambda Step**

A pipeline execution can't be stopped while a lambda step is running because the Lambda function invoked by the lambda step can't be stopped. If you attempt to stop the execution while the Lambda function is running, the pipeline waits for the Lambda function to finish or until the timeout is hit, whichever occurs first, and then stops. If the Lambda function finishes, the pipeline execution status is `Stopped`. If the timeout is hit the pipeline execution status is `Failed`.

## Request Syntax
<a name="API_StopPipelineExecution_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "PipelineExecutionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_StopPipelineExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_StopPipelineExecution_RequestSyntax) **   <a name="sagemaker-StopPipelineExecution-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: Yes

 ** [PipelineExecutionArn](#API_StopPipelineExecution_RequestSyntax) **   <a name="sagemaker-StopPipelineExecution-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: Yes

## Response Syntax
<a name="API_StopPipelineExecution_ResponseSyntax"></a>

```
{
   "PipelineExecutionArn": "string"
}
```

## Response Elements
<a name="API_StopPipelineExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineExecutionArn](#API_StopPipelineExecution_ResponseSyntax) **   <a name="sagemaker-StopPipelineExecution-response-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`

## Errors
<a name="API_StopPipelineExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StopPipelineExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StopPipelineExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StopPipelineExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
