---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_CreateResponderGateway.html
---

# CreateResponderGateway
<a name="API_CreateResponderGateway"></a>

Creates a responder gateway.

**Important**
A domain name or managed endpoint is required.

## Request Syntax
<a name="API_CreateResponderGateway_RequestSyntax"></a>

```
POST /responder-gateway HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "domainName": "{{string}}",
   "gatewayType": "{{string}}",
   "listenerConfig": {
      "protocols": [ "{{string}}" ]
   },
   "managedEndpointConfiguration": { ... },
   "port": {{number}},
   "protocol": "{{string}}",
   "securityGroupIds": [ "{{string}}" ],
   "subnetIds": [ "{{string}}" ],
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "trustStoreConfiguration": {
      "certificateAuthorityCertificates": [ "{{string}}" ]
   },
   "vpcId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateResponderGateway_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateResponderGateway_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `clientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: Yes

 ** [description](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-description"></a>
An optional description for the responder gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`
Required: No

 ** [domainName](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-domainName"></a>
The domain name for the responder gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`
Required: No

 ** [gatewayType](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-gatewayType"></a>
The type of gateway. Valid values are `EXTERNAL` or `INTERNAL`.
Type: String
Valid Values: `EXTERNAL | INTERNAL`
Required: No

 ** [listenerConfig](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-listenerConfig"></a>
Listener configuration for the protocols (HTTP, HTTPS, or both) accepted by the gateway.
Type: [ListenerConfig](API_ListenerConfig.md) object
Required: No

 ** [managedEndpointConfiguration](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-managedEndpointConfiguration"></a>
The configuration for the managed endpoint.
Type: [ManagedEndpointConfiguration](API_ManagedEndpointConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [port](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-port"></a>
The networking port to use.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** [protocol](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-protocol"></a>
The networking protocol to use.
Type: String
Valid Values: `HTTP | HTTPS`
Required: Yes

 ** [securityGroupIds](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-securityGroupIds"></a>
The unique identifiers of the security groups.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 11. Maximum length of 43.
Pattern: `sg-[0-9a-f]{8,40}`
Required: Yes

 ** [subnetIds](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-subnetIds"></a>
Unique identifiers of the subnets. A service quota for your account sets the number of Availability Zones that your subnets can span. By default, this quota is one Availability Zone. To span more Availability Zones, request a quota increase.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-\w{8,17}`
Required: Yes

 ** [tags](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: No

 ** [trustStoreConfiguration](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-trustStoreConfiguration"></a>
The configuration of the trust store.
Type: [TrustStoreConfiguration](API_TrustStoreConfiguration.md) object
Required: No

 ** [vpcId](#API_CreateResponderGateway_RequestSyntax) **   <a name="rtbfabric-CreateResponderGateway-request-vpcId"></a>
The unique identifier of the Virtual Private Cloud (VPC).
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[a-f0-9]{8,17}`
Required: Yes

## Response Syntax
<a name="API_CreateResponderGateway_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "externalInboundEndpoint": "string",
   "gatewayId": "string",
   "listenerConfig": {
      "protocols": [ "string" ]
   },
   "status": "string"
}
```

## Response Elements
<a name="API_CreateResponderGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [externalInboundEndpoint](#API_CreateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-CreateResponderGateway-response-externalInboundEndpoint"></a>
The external inbound endpoint for the responder gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?)(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))+`

 ** [gatewayId](#API_CreateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-CreateResponderGateway-response-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`

 ** [listenerConfig](#API_CreateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-CreateResponderGateway-response-listenerConfig"></a>
The listener configuration for the responder gateway.
Type: [ListenerConfig](API_ListenerConfig.md) object

 ** [status](#API_CreateResponderGateway_ResponseSyntax) **   <a name="rtbfabric-CreateResponderGateway-response-status"></a>
The status of the request.
Type: String
Valid Values: `PENDING_CREATION | ACTIVE | PENDING_DELETION | DELETED | ERROR | PENDING_UPDATE | ISOLATED | PENDING_ISOLATION | PENDING_RESTORATION`

## Errors
<a name="API_CreateResponderGateway_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request could not be completed because you exceeded a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request could not be completed because it fails satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_CreateResponderGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rtbfabric-2023-05-15/CreateResponderGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/CreateResponderGateway)
