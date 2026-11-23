---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html
---

# GetOfferTerms

Retrieves the terms attached to an offer, such as pricing terms (usage-based, contract, Bring Your Own License (BYOL), free trial), legal terms, payment schedules, validity terms, support terms, and renewal terms. The operation returns results in pages. Use `nextToken` to retrieve the next page.

## Request Syntax
<a name="API_marketplace-discovery_GetOfferTerms_RequestSyntax"></a>

```
POST /2026-02-05/getOfferTerms HTTP/1.1
Content-type: application/json

{
   "locale": "{{string}}",
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

 ** [locale](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-maxResults"></a>
The maximum number of terms to return in each call. If you omit this field, the default is 10. Use `nextToken` to retrieve the next page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_marketplace-discovery_GetOfferTerms_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
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
   "locale": "string",
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

 ** [locale](#API_marketplace-discovery_GetOfferTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-response-locale"></a>
The locale of the returned content. This value indicates whether the response contains content in the requested locale or fell back to the default locale. See `Locale` for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`

 ** [nextToken](#API_marketplace-discovery_GetOfferTerms_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_GetOfferTerms-response-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_GetOfferTerms_Errors"></a>

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
