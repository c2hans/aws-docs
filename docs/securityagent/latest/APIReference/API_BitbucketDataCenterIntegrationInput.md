---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BitbucketDataCenterIntegrationInput.html
---

# BitbucketDataCenterIntegrationInput
<a name="API_BitbucketDataCenterIntegrationInput"></a>

Connection details for a self-managed Bitbucket Data Center integration.

## Contents
<a name="API_BitbucketDataCenterIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-BitbucketDataCenterIntegrationInput-code"></a>
The OAuth 2.0 authorization code returned to your redirect URL after the connection is authorized.
Type: String
Required: Yes

 ** state **   <a name="securityagent-Type-BitbucketDataCenterIntegrationInput-state"></a>
The CSRF state value returned by `InitiateProviderRegistration` and echoed back on the authorization redirect.
Type: String
Required: Yes

 ** targetUrl **   <a name="securityagent-Type-BitbucketDataCenterIntegrationInput-targetUrl"></a>
The HTTPS URL of your Bitbucket Data Center instance, for example `https://bitbucket.example.com`.
Type: String
Required: Yes

## See Also
<a name="API_BitbucketDataCenterIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BitbucketDataCenterIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BitbucketDataCenterIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BitbucketDataCenterIntegrationInput)
