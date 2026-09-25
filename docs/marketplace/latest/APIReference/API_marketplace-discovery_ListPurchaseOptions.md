---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html
---

# ListPurchaseOptions
<a name="API_marketplace-discovery_ListPurchaseOptions"></a>

Returns the purchase options (offers and offer sets) available to the buyer. You can filter results by product, seller, purchase option type, visibility scope, and availability status.

**Note**
You must include at least one of the following filters in the request: a `PRODUCT_ID` filter to specify the product for which to retrieve purchase options, or a `VISIBILITY_SCOPE` filter to retrieve purchase options by visibility.

## Request Syntax
<a name="API_marketplace-discovery_ListPurchaseOptions_RequestSyntax"></a>

```
POST /2026-02-05/listPurchaseOptions HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "filterType": "{{string}}",
         "filterValues": [ "{{string}}" ]
      }
   ],
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_ListPurchaseOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_ListPurchaseOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-filters"></a>
Filters to narrow the results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.
Type: Array of [PurchaseOptionFilter](API_marketplace-discovery_PurchaseOptionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [locale](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-locale"></a>
A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to get more results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_ListPurchaseOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "purchaseOptions": [
      {
         "associatedEntities": [
            {
               "offer": {
                  "offerId": "string",
                  "offerName": "string",
                  "sellerOfRecord": {
                     "displayName": "string",
                     "sellerProfileId": "string"
                  }
               },
               "offerSet": {
                  "offerSetId": "string",
                  "sellerOfRecord": {
                     "displayName": "string",
                     "sellerProfileId": "string"
                  }
               },
               "product": {
                  "manufacturer": {
                     "displayName": "string",
                     "sellerProfileId": "string"
                  },
                  "productId": "string",
                  "productName": "string"
               }
            }
         ],
         "availableFromTime": number,
         "badges": [
            {
               "badgeType": "string",
               "displayName": "string"
            }
         ],
         "catalog": "string",
         "expirationTime": number,
         "purchaseOptionId": "string",
         "purchaseOptionName": "string",
         "purchaseOptionType": "string",
         "sellerOfRecord": {
            "displayName": "string",
            "sellerProfileId": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_marketplace-discovery_ListPurchaseOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_marketplace-discovery_ListPurchaseOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-response-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

 ** [purchaseOptions](#API_marketplace-discovery_ListPurchaseOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-response-purchaseOptions"></a>
The purchase options available to the buyer. Each option is either an offer for a single product or an offer set spanning multiple products.
Type: Array of [PurchaseOptionSummary](API_marketplace-discovery_PurchaseOptionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_marketplace-discovery_ListPurchaseOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** reason **
The reason that the input fails to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_marketplace-discovery_ListPurchaseOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/ListPurchaseOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListPurchaseOptions)
