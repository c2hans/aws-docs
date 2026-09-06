---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIBenchmarkJob.html
---

# CreateAIBenchmarkJob
<a name="API_CreateAIBenchmarkJob"></a>

Creates a benchmark job that runs performance benchmarks against inference infrastructure using a predefined AI workload configuration. The benchmark job measures metrics such as latency, throughput, and cost for your generative AI inference endpoints.

## Request Syntax
<a name="API_CreateAIBenchmarkJob_RequestSyntax"></a>

```
{
   "AIBenchmarkJobName": "{{string}}",
   "AIWorkloadConfigIdentifier": "{{string}}",
   "BenchmarkTarget": { ... },
   "NetworkConfig": {
      "VpcConfig": {
         "SecurityGroupIds": [ "{{string}}" ],
         "Subnets": [ "{{string}}" ]
      }
   },
   "OutputConfig": {
      "MlflowConfig": {
         "MlflowExperimentName": "{{string}}",
         "MlflowResourceArn": "{{string}}",
         "MlflowRunName": "{{string}}"
      },
      "S3OutputLocation": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAIBenchmarkJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIBenchmarkJobName](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-AIBenchmarkJobName"></a>
The name of the AI benchmark job. The name must be unique within your AWS account in the current AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [AIWorkloadConfigIdentifier](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-AIWorkloadConfigIdentifier"></a>
The name or Amazon Resource Name (ARN) of the AI workload configuration to use for this benchmark job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`
Required: Yes

 ** [BenchmarkTarget](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-BenchmarkTarget"></a>
The target endpoint to benchmark. Specify a SageMaker endpoint by providing its name or Amazon Resource Name (ARN).
Type: [AIBenchmarkTarget](API_AIBenchmarkTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [NetworkConfig](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-NetworkConfig"></a>
The network configuration for the benchmark job, including VPC settings.
Type: [AIBenchmarkNetworkConfig](API_AIBenchmarkNetworkConfig.md) object
Required: No

 ** [OutputConfig](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-OutputConfig"></a>
The output configuration for the benchmark job, including the Amazon S3 location where benchmark results are stored.
Type: [AIBenchmarkOutputConfig](API_AIBenchmarkOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-request-Tags"></a>
The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAIBenchmarkJob_ResponseSyntax"></a>

```
{
   "AIBenchmarkJobArn": "string"
}
```

## Response Elements
<a name="API_CreateAIBenchmarkJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIBenchmarkJobArn](#API_CreateAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-CreateAIBenchmarkJob-response-AIBenchmarkJobArn"></a>
The Amazon Resource Name (ARN) of the created benchmark job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-benchmark-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateAIBenchmarkJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateAIBenchmarkJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAIBenchmarkJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAIBenchmarkJob)
