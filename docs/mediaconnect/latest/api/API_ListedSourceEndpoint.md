---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedSourceEndpoint.html
---

# ListedSourceEndpoint
<a name="API_ListedSourceEndpoint"></a>

A summary of a source endpoint that the `ListSourceEndpoints` operation returns.

## Contents
<a name="API_ListedSourceEndpoint_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-ListedSourceEndpoint-arn"></a>
The Amazon Resource Name (ARN) of the source endpoint.
Type: String
Length Constraints: Minimum length of 64. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:sourceEndpoint:[a-z0-9]{12}`
Required: Yes

 ** connectedDestinationCount **   <a name="mediaconnect-Type-ListedSourceEndpoint-connectedDestinationCount"></a>
The number of destination endpoints that are connected to the source endpoint.
Type: Integer
Required: Yes

 ** connectionState **   <a name="mediaconnect-Type-ListedSourceEndpoint-connectionState"></a>
The connection state of the source endpoint. Valid values include the following:
+  `CONNECTED` – The source endpoint is connected to a destination endpoint.
+  `DISCONNECTED` – The source endpoint isn't connected to a destination endpoint.
+  `CONNECTING` – The source endpoint is connecting to a destination endpoint.
+  `DISCONNECTING` – The source endpoint is disconnecting from a destination endpoint.
Type: String
Valid Values: `CONNECTED | DISCONNECTED | CONNECTING | DISCONNECTING`
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-ListedSourceEndpoint-createdAt"></a>
The date and time when the source endpoint was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-ListedSourceEndpoint-id"></a>
The unique identifier of the source endpoint.
Type: String
Required: Yes

 ** lifecycleManagement **   <a name="mediaconnect-Type-ListedSourceEndpoint-lifecycleManagement"></a>
The entity that manages the lifecycle of the source endpoint.
Type: String
Valid Values: `MANAGED | UNMANAGED`
Required: Yes

 ** messageCount **   <a name="mediaconnect-Type-ListedSourceEndpoint-messageCount"></a>
The number of status messages for the source endpoint.
Type: Integer
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedSourceEndpoint-name"></a>
The name of the source endpoint.
Type: String
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-ListedSourceEndpoint-regionName"></a>
The name of the AWS Region in which the source endpoint is located.
Type: String
Required: Yes

 ** registrationState **   <a name="mediaconnect-Type-ListedSourceEndpoint-registrationState"></a>
The registration state of the source endpoint. Valid values include the following:
+  `REGISTERED` – The source endpoint is registered and ready to use.
+  `REGISTERING` – MediaConnect is registering the source endpoint.
+  `DEREGISTERING` – MediaConnect is deregistering the source endpoint.
+  `REGISTRATION_FAILED` – MediaConnect couldn't register the source endpoint.
Type: String
Valid Values: `REGISTERED | REGISTERING | DEREGISTERING | REGISTRATION_FAILED`
Required: Yes

 ** resourceShareOwnership **   <a name="mediaconnect-Type-ListedSourceEndpoint-resourceShareOwnership"></a>
Indicates whether this account owns the source endpoint or consumes it from another account through AWS RAM.
Type: String
Valid Values: `OWNED | CONSUMED`
Required: Yes

 ** resourceShareState **   <a name="mediaconnect-Type-ListedSourceEndpoint-resourceShareState"></a>
The sharing state of the source endpoint.
Type: String
Valid Values: `SHARED | UNSHARED`
Required: Yes

 ** sourceType **   <a name="mediaconnect-Type-ListedSourceEndpoint-sourceType"></a>
The type of the source endpoint. Valid values include the following:
+  `STANDARD` – A source endpoint that represents an external source over a standard protocol, such as RTP, RIST, or SRT.
+  `ROUTER_OUTPUT` – A source endpoint that represents a router output.
Type: String
Valid Values: `STANDARD | ROUTER_OUTPUT`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-ListedSourceEndpoint-updatedAt"></a>
The date and time when the source endpoint was last updated.
Type: Timestamp
Required: Yes

 ** associatedResourceArn **   <a name="mediaconnect-Type-ListedSourceEndpoint-associatedResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that is associated with the source endpoint.
Type: String
Required: No

 ** availabilityZone **   <a name="mediaconnect-Type-ListedSourceEndpoint-availabilityZone"></a>
The Availability Zone in which the source endpoint is located.
Type: String
Required: No

 ** availabilityZoneId **   <a name="mediaconnect-Type-ListedSourceEndpoint-availabilityZoneId"></a>
The ID of the Availability Zone in which the source endpoint is located.
Type: String
Required: No

 ** encryptionType **   <a name="mediaconnect-Type-ListedSourceEndpoint-encryptionType"></a>
The type of encryption used for the source endpoint connection.
Type: String
Valid Values: `SECRETS_MANAGER | AUTOMATIC`
Required: No

## See Also
<a name="API_ListedSourceEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedSourceEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedSourceEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedSourceEndpoint)
