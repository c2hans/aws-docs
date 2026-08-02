---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SourceFlowConfig.html
---

# SourceFlowConfig
<a name="API_SourceFlowConfig"></a>

 Contains information about the configuration of the source connector used in the flow.

## Contents
<a name="API_SourceFlowConfig_Contents"></a>

 ** connectorType **   <a name="appflow-Type-SourceFlowConfig-connectorType"></a>
 The type of connector, such as Salesforce, Amplitude, and so on.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: Yes

 ** sourceConnectorProperties **   <a name="appflow-Type-SourceFlowConfig-sourceConnectorProperties"></a>
 Specifies the information that is required to query a particular source connector.
Type: [SourceConnectorProperties](API_SourceConnectorProperties.md) object
Required: Yes

 ** apiVersion **   <a name="appflow-Type-SourceFlowConfig-apiVersion"></a>
The API version of the connector when it's used as a source in the flow.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** connectorProfileName **   <a name="appflow-Type-SourceFlowConfig-connectorProfileName"></a>
 The name of the connector profile. This name must be unique for each connector profile in the AWS account.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[\w/!@#+=.-]+`
Required: No

 ** incrementalPullConfig **   <a name="appflow-Type-SourceFlowConfig-incrementalPullConfig"></a>
 Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.
Type: [IncrementalPullConfig](API_IncrementalPullConfig.md) object
Required: No

## See Also
<a name="API_SourceFlowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SourceFlowConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SourceFlowConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SourceFlowConfig)
