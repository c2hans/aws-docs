---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ProviderInput.html
---

# ProviderInput
<a name="API_ProviderInput"></a>

The provider-specific input for creating an integration. This is a union type that contains provider-specific configuration.

## Contents
<a name="API_ProviderInput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** azureDevOps **   <a name="securityagent-Type-ProviderInput-azureDevOps"></a>
The Azure DevOps-specific input for creating an integration.
Type: [AzureDevOpsIntegrationInput](API_AzureDevOpsIntegrationInput.md) object
Required: No

 ** bitbucket **   <a name="securityagent-Type-ProviderInput-bitbucket"></a>
The configuration for a Bitbucket integration.
Type: [BitbucketIntegrationInput](API_BitbucketIntegrationInput.md) object
Required: No

 ** bitbucketDataCenter **   <a name="securityagent-Type-ProviderInput-bitbucketDataCenter"></a>
The Bitbucket Data Center-specific input for creating an integration.
Type: [BitbucketDataCenterIntegrationInput](API_BitbucketDataCenterIntegrationInput.md) object
Required: No

 ** confluence **   <a name="securityagent-Type-ProviderInput-confluence"></a>
The configuration for a Confluence integration.
Type: [ConfluenceIntegrationInput](API_ConfluenceIntegrationInput.md) object
Required: No

 ** github **   <a name="securityagent-Type-ProviderInput-github"></a>
The GitHub-specific input for creating an integration.
Type: [GitHubIntegrationInput](API_GitHubIntegrationInput.md) object
Required: No

 ** gitlab **   <a name="securityagent-Type-ProviderInput-gitlab"></a>
The configuration for a GitLab integration.
Type: [GitLabIntegrationInput](API_GitLabIntegrationInput.md) object
Required: No

## See Also
<a name="API_ProviderInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ProviderInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ProviderInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ProviderInput)
