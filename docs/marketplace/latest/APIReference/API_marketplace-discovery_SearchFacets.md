---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchFacets.html
---

# SearchFacets

Retrieves the available facet values for filtering listings, such as categories, pricing models, fulfillment option types, publishers, and customer ratings. Each facet value includes a count of matching listings.

## Request Syntax
<a name="API_marketplace-discovery_SearchFacets_RequestSyntax"></a>

```
POST /2026-02-05/searchFacets HTTP/1.1
Content-type: application/json

{
   "facetTypes": [ "{{string}}" ],
   "filters": [
      {
         "filterType": "{{string}}",
         "filterValues": [ "{{string}}" ]
      }
   ],
   "locale": "{{string}}",
   "nextToken": "{{string}}",
   "searchText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_SearchFacets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_SearchFacets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [facetTypes](#API_marketplace-discovery_SearchFacets_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-request-facetTypes"></a>
The facet types to retrieve. If you omit this field or leave it empty, the service returns all available facets.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Valid Values: `AVERAGE_CUSTOMER_RATING | CATEGORY | PUBLISHER | FULFILLMENT_OPTION_TYPE | PRICING_MODEL | PRICING_UNIT | DEPLOYED_ON_AWS | NUMBER_OF_PRODUCTS | CERTIFICATES | SPECIALIZATION | SPECIALIZATION_CATEGORY | SELLER_ENGAGEMENT | TRUST_CENTER`
Required: No

 ** [filters](#API_marketplace-discovery_SearchFacets_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-request-filters"></a>
Filters to apply before retrieving facets. A result must match every filter. Within one filter, a result matches if it has any of the values.
Type: Array of [SearchFilter](API_marketplace-discovery_SearchFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: No

 ** [locale](#API_marketplace-discovery_SearchFacets_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [nextToken](#API_marketplace-discovery_SearchFacets_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

 ** [searchText](#API_marketplace-discovery_SearchFacets_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-request-searchText"></a>
The search query text to filter listings before retrieving facets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*[^ ]*.*`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_SearchFacets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "listingFacets": {
      "string" : [
         {
            "count": number,
            "displayName": "string",
            "parent": "string",
            "value": "string"
         }
      ]
   },
   "nextToken": "string",
   "totalResults": number
}
```

## Response Elements
<a name="API_marketplace-discovery_SearchFacets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [listingFacets](#API_marketplace-discovery_SearchFacets_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-response-listingFacets"></a>
A map of facet types to their corresponding facet values. Each facet value includes a display name, internal value, and count of matching listings.
Type: String to array of [ListingFacet](API_marketplace-discovery_ListingFacet.md) objects map
Valid Keys: `AVERAGE_CUSTOMER_RATING | CATEGORY | PUBLISHER | FULFILLMENT_OPTION_TYPE | PRICING_MODEL | PRICING_UNIT | DEPLOYED_ON_AWS | NUMBER_OF_PRODUCTS | CERTIFICATES | SPECIALIZATION | SPECIALIZATION_CATEGORY | SELLER_ENGAGEMENT | TRUST_CENTER`
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [totalResults](#API_marketplace-discovery_SearchFacets_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-response-totalResults"></a>
The total number of listings matching the search criteria.
Type: Long
Valid Range: Minimum value of 0.

 ** [nextToken](#API_marketplace-discovery_SearchFacets_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_SearchFacets-response-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_SearchFacets_Errors"></a>

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
<a name="API_marketplace-discovery_SearchFacets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/SearchFacets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SearchFacets)
