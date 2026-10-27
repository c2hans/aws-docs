---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_DestinationEndpoint.html
---

# DestinationEndpoint
<a name="API_DestinationEndpoint"></a>

The details of a destination endpoint in MediaConnect, including its configuration, state, and connection details.

## Contents
<a name="API_DestinationEndpoint_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-DestinationEndpoint-arn"></a>
The Amazon Resource Name (ARN) of the destination endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`
Required: Yes

 ** associatedResourceDetails **   <a name="mediaconnect-Type-DestinationEndpoint-associatedResourceDetails"></a>
The details of the resource that is associated with the destination endpoint.
Type: [DestinationEndpointAssociatedResourceDetails](API_DestinationEndpointAssociatedResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** configuration **   <a name="mediaconnect-Type-DestinationEndpoint-configuration"></a>
The configuration settings for the destination endpoint.
Type: [DestinationEndpointConfiguration](API_DestinationEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** connectionState **   <a name="mediaconnect-Type-DestinationEndpoint-connectionState"></a>
The connection state of the destination endpoint. Valid values include the following:
+  `CONNECTED` – The destination endpoint is connected to a source endpoint.
+  `DISCONNECTED` – The destination endpoint isn't connected to a source endpoint.
+  `CONNECTING` – The destination endpoint is connecting to a source endpoint.
+  `DISCONNECTING` – The destination endpoint is disconnecting from a source endpoint.
Type: String
Valid Values: `CONNECTED | DISCONNECTED | CONNECTING | DISCONNECTING`
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-DestinationEndpoint-createdAt"></a>
The date and time when the destination endpoint was created.
Type: Timestamp
Required: Yes

 ** description **   <a name="mediaconnect-Type-DestinationEndpoint-description"></a>
The description of the destination endpoint.
Type: String
Required: Yes

 ** destinationType **   <a name="mediaconnect-Type-DestinationEndpoint-destinationType"></a>
The type of the destination endpoint. Valid values include the following:
+  `STANDARD` – A destination endpoint that represents an external destination over a standard protocol, such as RTP, RIST, or SRT.
+  `ROUTER_INPUT` – A destination endpoint that represents a router input.
Type: String
Valid Values: `STANDARD | ROUTER_INPUT`
Required: Yes

 ** id **   <a name="mediaconnect-Type-DestinationEndpoint-id"></a>
The unique identifier of the destination endpoint.
Type: String
Required: Yes

 ** lifecycleManagement **   <a name="mediaconnect-Type-DestinationEndpoint-lifecycleManagement"></a>
The entity that manages the lifecycle of the destination endpoint.
Type: String
Valid Values: `MANAGED | UNMANAGED`
Required: Yes

 ** messages **   <a name="mediaconnect-Type-DestinationEndpoint-messages"></a>
The status messages for the destination endpoint.
Type: Array of [DestinationEndpointMessage](API_DestinationEndpointMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-DestinationEndpoint-name"></a>
The name of the destination endpoint.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-DestinationEndpoint-regionName"></a>
The name of the AWS Region in which the destination endpoint is located.
Type: String
Required: Yes

 ** registrationState **   <a name="mediaconnect-Type-DestinationEndpoint-registrationState"></a>
The registration state of the destination endpoint. Valid values include the following:
+  `REGISTERED` – The destination endpoint is registered and ready to use.
+  `REGISTERING` – MediaConnect is registering the destination endpoint.
+  `DEREGISTERING` – MediaConnect is deregistering the destination endpoint.
+  `REGISTRATION_FAILED` – MediaConnect couldn't register the destination endpoint.
Type: String
Valid Values: `REGISTERED | REGISTERING | DEREGISTERING | REGISTRATION_FAILED`
Required: Yes

 ** resourceShareDetails **   <a name="mediaconnect-Type-DestinationEndpoint-resourceShareDetails"></a>
The cross-account sharing details for an endpoint. Endpoints are shared through AWS Resource Access Manager (AWS RAM). This is a union type, so exactly one of its members is set: `owned` when this account owns the endpoint and shares it with other accounts, or `consumed` when this account consumes an endpoint that another account shares. To change how an endpoint is shared, use AWS RAM.
Type: [ResourceShareDetails](API_ResourceShareDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** resourceShareOwnership **   <a name="mediaconnect-Type-DestinationEndpoint-resourceShareOwnership"></a>
Indicates whether this account owns the destination endpoint or consumes it from another account through AWS RAM.
Type: String
Valid Values: `OWNED | CONSUMED`
Required: Yes

 ** tags **   <a name="mediaconnect-Type-DestinationEndpoint-tags"></a>
The tags associated with the destination endpoint. Each tag is a key-value pair.
Type: String to string map
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-DestinationEndpoint-updatedAt"></a>
The date and time when the destination endpoint was last updated.
Type: Timestamp
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-DestinationEndpoint-availabilityZone"></a>
The Availability Zone in which the destination endpoint is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="mediaconnect-Type-DestinationEndpoint-availabilityZoneId"></a>
The ID of the Availability Zone in which the destination endpoint is located.
Type: String
Required: No

 ** connectedSource **   <a name="mediaconnect-Type-DestinationEndpoint-connectedSource"></a>
The Amazon Resource Name (ARN) of the source endpoint that is connected to the destination endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: No

 ** connectionDetails **   <a name="mediaconnect-Type-DestinationEndpoint-connectionDetails"></a>
The connection details for the destination endpoint.
Type: [DestinationEndpointConnectionDetails](API_DestinationEndpointConnectionDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** decryptionConfiguration **   <a name="mediaconnect-Type-DestinationEndpoint-decryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** decryptionType **   <a name="mediaconnect-Type-DestinationEndpoint-decryptionType"></a>
The type of decryption used for the destination endpoint connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_DestinationEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/DestinationEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/DestinationEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/DestinationEndpoint)
