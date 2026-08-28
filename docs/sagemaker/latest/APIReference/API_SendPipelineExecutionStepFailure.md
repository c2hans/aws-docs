---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SendPipelineExecutionStepFailure.html
---

# SendPipelineExecutionStepFailure
<a name="API_SendPipelineExecutionStepFailure"></a>

Notifies the pipeline that the execution of a callback step failed, along with a message describing why. When a callback step is run, the pipeline generates a callback token and includes the token in a message sent to Amazon Simple Queue Service (Amazon SQS).

## Request Syntax
<a name="API_SendPipelineExecutionStepFailure_RequestSyntax"></a>

```
{
   "CallbackToken": "{{string}}",
   "ClientRequestToken": "{{string}}",
   "FailureReason": "{{string}}"
}
```

## Request Parameters
<a name="API_SendPipelineExecutionStepFailure_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CallbackToken](#API_SendPipelineExecutionStepFailure_RequestSyntax) **   <a name="sagemaker-SendPipelineExecutionStepFailure-request-CallbackToken"></a>
The pipeline generated token from the Amazon SQS queue.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** [ClientRequestToken](#API_SendPipelineExecutionStepFailure_RequestSyntax) **   <a name="sagemaker-SendPipelineExecutionStepFailure-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 128.
Required: No

 ** [FailureReason](#API_SendPipelineExecutionStepFailure_RequestSyntax) **   <a name="sagemaker-SendPipelineExecutionStepFailure-request-FailureReason"></a>
A message describing why the step failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_SendPipelineExecutionStepFailure_ResponseSyntax"></a>

```
{
   "PipelineExecutionArn": "string"
}
```

## Response Elements
<a name="API_SendPipelineExecutionStepFailure_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PipelineExecutionArn](#API_SendPipelineExecutionStepFailure_ResponseSyntax) **   <a name="sagemaker-SendPipelineExecutionStepFailure-response-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`

## Errors
<a name="API_SendPipelineExecutionStepFailure_Errors"></a>

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
<a name="API_SendPipelineExecutionStepFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SendPipelineExecutionStepFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
