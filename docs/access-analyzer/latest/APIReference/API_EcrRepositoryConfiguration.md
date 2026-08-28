---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_EcrRepositoryConfiguration.html
---

# EcrRepositoryConfiguration
<a name="API_EcrRepositoryConfiguration"></a>

The proposed access control configuration for an Amazon ECR repository. You can propose a configuration for a new Amazon ECR repository or an existing Amazon ECR repository that you own by specifying the Amazon ECR policy. For more information, see [Repository](https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Repository.html).
+ If the configuration is for an existing Amazon ECR repository and you do not specify the Amazon ECR policy, then the access preview uses the existing Amazon ECR policy for the repository.
+ If the access preview is for a new resource and you do not specify the policy, then the access preview assumes an Amazon ECR repository without a policy.
+ To propose deletion of an existing Amazon ECR repository policy, you can specify an empty string for the Amazon ECR policy.

## Contents
<a name="API_EcrRepositoryConfiguration_Contents"></a>

 ** repositoryPolicy **   <a name="accessanalyzer-Type-EcrRepositoryConfiguration-repositoryPolicy"></a>
The JSON repository policy text to apply to the Amazon ECR repository. For more information, see [Private repository policy examples](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the *Amazon ECR User Guide*.
Type: String
Required: No

## See Also
<a name="API_EcrRepositoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/EcrRepositoryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Access Analyzer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query access-analyzer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
