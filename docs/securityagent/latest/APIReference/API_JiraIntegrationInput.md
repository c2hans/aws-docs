---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_JiraIntegrationInput.html
---

# JiraIntegrationInput
<a name="API_JiraIntegrationInput"></a>

The configuration for creating a Jira integration.

## Contents
<a name="API_JiraIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-JiraIntegrationInput-code"></a>
The OAuth 2.0 authorization code returned from the consent redirect.
Type: String
Required: Yes

 ** installationId **   <a name="securityagent-Type-JiraIntegrationInput-installationId"></a>
The Atlassian installation identifier, available from the Atlassian administration console.
Type: String
Required: Yes

 ** siteUrl **   <a name="securityagent-Type-JiraIntegrationInput-siteUrl"></a>
The Jira Cloud site URL, for example https://mysite.atlassian.net.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `https://[a-zA-Z0-9\-]+\.atlassian\.net`
Required: Yes

 ** state **   <a name="securityagent-Type-JiraIntegrationInput-state"></a>
The CSRF state token echoed back from the OAuth redirect.
Type: String
Required: Yes

## See Also
<a name="API_JiraIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/JiraIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/JiraIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/JiraIntegrationInput)
