---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorConfiguration.html
---

# ConnectorConfiguration
<a name="API_ConnectorConfiguration"></a>

 The configuration settings related to a given connector.

## Contents
<a name="API_ConnectorConfiguration_Contents"></a>

 ** authenticationConfig **   <a name="appflow-Type-ConnectorConfiguration-authenticationConfig"></a>
The authentication config required for the connector.
Type: [AuthenticationConfig](API_AuthenticationConfig.md) object
Required: No

 ** canUseAsDestination **   <a name="appflow-Type-ConnectorConfiguration-canUseAsDestination"></a>
 Specifies whether the connector can be used as a destination.
Type: Boolean
Required: No

 ** canUseAsSource **   <a name="appflow-Type-ConnectorConfiguration-canUseAsSource"></a>
 Specifies whether the connector can be used as a source.
Type: Boolean
Required: No

 ** connectorArn **   <a name="appflow-Type-ConnectorConfiguration-connectorArn"></a>
The Amazon Resource Name (ARN) for the registered connector.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:.*:.*:[0-9]+:.*`
Required: No

 ** connectorDescription **   <a name="appflow-Type-ConnectorConfiguration-connectorDescription"></a>
A description about the connector.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

 ** connectorLabel **   <a name="appflow-Type-ConnectorConfiguration-connectorLabel"></a>
The label used for registering the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `[a-zA-Z0-9][\w!@#.-]+`
Required: No

 ** connectorMetadata **   <a name="appflow-Type-ConnectorConfiguration-connectorMetadata"></a>
 Specifies connector-specific metadata such as `oAuthScopes`, `supportedRegions`, `privateLinkServiceUrl`, and so on.
Type: [ConnectorMetadata](API_ConnectorMetadata.md) object
Required: No

 ** connectorModes **   <a name="appflow-Type-ConnectorConfiguration-connectorModes"></a>
The connection modes that the connector supports.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** connectorName **   <a name="appflow-Type-ConnectorConfiguration-connectorName"></a>
The connector name.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** connectorOwner **   <a name="appflow-Type-ConnectorConfiguration-connectorOwner"></a>
The owner who developed the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** connectorProvisioningConfig **   <a name="appflow-Type-ConnectorConfiguration-connectorProvisioningConfig"></a>
The configuration required for registering the connector.
Type: [ConnectorProvisioningConfig](API_ConnectorProvisioningConfig.md) object
Required: No

 ** connectorProvisioningType **   <a name="appflow-Type-ConnectorConfiguration-connectorProvisioningType"></a>
The provisioning type used to register the connector.
Type: String
Valid Values: `LAMBDA`
Required: No

 ** connectorRuntimeSettings **   <a name="appflow-Type-ConnectorConfiguration-connectorRuntimeSettings"></a>
The required connector runtime settings.
Type: Array of [ConnectorRuntimeSetting](API_ConnectorRuntimeSetting.md) objects
Required: No

 ** connectorType **   <a name="appflow-Type-ConnectorConfiguration-connectorType"></a>
The connector type.
Type: String
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** connectorVersion **   <a name="appflow-Type-ConnectorConfiguration-connectorVersion"></a>
The connector version.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** isPrivateLinkEnabled **   <a name="appflow-Type-ConnectorConfiguration-isPrivateLinkEnabled"></a>
 Specifies if PrivateLink is enabled for that connector.
Type: Boolean
Required: No

 ** isPrivateLinkEndpointUrlRequired **   <a name="appflow-Type-ConnectorConfiguration-isPrivateLinkEndpointUrlRequired"></a>
 Specifies if a PrivateLink endpoint URL is required.
Type: Boolean
Required: No

 ** logoURL **   <a name="appflow-Type-ConnectorConfiguration-logoURL"></a>
Logo URL of the connector.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?|ftp|file)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: No

 ** registeredAt **   <a name="appflow-Type-ConnectorConfiguration-registeredAt"></a>
The date on which the connector was registered.
Type: Timestamp
Required: No

 ** registeredBy **   <a name="appflow-Type-ConnectorConfiguration-registeredBy"></a>
Information about who registered the connector.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** supportedApiVersions **   <a name="appflow-Type-ConnectorConfiguration-supportedApiVersions"></a>
A list of API versions that are supported by the connector.
Type: Array of strings
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** supportedDataTransferApis **   <a name="appflow-Type-ConnectorConfiguration-supportedDataTransferApis"></a>
The APIs of the connector application that Amazon AppFlow can use to transfer your data.
Type: Array of [DataTransferApi](API_DataTransferApi.md) objects
Required: No

 ** supportedDataTransferTypes **   <a name="appflow-Type-ConnectorConfiguration-supportedDataTransferTypes"></a>
The data transfer types that the connector supports.
RECORD
Structured records.
FILE
Files or binary data.
Type: Array of strings
Valid Values: `RECORD | FILE`
Required: No

 ** supportedDestinationConnectors **   <a name="appflow-Type-ConnectorConfiguration-supportedDestinationConnectors"></a>
 Lists the connectors that are available for use as destinations.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Valid Values: `Salesforce | Singular | Slack | Redshift | S3 | Marketo | Googleanalytics | Zendesk | Servicenow | Datadog | Trendmicro | Snowflake | Dynatrace | Infornexus | Amplitude | Veeva | EventBridge | LookoutMetrics | Upsolver | Honeycode | CustomerProfiles | SAPOData | CustomConnector | Pardot`
Required: No

 ** supportedOperators **   <a name="appflow-Type-ConnectorConfiguration-supportedOperators"></a>
A list of operators supported by the connector.
Type: Array of strings
Valid Values: `PROJECTION | LESS_THAN | GREATER_THAN | CONTAINS | BETWEEN | LESS_THAN_OR_EQUAL_TO | GREATER_THAN_OR_EQUAL_TO | EQUAL_TO | NOT_EQUAL_TO | ADDITION | MULTIPLICATION | DIVISION | SUBTRACTION | MASK_ALL | MASK_FIRST_N | MASK_LAST_N | VALIDATE_NON_NULL | VALIDATE_NON_ZERO | VALIDATE_NON_NEGATIVE | VALIDATE_NUMERIC | NO_OP`
Required: No

 ** supportedSchedulingFrequencies **   <a name="appflow-Type-ConnectorConfiguration-supportedSchedulingFrequencies"></a>
 Specifies the supported flow frequency for that connector.
Type: Array of strings
Valid Values: `BYMINUTE | HOURLY | DAILY | WEEKLY | MONTHLY | ONCE`
Required: No

 ** supportedTriggerTypes **   <a name="appflow-Type-ConnectorConfiguration-supportedTriggerTypes"></a>
 Specifies the supported trigger types for the flow.
Type: Array of strings
Valid Values: `Scheduled | Event | OnDemand`
Required: No

 ** supportedWriteOperations **   <a name="appflow-Type-ConnectorConfiguration-supportedWriteOperations"></a>
A list of write operations supported by the connector.
Type: Array of strings
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_ConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
