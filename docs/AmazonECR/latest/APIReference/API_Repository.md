---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_Repository.html
---

# Repository
<a name="API_Repository"></a>

An object representing a repository.

## Contents
<a name="API_Repository_Contents"></a>

 ** createdAt **   <a name="ECR-Type-Repository-createdAt"></a>
The date and time, in JavaScript date format, when the repository was created.
Type: Timestamp
Required: No

 ** encryptionConfiguration **   <a name="ECR-Type-Repository-encryptionConfiguration"></a>
The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** imageScanningConfiguration **   <a name="ECR-Type-Repository-imageScanningConfiguration"></a>
The image scanning configuration for a repository.
Type: [ImageScanningConfiguration](API_ImageScanningConfiguration.md) object
Required: No

 ** imageTagMutability **   <a name="ECR-Type-Repository-imageTagMutability"></a>
The tag mutability setting for the repository.
Type: String
Valid Values: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`
Required: No

 ** imageTagMutabilityExclusionFilters **   <a name="ECR-Type-Repository-imageTagMutabilityExclusionFilters"></a>
A list of filters that specify which image tags are excluded from the repository's image tag mutability setting.
Type: Array of [ImageTagMutabilityExclusionFilter](API_ImageTagMutabilityExclusionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** registryId **   <a name="ECR-Type-Repository-registryId"></a>
The AWS account ID associated with the registry that contains the repository.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryArn **   <a name="ECR-Type-Repository-repositoryArn"></a>
The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the `arn:aws:ecr` namespace, followed by the region of the repository, AWS account ID of the repository owner, and repository name. For example, `arn:aws:ecr:region:012345678910:repository/repository-name`.
Type: String
Required: No

 ** repositoryName **   <a name="ECR-Type-Repository-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

 ** repositoryUri **   <a name="ECR-Type-Repository-repositoryUri"></a>
The URI for the repository. You can use this URI for container image `push` and `pull` operations.
Type: String
Required: No

## See Also
<a name="API_Repository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/Repository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/Repository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/Repository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
