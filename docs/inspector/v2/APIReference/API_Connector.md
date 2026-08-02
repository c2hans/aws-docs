---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

Describes a connector that links an external cloud provider to Amazon Inspector for vulnerability scanning.

## Contents
<a name="API_Connector_Contents"></a>

 ** connectorArn **   <a name="inspector2-Type-Connector-connectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `arn:aws(-[a-z]+)*:inspector2:[a-z0-9-]+:[0-9]{12}:connector/([a-f0-9-]+|aws-service-connector/.+/[a-f0-9-]+)`
Required: Yes

 ** createdAt **   <a name="inspector2-Type-Connector-createdAt"></a>
The date and time when the connector was created.
Type: Timestamp
Required: Yes

 ** provider **   <a name="inspector2-Type-Connector-provider"></a>
The cloud provider for the connector.
Type: String
Valid Values: `AZURE`
Required: Yes

 ** updatedAt **   <a name="inspector2-Type-Connector-updatedAt"></a>
The date and time when the connector was last updated.
Type: Timestamp
Required: Yes

 ** autoInstallVMScanner **   <a name="inspector2-Type-Connector-autoInstallVMScanner"></a>
Specifies whether the VM scanner is automatically installed on connected resources.
Type: Boolean
Required: No

 ** awsConfigConnectorArn **   <a name="inspector2-Type-Connector-awsConfigConnectorArn"></a>
The ARN of the AWS Config connector associated with this connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: No

 ** azureRegions **   <a name="inspector2-Type-Connector-azureRegions"></a>
The Azure regions configured for the connector.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** description **   <a name="inspector2-Type-Connector-description"></a>
A description of the connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `[^\p{C}]*`
Required: No

 ** enablementStatus **   <a name="inspector2-Type-Connector-enablementStatus"></a>
The enablement status of the connector, which indicates whether the connector is active and scanning resources.
Type: String
Valid Values: `ENABLED | PENDING_ENABLEMENT | FAILED_TO_ENABLE | PENDING_UPDATE | FAILED_TO_UPDATE | PENDING_DELETION | DELETED | FAILED_TO_DELETE`
Required: No

 ** enablementStatusReason **   <a name="inspector2-Type-Connector-enablementStatusReason"></a>
Additional information about the current enablement status of the connector.
Type: String
Required: No

 ** health **   <a name="inspector2-Type-Connector-health"></a>
The health of the connector, which indicates whether Amazon Inspector can reach and scan the connected resources.
Type: [ConnectorHealth](API_ConnectorHealth.md) object
Required: No

 ** name **   <a name="inspector2-Type-Connector-name"></a>
The name of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\p{L}\p{N}_-]+`
Required: No

 ** scopeConfiguration **   <a name="inspector2-Type-Connector-scopeConfiguration"></a>
The Azure scope configuration for the connector.
Type: [AzureScopeConfiguration](API_AzureScopeConfiguration.md) object
Required: No

 ** tags **   <a name="inspector2-Type-Connector-tags"></a>
The tags associated with the connector.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Connector)
