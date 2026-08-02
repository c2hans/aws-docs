---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html
---

# GetOffer
<a name="API_marketplace-discovery_GetOffer"></a>

Provides details about an offer, such as the pricing model, seller of record, availability dates, badges, and associated products.

## Request Syntax
<a name="API_marketplace-discovery_GetOffer_RequestSyntax"></a>

```
POST /2026-02-05/getOffer HTTP/1.1
Content-type: application/json

{
   "offerId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_GetOffer_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_GetOffer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [offerId](#API_marketplace-discovery_GetOffer_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-request-offerId"></a>
The unique identifier of the offer to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-discovery_GetOffer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agreementProposalId": "string",
   "associatedEntities": [
      {
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
   "offerId": "string",
   "offerName": "string",
   "pricingModel": {
      "displayName": "string",
      "pricingModelType": "string"
   },
   "replacementAgreementId": "string",
   "sellerOfRecord": {
      "displayName": "string",
      "sellerProfileId": "string"
   }
}
```

## Response Elements
<a name="API_marketplace-discovery_GetOffer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementProposalId](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-agreementProposalId"></a>
An encoded string to be passed by the acceptor of the terms when creating an agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [associatedEntities](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-associatedEntities"></a>
The products and offer sets associated with this offer.
Type: Array of [OfferAssociatedEntity](API_marketplace-discovery_OfferAssociatedEntity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [badges](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-badges"></a>
Badges indicating special attributes of the offer, such as private pricing, future dated, or replacement offer.
Type: Array of [PurchaseOptionBadge](API_marketplace-discovery_PurchaseOptionBadge.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [catalog](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-catalog"></a>
The name of the catalog that the offer belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [offerId](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-offerId"></a>
The unique identifier of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`

 ** [pricingModel](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-pricingModel"></a>
The pricing model that determines how buyers are charged, such as usage-based, contract, BYOL, or free.
Type: [PricingModel](API_marketplace-discovery_PricingModel.md) object

 ** [sellerOfRecord](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-sellerOfRecord"></a>
The entity responsible for selling the product under this offer.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object

 ** [availableFromTime](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-availableFromTime"></a>
The date and time when the offer became available to the buyer.
Type: Timestamp

 ** [expirationTime](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-expirationTime"></a>
The date and time until when the offer can be procured. This value is null for offers that never expire.
Type: Timestamp

 ** [offerName](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-offerName"></a>
The display name of the offer. This is free-form text provided by the seller.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.

 ** [replacementAgreementId](#API_marketplace-discovery_GetOffer_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOffer-response-replacementAgreementId"></a>
The identifier of the existing agreement that this offer would replace. Enables agreement-based offer functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

## Errors
<a name="API_marketplace-discovery_GetOffer_Errors"></a>

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
<a name="API_marketplace-discovery_GetOffer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/GetOffer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GetOffer)
