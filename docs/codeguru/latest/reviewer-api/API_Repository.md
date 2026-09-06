---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_Repository.html
---

# Repository
<a name="API_Repository"></a>

Information about an associated AWS CodeCommit repository or an associated repository that is managed by AWS CodeStar Connections (for example, Bitbucket). This `Repository` object is not used if your source code is in an associated GitHub repository.

## Contents
<a name="API_Repository_Contents"></a>

 ** Bitbucket **   <a name="reviewer-Type-Repository-Bitbucket"></a>
 Information about a Bitbucket repository.
Type: [ThirdPartySourceRepository](API_ThirdPartySourceRepository.md) object
Required: No

 ** CodeCommit **   <a name="reviewer-Type-Repository-CodeCommit"></a>
Information about an AWS CodeCommit repository.
Type: [CodeCommitRepository](API_CodeCommitRepository.md) object
Required: No

 ** GitHub **   <a name="reviewer-Type-Repository-GitHub"></a>
Information about a GitHub repository associated with CodeGuru Reviewer.
Type: [GitHubRepository](API_GitHubRepository.md) object
Required: No

 ** GitHubEnterpriseServer **   <a name="reviewer-Type-Repository-GitHubEnterpriseServer"></a>
Information about a GitHub Enterprise Server repository.
Type: [ThirdPartySourceRepository](API_ThirdPartySourceRepository.md) object
Required: No

 ** S3Bucket **   <a name="reviewer-Type-Repository-S3Bucket"></a>
Information about a repository in an S3 bucket.
Type: [S3Repository](API_S3Repository.md) object
Required: No

## See Also
<a name="API_Repository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/Repository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/Repository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/Repository)
