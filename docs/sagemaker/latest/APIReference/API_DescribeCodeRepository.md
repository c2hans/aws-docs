---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeCodeRepository.html
---

# DescribeCodeRepository
<a name="API_DescribeCodeRepository"></a>

Gets details about the specified Git repository.

## Request Syntax
<a name="API_DescribeCodeRepository_RequestSyntax"></a>

```
{
   "CodeRepositoryName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCodeRepository_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CodeRepositoryName](#API_DescribeCodeRepository_RequestSyntax) **   <a name="sagemaker-DescribeCodeRepository-request-CodeRepositoryName"></a>
The name of the Git repository to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

## Response Syntax
<a name="API_DescribeCodeRepository_ResponseSyntax"></a>

```
{
   "CodeRepositoryArn": "string",
   "CodeRepositoryName": "string",
   "CreationTime": number,
   "GitConfig": {
      "Branch": "string",
      "RepositoryUrl": "string",
      "SecretArn": "string"
   },
   "LastModifiedTime": number
}
```

## Response Elements
<a name="API_DescribeCodeRepository_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CodeRepositoryArn](#API_DescribeCodeRepository_ResponseSyntax) **   <a name="sagemaker-DescribeCodeRepository-response-CodeRepositoryArn"></a>
The Amazon Resource Name (ARN) of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:code-repository/[\S]{1,2048}`

 ** [CodeRepositoryName](#API_DescribeCodeRepository_ResponseSyntax) **   <a name="sagemaker-DescribeCodeRepository-response-CodeRepositoryName"></a>
The name of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

 ** [CreationTime](#API_DescribeCodeRepository_ResponseSyntax) **   <a name="sagemaker-DescribeCodeRepository-response-CreationTime"></a>
The date and time that the repository was created.
Type: Timestamp

 ** [GitConfig](#API_DescribeCodeRepository_ResponseSyntax) **   <a name="sagemaker-DescribeCodeRepository-response-GitConfig"></a>
Configuration details about the repository, including the URL where the repository is located, the default branch, and the Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the repository.
Type: [GitConfig](API_GitConfig.md) object

 ** [LastModifiedTime](#API_DescribeCodeRepository_ResponseSyntax) **   <a name="sagemaker-DescribeCodeRepository-response-LastModifiedTime"></a>
The date and time that the repository was last changed.
Type: Timestamp

## Errors
<a name="API_DescribeCodeRepository_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeCodeRepository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeCodeRepository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeCodeRepository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
