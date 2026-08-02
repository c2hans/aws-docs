---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateImage.html
---

# UpdateImage
<a name="API_UpdateImage"></a>

Updates the properties of a SageMaker AI image. To change the image's tags, use the [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) and [DeleteTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTags.html) APIs.

## Request Syntax
<a name="API_UpdateImage_RequestSyntax"></a>

```
{
   "DeleteProperties": [ "{{string}}" ],
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "ImageName": "{{string}}",
   "RoleArn": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeleteProperties](#API_UpdateImage_RequestSyntax) **   <a name="sagemaker-UpdateImage-request-DeleteProperties"></a>
A list of properties to delete. Only the `Description` and `DisplayName` properties can be deleted.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Length Constraints: Minimum length of 1. Maximum length of 11.
Pattern: `(^DisplayName$)|(^Description$)`
Required: No

 ** [Description](#API_UpdateImage_RequestSyntax) **   <a name="sagemaker-UpdateImage-request-Description"></a>
The new description for the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: No

 ** [DisplayName](#API_UpdateImage_RequestSyntax) **   <a name="sagemaker-UpdateImage-request-DisplayName"></a>
The new display name for the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S(.*\S)?`
Required: No

 ** [ImageName](#API_UpdateImage_RequestSyntax) **   <a name="sagemaker-UpdateImage-request-ImageName"></a>
The name of the image to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [RoleArn](#API_UpdateImage_RequestSyntax) **   <a name="sagemaker-UpdateImage-request-RoleArn"></a>
The new ARN for the IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

## Response Syntax
<a name="API_UpdateImage_ResponseSyntax"></a>

```
{
   "ImageArn": "string"
}
```

## Response Elements
<a name="API_UpdateImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ImageArn](#API_UpdateImage_ResponseSyntax) **   <a name="sagemaker-UpdateImage-response-ImageArn"></a>
The ARN of the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`

## Errors
<a name="API_UpdateImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateImage)
