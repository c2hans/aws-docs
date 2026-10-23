---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GitHubTarget.html
---

# GitHubTarget
<a name="API_GitHubTarget"></a>

The git Hub Target.

## Contents
<a name="API_GitHubTarget_Contents"></a>

 ** owner **   <a name="continuum-Type-GitHubTarget-owner"></a>
The owner.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** repository **   <a name="continuum-Type-GitHubTarget-repository"></a>
The repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** headSha **   <a name="continuum-Type-GitHubTarget-headSha"></a>
The head Sha.
Type: String
Length Constraints: Fixed length of 40.
Pattern: `[a-fA-F0-9]{40}`
Required: No

 ** pullRequestNumber **   <a name="continuum-Type-GitHubTarget-pullRequestNumber"></a>
The pull Request Number.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_GitHubTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GitHubTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GitHubTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GitHubTarget)
