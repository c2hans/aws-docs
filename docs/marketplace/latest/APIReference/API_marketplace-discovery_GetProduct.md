---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetProduct.html
---

# GetProduct
<a name="API_marketplace-discovery_GetProduct"></a>

Provides details about a product, such as descriptions, highlights, categories, fulfillment option summaries, promotional media, and seller engagement options.

## Request Syntax
<a name="API_marketplace-discovery_GetProduct_RequestSyntax"></a>

```
POST /2026-02-05/getProduct HTTP/1.1
Content-type: application/json

{
   "locale": "{{string}}",
   "productId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_GetProduct_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_GetProduct_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [productId](#API_marketplace-discovery_GetProduct_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-request-productId"></a>
The unique identifier of the product to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [locale](#API_marketplace-discovery_GetProduct_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-request-locale"></a>
A BCP 47 language tag or comma-separated priority list specifying the preferred locale for response content. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If omitted, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_GetProduct_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "catalog": "string",
   "categories": [
      {
         "categoryId": "string",
         "displayName": "string"
      }
   ],
   "deployedOnAws": "string",
   "fulfillmentOptionSummaries": [
      {
         "displayName": "string",
         "fulfillmentOptionType": "string"
      }
   ],
   "highlights": [ "string" ],
   "listingId": "string",
   "locale": "string",
   "logoThumbnailUrl": "string",
   "longDescription": "string",
   "manufacturer": {
      "displayName": "string",
      "sellerProfileId": "string"
   },
   "productId": "string",
   "productName": "string",
   "promotionalMedia": [
      { ... }
   ],
   "resources": [
      {
         "contentType": "string",
         "displayName": "string",
         "resourceType": "string",
         "value": "string"
      }
   ],
   "sellerEngagements": [
      {
         "contentType": "string",
         "engagementType": "string",
         "value": "string"
      }
   ],
   "shortDescription": "string"
}
```

## Response Elements
<a name="API_marketplace-discovery_GetProduct_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [catalog](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-catalog"></a>
The name of the catalog that the product belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [categories](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-categories"></a>
The categories used to classify this product into logical groups.
Type: Array of [Category](API_marketplace-discovery_Category.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

 ** [deployedOnAws](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-deployedOnAws"></a>
Indicates whether the product is deployed on AWS infrastructure.
Type: String
Valid Values: `DEPLOYED | NOT_DEPLOYED | NOT_APPLICABLE`

 ** [fulfillmentOptionSummaries](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-fulfillmentOptionSummaries"></a>
A summary of fulfillment options available for deploying or accessing the product, such as AMI, SaaS, or Container.
Type: Array of [FulfillmentOptionSummary](API_marketplace-discovery_FulfillmentOptionSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [highlights](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-highlights"></a>
A list of key features that the product offers to customers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [listingId](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-listingId"></a>
The default listing identifier associated with the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [logoThumbnailUrl](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-logoThumbnailUrl"></a>
The URL of the logo thumbnail image for the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`

 ** [longDescription](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-longDescription"></a>
A detailed description of what the product does, in paragraph format.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32768.
Pattern: `.*\S.*`

 ** [manufacturer](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-manufacturer"></a>
The entity who manufactured the product.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object

 ** [productId](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-productId"></a>
The unique identifier of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [productName](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-productName"></a>
The human-readable display name of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [promotionalMedia](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-promotionalMedia"></a>
Embedded promotional media provided by the creator of the product, such as images and videos.
Type: Array of [PromotionalMedia](API_marketplace-discovery_PromotionalMedia.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [resources](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-resources"></a>
Resources that provide further information about using the product or requesting support, such as documentation links, support contacts, and usage instructions.
Type: Array of [Resource](API_marketplace-discovery_Resource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [sellerEngagements](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-sellerEngagements"></a>
Engagement options available to potential buyers, such as requesting a private offer or requesting a demo.
Type: Array of [SellerEngagement](API_marketplace-discovery_SellerEngagement.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [shortDescription](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-shortDescription"></a>
A 1–3 sentence summary describing the key aspects of the product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

 ** [locale](#API_marketplace-discovery_GetProduct_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetProduct-response-locale"></a>
The locale of the returned content. Indicates whether the response contains content in the requested locale, or fell back to the default locale. See `Locale` for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`

## Errors
<a name="API_marketplace-discovery_GetProduct_Errors"></a>

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
<a name="API_marketplace-discovery_GetProduct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/GetProduct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GetProduct)
