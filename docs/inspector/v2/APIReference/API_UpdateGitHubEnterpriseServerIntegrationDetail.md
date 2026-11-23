---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateGitHubEnterpriseServerIntegrationDetail.html
---

# UpdateGitHubEnterpriseServerIntegrationDetail

Contains the details required to update an integration with a GitHub Enterprise Server instance. Provide one of the following, depending on the step of the setup flow.

## Contents
<a name="API_UpdateGitHubEnterpriseServerIntegrationDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** appInstallation **   <a name="inspector2-Type-UpdateGitHubEnterpriseServerIntegrationDetail-appInstallation"></a>
Details for completing the GitHub App installation step of the GitHub Enterprise Server integration.
Type: [UpdateGitHubEnterpriseServerAppInstallationDetail](API_UpdateGitHubEnterpriseServerAppInstallationDetail.md) object
Required: No

 ** appRegistration **   <a name="inspector2-Type-UpdateGitHubEnterpriseServerIntegrationDetail-appRegistration"></a>
Details for completing the GitHub App manifest registration step of the GitHub Enterprise Server integration.
Type: [GitHubEnterpriseServerAppRegistrationDetail](API_GitHubEnterpriseServerAppRegistrationDetail.md) object
Required: No

## See Also
<a name="API_UpdateGitHubEnterpriseServerIntegrationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/UpdateGitHubEnterpriseServerIntegrationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/UpdateGitHubEnterpriseServerIntegrationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/UpdateGitHubEnterpriseServerIntegrationDetail)
