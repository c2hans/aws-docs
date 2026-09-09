---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeImage.html
---

# DescribeImage
<a name="API_DescribeImage"></a>

Describes a SageMaker AI image.

## Request Syntax
<a name="API_DescribeImage_RequestSyntax"></a>

```
{
   "ImageName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeImage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ImageName](#API_DescribeImage_RequestSyntax) **   <a name="sagemaker-DescribeImage-request-ImageName"></a>
The name of the image to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeImage_ResponseSyntax"></a>

```
{
   "Description": "string",
   "DisplayName": "string",
   "FailureReason": "string",
   "ImageArn": "string",
   "ImageName": "string",
   "ImageStatus": "string",
   "RoleArn": "string"
}
```

## Response Elements
<a name="API_DescribeImage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-Description"></a>
The description of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`

 ** [DisplayName](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-DisplayName"></a>
The name of the image as displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\S(.*\S)?`

 ** [FailureReason](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-FailureReason"></a>
When a create, update, or delete operation fails, the reason for the failure.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [ImageArn](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-ImageArn"></a>
The ARN of the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:sagemaker:.+:[0-9]{12}:image/[a-zA-Z0-9]([-.]?[a-zA-Z0-9])*`

 ** [ImageName](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-ImageName"></a>
The name of the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([-.]?[a-zA-Z0-9]){0,62}`

 ** [ImageStatus](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-ImageStatus"></a>
The status of the image.
Type: String
Valid Values: `CREATING | CREATED | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETE_FAILED`

 ** [RoleArn](#API_DescribeImage_ResponseSyntax) **   <a name="sagemaker-DescribeImage-response-RoleArn"></a>
The ARN of the IAM role that enables Amazon SageMaker AI to perform tasks on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

## Errors
<a name="API_DescribeImage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeImage)
