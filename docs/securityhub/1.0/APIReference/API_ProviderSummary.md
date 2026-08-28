---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ProviderSummary.html
---

# ProviderSummary
<a name="API_ProviderSummary"></a>

The connectorV2 third-party provider configuration summary.

## Contents
<a name="API_ProviderSummary_Contents"></a>

 ** ConnectorStatus **   <a name="securityhub-Type-ProviderSummary-ConnectorStatus"></a>
The status for the connectorV2.
Type: String
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | PENDING_AUTHORIZATION | PENDING_CONFIGURATION | UNKNOWN`
Required: No

 ** ProviderConfiguration **   <a name="securityhub-Type-ProviderSummary-ProviderConfiguration"></a>
The third-party provider detail for a service configuration.
Type: [ProviderDetail](API_ProviderDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ProviderName **   <a name="securityhub-Type-ProviderSummary-ProviderName"></a>
The name of the provider.
Type: String
Valid Values: `JIRA_CLOUD | SERVICENOW | AZURE`
Required: No

## See Also
<a name="API_ProviderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ProviderSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ProviderSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ProviderSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
