---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.html
---

# SearchListings
<a name="API_marketplace-discovery_SearchListings"></a>

Returns a list of product listings based on search criteria and filters. You can search by keyword, filter by category, pricing model, fulfillment type, and other attributes, and sort results by relevance or customer rating.

## Request Syntax
<a name="API_marketplace-discovery_SearchListings_RequestSyntax"></a>

```
POST /2026-02-05/searchListings HTTP/1.1
Content-type: application/json

{
   "filters": [
      {
         "filterType": "{{string}}",
         "filterValues": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchText": "{{string}}",
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_SearchListings_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_SearchListings_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-filters"></a>
Filters to narrow search results. Multiple filters are combined with AND logic. Multiple values within the same filter are combined with OR logic.
Type: Array of [SearchFilter](API_marketplace-discovery_SearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: No

 ** [maxResults](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to get more results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

 ** [searchText](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-searchText"></a>
The search query text to find relevant listings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*[^ ]*.*`
Required: No

 ** [sortBy](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-sortBy"></a>
The field to sort results by. Valid values are `RELEVANCE` and `AVERAGE_CUSTOMER_RATING`.
Type: String
Valid Values: `RELEVANCE | AVERAGE_CUSTOMER_RATING`
Required: No

 ** [sortOrder](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-sortOrder"></a>
The sort direction. Valid values are `DESCENDING` and `ASCENDING`.
Type: String
Valid Values: `DESCENDING | ASCENDING`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_SearchListings_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "listingSummaries": [
      {
         "associatedEntities": [
            {
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
         "badges": [
            {
               "badgeType": "string",
               "displayName": "string"
            }
         ],
         "catalog": "string",
         "categories": [
            {
               "categoryId": "string",
               "displayName": "string"
            }
         ],
         "fulfillmentOptionSummaries": [
            {
               "displayName": "string",
               "fulfillmentOptionType": "string"
            }
         ],
         "listingId": "string",
         "listingName": "string",
         "logoThumbnailUrl": "string",
         "pricingModels": [
            {
               "displayName": "string",
               "pricingModelType": "string"
            }
         ],
         "pricingUnits": [
            {
               "displayName": "string",
               "pricingUnitType": "string"
            }
         ],
         "publisher": {
            "displayName": "string",
            "sellerProfileId": "string"
         },
         "reviewSummary": {
            "reviewSourceSummaries": [
               {
                  "averageRating": "string",
                  "sourceId": "string",
                  "sourceName": "string",
                  "sourceUrl": "string",
                  "totalReviews": number
               }
            ]
         },
         "shortDescription": "string"
      }
   ],
   "nextToken": "string",
   "totalResults": number
}
```

## Response Elements
<a name="API_marketplace-discovery_SearchListings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [listingSummaries](#API_marketplace-discovery_SearchListings_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-response-listingSummaries"></a>
The listing summaries matching the search criteria. Each summary includes the listing name, description, badges, categories, pricing models, reviews, and associated products.
Type: Array of [ListingSummary](API_marketplace-discovery_ListingSummary.md) objects

 ** [totalResults](#API_marketplace-discovery_SearchListings_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-response-totalResults"></a>
The total number of listings matching the search criteria.
Type: Long
Valid Range: Minimum value of 0.

 ** [nextToken](#API_marketplace-discovery_SearchListings_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-response-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_SearchListings_Errors"></a>

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
<a name="API_marketplace-discovery_SearchListings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SearchListings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
