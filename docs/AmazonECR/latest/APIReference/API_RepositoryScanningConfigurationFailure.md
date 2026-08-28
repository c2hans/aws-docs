---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryScanningConfigurationFailure.html
---

# RepositoryScanningConfigurationFailure
<a name="API_RepositoryScanningConfigurationFailure"></a>

The details about any failures associated with the scanning configuration of a repository.

## Contents
<a name="API_RepositoryScanningConfigurationFailure_Contents"></a>

 ** failureCode **   <a name="ECR-Type-RepositoryScanningConfigurationFailure-failureCode"></a>
The failure code.
Type: String
Valid Values: `REPOSITORY_NOT_FOUND`
Required: No

 ** failureReason **   <a name="ECR-Type-RepositoryScanningConfigurationFailure-failureReason"></a>
The reason for the failure.
Type: String
Required: No

 ** repositoryName **   <a name="ECR-Type-RepositoryScanningConfigurationFailure-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

## See Also
<a name="API_RepositoryScanningConfigurationFailure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RepositoryScanningConfigurationFailure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RepositoryScanningConfigurationFailure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RepositoryScanningConfigurationFailure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
