---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.html
---

# SearchListings

Searches for listings that match your search criteria and filters. You can search by keyword, filter by category, pricing model, fulfillment type, and other attributes, and sort results by relevance or customer rating. The operation returns results in pages. Use `nextToken` to retrieve the next page.

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
   "locale": "{{string}}",
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
Filters to narrow search results. A result must match every filter. Within one filter, a result matches if it has any of the values.
Type: Array of [SearchFilter](API_marketplace-discovery_SearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: No

 ** [locale](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-maxResults"></a>
The maximum number of listings to return in each call. If you omit this field, the default is 25. Use `nextToken` to retrieve the next page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
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
The field to sort results by. If you do not specify a value, the service sorts by `RELEVANCE`. This field has one of the following values:
AVERAGE\_CUSTOMER\_RATING
Sorts by average customer rating.
RELEVANCE
Sorts by relevance to the search query.
Type: String
Valid Values: `RELEVANCE | AVERAGE_CUSTOMER_RATING`
Required: No

 ** [sortOrder](#API_marketplace-discovery_SearchListings_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchListings-request-sortOrder"></a>
The sort direction. If you do not specify a value, the service sorts in `DESCENDING` order. This field has one of the following values:
ASCENDING
Sorts from lowest to highest.
DESCENDING
Sorts from highest to lowest.
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
         "caseStudiesSummary": {
            "caseStudyCount": number
         },
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
         "sellerEngagements": [
            {
               "contentType": "string",
               "engagementType": "string",
               "value": "string"
            }
         ],
         "shortDescription": "string",
         "trustCenterSummary": {
            "certificationSummaries": [
               {
                  "certificationType": "string",
                  "displayName": "string",
                  "logoUrl": "string"
               }
            ],
            "sourceSummaries": [
               {
                  "contentType": "string",
                  "displayName": "string",
                  "provider": "string",
                  "value": "string"
               }
            ],
            "totalCertificationCount": number
         },
         "useCaseSummary": {
            "useCases": [
               {
                  "useCase": {
                     "displayName": "string",
                     "value": "string"
                  }
               }
            ]
         }
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
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_SearchListings_Errors"></a>

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
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/SearchListings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SearchListings)
