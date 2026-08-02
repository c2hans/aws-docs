---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_GitLabIntegrationInput.html
---

# GitLabIntegrationInput
<a name="API_GitLabIntegrationInput"></a>

The configuration for creating a GitLab integration.

## Contents
<a name="API_GitLabIntegrationInput_Contents"></a>

 ** accessToken **   <a name="securityagent-Type-GitLabIntegrationInput-accessToken"></a>
The GitLab access token used to authenticate. This can be a personal access token or a group access token.
Type: String
Required: Yes

 ** tokenType **   <a name="securityagent-Type-GitLabIntegrationInput-tokenType"></a>
The type of GitLab access token provided in accessToken.
Type: String
Valid Values: `PERSONAL | GROUP`
Required: Yes

 ** groupId **   <a name="securityagent-Type-GitLabIntegrationInput-groupId"></a>
The identifier of the GitLab group. Required when tokenType is group and ignored for personal tokens.
Type: String
Required: No

 ** targetUrl **   <a name="securityagent-Type-GitLabIntegrationInput-targetUrl"></a>
The HTTPS URL of a self-managed GitLab instance. Omit this value for GitLab SaaS (gitlab.com).
Type: String
Required: No

## See Also
<a name="API_GitLabIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/GitLabIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/GitLabIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/GitLabIntegrationInput)
