---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListFulfillmentOptions.html
---

# ListFulfillmentOptions
<a name="API_marketplace-discovery_ListFulfillmentOptions"></a>

Returns the fulfillment options available for a product, including deployment details such as version information, operating systems, usage instructions, and release notes.

## Request Syntax
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax"></a>

```
POST /2026-02-05/listFulfillmentOptions HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "productId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [productId](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-productId"></a>
The unique identifier of the product for which to list fulfillment options.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [maxResults](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to get more results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fulfillmentOptions": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-discovery_ListFulfillmentOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fulfillmentOptions](#API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-response-fulfillmentOptions"></a>
The fulfillment options available for the product. Each option describes how the buyer can deploy or access the product.
Type: Array of [FulfillmentOption](API_marketplace-discovery_FulfillmentOption.md) objects

 ** [nextToken](#API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-response-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_ListFulfillmentOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason that the input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-discovery_ListFulfillmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
