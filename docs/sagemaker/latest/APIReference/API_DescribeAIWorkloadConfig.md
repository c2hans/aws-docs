---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAIWorkloadConfig.html
---

# DescribeAIWorkloadConfig
<a name="API_DescribeAIWorkloadConfig"></a>

Returns details of an AI workload configuration, including the dataset configuration, benchmark tool settings, tags, and creation time.

## Request Syntax
<a name="API_DescribeAIWorkloadConfig_RequestSyntax"></a>

```
{
   "AIWorkloadConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAIWorkloadConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AIWorkloadConfigName](#API_DescribeAIWorkloadConfig_RequestSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-request-AIWorkloadConfigName"></a>
The name of the AI workload configuration to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeAIWorkloadConfig_ResponseSyntax"></a>

```
{
   "AIWorkloadConfigArn": "string",
   "AIWorkloadConfigName": "string",
   "AIWorkloadConfigs": {
      "WorkloadSpec": { ... }
   },
   "CreationTime": number,
   "DatasetConfig": { ... },
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeAIWorkloadConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AIWorkloadConfigArn](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-AIWorkloadConfigArn"></a>
The Amazon Resource Name (ARN) of the AI workload configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-workload-config/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIWorkloadConfigName](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-AIWorkloadConfigName"></a>
The name of the AI workload configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [AIWorkloadConfigs](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-AIWorkloadConfigs"></a>
The benchmark tool configuration and workload specification.
Type: [AIWorkloadConfigs](API_AIWorkloadConfigs.md) object

 ** [CreationTime](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-CreationTime"></a>
A timestamp that indicates when the AI workload configuration was created.
Type: Timestamp

 ** [DatasetConfig](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-DatasetConfig"></a>
The dataset configuration for the workload.
Type: [AIDatasetConfig](API_AIDatasetConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Tags](#API_DescribeAIWorkloadConfig_ResponseSyntax) **   <a name="sagemaker-DescribeAIWorkloadConfig-response-Tags"></a>
The tags associated with the AI workload configuration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_DescribeAIWorkloadConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAIWorkloadConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeAIWorkloadConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeAIWorkloadConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
