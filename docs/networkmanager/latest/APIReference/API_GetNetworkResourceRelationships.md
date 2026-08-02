---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_GetNetworkResourceRelationships.html
---

# GetNetworkResourceRelationships
<a name="API_GetNetworkResourceRelationships"></a>

Gets the network resource relationships for the specified global network.

## Request Syntax
<a name="API_GetNetworkResourceRelationships_RequestSyntax"></a>

```
GET /global-networks/{{globalNetworkId}}/network-resource-relationships?accountId={{AccountId}}&awsRegion={{AwsRegion}}&coreNetworkId={{CoreNetworkId}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&registeredGatewayArn={{RegisteredGatewayArn}}&resourceArn={{ResourceArn}}&resourceType={{ResourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetNetworkResourceRelationships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountId](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-AccountId"></a>
The AWS account ID.
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`

 ** [AwsRegion](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-AwsRegion"></a>
The AWS Region.
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`

 ** [CoreNetworkId](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-CoreNetworkId"></a>
The ID of a core network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`

 ** [globalNetworkId](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-GlobalNetworkId"></a>
The ID of the global network.
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: Yes

 ** [MaxResults](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 500.

 ** [NextToken](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [RegisteredGatewayArn](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-RegisteredGatewayArn"></a>
The ARN of the registered gateway.
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`

 ** [ResourceArn](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-ResourceArn"></a>
The ARN of the gateway.
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`

 ** [ResourceType](#API_GetNetworkResourceRelationships_RequestSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-request-uri-ResourceType"></a>
The resource type.
The following are the supported resource types for Direct Connect:
+  `dxcon`
+  `dx-gateway`
+  `dx-vif`
The following are the supported resource types for Network Manager:
+  `attachment`
+  `connect-peer`
+  `connection`
+  `core-network`
+  `device`
+  `link`
+  `peering`
+  `site`
The following are the supported resource types for Amazon VPC:
+  `customer-gateway`
+  `transit-gateway`
+  `transit-gateway-attachment`
+  `transit-gateway-connect-peer`
+  `transit-gateway-route-table`
+  `vpn-connection`
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`

## Request Body
<a name="API_GetNetworkResourceRelationships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetNetworkResourceRelationships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Relationships": [
      {
         "From": "string",
         "To": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetNetworkResourceRelationships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetNetworkResourceRelationships_ResponseSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\s\S]*`

 ** [Relationships](#API_GetNetworkResourceRelationships_ResponseSyntax) **   <a name="networkmanager-GetNetworkResourceRelationships-response-Relationships"></a>
The resource relationships.
Type: Array of [Relationship](API_Relationship.md) objects

## Errors
<a name="API_GetNetworkResourceRelationships_Errors"></a>

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
<a name="API_GetNetworkResourceRelationships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmanager-2019-07-05/GetNetworkResourceRelationships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/GetNetworkResourceRelationships)
