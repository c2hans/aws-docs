---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryCreationTemplate.html
---

# RepositoryCreationTemplate
<a name="API_RepositoryCreationTemplate"></a>

The details of the repository creation template associated with the request.

## Contents
<a name="API_RepositoryCreationTemplate_Contents"></a>

 ** appliedFor **   <a name="ECR-Type-RepositoryCreationTemplate-appliedFor"></a>
A list of enumerable Strings representing the repository creation scenarios that this template will apply towards. The supported scenarios are PULL\_THROUGH\_CACHE, REPLICATION, and CREATE\_ON\_PUSH
Type: Array of strings
Valid Values: `REPLICATION | PULL_THROUGH_CACHE | CREATE_ON_PUSH`
Required: No

 ** createdAt **   <a name="ECR-Type-RepositoryCreationTemplate-createdAt"></a>
The date and time, in JavaScript date format, when the repository creation template was created.
Type: Timestamp
Required: No

 ** customRoleArn **   <a name="ECR-Type-RepositoryCreationTemplate-customRoleArn"></a>
The ARN of the role to be assumed by Amazon ECR. Amazon ECR will assume your supplied role when the customRoleArn is specified. When this field isn't specified, Amazon ECR will use the service-linked role for the repository creation template.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** description **   <a name="ECR-Type-RepositoryCreationTemplate-description"></a>
The description associated with the repository creation template.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** encryptionConfiguration **   <a name="ECR-Type-RepositoryCreationTemplate-encryptionConfiguration"></a>
The encryption configuration associated with the repository creation template.
Type: [EncryptionConfigurationForRepositoryCreationTemplate](API_EncryptionConfigurationForRepositoryCreationTemplate.md) object
Required: No

 ** imageTagMutability **   <a name="ECR-Type-RepositoryCreationTemplate-imageTagMutability"></a>
The tag mutability setting for the repository. If this parameter is omitted, the default setting of `MUTABLE` will be used which will allow image tags to be overwritten. If `IMMUTABLE` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.
Type: String
Valid Values: `MUTABLE | IMMUTABLE | IMMUTABLE_WITH_EXCLUSION | MUTABLE_WITH_EXCLUSION`
Required: No

 ** imageTagMutabilityExclusionFilters **   <a name="ECR-Type-RepositoryCreationTemplate-imageTagMutabilityExclusionFilters"></a>
A list of filters that specify which image tags are excluded from the repository creation template's image tag mutability setting.
Type: Array of [ImageTagMutabilityExclusionFilter](API_ImageTagMutabilityExclusionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** lifecyclePolicy **   <a name="ECR-Type-RepositoryCreationTemplate-lifecyclePolicy"></a>
The lifecycle policy to use for repositories created using the template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 30720.
Required: No

 ** prefix **   <a name="ECR-Type-RepositoryCreationTemplate-prefix"></a>
The repository namespace prefix associated with the repository creation template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^([a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*\/?|ROOT)$`
Required: No

 ** repositoryPolicy **   <a name="ECR-Type-RepositoryCreationTemplate-repositoryPolicy"></a>
The repository policy to apply to repositories created using the template. A repository policy is a permissions policy associated with a repository to control access permissions.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: No

 ** resourceTags **   <a name="ECR-Type-RepositoryCreationTemplate-resourceTags"></a>
The metadata to apply to the repository to help you categorize and organize. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** updatedAt **   <a name="ECR-Type-RepositoryCreationTemplate-updatedAt"></a>
The date and time, in JavaScript date format, when the repository creation template was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_RepositoryCreationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RepositoryCreationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RepositoryCreationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RepositoryCreationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
