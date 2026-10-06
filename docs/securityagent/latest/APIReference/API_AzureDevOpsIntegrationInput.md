---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_AzureDevOpsIntegrationInput.html
---

# AzureDevOpsIntegrationInput
<a name="API_AzureDevOpsIntegrationInput"></a>

Connection details for an Azure DevOps integration.

## Contents
<a name="API_AzureDevOpsIntegrationInput_Contents"></a>

 ** code **   <a name="securityagent-Type-AzureDevOpsIntegrationInput-code"></a>
The OAuth 2.0 authorization code returned to your redirect URL after the connection is authorized.
Type: String
Required: Yes

 ** organizationName **   <a name="securityagent-Type-AzureDevOpsIntegrationInput-organizationName"></a>
The name of the Azure DevOps organization to connect, for example `my-org`.
Type: String
Required: Yes

 ** state **   <a name="securityagent-Type-AzureDevOpsIntegrationInput-state"></a>
The CSRF state value returned by `InitiateProviderRegistration` and echoed back on the authorization redirect.
Type: String
Required: Yes

## See Also
<a name="API_AzureDevOpsIntegrationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/AzureDevOpsIntegrationInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/AzureDevOpsIntegrationInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/AzureDevOpsIntegrationInput)
