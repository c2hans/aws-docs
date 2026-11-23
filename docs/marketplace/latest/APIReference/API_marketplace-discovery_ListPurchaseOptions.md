---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html
---

# ListPurchaseOptions

Retrieves the purchase options (offers and offer sets) available to you. You can filter results by product, seller, purchase option type, visibility scope, and availability status. The operation returns results in pages. Use `nextToken` to retrieve the next page.

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
Filters to narrow the results. A result must match every filter. Within one filter, a result matches if it has any of the values.
Type: Array of [PurchaseOptionFilter](API_marketplace-discovery_PurchaseOptionFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [locale](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-maxResults"></a>
The maximum number of purchase options to return in each call. If you omit this field, the default is 25. Use `nextToken` to retrieve the next page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_marketplace-discovery_ListPurchaseOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
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
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

 ** [purchaseOptions](#API_marketplace-discovery_ListPurchaseOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListPurchaseOptions-response-purchaseOptions"></a>
The purchase options available to you. Each option is either an offer for a single product or an offer set spanning multiple products.
Type: Array of [PurchaseOptionSummary](API_marketplace-discovery_PurchaseOptionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_marketplace-discovery_ListPurchaseOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. For the permissions that each operation requires, see [Access control for the AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/developerguide/discovery-api-access-control.html) in the *AWS Marketplace Developer Guide*.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of your requests and retry.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check the `reason` field for the constraint that failed.
 ** reason **
The reason that the input fails to satisfy the constraints that the Discovery API specifies. This field has one of the following values:
INVALID\_PAGINATION\_TOKEN
The `nextToken` value is malformed, expired, or belongs to a different request. Start the pagination again from the first page.
MALFORMED\_REQUEST\_PARAMETERS
One or more request parameters have an invalid value. Correct the parameters that you specified, and then resubmit your request.
PAGINATION\_LIMIT\_EXCEEDED
The request asks for results beyond the deepest page that the operation returns. Narrow your request with filters or a more specific search.
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
