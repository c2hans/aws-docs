---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreatePresignedMlflowAppUrl.html
---

# CreatePresignedMlflowAppUrl
<a name="API_CreatePresignedMlflowAppUrl"></a>

Returns a presigned URL that you can use to connect to the MLflow UI attached to your MLflow App. For more information, see [Launch the MLflow UI using a presigned URL](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-launch-ui.html).

## Request Syntax
<a name="API_CreatePresignedMlflowAppUrl_RequestSyntax"></a>

```
{
   "Arn": "{{string}}",
   "ExpiresInSeconds": {{number}},
   "SessionExpirationDurationInSeconds": {{number}}
}
```

## Request Parameters
<a name="API_CreatePresignedMlflowAppUrl_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Arn](#API_CreatePresignedMlflowAppUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowAppUrl-request-Arn"></a>
The ARN of the MLflow App to connect to your MLflow UI.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:mlflow-app/.*`
Required: Yes

 ** [ExpiresInSeconds](#API_CreatePresignedMlflowAppUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowAppUrl-request-ExpiresInSeconds"></a>
The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 300.
Required: No

 ** [SessionExpirationDurationInSeconds](#API_CreatePresignedMlflowAppUrl_RequestSyntax) **   <a name="sagemaker-CreatePresignedMlflowAppUrl-request-SessionExpirationDurationInSeconds"></a>
The duration in seconds that your presigned URL is valid. The presigned URL can be used only once.
Type: Integer
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

## Response Syntax
<a name="API_CreatePresignedMlflowAppUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string"
}
```

## Response Elements
<a name="API_CreatePresignedMlflowAppUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreatePresignedMlflowAppUrl_ResponseSyntax) **   <a name="sagemaker-CreatePresignedMlflowAppUrl-response-AuthorizedUrl"></a>
A presigned URL with an authorization token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.

## Errors
<a name="API_CreatePresignedMlflowAppUrl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreatePresignedMlflowAppUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreatePresignedMlflowAppUrl)
