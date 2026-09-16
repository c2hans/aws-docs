---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAIWorkloadConfig.html
---

# CreateAIWorkloadConfig
<a name="API_CreateAIWorkloadConfig"></a>

Creates a reusable AI workload configuration that defines datasets, data sources, and benchmark tool settings for consistent performance testing of generative AI inference deployments on Amazon SageMaker AI.

## Request Syntax
<a name="API_CreateAIWorkloadConfig_RequestSyntax"></a>

```
{
   "AIWorkloadConfigName": "{{string}}",
   "AIWorkloadConfigs": {
      "WorkloadSpec": { ... }
   },
   "DatasetConfig": { ... },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAIWorkloadConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIWorkloadConfigName](#API_CreateAIWorkloadConfig_RequestSyntax) **   <a name="sagemaker-CreateAIWorkloadConfig-request-AIWorkloadConfigName"></a>
The name of the AI workload configuration. The name must be unique within your AWS account in the current AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [AIWorkloadConfigs](#API_CreateAIWorkloadConfig_RequestSyntax) **   <a name="sagemaker-CreateAIWorkloadConfig-request-AIWorkloadConfigs"></a>
The benchmark tool configuration and workload specification. Provide the specification as an inline YAML or JSON string.
Type: [AIWorkloadConfigs](API_AIWorkloadConfigs.md) object
Required: No

 ** [DatasetConfig](#API_CreateAIWorkloadConfig_RequestSyntax) **   <a name="sagemaker-CreateAIWorkloadConfig-request-DatasetConfig"></a>
The dataset configuration for the workload. Specify input data channels with their data sources for benchmark workloads.
Type: [AIDatasetConfig](API_AIDatasetConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [Tags](#API_CreateAIWorkloadConfig_RequestSyntax) **   <a name="sagemaker-CreateAIWorkloadConfig-request-Tags"></a>
The metadata that you apply to AWS resources to help you categorize and organize them. Each tag consists of a key and a value, both of which you define. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the AWS General Reference.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAIWorkloadConfig_ResponseSyntax"></a>

```
{
   "AIWorkloadConfigArn": "string"
}
```

## Response Elements
<a name="API_CreateAIWorkloadConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIWorkloadConfigArn](#API_CreateAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-CreateAIWorkloadConfig-response-AIWorkloadConfigArn"></a>
The Amazon Resource Name (ARN) of the created AI workload configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-workload-config/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateAIWorkloadConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateAIWorkloadConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateAIWorkloadConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateAIWorkloadConfig)
