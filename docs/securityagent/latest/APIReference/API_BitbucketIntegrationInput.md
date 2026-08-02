---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BitbucketIntegrationInput.html
---

# BitbucketIntegrationInput
<a name="API_BitbucketIntegrationInput"></a>

The configuration for creating a Bitbucket integration.

## Contents
<a name="API_BitbucketIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-BitbucketIntegrationInput-code"></a>
The OAuth 2.0 authorization code returned from the consent redirect.
Type: String
Required: Yes

 ** installationId **   <a name="securityagent-Type-BitbucketIntegrationInput-installationId"></a>
The Atlassian installation identifier, available from the Atlassian administration console.
Type: String
Required: Yes

 ** state **   <a name="securityagent-Type-BitbucketIntegrationInput-state"></a>
The CSRF state token echoed back from the OAuth redirect.
Type: String
Required: Yes

 ** workspace **   <a name="securityagent-Type-BitbucketIntegrationInput-workspace"></a>
The Bitbucket workspace slug that identifies the workspace to integrate, for example acme-corp.
Type: String
Required: Yes

## See Also
<a name="API_BitbucketIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BitbucketIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BitbucketIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BitbucketIntegrationInput)
