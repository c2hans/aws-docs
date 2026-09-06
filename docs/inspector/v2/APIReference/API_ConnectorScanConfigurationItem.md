---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorScanConfigurationItem.html
---

# ConnectorScanConfigurationItem
<a name="API_ConnectorScanConfigurationItem"></a>

Represents a scan configuration and the connectors it applies to. Returned in the results of a `ListConnectorScanConfigurations` request.

## Contents
<a name="API_ConnectorScanConfigurationItem_Contents"></a>

 ** awsConfigConnectorArn **   <a name="inspector2-Type-ConnectorScanConfigurationItem-awsConfigConnectorArn"></a>
The ARN of the AWS Config connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: Yes

 ** connectorArns **   <a name="inspector2-Type-ConnectorScanConfigurationItem-connectorArns"></a>
The list of connector ARNs associated with this AWS Config connector.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`
Required: Yes

 ** scanConfiguration **   <a name="inspector2-Type-ConnectorScanConfigurationItem-scanConfiguration"></a>
The scan configuration settings.
Type: [ConnectorScanConfiguration](API_ConnectorScanConfiguration.md) object
Required: Yes

## See Also
<a name="API_ConnectorScanConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorScanConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorScanConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorScanConfigurationItem)
