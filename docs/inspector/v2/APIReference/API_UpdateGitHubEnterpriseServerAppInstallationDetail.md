---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateGitHubEnterpriseServerAppInstallationDetail.html
---

# UpdateGitHubEnterpriseServerAppInstallationDetail

Contains the details required to complete the GitHub App installation for a GitHub Enterprise Server integration.

## Contents
<a name="API_UpdateGitHubEnterpriseServerAppInstallationDetail_Contents"></a>

 ** code **   <a name="inspector2-Type-UpdateGitHubEnterpriseServerAppInstallationDetail-code"></a>
The authorization code received from GitHub Enterprise Server.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** installationId **   <a name="inspector2-Type-UpdateGitHubEnterpriseServerAppInstallationDetail-installationId"></a>
The installation ID of the GitHub App associated with the integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** stateToken **   <a name="inspector2-Type-UpdateGitHubEnterpriseServerAppInstallationDetail-stateToken"></a>
The PKCE state token used to validate the authorization request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[A-Za-z0-9_-]+`
Required: No

## See Also
<a name="API_UpdateGitHubEnterpriseServerAppInstallationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateGitHubEnterpriseServerAppInstallationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateGitHubEnterpriseServerAppInstallationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateGitHubEnterpriseServerAppInstallationDetail)
