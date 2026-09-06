---
source_url: https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html
---

# RepositorySummary
<a name="API_RepositorySummary"></a>

 Details about a repository, including its Amazon Resource Name (ARN), description, and domain information. The [ListRepositories](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListRepositories.html) operation returns a list of `RepositorySummary` objects.

## Contents
<a name="API_RepositorySummary_Contents"></a>

 ** administratorAccount **   <a name="codeartifact-Type-RepositorySummary-administratorAccount"></a>
 The AWS account ID that manages the repository.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** arn **   <a name="codeartifact-Type-RepositorySummary-arn"></a>
 The ARN of the repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `\S+`
Required: No

 ** createdTime **   <a name="codeartifact-Type-RepositorySummary-createdTime"></a>
A timestamp that represents the date and time the repository was created.
Type: Timestamp
Required: No

 ** description **   <a name="codeartifact-Type-RepositorySummary-description"></a>
 The description of the repository.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** domainName **   <a name="codeartifact-Type-RepositorySummary-domainName"></a>
 The name of the domain that contains the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-z][a-z0-9\-]{0,48}[a-z0-9]`
Required: No

 ** domainOwner **   <a name="codeartifact-Type-RepositorySummary-domainOwner"></a>
 The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** name **   <a name="codeartifact-Type-RepositorySummary-name"></a>
 The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `[A-Za-z0-9][A-Za-z0-9._\-]{1,99}`
Required: No

## See Also
<a name="API_RepositorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeartifact-2018-09-22/RepositorySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeartifact-2018-09-22/RepositorySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeartifact-2018-09-22/RepositorySummary)
