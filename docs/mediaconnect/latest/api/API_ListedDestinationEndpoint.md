---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedDestinationEndpoint.html
---

# ListedDestinationEndpoint
<a name="API_ListedDestinationEndpoint"></a>

A summary of a destination endpoint that the `ListDestinationEndpoints` operation returns.

## Contents
<a name="API_ListedDestinationEndpoint_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-ListedDestinationEndpoint-arn"></a>
The Amazon Resource Name (ARN) of the destination endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:destinationEndpoint:[a-z0-9]{12}`
Required: Yes

 ** connectionState **   <a name="mediaconnect-Type-ListedDestinationEndpoint-connectionState"></a>
The connection state of the destination endpoint. Valid values include the following:
+  `CONNECTED` – The destination endpoint is connected to a source endpoint.
+  `DISCONNECTED` – The destination endpoint isn't connected to a source endpoint.
+  `CONNECTING` – The destination endpoint is connecting to a source endpoint.
+  `DISCONNECTING` – The destination endpoint is disconnecting from a source endpoint.
Type: String
Valid Values: `CONNECTED | DISCONNECTED | CONNECTING | DISCONNECTING`
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-ListedDestinationEndpoint-createdAt"></a>
The date and time when the destination endpoint was created.
Type: Timestamp
Required: Yes

 ** destinationType **   <a name="mediaconnect-Type-ListedDestinationEndpoint-destinationType"></a>
The type of the destination endpoint. Valid values include the following:
+  `STANDARD` – A destination endpoint that represents an external destination over a standard protocol, such as RTP, RIST, or SRT.
+  `ROUTER_INPUT` – A destination endpoint that represents a router input.
Type: String
Valid Values: `STANDARD | ROUTER_INPUT`
Required: Yes

 ** id **   <a name="mediaconnect-Type-ListedDestinationEndpoint-id"></a>
The unique identifier of the destination endpoint.
Type: String
Required: Yes

 ** lifecycleManagement **   <a name="mediaconnect-Type-ListedDestinationEndpoint-lifecycleManagement"></a>
The entity that manages the lifecycle of the destination endpoint.
Type: String
Valid Values: `MANAGED | UNMANAGED`
Required: Yes

 ** messageCount **   <a name="mediaconnect-Type-ListedDestinationEndpoint-messageCount"></a>
The number of status messages for the destination endpoint.
Type: Integer
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedDestinationEndpoint-name"></a>
The name of the destination endpoint.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-ListedDestinationEndpoint-regionName"></a>
The name of the AWS Region in which the destination endpoint is located.
Type: String
Required: Yes

 ** registrationState **   <a name="mediaconnect-Type-ListedDestinationEndpoint-registrationState"></a>
The registration state of the destination endpoint. Valid values include the following:
+  `REGISTERED` – The destination endpoint is registered and ready to use.
+  `REGISTERING` – MediaConnect is registering the destination endpoint.
+  `DEREGISTERING` – MediaConnect is deregistering the destination endpoint.
+  `REGISTRATION_FAILED` – MediaConnect couldn't register the destination endpoint.
Type: String
Valid Values: `REGISTERED | REGISTERING | DEREGISTERING | REGISTRATION_FAILED`
Required: Yes

 ** resourceShareOwnership **   <a name="mediaconnect-Type-ListedDestinationEndpoint-resourceShareOwnership"></a>
Indicates whether this account owns the destination endpoint or consumes it from another account through AWS RAM.
Type: String
Valid Values: `OWNED | CONSUMED`
Required: Yes

 ** resourceShareState **   <a name="mediaconnect-Type-ListedDestinationEndpoint-resourceShareState"></a>
The sharing state of the destination endpoint.
Type: String
Valid Values: `SHARED | UNSHARED`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-ListedDestinationEndpoint-updatedAt"></a>
The date and time when the destination endpoint was last updated.
Type: Timestamp
Required: Yes

 ** associatedResourceArn **   <a name="mediaconnect-Type-ListedDestinationEndpoint-associatedResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that is associated with the destination endpoint.
Type: String
Required: No

 ** availabilityZone **   <a name="mediaconnect-Type-ListedDestinationEndpoint-availabilityZone"></a>
The Availability Zone in which the destination endpoint is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="mediaconnect-Type-ListedDestinationEndpoint-availabilityZoneId"></a>
The ID of the Availability Zone in which the destination endpoint is located.
Type: String
Required: No

 ** connectedSource **   <a name="mediaconnect-Type-ListedDestinationEndpoint-connectedSource"></a>
The Amazon Resource Name (ARN) of the source endpoint that is connected to the destination endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: No

 ** decryptionType **   <a name="mediaconnect-Type-ListedDestinationEndpoint-decryptionType"></a>
The type of decryption used for the destination endpoint connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_ListedDestinationEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedDestinationEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedDestinationEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedDestinationEndpoint)
