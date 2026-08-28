---
source_url: https://docs.aws.amazon.com/codecommit/latest/APIReference/API_RepositoryMetadata.html
---

# RepositoryMetadata
<a name="API_RepositoryMetadata"></a>

Information about a repository.

## Contents
<a name="API_RepositoryMetadata_Contents"></a>

 ** accountId **   <a name="CodeCommit-Type-RepositoryMetadata-accountId"></a>
The ID of the AWS account associated with the repository.
Type: String
Required: No

 ** Arn **   <a name="CodeCommit-Type-RepositoryMetadata-Arn"></a>
The Amazon Resource Name (ARN) of the repository.
Type: String
Required: No

 ** cloneUrlHttp **   <a name="CodeCommit-Type-RepositoryMetadata-cloneUrlHttp"></a>
The URL to use for cloning the repository over HTTPS.
Type: String
Required: No

 ** cloneUrlSsh **   <a name="CodeCommit-Type-RepositoryMetadata-cloneUrlSsh"></a>
The URL to use for cloning the repository over SSH.
Type: String
Required: No

 ** creationDate **   <a name="CodeCommit-Type-RepositoryMetadata-creationDate"></a>
The date and time the repository was created, in timestamp format.
Type: Timestamp
Required: No

 ** defaultBranch **   <a name="CodeCommit-Type-RepositoryMetadata-defaultBranch"></a>
The repository's default branch name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** kmsKeyId **   <a name="CodeCommit-Type-RepositoryMetadata-kmsKeyId"></a>
The ID of the AWS Key Management Service encryption key used to encrypt and decrypt the repository.
Type: String
Pattern: `^[a-zA-Z0-9:/_-]+$`
Required: No

 ** lastModifiedDate **   <a name="CodeCommit-Type-RepositoryMetadata-lastModifiedDate"></a>
The date and time the repository was last modified, in timestamp format.
Type: Timestamp
Required: No

 ** repositoryDescription **   <a name="CodeCommit-Type-RepositoryMetadata-repositoryDescription"></a>
A comment or description about the repository.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** repositoryId **   <a name="CodeCommit-Type-RepositoryMetadata-repositoryId"></a>
The ID of the repository.
Type: String
Required: No

 ** repositoryName **   <a name="CodeCommit-Type-RepositoryMetadata-repositoryName"></a>
The repository's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\.-]+`
Required: No

## See Also
<a name="API_RepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecommit-2015-04-13/RepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecommit-2015-04-13/RepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecommit-2015-04-13/RepositoryMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
