---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CspmConnectorSummary.html
---

# CspmConnectorSummary
<a name="API_CspmConnectorSummary"></a>

A summary of a CSPM connector.

## Contents
<a name="API_CspmConnectorSummary_Contents"></a>

 ** ConnectorArn **   <a name="securityhub-Type-CspmConnectorSummary-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ConnectorId **   <a name="securityhub-Type-CspmConnectorSummary-ConnectorId"></a>
The unique identifier of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedAt **   <a name="securityhub-Type-CspmConnectorSummary-CreatedAt"></a>
The ISO 8601 UTC timestamp indicating when the connector was created.
Type: Timestamp
Required: No

 ** CreatedBy **   <a name="securityhub-Type-CspmConnectorSummary-CreatedBy"></a>
The service principal that created the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-CspmConnectorSummary-Description"></a>
The description of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnablementStatus **   <a name="securityhub-Type-CspmConnectorSummary-EnablementStatus"></a>
The enablement status of the connector.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`
Required: No

 ** Name **   <a name="securityhub-Type-CspmConnectorSummary-Name"></a>
The name of the connector.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProviderSummary **   <a name="securityhub-Type-CspmConnectorSummary-ProviderSummary"></a>
A summary of the cloud provider configuration for the connector.
Type: [CspmProviderSummary](API_CspmProviderSummary.md) object
Required: No

## See Also
<a name="API_CspmConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CspmConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CspmConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CspmConnectorSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
