---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_IntegrationSummary.html
---

# IntegrationSummary
<a name="API_IntegrationSummary"></a>

Contains summary information about an integration.

## Contents
<a name="API_IntegrationSummary_Contents"></a>

 ** displayName **   <a name="securityagent-Type-IntegrationSummary-displayName"></a>
The display name of the integration.
Type: String
Required: Yes

 ** installationId **   <a name="securityagent-Type-IntegrationSummary-installationId"></a>
The installation identifier from the integration provider.
Type: String
Required: Yes

 ** integrationId **   <a name="securityagent-Type-IntegrationSummary-integrationId"></a>
The unique identifier of the integration.
Type: String
Required: Yes

 ** provider **   <a name="securityagent-Type-IntegrationSummary-provider"></a>
The integration provider.
Type: String
Valid Values: `GITHUB | GITLAB | BITBUCKET | CONFLUENCE | AZURE_DEVOPS`
Required: Yes

 ** providerType **   <a name="securityagent-Type-IntegrationSummary-providerType"></a>
The type of the integration provider.
Type: String
Valid Values: `SOURCE_CODE | DOCUMENTATION`
Required: Yes

 ** privateConnectionName **   <a name="securityagent-Type-IntegrationSummary-privateConnectionName"></a>
The name of the private connection used to reach the integration's self-hosted instance over private networking, if one is configured.
Type: String
Required: No

 ** targetUrl **   <a name="securityagent-Type-IntegrationSummary-targetUrl"></a>
The HTTPS URL of the customer self-hosted instance, such as a GitHub Enterprise Server or self-managed GitLab instance. This value is absent for SaaS integrations.
Type: String
Required: No

 ** webhookUrl **   <a name="securityagent-Type-IntegrationSummary-webhookUrl"></a>
The payload URL of the integration's webhook, once it has been created. The signing secret is never returned on a read.
Type: String
Required: No

## See Also
<a name="API_IntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/IntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/IntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/IntegrationSummary)
