---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CreateOdbPeeringConnection.html
---

# CreateOdbPeeringConnection
<a name="API_CreateOdbPeeringConnection"></a>

Creates a peering connection between an ODB network and a VPC.

A peering connection enables private connectivity between the networks for application-tier communication.

## Request Syntax
<a name="API_CreateOdbPeeringConnection_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "displayName": "{{string}}",
   "odbNetworkId": "{{string}}",
   "peerNetworkCidrsToBeAdded": [ "{{string}}" ],
   "peerNetworkId": "{{string}}",
   "peerNetworkRouteTableIds": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateOdbPeeringConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-clientToken"></a>
The client token for the ODB peering connection request.
Constraints:
+ Must be unique for each request.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 64.
Pattern: `[a-zA-Z0-9_\/.=-]+`
Required: No

 ** [displayName](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-displayName"></a>
The display name for the ODB peering connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [odbNetworkId](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-odbNetworkId"></a>
The unique identifier of the ODB network that initiates the peering connection.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [peerNetworkCidrsToBeAdded](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-peerNetworkCidrsToBeAdded"></a>
A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)\/(?:[1-2][0-9]|3[0-2]|[1-9])`
Required: No

 ** [peerNetworkId](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-peerNetworkId"></a>
The unique identifier of the peer network. This can be either a VPC ID or another ODB network ID.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [peerNetworkRouteTableIds](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-peerNetworkRouteTableIds"></a>
The unique identifier of the VPC route table for which a route to the ODB network is automatically created during peering connection establishment.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `rtb-[a-z0-9]{8,17}`
Required: No

 ** [tags](#API_CreateOdbPeeringConnection_RequestSyntax) **   <a name="odb-CreateOdbPeeringConnection-request-tags"></a>
The tags to assign to the ODB peering connection.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateOdbPeeringConnection_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "odbPeeringConnectionId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_CreateOdbPeeringConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_CreateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-CreateOdbPeeringConnection-response-displayName"></a>
The display name of the ODB peering connection.
Type: String

 ** [odbPeeringConnectionId](#API_CreateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-CreateOdbPeeringConnection-response-odbPeeringConnectionId"></a>
The unique identifier of the ODB peering connection.
Type: String

 ** [status](#API_CreateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-CreateOdbPeeringConnection-response-status"></a>
The status of the ODB peering connection.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_CreateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-CreateOdbPeeringConnection-response-statusReason"></a>
The reason for the current status of the ODB peering connection.
Type: String

## Errors
<a name="API_CreateOdbPeeringConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateOdbPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/CreateOdbPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CreateOdbPeeringConnection)
