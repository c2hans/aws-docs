---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_IntegrationSummary.html
---

# IntegrationSummary
<a name="API_IntegrationSummary"></a>

This structure contains information about one CloudWatch Logs integration. This structure is returned by a [ListIntegrations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html) operation.

## Contents
<a name="API_IntegrationSummary_Contents"></a>

 ** integrationName **   <a name="CWL-Type-IntegrationSummary-integrationName"></a>
The name of this integration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** integrationStatus **   <a name="CWL-Type-IntegrationSummary-integrationStatus"></a>
The current status of this integration.
Type: String
Valid Values: `PROVISIONING | ACTIVE | FAILED`
Required: No

 ** integrationType **   <a name="CWL-Type-IntegrationSummary-integrationType"></a>
The type of integration. Integrations with OpenSearch Service have the type `OPENSEARCH`.
Type: String
Valid Values: `OPENSEARCH`
Required: No

## See Also
<a name="API_IntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/IntegrationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/IntegrationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/IntegrationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
