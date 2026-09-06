---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeStudioLifecycleConfig.html
---

# DescribeStudioLifecycleConfig
<a name="API_DescribeStudioLifecycleConfig"></a>

Describes the Amazon SageMaker AI Studio Lifecycle Configuration.

## Request Syntax
<a name="API_DescribeStudioLifecycleConfig_RequestSyntax"></a>

```
{
   "StudioLifecycleConfigName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeStudioLifecycleConfig_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [StudioLifecycleConfigName](#API_DescribeStudioLifecycleConfig_RequestSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-request-StudioLifecycleConfigName"></a>
The name of the Amazon SageMaker AI Studio Lifecycle Configuration to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeStudioLifecycleConfig_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "LastModifiedTime": number,
   "StudioLifecycleConfigAppType": "string",
   "StudioLifecycleConfigArn": "string",
   "StudioLifecycleConfigContent": "string",
   "StudioLifecycleConfigName": "string"
}
```

## Response Elements
<a name="API_DescribeStudioLifecycleConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-CreationTime"></a>
The creation time of the Amazon SageMaker AI Studio Lifecycle Configuration.
Type: Timestamp

 ** [LastModifiedTime](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-LastModifiedTime"></a>
This value is equivalent to CreationTime because Amazon SageMaker AI Studio Lifecycle Configurations are immutable.
Type: Timestamp

 ** [StudioLifecycleConfigAppType](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-StudioLifecycleConfigAppType"></a>
The App type that the Lifecycle Configuration is attached to.
Type: String
Valid Values: `JupyterServer | KernelGateway | CodeEditor | JupyterLab`

 ** [StudioLifecycleConfigArn](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-StudioLifecycleConfigArn"></a>
The ARN of the Lifecycle Configuration to describe.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:studio-lifecycle-config/.*|None)`

 ** [StudioLifecycleConfigContent](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-StudioLifecycleConfigContent"></a>
The content of your Amazon SageMaker AI Studio Lifecycle Configuration script.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Pattern: `[\S\s]+`

 ** [StudioLifecycleConfigName](#API_DescribeStudioLifecycleConfig_ResponseSyntax) **   <a name="sagemaker-DescribeStudioLifecycleConfig-response-StudioLifecycleConfigName"></a>
The name of the Amazon SageMaker AI Studio Lifecycle Configuration that is described.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_DescribeStudioLifecycleConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStudioLifecycleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeStudioLifecycleConfig)
