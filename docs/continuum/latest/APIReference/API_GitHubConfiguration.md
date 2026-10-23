---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_GitHubConfiguration.html
---

# GitHubConfiguration
<a name="API_GitHubConfiguration"></a>

Configuration for a GitHub.com integration using the OAuth authorization code flow.

## Contents
<a name="API_GitHubConfiguration_Contents"></a>

 ** authorization **   <a name="continuum-Type-GitHubConfiguration-authorization"></a>
Write-only OAuth credentials used to authorize a GitHub.com integration. Not stored or returned after creation.
Type: [GitHubAuthorizationConfiguration](API_GitHubAuthorizationConfiguration.md) object
Required: Yes

 ** organizationName **   <a name="continuum-Type-GitHubConfiguration-organizationName"></a>
The organization Name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?`
Required: No

## See Also
<a name="API_GitHubConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/GitHubConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/GitHubConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/GitHubConfiguration)
