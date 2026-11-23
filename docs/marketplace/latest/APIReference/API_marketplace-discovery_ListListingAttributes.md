---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListListingAttributes.html
---

# ListListingAttributes

Retrieves the requested attributes for a listing, including case studies and trust center information. The operation returns results in pages. Use `nextToken` to retrieve the next page.

**Important**
 **Do not depend on the order of attribute types in the response.** The order does not follow the order of the values in `attributeTypes`. The service does not guarantee any order between attribute types, and the order can change without notice. You should identify each entry by the attribute type it contains instead of relying on its position in the list.

## Request Syntax
<a name="API_marketplace-discovery_ListListingAttributes_RequestSyntax"></a>

```
POST /2026-02-05/listListingAttributes HTTP/1.1
Content-type: application/json

{
   "attributeTypes": [ "{{string}}" ],
   "listingId": "{{string}}",
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_ListListingAttributes_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_ListListingAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributeTypes](#API_marketplace-discovery_ListListingAttributes_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-request-attributeTypes"></a>
The attribute types to retrieve. Specify one or more of the following values:
CASE\_STUDY
Case studies associated with the listing.
SPECIALIZATION\_DETAIL
Specializations earned for the listing.
TRUST\_CENTER\_CERTIFICATION
Trust center certifications associated with the listing.
TRUST\_CENTER\_CONTROL
Trust center controls associated with the listing.
TRUST\_CENTER\_DOCUMENT
Trust center documents associated with the listing.
TRUST\_CENTER\_FAQ
The trust center FAQ associated with the listing.
TRUST\_CENTER\_SOURCE
Trust center sources associated with the listing.
TRUST\_CENTER\_UPDATE
Trust center updates associated with the listing.
The order of these values does not control the order of attribute types in the response.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Valid Values: `CASE_STUDY | SPECIALIZATION_DETAIL | TRUST_CENTER_SOURCE | TRUST_CENTER_CERTIFICATION | TRUST_CENTER_DOCUMENT | TRUST_CENTER_CONTROL | TRUST_CENTER_FAQ | TRUST_CENTER_UPDATE`
Required: Yes

 ** [listingId](#API_marketplace-discovery_ListListingAttributes_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-request-listingId"></a>
The unique identifier of the listing whose attributes are requested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [locale](#API_marketplace-discovery_ListListingAttributes_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_ListListingAttributes_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-request-maxResults"></a>
The maximum number of attributes to return in each call. If you omit this field, the default is 25. Use `nextToken` to retrieve the next page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_marketplace-discovery_ListListingAttributes_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_ListListingAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "listingAttributes": [
      { ... }
   ],
   "locale": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-discovery_ListListingAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [listingAttributes](#API_marketplace-discovery_ListListingAttributes_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-response-listingAttributes"></a>
The requested attributes. Each entry contains one attribute type.
The order of attribute types in this list is not guaranteed.
Type: Array of [ListingAttributeResults](API_marketplace-discovery_ListingAttributeResults.md) objects

 ** [locale](#API_marketplace-discovery_ListListingAttributes_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-response-locale"></a>
The locale of the returned content. See `Locale` for details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`

 ** [nextToken](#API_marketplace-discovery_ListListingAttributes_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListListingAttributes-response-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_ListListingAttributes_Errors"></a>

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
<a name="API_marketplace-discovery_ListListingAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/ListListingAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListListingAttributes)
