---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateCodeRepository.html
---

# CreateCodeRepository
<a name="API_CreateCodeRepository"></a>

Creates a Git repository as a resource in your SageMaker AI account. You can associate the repository with notebook instances so that you can use Git source control for the notebooks you create. The Git repository is a resource in your SageMaker AI account, so it can be associated with more than one notebook instance, and it persists independently from the lifecycle of any notebook instances it is associated with.

The repository can be hosted either in [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) or in any other Git repository.

## Request Syntax
<a name="API_CreateCodeRepository_RequestSyntax"></a>

```
{
   "CodeRepositoryName": "{{string}}",
   "GitConfig": {
      "Branch": "{{string}}",
      "RepositoryUrl": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateCodeRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CodeRepositoryName](#API_CreateCodeRepository_RequestSyntax) **   <a name="sagemaker-CreateCodeRepository-request-CodeRepositoryName"></a>
The name of the Git repository. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [GitConfig](#API_CreateCodeRepository_RequestSyntax) **   <a name="sagemaker-CreateCodeRepository-request-GitConfig"></a>
Specifies details about the repository, including the URL where the repository is located, the default branch, and credentials to use to access the repository.
Type: [GitConfig](API_GitConfig.md) object
Required: Yes

 ** [Tags](#API_CreateCodeRepository_RequestSyntax) **   <a name="sagemaker-CreateCodeRepository-request-Tags"></a>
An array of key-value pairs. You can use tags to categorize your AWS resources in different ways, for example, by purpose, owner, or environment. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateCodeRepository_ResponseSyntax"></a>

```
{
   "CodeRepositoryArn": "string"
}
```

## Response Elements
<a name="API_CreateCodeRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeRepositoryArn](#API_CreateCodeRepository_ResponseSyntax) **   <a name="sagemaker-CreateCodeRepository-response-CodeRepositoryArn"></a>
The Amazon Resource Name (ARN) of the new repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:code-repository/[\S]{1,2048}`

## Errors
<a name="API_CreateCodeRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateCodeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateCodeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateCodeRepository)
