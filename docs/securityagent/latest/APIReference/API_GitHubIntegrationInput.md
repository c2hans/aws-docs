---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GitHubIntegrationInput.html
---

# GitHubIntegrationInput
<a name="API_GitHubIntegrationInput"></a>

The input required to create a GitHub integration, including the OAuth authorization code and CSRF state.

## Contents
<a name="API_GitHubIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-GitHubIntegrationInput-code"></a>
The OAuth authorization code received from GitHub.
Type: String
Required: Yes

 ** state **   <a name="securityagent-Type-GitHubIntegrationInput-state"></a>
The CSRF state token for validating the OAuth flow.
Type: String
Required: Yes

 ** installationId **   <a name="securityagent-Type-GitHubIntegrationInput-installationId"></a>
The installation identifier provided by GitHub Enterprise Server on the install callback. Required for GitHub Enterprise Server integrations and ignored for GitHub.com.
Type: String
Required: No

 ** organizationName **   <a name="securityagent-Type-GitHubIntegrationInput-organizationName"></a>
The name of the GitHub organization to integrate with.
Type: String
Required: No

 ** targetUrl **   <a name="securityagent-Type-GitHubIntegrationInput-targetUrl"></a>
The HTTPS URL of a self-hosted GitHub Enterprise Server instance. Omit this value for GitHub.com.
Type: String
Required: No

## See Also
<a name="API_GitHubIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GitHubIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GitHubIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GitHubIntegrationInput)
