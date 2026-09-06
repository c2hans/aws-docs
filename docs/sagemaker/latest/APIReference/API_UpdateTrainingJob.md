---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateTrainingJob.html
---

# UpdateTrainingJob
<a name="API_UpdateTrainingJob"></a>

Update a model training job to request a new Debugger profiling configuration or to change warm pool retention length.

## Request Syntax
<a name="API_UpdateTrainingJob_RequestSyntax"></a>

```
{
   "ProfilerConfig": {
      "DisableProfiler": {{boolean}},
      "ProfilingIntervalInMilliseconds": {{number}},
      "ProfilingParameters": {
         "{{string}}" : "{{string}}"
      },
      "S3OutputPath": "{{string}}"
   },
   "ProfilerRuleConfigurations": [
      {
         "InstanceType": "{{string}}",
         "LocalPath": "{{string}}",
         "RuleConfigurationName": "{{string}}",
         "RuleEvaluatorImage": "{{string}}",
         "RuleParameters": {
            "{{string}}" : "{{string}}"
         },
         "S3OutputPath": "{{string}}",
         "VolumeSizeInGB": {{number}}
      }
   ],
   "RemoteDebugConfig": {
      "EnableRemoteDebug": {{boolean}}
   },
   "ResourceConfig": {
      "KeepAlivePeriodInSeconds": {{number}}
   },
   "TrainingJobName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateTrainingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProfilerConfig](#API_UpdateTrainingJob_RequestSyntax) **   <a name="sagemaker-UpdateTrainingJob-request-ProfilerConfig"></a>
Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.
Type: [ProfilerConfigForUpdate](API_ProfilerConfigForUpdate.md) object
Required: No

 ** [ProfilerRuleConfigurations](#API_UpdateTrainingJob_RequestSyntax) **   <a name="sagemaker-UpdateTrainingJob-request-ProfilerRuleConfigurations"></a>
Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.
Type: Array of [ProfilerRuleConfiguration](API_ProfilerRuleConfiguration.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [RemoteDebugConfig](#API_UpdateTrainingJob_RequestSyntax) **   <a name="sagemaker-UpdateTrainingJob-request-RemoteDebugConfig"></a>
Configuration for remote debugging while the training job is running. You can update the remote debugging configuration when the `SecondaryStatus` of the job is `Downloading` or `Training`.To learn more about the remote debugging functionality of SageMaker, see [Access a training container through AWS Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html).
Type: [RemoteDebugConfigForUpdate](API_RemoteDebugConfigForUpdate.md) object
Required: No

 ** [ResourceConfig](#API_UpdateTrainingJob_RequestSyntax) **   <a name="sagemaker-UpdateTrainingJob-request-ResourceConfig"></a>
The training job `ResourceConfig` to update warm pool retention length.
Type: [ResourceConfigForUpdate](API_ResourceConfigForUpdate.md) object
Required: No

 ** [TrainingJobName](#API_UpdateTrainingJob_RequestSyntax) **   <a name="sagemaker-UpdateTrainingJob-request-TrainingJobName"></a>
The name of a training job to update the Debugger profiling configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_UpdateTrainingJob_ResponseSyntax"></a>

```
{
   "TrainingJobArn": "string"
}
```

## Response Elements
<a name="API_UpdateTrainingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrainingJobArn](#API_UpdateTrainingJob_ResponseSyntax) **   <a name="sagemaker-UpdateTrainingJob-response-TrainingJobArn"></a>
The Amazon Resource Name (ARN) of the training job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_UpdateTrainingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTrainingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateTrainingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateTrainingJob)
