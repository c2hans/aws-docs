---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

An object that represents a connector for an Amazon EVS environment. A connector establishes a connection to the given appliance type using the credentials stored in AWS Secrets Manager.

## Contents
<a name="API_Connector_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** applianceFqdn **   <a name="evs-Type-Connector-applianceFqdn"></a>
The fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: No

 ** checks **   <a name="evs-Type-Connector-checks"></a>
A list of checks that are run on the connector.
Type: Array of [ConnectorCheck](API_ConnectorCheck.md) objects
Required: No

 ** connectorId **   <a name="evs-Type-Connector-connectorId"></a>
The unique ID of the connector.
Type: String
Pattern: `(cnctr-[a-zA-Z0-9]{10})`
Required: No

 ** createdAt **   <a name="evs-Type-Connector-createdAt"></a>
The date and time that the connector was created.
Type: Timestamp
Required: No

 ** environmentId **   <a name="evs-Type-Connector-environmentId"></a>
The unique ID of the environment that the connector belongs to.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: No

 ** modifiedAt **   <a name="evs-Type-Connector-modifiedAt"></a>
The date and time that the connector was modified.
Type: Timestamp
Required: No

 ** secretArn **   <a name="evs-Type-Connector-secretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that stores the credentials for the VCF appliance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(arn:aws:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@!-]+|[a-zA-Z0-9/_+=.@!-]+)`
Required: No

 ** state **   <a name="evs-Type-Connector-state"></a>
The state of the connector.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING | DELETED`
Required: No

 ** stateDetails **   <a name="evs-Type-Connector-stateDetails"></a>
A detailed description of the connector state.
Type: String
Required: No

 ** status **   <a name="evs-Type-Connector-status"></a>
The status of the connector.
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

 ** type **   <a name="evs-Type-Connector-type"></a>
The type of the connector.
Type: String
Valid Values: `OPERATIONS_MANAGER | SDDC_MANAGER | VCENTER`
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Connector)
