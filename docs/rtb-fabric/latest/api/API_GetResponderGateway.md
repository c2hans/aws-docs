---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_GetResponderGateway.html
---

# GetResponderGateway
<a name="API_GetResponderGateway"></a>

Retrieves information about a responder gateway.

## Request Syntax
<a name="API_GetResponderGateway_RequestSyntax"></a>

```
GET /responder-gateway/{{gatewayId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResponderGateway_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayId](#API_GetResponderGateway_RequestSyntax) **   <a name="rtbfabric-GetResponderGateway-request-uri-gatewayId"></a>
The unique identifier of the gateway.
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

## Request Body
<a name="API_GetResponderGateway_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResponderGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "activeLinksCount": number,
   "clientRoutingPolicy": "string",
   "createdAt": number,
   "description": "string",
   "domainName": "string",
   "externalInboundEndpoint": "string",
   "gatewayId": "string",
   "gatewayType": "string",
   "linksRequestedCount": number,
   "listenerConfig": {
      "protocols": [ "string" ]
   },
   "managedEndpointConfiguration": { ... },
   "port": number,
   "protocol": "string",
   "securityGroupIds": [ "string" ],
   "status": "string",
   "subnetIds": [ "string" ],
   "tags": {
      "string" : "string"
   },
   "totalLinksCount": number,
   "trustStoreConfiguration": {
      "certificateAuthorityCertificates": [ "string" ]
   },
   "updatedAt": number,
   "vpcId": "string"
}
```

## Response Elements
<a name="API_GetResponderGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activeLinksCount](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-activeLinksCount"></a>
The count of active links for the responder gateway.
Type: Integer

 ** [clientRoutingPolicy](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-clientRoutingPolicy"></a>
The client routing policy of the gateway. This policy controls which Availability Zones RTB Fabric uses to reach the gateway for the requester gateways that send traffic to it. RTB Fabric omits this member if the gateway has never had a client routing policy. An omitted value means that the gateway uses `AVAILABILITY_ZONE_AFFINITY`. For more information, see [Configuring Availability Zone affinity](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/working-with-responder-gateways.html#configuring-availability-zone-affinity) in the * AWS RTB Fabric User Guide*.
Type: String
Valid Values: `AVAILABILITY_ZONE_AFFINITY | ANY_AVAILABILITY_ZONE`

 ** [createdAt](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-createdAt"></a>
The timestamp of when the responder gateway was created.
Type: Timestamp

 ** [description](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-description"></a>
The description of the responder gateway.
Type: String
Pattern: `[A-Za-z0-9 ]+`

 ** [domainName](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-domainName"></a>
The domain name of the responder gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`

 ** [externalInboundEndpoint](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-externalInboundEndpoint"></a>
The external inbound endpoint for the responder gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`

 ** [gatewayId](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [gatewayType](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-gatewayType"></a>
The type of gateway. Valid values are `EXTERNAL` or `INTERNAL`.
Type: String
Valid Values: `EXTERNAL | INTERNAL`

 ** [linksRequestedCount](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-linksRequestedCount"></a>
The count of requested links waiting for the responder gateway to accept or reject.
Type: Integer

 ** [listenerConfig](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-listenerConfig"></a>
The listener configuration for the responder gateway.
Type: [ListenerConfig](API_ListenerConfig.md) object

 ** [managedEndpointConfiguration](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-managedEndpointConfiguration"></a>
The configuration of the managed endpoint.
Type: [ManagedEndpointConfiguration](API_ManagedEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [port](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-port"></a>
The networking port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.

 ** [protocol](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-protocol"></a>
The networking protocol.
Type: String
Valid Values: `HTTP | HTTPS`

 ** [securityGroupIds](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-securityGroupIds"></a>
The unique identifiers of the security groups.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 11. Maximum length of 43.
Pattern: `sg-[0-9a-f]{8,40}`

 ** [status](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | ACTIVE | PENDING_DELETION | DELETED | ERROR | PENDING_UPDATE | ISOLATED | PENDING_ISOLATION | PENDING_RESTORATION`

 ** [subnetIds](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-subnetIds"></a>
The unique identifiers of the subnets.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-\w{8,17}`

 ** [tags](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-tags"></a>
A map of the key-value pairs for the tag or tags assigned to the specified resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.

 ** [totalLinksCount](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-totalLinksCount"></a>
The total count of links for the responder gateway.
Type: Integer

 ** [trustStoreConfiguration](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-trustStoreConfiguration"></a>
The configuration of the trust store.
Type: [TrustStoreConfiguration](API_TrustStoreConfiguration.md) object

 ** [updatedAt](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-updatedAt"></a>
The timestamp of when the responder gateway was updated.
Type: Timestamp

 ** [vpcId](#API_GetResponderGateway_ResponseSyntax) **   <a name="rtbfabric-GetResponderGateway-response-vpcId"></a>
The unique identifier of the Virtual Private Cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[a-f0-9]{8,17}`

## Errors
<a name="API_GetResponderGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request could not be completed because you do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request could not be completed because of an internal server error. Try your call again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request could not be completed because the resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetResponderGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/GetResponderGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/GetResponderGateway)
