---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DestinationFlowConfig.html
---

# DestinationFlowConfig
<a name="API_DestinationFlowConfig"></a>

 Contains information about the configuration of destination connectors present in the flow.

## Contents
<a name="API_DestinationFlowConfig_Contents"></a>

 ** connectorType **   <a name="appflow-Type-DestinationFlowConfig-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: Yes

 ** destinationConnectorProperties **   <a name="appflow-Type-DestinationFlowConfig-destinationConnectorProperties"></a>
 This stores the information that is required to query a particular connector.
Type: [DestinationConnectorProperties](API_DestinationConnectorProperties.md) object
Required: Yes

 ** apiVersion **   <a name="appflow-Type-DestinationFlowConfig-apiVersion"></a>
The API version that the destination connector uses.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** connectorProfileName **   <a name="appflow-Type-DestinationFlowConfig-connectorProfileName"></a>
 The name of the connector profile. This name must be unique for each connector profile in the AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

## See Also
<a name="API_DestinationFlowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DestinationFlowConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DestinationFlowConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DestinationFlowConfig)
