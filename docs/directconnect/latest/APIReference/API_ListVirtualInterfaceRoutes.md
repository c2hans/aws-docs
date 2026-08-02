---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceRoutes.html
---

# ListVirtualInterfaceRoutes
<a name="API_ListVirtualInterfaceRoutes"></a>

Lists the routes for the specified virtual interface.

Use the `routeDirection` filter to control which routes are returned:
+  `accepted`: routes received from the customer network over the virtual interface.
+  `advertised`: routes advertised to the customer network over the virtual interface.

## Request Syntax
<a name="API_ListVirtualInterfaceRoutes_RequestSyntax"></a>

```
{
   "filters": {
      "addressFamily": "{{string}}",
      "asPath": [ {{number}} ],
      "cidrs": [ "{{string}}" ],
      "communities": [ "{{string}}" ],
      "routeDirection": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "virtualInterfaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListVirtualInterfaceRoutes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_ListVirtualInterfaceRoutes_RequestSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-request-filters"></a>
The filters to apply to the routes returned.
Type: [RouteFilters](API_RouteFilters.md) object
Required: No

 ** [maxResults](#API_ListVirtualInterfaceRoutes_RequestSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-request-maxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
If `MaxResults` is given a value larger than 100, only 100 results are returned.
Type: Integer
Required: No

 ** [nextToken](#API_ListVirtualInterfaceRoutes_RequestSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-request-nextToken"></a>
The token for the next page of results.
Type: String
Required: No

 ** [virtualInterfaceId](#API_ListVirtualInterfaceRoutes_RequestSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-request-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String
Required: No

## Response Syntax
<a name="API_ListVirtualInterfaceRoutes_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "routes": [
      {
         "addressFamily": "string",
         "asPath": [
            {
               "path": [ number ],
               "pathType": "string"
            }
         ],
         "awsLogicalDeviceId": "string",
         "cidr": "string",
         "communities": [ "string" ],
         "routeDirection": "string",
         "routeInstalledAt": number
      }
   ],
   "virtualInterfaceId": "string"
}
```

## Response Elements
<a name="API_ListVirtualInterfaceRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListVirtualInterfaceRoutes_ResponseSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-response-nextToken"></a>
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 ** [routes](#API_ListVirtualInterfaceRoutes_ResponseSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-response-routes"></a>
The routes for the virtual interface.
Type: Array of [Route](API_Route.md) objects

 ** [virtualInterfaceId](#API_ListVirtualInterfaceRoutes_ResponseSyntax) **   <a name="DX-ListVirtualInterfaceRoutes-response-virtualInterfaceId"></a>
The ID of the virtual interface.
Type: String

## Errors
<a name="API_ListVirtualInterfaceRoutes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

## See Also
<a name="API_ListVirtualInterfaceRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/ListVirtualInterfaceRoutes)
