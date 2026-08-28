---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociationSummary.html
---

# RepositoryAssociationSummary
<a name="API_RepositoryAssociationSummary"></a>

Summary information about a repository association. The [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html) operation returns a list of `RepositoryAssociationSummary` objects.

## Contents
<a name="API_RepositoryAssociationSummary_Contents"></a>

 ** AssociationArn **   <a name="reviewer-Type-RepositoryAssociationSummary-AssociationArn"></a>
The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object. You can retrieve this ARN by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws:codeguru-reviewer:[^:\s]+:[\d]{12}:association:[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: No

 ** AssociationId **   <a name="reviewer-Type-RepositoryAssociationSummary-AssociationId"></a>
The repository association ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** ConnectionArn **   <a name="reviewer-Type-RepositoryAssociationSummary-ConnectionArn"></a>
The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection. Its format is `arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id`. For more information, see [Connection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html) in the * AWS CodeStar Connections API Reference*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws(-[\w]+)*:.+:.+:[0-9]{12}:.+`
Required: No

 ** LastUpdatedTimeStamp **   <a name="reviewer-Type-RepositoryAssociationSummary-LastUpdatedTimeStamp"></a>
The time, in milliseconds since the epoch, since the repository association was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="reviewer-Type-RepositoryAssociationSummary-Name"></a>
The name of the repository association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** Owner **   <a name="reviewer-Type-RepositoryAssociationSummary-Owner"></a>
The owner of the repository. For an AWS CodeCommit repository, this is the AWS account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or AWS account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** ProviderType **   <a name="reviewer-Type-RepositoryAssociationSummary-ProviderType"></a>
The provider type of the repository association.
Type: String
Valid Values: `CodeCommit | GitHub | Bitbucket | GitHubEnterpriseServer | S3Bucket`
Required: No

 ** State **   <a name="reviewer-Type-RepositoryAssociationSummary-State"></a>
The state of the repository association.
The valid repository association states are:
+  **Associated**: The repository association is complete.
+  **Associating**: CodeGuru Reviewer is:
  + Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.
**Note**
If your repository `ProviderType` is `GitHub`, `GitHub Enterprise Server`, or `Bitbucket`, CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.
  + Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.
+  **Failed**: The repository failed to associate or disassociate.
+  **Disassociating**: CodeGuru Reviewer is removing the repository's pull request notifications and source code access.
+  **Disassociated**: CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see [Using tags to control access to associated repositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html) in the *Amazon CodeGuru Reviewer User Guide*.
Type: String
Valid Values: `Associated | Associating | Failed | Disassociating | Disassociated`
Required: No

## See Also
<a name="API_RepositoryAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RepositoryAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RepositoryAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RepositoryAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
