---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateModelPackageGroup.html
---

# CreateModelPackageGroup
<a name="API_CreateModelPackageGroup"></a>

Creates a model group. A model group contains a group of model versions.

## Request Syntax
<a name="API_CreateModelPackageGroup_RequestSyntax"></a>

```
{
   "ManagedConfiguration": {
      "ManagedStorageType": "{{string}}"
   },
   "ModelPackageGroupDescription": "{{string}}",
   "ModelPackageGroupName": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateModelPackageGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ManagedConfiguration](#API_CreateModelPackageGroup_RequestSyntax) **   <a name="sagemaker-CreateModelPackageGroup-request-ManagedConfiguration"></a>
The managed configuration of the model package group.
Type: [ManagedConfiguration](API_ManagedConfiguration.md) object
Required: No

 ** [ModelPackageGroupDescription](#API_CreateModelPackageGroup_RequestSyntax) **   <a name="sagemaker-CreateModelPackageGroup-request-ModelPackageGroupDescription"></a>
A description for the model group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}]*`
Required: No

 ** [ModelPackageGroupName](#API_CreateModelPackageGroup_RequestSyntax) **   <a name="sagemaker-CreateModelPackageGroup-request-ModelPackageGroupName"></a>
The name of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [Tags](#API_CreateModelPackageGroup_RequestSyntax) **   <a name="sagemaker-CreateModelPackageGroup-request-Tags"></a>
A list of key value pairs associated with the model group. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the * AWS General Reference Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateModelPackageGroup_ResponseSyntax"></a>

```
{
   "ModelPackageGroupArn": "string"
}
```

## Response Elements
<a name="API_CreateModelPackageGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ModelPackageGroupArn](#API_CreateModelPackageGroup_ResponseSyntax) **   <a name="sagemaker-CreateModelPackageGroup-response-ModelPackageGroupArn"></a>
The Amazon Resource Name (ARN) of the model group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:model-package-group/[\S]{1,2048}`

## Errors
<a name="API_CreateModelPackageGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateModelPackageGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateModelPackageGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateModelPackageGroup)
