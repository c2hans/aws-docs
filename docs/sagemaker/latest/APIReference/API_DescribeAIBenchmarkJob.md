---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIBenchmarkJob.html
---

# DescribeAIBenchmarkJob
<a name="API_DescribeAIBenchmarkJob"></a>

Returns details of an AI benchmark job, including its status, configuration, target endpoint, and timing information.

## Request Syntax
<a name="API_DescribeAIBenchmarkJob_RequestSyntax"></a>

```
{
   "AIBenchmarkJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAIBenchmarkJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIBenchmarkJobName](#API_DescribeAIBenchmarkJob_RequestSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-request-AIBenchmarkJobName"></a>
The name of the AI benchmark job to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeAIBenchmarkJob_ResponseSyntax"></a>

```
{
   "AIBenchmarkJobArn": "string",
   "AIBenchmarkJobName": "string",
   "AIBenchmarkJobStatus": "string",
   "AIWorkloadConfigIdentifier": "string",
   "BenchmarkTarget": { ... },
   "CreationTime": number,
   "EndTime": number,
   "FailureReason": "string",
   "NetworkConfig": {
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "Subnets": [ "string" ]
      }
   },
   "OutputConfig": {
      "CloudWatchLogs": [
         {
            "LogGroupArn": "string",
            "LogStreamName": "string"
         }
      ],
      "MlflowConfig": {
         "MlflowExperimentName": "string",
         "MlflowResourceArn": "string",
         "MlflowRunName": "string"
      },
      "S3OutputLocation": "string"
   },
   "RoleArn": "string",
   "StartTime": number,
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAIBenchmarkJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIBenchmarkJobArn](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-AIBenchmarkJobArn"></a>
The Amazon Resource Name (ARN) of the AI benchmark job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-benchmark-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIBenchmarkJobName](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-AIBenchmarkJobName"></a>
The name of the AI benchmark job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIBenchmarkJobStatus](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-AIBenchmarkJobStatus"></a>
The status of the AI benchmark job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`

 ** [AIWorkloadConfigIdentifier](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-AIWorkloadConfigIdentifier"></a>
The name or Amazon Resource Name (ARN) of the AI workload configuration used for this benchmark job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:[a-z\-]*/)?([a-zA-Z0-9]([a-zA-Z0-9\-]){0,62})(?<!-)`

 ** [BenchmarkTarget](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-BenchmarkTarget"></a>
The target endpoint that was benchmarked.
Type: [AIBenchmarkTarget](API_AIBenchmarkTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [CreationTime](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-CreationTime"></a>
A timestamp that indicates when the benchmark job was created.
Type: Timestamp

 ** [EndTime](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-EndTime"></a>
A timestamp that indicates when the benchmark job completed.
Type: Timestamp

 ** [FailureReason](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-FailureReason"></a>
If the benchmark job failed, the reason it failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [NetworkConfig](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-NetworkConfig"></a>
The network configuration for the benchmark job.
Type: [AIBenchmarkNetworkConfig](API_AIBenchmarkNetworkConfig.md) object

 ** [OutputConfig](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-OutputConfig"></a>
The output configuration for the benchmark job, including the Amazon S3 output location and CloudWatch log information.
Type: [AIBenchmarkOutputResult](API_AIBenchmarkOutputResult.md) object

 ** [RoleArn](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role used by the benchmark job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

 ** [StartTime](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-StartTime"></a>
A timestamp that indicates when the benchmark job started running.
Type: Timestamp

 ** [Tags](#API_DescribeAIBenchmarkJob_ResponseSyntax) **   <a name="sagemaker-DescribeAIBenchmarkJob-response-Tags"></a>
The tags associated with the benchmark job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DescribeAIBenchmarkJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAIBenchmarkJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAIBenchmarkJob)
