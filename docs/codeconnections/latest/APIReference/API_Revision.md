---
source_url: https://docs.aws.amazon.com/codeconnections/latest/APIReference/API_Revision.html
---

# Revision
<a name="API_Revision"></a>

Information about the revision for a specific sync event, such as the branch, owner ID, and name of the repository.

## Contents
<a name="API_Revision_Contents"></a>

 ** Branch **   <a name="codeconnections-Type-Revision-Branch"></a>
The branch name for a specific revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** Directory **   <a name="codeconnections-Type-Revision-Directory"></a>
The directory, if any, for a specific revision.
Type: String
Required: Yes

 ** OwnerId **   <a name="codeconnections-Type-Revision-OwnerId"></a>
The owner ID for a specific revision, such as the GitHub owner ID for a GitHub repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^.*$`
Required: Yes

 ** ProviderType **   <a name="codeconnections-Type-Revision-ProviderType"></a>
The provider type for a revision, such as GitHub.
Type: String
Valid Values: `Bitbucket | GitHub | GitHubEnterpriseServer | GitLab | GitLabSelfManaged | AzureDevOps`
Required: Yes

 ** RepositoryName **   <a name="codeconnections-Type-Revision-RepositoryName"></a>
The repository name for a specific revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^.*$`
Required: Yes

 ** Sha **   <a name="codeconnections-Type-Revision-Sha"></a>
The SHA, such as the commit ID, for a specific revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_Revision_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeconnections-2023-12-01/Revision)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeconnections-2023-12-01/Revision)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeconnections-2023-12-01/Revision)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeConnections. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeconnections` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
