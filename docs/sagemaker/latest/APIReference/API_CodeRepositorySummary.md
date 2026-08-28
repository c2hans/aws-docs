---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CodeRepositorySummary.html
---

# CodeRepositorySummary
<a name="API_CodeRepositorySummary"></a>

Specifies summary information about a Git repository.

## Contents
<a name="API_CodeRepositorySummary_Contents"></a>

 ** CodeRepositoryArn **   <a name="sagemaker-Type-CodeRepositorySummary-CodeRepositoryArn"></a>
The Amazon Resource Name (ARN) of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]{9,16}:[0-9]{12}:code-repository/[\S]{1,2048}`
Required: Yes

 ** CodeRepositoryName **   <a name="sagemaker-Type-CodeRepositorySummary-CodeRepositoryName"></a>
The name of the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-CodeRepositorySummary-CreationTime"></a>
The date and time that the Git repository was created.
Type: Timestamp
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-CodeRepositorySummary-LastModifiedTime"></a>
The date and time that the Git repository was last modified.
Type: Timestamp
Required: Yes

 ** GitConfig **   <a name="sagemaker-Type-CodeRepositorySummary-GitConfig"></a>
Configuration details for the Git repository, including the URL where it is located and the ARN of the AWS Secrets Manager secret that contains the credentials used to access the repository.
Type: [GitConfig](API_GitConfig.md) object
Required: No

## See Also
<a name="API_CodeRepositorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CodeRepositorySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CodeRepositorySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CodeRepositorySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
