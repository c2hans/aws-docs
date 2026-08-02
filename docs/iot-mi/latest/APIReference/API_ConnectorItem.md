---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ConnectorItem.html
---

# ConnectorItem
<a name="API_ConnectorItem"></a>

Structure describing a connector.

## Contents
<a name="API_ConnectorItem_Contents"></a>

 ** EndpointConfig **   <a name="managedintegrations-Type-ConnectorItem-EndpointConfig"></a>
The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.
Type: [EndpointConfig](API_EndpointConfig.md) object
Required: Yes

 ** Name **   <a name="managedintegrations-Type-ConnectorItem-Name"></a>
The display name of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9-_ ]+`
Required: Yes

 ** Description **   <a name="managedintegrations-Type-ConnectorItem-Description"></a>
A description of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[0-9A-Za-z_\- ]+`
Required: No

 ** EndpointType **   <a name="managedintegrations-Type-ConnectorItem-EndpointType"></a>
The type of endpoint used for the C2C connector.
Type: String
Valid Values: `LAMBDA`
Required: No

 ** Id **   <a name="managedintegrations-Type-ConnectorItem-Id"></a>
The identifier of the C2C connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Type **   <a name="managedintegrations-Type-ConnectorItem-Type"></a>
The type of cloud connector created.
Type: String
Valid Values: `LISTED | UNLISTED`
Required: No

## See Also
<a name="API_ConnectorItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ConnectorItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ConnectorItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ConnectorItem)
