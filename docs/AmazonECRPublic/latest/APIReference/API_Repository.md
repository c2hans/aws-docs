---
source_url: https://docs.aws.amazon.com/AmazonECRPublic/latest/APIReference/API_Repository.html
---

# Repository
<a name="API_Repository"></a>

An object representing a repository.

## Contents
<a name="API_Repository_Contents"></a>

 ** createdAt **   <a name="ecrpublic-Type-Repository-createdAt"></a>
The date and time, in JavaScript date format, when the repository was created.
Type: Timestamp
Required: No

 ** registryId **   <a name="ecrpublic-Type-Repository-registryId"></a>
The AWS account ID that's associated with the public registry that contains the repository.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** repositoryArn **   <a name="ecrpublic-Type-Repository-repositoryArn"></a>
The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the `arn:aws:ecr` namespace, followed by the region of the repository, AWS account ID of the repository owner, repository namespace, and repository name. For example, `arn:aws:ecr:region:012345678910:repository/test`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** repositoryName **   <a name="ecrpublic-Type-Repository-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 205.
Pattern: `(?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*`
Required: No

 ** repositoryUri **   <a name="ecrpublic-Type-Repository-repositoryUri"></a>
The URI for the repository. You can use this URI for container image `push` and `pull` operations.
Type: String
Required: No

## See Also
<a name="API_Repository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-public-2020-10-30/Repository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-public-2020-10-30/Repository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-public-2020-10-30/Repository)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ECR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECRPublic` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
