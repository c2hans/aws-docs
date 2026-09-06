---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_Connector.html
---

# Connector
<a name="API_Connector"></a>

The details of the connector, including the connector configuration and connector ARN.

## Contents
<a name="API_Connector_Contents"></a>

 ** arn **   <a name="config-Type-Connector-arn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** connectorConfiguration **   <a name="config-Type-Connector-connectorConfiguration"></a>
The provider-specific configuration for connecting to the third-party cloud service provider.
Type: [ConnectorConfiguration](API_ConnectorConfiguration.md) object
Required: Yes

 ** createdTime **   <a name="config-Type-Connector-createdTime"></a>
The date and time that the connector was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="config-Type-Connector-name"></a>
The name of the connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/Connector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/Connector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/Connector)
