---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingRepositoryAuthConfig.html
---

# TrainingRepositoryAuthConfig
<a name="API_TrainingRepositoryAuthConfig"></a>

An object containing authentication information for a private Docker registry.

## Contents
<a name="API_TrainingRepositoryAuthConfig_Contents"></a>

 ** TrainingRepositoryCredentialsProviderArn **   <a name="sagemaker-Type-TrainingRepositoryAuthConfig-TrainingRepositoryCredentialsProviderArn"></a>
The Amazon Resource Name (ARN) of an AWS Lambda function used to give SageMaker access credentials to your private Docker registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[\p{Alnum}\-]+:lambda:[\p{Alnum}\-]+:[0-9]{12}:function:.*`
Required: Yes

## See Also
<a name="API_TrainingRepositoryAuthConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingRepositoryAuthConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingRepositoryAuthConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingRepositoryAuthConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
