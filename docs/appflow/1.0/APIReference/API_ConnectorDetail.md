---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorDetail.html
---

# ConnectorDetail
<a name="API_ConnectorDetail"></a>

Information about the registered connector.

## Contents
<a name="API_ConnectorDetail_Contents"></a>

 ** applicationType **   <a name="appflow-Type-ConnectorDetail-applicationType"></a>
The application type of the connector.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** connectorDescription **   <a name="appflow-Type-ConnectorDetail-connectorDescription"></a>
A description about the registered connector.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

 ** connectorLabel **   <a name="appflow-Type-ConnectorDetail-connectorLabel"></a>
A label used for the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** connectorModes **   <a name="appflow-Type-ConnectorDetail-connectorModes"></a>
The connection mode that the connector supports.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** connectorName **   <a name="appflow-Type-ConnectorDetail-connectorName"></a>
The name of the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** connectorOwner **   <a name="appflow-Type-ConnectorDetail-connectorOwner"></a>
The owner of the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** connectorProvisioningType **   <a name="appflow-Type-ConnectorDetail-connectorProvisioningType"></a>
The provisioning type that the connector uses.
Type: String
Valid Values: `LAMBDA`
Required: No

 ** connectorType **   <a name="appflow-Type-ConnectorDetail-connectorType"></a>
The connector type.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** connectorVersion **   <a name="appflow-Type-ConnectorDetail-connectorVersion"></a>
The connector version.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** registeredAt **   <a name="appflow-Type-ConnectorDetail-registeredAt"></a>
The time at which the connector was registered.
Type: Timestamp
Required: No

 ** registeredBy **   <a name="appflow-Type-ConnectorDetail-registeredBy"></a>
The user who registered the connector.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** supportedDataTransferTypes **   <a name="appflow-Type-ConnectorDetail-supportedDataTransferTypes"></a>
The data transfer types that the connector supports.
RECORD
Structured records.
FILE
Files or binary data.
Type: Array of strings
Valid Values: `RECORD | FILE`
Required: No

## See Also
<a name="API_ConnectorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorDetail)
