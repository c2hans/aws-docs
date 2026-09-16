---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferSet.html
---

# GetOfferSet
<a name="API_marketplace-discovery_GetOfferSet"></a>

Provides details about an offer set, which is a bundle of offers across multiple products. Includes the seller, availability dates, buyer notes, and associated product-offer pairs.

## Request Syntax
<a name="API_marketplace-discovery_GetOfferSet_RequestSyntax"></a>

```
POST /2026-02-05/getOfferSet HTTP/1.1
Content-type: application/json

{
   "offerSetId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_GetOfferSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_GetOfferSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [offerSetId](#API_marketplace-discovery_GetOfferSet_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-request-offerSetId"></a>
The unique identifier of the offer set to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-discovery_GetOfferSet_ResponseSyntax"></a>

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
   "availableFromTime": number,
   "badges": [
      {
         "badgeType": "string",
         "displayName": "string"
      }
   ],
   "buyerNotes": "string",
   "catalog": "string",
   "expirationTime": number,
   "offerSetId": "string",
   "offerSetName": "string",
   "sellerOfRecord": {
      "displayName": "string",
      "sellerProfileId": "string"
   }
}
```

## Response Elements
<a name="API_marketplace-discovery_GetOfferSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedEntities](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-associatedEntities"></a>
The products and offers included in this offer set.
Type: Array of [OfferSetAssociatedEntity](API_marketplace-discovery_OfferSetAssociatedEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [badges](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-badges"></a>
Badges indicating special attributes of the offer set, such as private pricing or future dated.
Type: Array of [PurchaseOptionBadge](API_marketplace-discovery_PurchaseOptionBadge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [catalog](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-catalog"></a>
The name of the catalog that the offer set belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [offerSetId](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-offerSetId"></a>
The unique identifier of the offer set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [sellerOfRecord](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-sellerOfRecord"></a>
The entity responsible for selling the products under this offer set.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object

 ** [availableFromTime](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-availableFromTime"></a>
The date and time when the offer set became available to the buyer.
Type: Timestamp

 ** [buyerNotes](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-buyerNotes"></a>
Detailed information about the offer set that helps buyers understand its purpose and contents.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [expirationTime](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-expirationTime"></a>
The date and time when the offer set expires and is no longer available for procurement.
Type: Timestamp

 ** [offerSetName](#API_marketplace-discovery_GetOfferSet_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferSet-response-offerSetName"></a>
The display name of the offer set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`

## Errors
<a name="API_marketplace-discovery_GetOfferSet_Errors"></a>

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
<a name="API_marketplace-discovery_GetOfferSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/GetOfferSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GetOfferSet)
