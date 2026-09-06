---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkRoutes.html
---

# GetNetworkRoutes
<a name="API_GetNetworkRoutes"></a>

Gets the network routes of the specified global network.

## Request Syntax
<a name="API_GetNetworkRoutes_RequestSyntax"></a>

```
POST /global-networks/{{globalNetworkId}}/network-routes HTTP/1.1
Content-type: application/json

{
   "DestinationFilters": {
      "{{string}}" : [ "{{string}}" ]
   },
   "ExactCidrMatches": [ "{{string}}" ],
   "LongestPrefixMatches": [ "{{string}}" ],
   "PrefixListIds": [ "{{string}}" ],
   "RouteTableIdentifier": {
      "CoreNetworkNetworkFunctionGroup": {
         "CoreNetworkId": "{{string}}",
         "EdgeLocation": "{{string}}",
         "NetworkFunctionGroupName": "{{string}}"
      },
      "CoreNetworkSegmentEdge": {
         "CoreNetworkId": "{{string}}",
         "EdgeLocation": "{{string}}",
         "SegmentName": "{{string}}"
      },
      "TransitGatewayRouteTableArn": "{{string}}"
   },
   "States": [ "{{string}}" ],
   "SubnetOfMatches": [ "{{string}}" ],
   "SupernetOfMatches": [ "{{string}}" ],
   "Types": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_GetNetworkRoutes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [globalNetworkId](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

## Request Body
<a name="API_GetNetworkRoutes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DestinationFilters](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-DestinationFilters"></a>
Filter by route table destination. Possible Values: TRANSIT\_GATEWAY\_ATTACHMENT\_ID, RESOURCE\_ID, or RESOURCE\_TYPE.
Type: String to array of strings map
Key Length Constraints: Maximum length of 128.
Key Pattern: `^[0-9a-zA-Z\.-]*$`
Length Constraints: Maximum length of 255.
Pattern: `^[0-9a-zA-Z\*\.\\/\?-]*$`
Required: No

 ** [ExactCidrMatches](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-ExactCidrMatches"></a>
An exact CIDR block.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [LongestPrefixMatches](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-LongestPrefixMatches"></a>
The most specific route that matches the traffic (longest prefix match).
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [PrefixListIds](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-PrefixListIds"></a>
The IDs of the prefix lists.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [RouteTableIdentifier](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-RouteTableIdentifier"></a>
The ID of the route table.
Type: [RouteTableIdentifier](API_RouteTableIdentifier.md) object
Required: Yes

 ** [States](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-States"></a>
The route states.
Type: Array of strings
Valid Values: `ACTIVE | BLACKHOLE`
Required: No

 ** [SubnetOfMatches](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-SubnetOfMatches"></a>
The routes with a subnet that match the specified CIDR filter.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [SupernetOfMatches](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-SupernetOfMatches"></a>
The routes with a CIDR that encompasses the CIDR filter. Example: If you specify 10.0.1.0/30, then the result returns 10.0.1.0/29.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** [Types](#API_GetNetworkRoutes_RequestSyntax) **   <a name="networkmanager-GetNetworkRoutes-request-Types"></a>
The route types.
Type: Array of strings
Valid Values: `PROPAGATED | STATIC`
Required: No

## Response Syntax
<a name="API_GetNetworkRoutes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CoreNetworkSegmentEdge": {
      "CoreNetworkId": "string",
      "EdgeLocation": "string",
      "SegmentName": "string"
   },
   "NetworkRoutes": [
      {
         "DestinationCidrBlock": "string",
         "Destinations": [
            {
               "CoreNetworkAttachmentId": "string",
               "EdgeLocation": "string",
               "NetworkFunctionGroupName": "string",
               "ResourceId": "string",
               "ResourceType": "string",
               "SegmentName": "string",
               "TransitGatewayAttachmentId": "string"
            }
         ],
         "PrefixListId": "string",
         "State": "string",
         "Type": "string"
      }
   ],
   "RouteTableArn": "string",
   "RouteTableTimestamp": number,
   "RouteTableType": "string"
}
```

## Response Elements
<a name="API_GetNetworkRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CoreNetworkSegmentEdge](#API_GetNetworkRoutes_ResponseSyntax) **   <a name="networkmanager-GetNetworkRoutes-response-CoreNetworkSegmentEdge"></a>
Describes a core network segment edge.
Type: [CoreNetworkSegmentEdgeIdentifier](API_CoreNetworkSegmentEdgeIdentifier.md) object

 ** [NetworkRoutes](#API_GetNetworkRoutes_ResponseSyntax) **   <a name="networkmanager-GetNetworkRoutes-response-NetworkRoutes"></a>
The network routes.
Type: Array of [NetworkRoute](API_NetworkRoute.md) objects

 ** [RouteTableArn](#API_GetNetworkRoutes_ResponseSyntax) **   <a name="networkmanager-GetNetworkRoutes-response-RouteTableArn"></a>
The ARN of the route table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`

 ** [RouteTableTimestamp](#API_GetNetworkRoutes_ResponseSyntax) **   <a name="networkmanager-GetNetworkRoutes-response-RouteTableTimestamp"></a>
The route table creation time.
Type: Timestamp

 ** [RouteTableType](#API_GetNetworkRoutes_ResponseSyntax) **   <a name="networkmanager-GetNetworkRoutes-response-RouteTableType"></a>
The route table type.
Type: String
Valid Values: `TRANSIT_GATEWAY_ROUTE_TABLE | CORE_NETWORK_SEGMENT | NETWORK_FUNCTION_GROUP`

## Errors
<a name="API_GetNetworkRoutes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal error.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found.
 ** Context **
The specified resource could not be found.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The resource type.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** RetryAfterSeconds **
Indicates when to retry the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints.
 ** Fields **
The fields that caused the error, if applicable.
 ** Reason **
The reason for the error.
HTTP Status Code: 400

## See Also
<a name="API_GetNetworkRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkRoutes)
