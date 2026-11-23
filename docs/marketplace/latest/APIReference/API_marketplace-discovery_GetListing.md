---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetListing.html
---

# GetListing

Provides details about a listing, such as descriptions, badges, categories, pricing model summaries, reviews, and associated products and offers.

## Request Syntax
<a name="API_marketplace-discovery_GetListing_RequestSyntax"></a>

```
POST /2026-02-05/getListing HTTP/1.1
Content-type: application/json

{
   "listingId": "{{string}}",
   "locale": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_GetListing_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_GetListing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [listingId](#API_marketplace-discovery_GetListing_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-request-listingId"></a>
The unique identifier of the listing to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [locale](#API_marketplace-discovery_GetListing_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_GetListing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
   "highlights": [ "string" ],
   "integrationGuide": "string",
   "listingId": "string",
   "listingName": "string",
   "locale": "string",
   "logoThumbnailUrl": "string",
   "longDescription": "string",
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
   "promotionalMedia": [
      { ... }
   ],
   "publisher": {
      "displayName": "string",
      "sellerProfileId": "string"
   },
   "purchaseIndicators": [
      {
         "indicatorType": "string"
      }
   ],
   "resources": [
      {
         "contentType": "string",
         "displayName": "string",
         "resourceType": "string",
         "value": "string"
      }
   ],
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
   "useCases": [
      {
         "useCase": {
            "description": "string",
            "displayName": "string",
            "value": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_marketplace-discovery_GetListing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedEntities](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-associatedEntities"></a>
The products and offers associated with this listing. Each entity contains product and offer information.
Type: Array of [ListingAssociatedEntity](API_marketplace-discovery_ListingAssociatedEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [badges](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-badges"></a>
Badges indicating special attributes of the listing, such as free tier eligibility, free trial availability, or Quick Launch support.
Type: Array of [ListingBadge](API_marketplace-discovery_ListingBadge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [catalog](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-catalog"></a>
The name of the catalog that the listing belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [categories](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-categories"></a>
The categories that classify this listing into logical groups.
Type: Array of [Category](API_marketplace-discovery_Category.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [fulfillmentOptionSummaries](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-fulfillmentOptionSummaries"></a>
A summary of fulfillment options available for deploying or accessing the listing, such as Amazon Machine Image (AMI), Software as a Service (SaaS), or Container.
Type: Array of [FulfillmentOptionSummary](API_marketplace-discovery_FulfillmentOptionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [highlights](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-highlights"></a>
A list of key features that the listing offers to customers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [listingId](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-listingId"></a>
The unique identifier of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [listingName](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-listingName"></a>
The human-readable display name of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [logoThumbnailUrl](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-logoThumbnailUrl"></a>
The URL of the logo thumbnail image for the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`

 ** [longDescription](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-longDescription"></a>
A detailed description of what the listing offers, in paragraph format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Pattern: `.*\S.*`

 ** [pricingModels](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-pricingModels"></a>
The pricing models for offers associated with this listing, such as usage-based, contract, Bring Your Own License (BYOL), or free.
Type: Array of [PricingModel](API_marketplace-discovery_PricingModel.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [pricingUnits](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-pricingUnits"></a>
The pricing units that define the billing dimensions for offers associated with this listing, such as users, hosts, or data.
Type: Array of [PricingUnit](API_marketplace-discovery_PricingUnit.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [promotionalMedia](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-promotionalMedia"></a>
Embedded promotional media provided by the creator of the product, such as images and videos.
Type: Array of [PromotionalMedia](API_marketplace-discovery_PromotionalMedia.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [publisher](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-publisher"></a>
The entity who created and published the listing.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object

 ** [purchaseIndicators](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-purchaseIndicators"></a>
Indicators describing purchase characteristics of this listing, such as whether you can subscribe to it or use it without a subscription. The list is empty when no special purchase conditions apply.
Type: Array of [PurchaseIndicator](API_marketplace-discovery_PurchaseIndicator.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [resources](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-resources"></a>
Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.
Type: Array of [Resource](API_marketplace-discovery_Resource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [sellerEngagements](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-sellerEngagements"></a>
The engagement options available to you, such as buying now, requesting a private offer, or requesting a demo.
Type: Array of [SellerEngagement](API_marketplace-discovery_SellerEngagement.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [shortDescription](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-shortDescription"></a>
A 1–3 sentence summary describing the key aspects of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [useCases](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-useCases"></a>
Use cases associated with the listing, describing scenarios where you can apply the product.
Type: Array of [UseCaseEntry](API_marketplace-discovery_UseCaseEntry.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [integrationGuide](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-integrationGuide"></a>
Optional guidance explaining how to use data in this listing. Primarily defines how to integrate with a multi-product listing.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [locale](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-locale"></a>
The locale of the returned content. This value indicates whether the response contains content in the requested locale or fell back to the default locale. See `Locale` for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`

 ** [reviewSummary](#API_marketplace-discovery_GetListing_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetListing-response-reviewSummary"></a>
A summary of customer reviews available for the listing, including average rating and total review count by source.
Type: [ReviewSummary](API_marketplace-discovery_ReviewSummary.md) object

## Errors
<a name="API_marketplace-discovery_GetListing_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. For the permissions that each operation requires, see [Access control for the AWS Marketplace Discovery API](https://docs.aws.amazon.com/marketplace/latest/developerguide/discovery-api-access-control.html) in the *AWS Marketplace Developer Guide*.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist. Verify that the identifier is correct.
HTTP Status Code: 404

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
<a name="API_marketplace-discovery_GetListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/GetListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GetListing)
