---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ConnectorSummary.html
---

# ConnectorSummary
<a name="API_ConnectorSummary"></a>

A condensed overview of the connectorV2..

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** ConnectorId **   <a name="securityhub-Type-ConnectorSummary-ConnectorId"></a>
The UUID of the connectorV2 to identify connectorV2 resource.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** CreatedAt **   <a name="securityhub-Type-ConnectorSummary-CreatedAt"></a>
ISO 8601 UTC timestamp for the time create the connectorV2.
Type: Timestamp
Required: Yes

 ** Name **   <a name="securityhub-Type-ConnectorSummary-Name"></a>
The Name field contains the user-defined name assigned to the integration connector. This helps identify and manage multiple connectors within Security Hub.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ProviderSummary **   <a name="securityhub-Type-ConnectorSummary-ProviderSummary"></a>
The connectorV2 third party provider configuration summary.
Type: [ProviderSummary](API_ProviderSummary.md) object
Required: Yes

 ** ConnectorArn **   <a name="securityhub-Type-ConnectorSummary-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connectorV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-ConnectorSummary-Description"></a>
The description of the connectorV2.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EnablementStatus **   <a name="securityhub-Type-ConnectorSummary-EnablementStatus"></a>
The enablement status of the connector.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | FAILED_TO_ENABLE | PENDING_UPDATE | FAILED_TO_UPDATE | PENDING_DELETION | FAILED_TO_DELETE`
Required: No

 ** EnablementStatusReason **   <a name="securityhub-Type-ConnectorSummary-EnablementStatusReason"></a>
The reason for the current enablement status. Provides additional context when the connector is in a failed state.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ConnectorSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ConnectorSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ConnectorSummary)
