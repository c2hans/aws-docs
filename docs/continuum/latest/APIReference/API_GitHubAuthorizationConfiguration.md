---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GitHubAuthorizationConfiguration.html
---

# GitHubAuthorizationConfiguration
<a name="API_GitHubAuthorizationConfiguration"></a>

Write-only OAuth credentials used to authorize a GitHub.com integration. Not stored or returned after creation.

## Contents
<a name="API_GitHubAuthorizationConfiguration_Contents"></a>

 ** authorizationCode **   <a name="continuum-Type-GitHubAuthorizationConfiguration-authorizationCode"></a>
The authorization Code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** state **   <a name="continuum-Type-GitHubAuthorizationConfiguration-state"></a>
The state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** redirectUrl **   <a name="continuum-Type-GitHubAuthorizationConfiguration-redirectUrl"></a>
The redirect Url.
Type: String
Length Constraints: Minimum length of 9. Maximum length of 2083.
Pattern: `https://.*`
Required: No

## See Also
<a name="API_GitHubAuthorizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GitHubAuthorizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GitHubAuthorizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GitHubAuthorizationConfiguration)
