---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEdgePackagingJob.html
---

# CreateEdgePackagingJob
<a name="API_CreateEdgePackagingJob"></a>

Starts a SageMaker Edge Manager model packaging job. Edge Manager will use the model artifacts from the Amazon Simple Storage Service bucket that you specify. After the model has been packaged, Amazon SageMaker saves the resulting artifacts to an S3 bucket that you specify.

## Request Syntax
<a name="API_CreateEdgePackagingJob_RequestSyntax"></a>

```
{
   "CompilationJobName": "{{string}}",
   "EdgePackagingJobName": "{{string}}",
   "ModelName": "{{string}}",
   "ModelVersion": "{{string}}",
   "OutputConfig": {
      "KmsKeyId": "{{string}}",
      "PresetDeploymentConfig": "{{string}}",
      "PresetDeploymentType": "{{string}}",
      "S3OutputLocation": "{{string}}"
   },
   "ResourceKey": "{{string}}",
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
<a name="API_CreateEdgePackagingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CompilationJobName](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-CompilationJobName"></a>
The name of the SageMaker Neo compilation job that will be used to locate model artifacts for packaging.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [EdgePackagingJobName](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-EdgePackagingJobName"></a>
The name of the edge packaging job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelName](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-ModelName"></a>
The name of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [ModelVersion](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-ModelVersion"></a>
The version of the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\ \_\.]+`
Required: Yes

 ** [OutputConfig](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-OutputConfig"></a>
Provides information about the output location for the packaged model.
Type: [EdgeOutputConfig](API_EdgeOutputConfig.md) object
Required: Yes

 ** [ResourceKey](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-ResourceKey"></a>
The AWS KMS key to use when encrypting the EBS volume the edge packaging job runs on.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** [RoleArn](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to download and upload the model, and to contact SageMaker Neo.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateEdgePackagingJob_RequestSyntax) **   <a name="sagemaker-CreateEdgePackagingJob-request-Tags"></a>
Creates tags for the packaging job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Elements
<a name="API_CreateEdgePackagingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateEdgePackagingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateEdgePackagingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateEdgePackagingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateEdgePackagingJob)
