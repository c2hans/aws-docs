---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SourceEndpoint.html
---

# SourceEndpoint
<a name="API_SourceEndpoint"></a>

The details of a source endpoint in MediaConnect, including its configuration, state, and connection details.

## Contents
<a name="API_SourceEndpoint_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-SourceEndpoint-arn"></a>
The Amazon Resource Name (ARN) of the source endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: Yes

 ** associatedResourceDetails **   <a name="mediaconnect-Type-SourceEndpoint-associatedResourceDetails"></a>
The details of the resource that is associated with the source endpoint.
Type: [SourceEndpointAssociatedResourceDetails](API_SourceEndpointAssociatedResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** configuration **   <a name="mediaconnect-Type-SourceEndpoint-configuration"></a>
The configuration settings for the source endpoint.
Type: [SourceEndpointConfiguration](API_SourceEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** connectedDestinations **   <a name="mediaconnect-Type-SourceEndpoint-connectedDestinations"></a>
The Amazon Resource Names (ARNs) of the destination endpoints that are connected to the source endpoint.
Type: Array of strings
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`
Required: Yes

 ** connectionState **   <a name="mediaconnect-Type-SourceEndpoint-connectionState"></a>
The connection state of the source endpoint. Valid values include the following:
+  `CONNECTED` – The source endpoint is connected to a destination endpoint.
+  `DISCONNECTED` – The source endpoint isn't connected to a destination endpoint.
+  `CONNECTING` – The source endpoint is connecting to a destination endpoint.
+  `DISCONNECTING` – The source endpoint is disconnecting from a destination endpoint.
Type: String
Valid Values: `CONNECTED | DISCONNECTED | CONNECTING | DISCONNECTING`
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-SourceEndpoint-createdAt"></a>
The date and time when the source endpoint was created.
Type: Timestamp
Required: Yes

 ** description **   <a name="mediaconnect-Type-SourceEndpoint-description"></a>
The description of the source endpoint.
Type: String
Required: Yes

 ** id **   <a name="mediaconnect-Type-SourceEndpoint-id"></a>
The unique identifier of the source endpoint.
Type: String
Required: Yes

 ** lifecycleManagement **   <a name="mediaconnect-Type-SourceEndpoint-lifecycleManagement"></a>
The entity that manages the lifecycle of the source endpoint.
Type: String
Valid Values: `MANAGED | UNMANAGED`
Required: Yes

 ** messages **   <a name="mediaconnect-Type-SourceEndpoint-messages"></a>
The status messages for the source endpoint.
Type: Array of [SourceEndpointMessage](API_SourceEndpointMessage.md) objects
Required: Yes

 ** name **   <a name="mediaconnect-Type-SourceEndpoint-name"></a>
The name of the source endpoint.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-SourceEndpoint-regionName"></a>
The name of the AWS Region in which the source endpoint is located.
Type: String
Required: Yes

 ** registrationState **   <a name="mediaconnect-Type-SourceEndpoint-registrationState"></a>
The registration state of the source endpoint. Valid values include the following:
+  `REGISTERED` – The source endpoint is registered and ready to use.
+  `REGISTERING` – MediaConnect is registering the source endpoint.
+  `DEREGISTERING` – MediaConnect is deregistering the source endpoint.
+  `REGISTRATION_FAILED` – MediaConnect couldn't register the source endpoint.
Type: String
Valid Values: `REGISTERED | REGISTERING | DEREGISTERING | REGISTRATION_FAILED`
Required: Yes

 ** resourceShareDetails **   <a name="mediaconnect-Type-SourceEndpoint-resourceShareDetails"></a>
The cross-account sharing details for an endpoint. Endpoints are shared through AWS Resource Access Manager (AWS RAM). This is a union type, so exactly one of its members is set: `owned` when this account owns the endpoint and shares it with other accounts, or `consumed` when this account consumes an endpoint that another account shares. To change how an endpoint is shared, use AWS RAM.
Type: [ResourceShareDetails](API_ResourceShareDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** resourceShareOwnership **   <a name="mediaconnect-Type-SourceEndpoint-resourceShareOwnership"></a>
Indicates whether this account owns the source endpoint or consumes it from another account through AWS RAM.
Type: String
Valid Values: `OWNED | CONSUMED`
Required: Yes

 ** sourceType **   <a name="mediaconnect-Type-SourceEndpoint-sourceType"></a>
The type of the source endpoint. Valid values include the following:
+  `STANDARD` – A source endpoint that represents an external source over a standard protocol, such as RTP, RIST, or SRT.
+  `ROUTER_OUTPUT` – A source endpoint that represents a router output.
Type: String
Valid Values: `STANDARD | ROUTER_OUTPUT`
Required: Yes

 ** tags **   <a name="mediaconnect-Type-SourceEndpoint-tags"></a>
The tags associated with the source endpoint. Each tag is a key-value pair.
Type: String to string map
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-SourceEndpoint-updatedAt"></a>
The date and time when the source endpoint was last updated.
Type: Timestamp
Required: Yes

 ** availabilityZone **   <a name="mediaconnect-Type-SourceEndpoint-availabilityZone"></a>
The Availability Zone in which the source endpoint is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="mediaconnect-Type-SourceEndpoint-availabilityZoneId"></a>
The ID of the Availability Zone in which the source endpoint is located.
Type: String
Required: No

 ** connectionDetails **   <a name="mediaconnect-Type-SourceEndpoint-connectionDetails"></a>
The connection details for the source endpoint.
Type: [SourceEndpointConnectionDetails](API_SourceEndpointConnectionDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** encryptionConfiguration **   <a name="mediaconnect-Type-SourceEndpoint-encryptionConfiguration"></a>
The encryption settings for an endpoint connection. This is a union type, so exactly one of its members is set: `secretsManager` when you store the encryption key or passphrase in AWS Secrets Manager, or `automatic` when you let MediaConnect determine the encryption key when the endpoint connects.
Type: [EndpointEncryptionConfiguration](API_EndpointEncryptionConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** encryptionType **   <a name="mediaconnect-Type-SourceEndpoint-encryptionType"></a>
The type of encryption used for the source endpoint connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_SourceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SourceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SourceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SourceEndpoint)
