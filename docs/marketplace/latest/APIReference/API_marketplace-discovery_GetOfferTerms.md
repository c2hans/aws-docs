---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html
---

# GetOfferTerms
<a name="API_marketplace-discovery_GetOfferTerms"></a>

Returns the terms attached to an offer, such as pricing terms (usage-based, contract, BYOL, free trial), legal terms, payment schedules, validity terms, support terms, and renewal terms.

## Request Syntax
<a name="API_marketplace-discovery_GetOfferTerms_RequestSyntax"></a>

```
POST /2026-02-05/getOfferTerms HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "offerId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_GetOfferTerms_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_GetOfferTerms_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [offerId](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-offerId"></a>
The unique identifier of the offer whose terms to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [maxResults](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to get more results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_GetOfferTerms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "offerTerms": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_marketplace-discovery_GetOfferTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [offerTerms](#API_marketplace-discovery_GetOfferTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-response-offerTerms"></a>
The terms attached to the offer. Each element contains exactly one term type.
Type: Array of [OfferTerm](API_marketplace-discovery_OfferTerm.md) objects

 ** [nextToken](#API_marketplace-discovery_GetOfferTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-response-nextToken"></a>
If `nextToken` is returned, there are more results available. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_GetOfferTerms_Errors"></a>

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
<a name="API_marketplace-discovery_GetOfferTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/GetOfferTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/GetOfferTerms)
