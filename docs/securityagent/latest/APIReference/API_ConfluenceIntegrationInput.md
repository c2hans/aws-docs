---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ConfluenceIntegrationInput.html
---

# ConfluenceIntegrationInput
<a name="API_ConfluenceIntegrationInput"></a>

The configuration for creating a Confluence integration.

## Contents
<a name="API_ConfluenceIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-ConfluenceIntegrationInput-code"></a>
The OAuth 2.0 authorization code returned from the consent redirect.
Type: String
Required: Yes

 ** installationId **   <a name="securityagent-Type-ConfluenceIntegrationInput-installationId"></a>
The Atlassian installation identifier, available from the Atlassian administration console.
Type: String
Required: Yes

 ** siteUrl **   <a name="securityagent-Type-ConfluenceIntegrationInput-siteUrl"></a>
The Confluence Cloud site URL, for example https://mysite.atlassian.net.
Type: String
Required: Yes

 ** state **   <a name="securityagent-Type-ConfluenceIntegrationInput-state"></a>
The CSRF state token echoed back from the OAuth redirect.
Type: String
Required: Yes

## See Also
<a name="API_ConfluenceIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ConfluenceIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ConfluenceIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ConfluenceIntegrationInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
