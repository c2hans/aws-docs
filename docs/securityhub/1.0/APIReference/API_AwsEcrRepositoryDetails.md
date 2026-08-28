---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcrRepositoryDetails.html
---

# AwsEcrRepositoryDetails
<a name="API_AwsEcrRepositoryDetails"></a>

Provides information about an Amazon Elastic Container Registry repository.

## Contents
<a name="API_AwsEcrRepositoryDetails_Contents"></a>

 ** Arn **   <a name="securityhub-Type-AwsEcrRepositoryDetails-Arn"></a>
The ARN of the repository.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ImageScanningConfiguration **   <a name="securityhub-Type-AwsEcrRepositoryDetails-ImageScanningConfiguration"></a>
The image scanning configuration for a repository.
Type: [AwsEcrRepositoryImageScanningConfigurationDetails](API_AwsEcrRepositoryImageScanningConfigurationDetails.md) object
Required: No

 ** ImageTagMutability **   <a name="securityhub-Type-AwsEcrRepositoryDetails-ImageTagMutability"></a>
The tag mutability setting for the repository. Valid values are `IMMUTABLE` or `MUTABLE`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LifecyclePolicy **   <a name="securityhub-Type-AwsEcrRepositoryDetails-LifecyclePolicy"></a>
Information about the lifecycle policy for the repository.
Type: [AwsEcrRepositoryLifecyclePolicyDetails](API_AwsEcrRepositoryLifecyclePolicyDetails.md) object
Required: No

 ** RepositoryName **   <a name="securityhub-Type-AwsEcrRepositoryDetails-RepositoryName"></a>
The name of the repository.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RepositoryPolicyText **   <a name="securityhub-Type-AwsEcrRepositoryDetails-RepositoryPolicyText"></a>
The text of the repository policy.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcrRepositoryDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcrRepositoryDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcrRepositoryDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcrRepositoryDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
