---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositoryDescription.html
---

# RepositoryDescription
<a name="API_RepositoryDescription"></a>

 The details of a repository stored in AWS CodeArtifact. A CodeArtifact repository contains a set of package versions, each of which maps to a set of assets. Repositories are polyglot—a single repository can contain packages of any supported type. Each repository exposes endpoints for fetching and publishing packages using tools like the `npm` CLI, the Maven CLI (`mvn`), and `pip`. You can create up to 100 repositories per AWS account.

## Contents
<a name="API_RepositoryDescription_Contents"></a>

 ** administratorAccount **   <a name="codeartifact-Type-RepositoryDescription-administratorAccount"></a>
 The 12-digit account number of the AWS account that manages the repository.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** arn **   <a name="codeartifact-Type-RepositoryDescription-arn"></a>
 The Amazon Resource Name (ARN) of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** createdTime **   <a name="codeartifact-Type-RepositoryDescription-createdTime"></a>
A timestamp that represents the date and time the repository was created.
Type: Timestamp
Required: No

 ** description **   <a name="codeartifact-Type-RepositoryDescription-description"></a>
 A text description of the repository.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** domainName **   <a name="codeartifact-Type-RepositoryDescription-domainName"></a>
 The name of the domain that contains the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: No

 ** domainOwner **   <a name="codeartifact-Type-RepositoryDescription-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain that contains the repository. It does not include dashes or spaces.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** externalConnections **   <a name="codeartifact-Type-RepositoryDescription-externalConnections"></a>
 An array of external connections associated with the repository.
Type: Array of [RepositoryExternalConnectionInfo](API_RepositoryExternalConnectionInfo.md) objects
Required: No

 ** name **   <a name="codeartifact-Type-RepositoryDescription-name"></a>
 The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: No

 ** upstreams **   <a name="codeartifact-Type-RepositoryDescription-upstreams"></a>
 A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when AWS CodeArtifact looks for a requested package version. For more information, see [Working with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html).
Type: Array of [UpstreamRepositoryInfo](API_UpstreamRepositoryInfo.md) objects
Required: No

## See Also
<a name="API_RepositoryDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/RepositoryDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/RepositoryDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/RepositoryDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeArtifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeartifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
