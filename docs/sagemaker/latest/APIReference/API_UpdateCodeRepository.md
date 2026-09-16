---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateCodeRepository.html
---

# UpdateCodeRepository
<a name="API_UpdateCodeRepository"></a>

Updates the specified Git repository with the specified values.

## Request Syntax
<a name="API_UpdateCodeRepository_RequestSyntax"></a>

```
{
   "CodeRepositoryName": "{{string}}",
   "GitConfig": {
      "SecretArn": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateCodeRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CodeRepositoryName](#API_UpdateCodeRepository_RequestSyntax) **   <a name="sagemaker-UpdateCodeRepository-request-CodeRepositoryName"></a>
The name of the Git repository to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [GitConfig](#API_UpdateCodeRepository_RequestSyntax) **   <a name="sagemaker-UpdateCodeRepository-request-GitConfig"></a>
The configuration of the git repository, including the URL and the Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the repository. The secret must have a staging label of `AWSCURRENT` and must be in the following format:
 `{"username": UserName, "password": Password}`
Type: [GitConfigForUpdate](API_GitConfigForUpdate.md) object
Required: No

## Response Syntax
<a name="API_UpdateCodeRepository_ResponseSyntax"></a>

```
{
   "CodeRepositoryArn": "string"
}
```

## Response Elements
<a name="API_UpdateCodeRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeRepositoryArn](#API_UpdateCodeRepository_ResponseSyntax) **   <a name="sagemaker-UpdateCodeRepository-response-CodeRepositoryArn"></a>
The ARN of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:code-repository/[\S]{1,2048}`

## Errors
<a name="API_UpdateCodeRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCodeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/UpdateCodeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/UpdateCodeRepository)
