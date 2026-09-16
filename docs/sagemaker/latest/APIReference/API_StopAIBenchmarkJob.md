---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAIBenchmarkJob.html
---

# StopAIBenchmarkJob
<a name="API_StopAIBenchmarkJob"></a>

Stops a running AI benchmark job.

## Request Syntax
<a name="API_StopAIBenchmarkJob_RequestSyntax"></a>

```
{
   "AIBenchmarkJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_StopAIBenchmarkJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIBenchmarkJobName](#API_StopAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-StopAIBenchmarkJob-request-AIBenchmarkJobName"></a>
The name of the AI benchmark job to stop.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_StopAIBenchmarkJob_ResponseSyntax"></a>

```
{
   "AIBenchmarkJobArn": "string"
}
```

## Response Elements
<a name="API_StopAIBenchmarkJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIBenchmarkJobArn](#API_StopAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-StopAIBenchmarkJob-response-AIBenchmarkJobArn"></a>
The Amazon Resource Name (ARN) of the stopped benchmark job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-benchmark-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_StopAIBenchmarkJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_StopAIBenchmarkJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/StopAIBenchmarkJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StopAIBenchmarkJob)
