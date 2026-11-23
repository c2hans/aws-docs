---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListFulfillmentOptions.html
---

# ListFulfillmentOptions

Retrieves the fulfillment options available for a product, including deployment details such as version information, operating systems, usage instructions, and release notes. The operation returns results in pages. Use `nextToken` to retrieve the next page.

## Request Syntax
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax"></a>

```
POST /2026-02-05/listFulfillmentOptions HTTP/1.1
Content-type: application/json

{
   "locale": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "productId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_marketplace-discovery_ListFulfillmentOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [productId](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-productId"></a>
The unique identifier of the product for which to list fulfillment options.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** [locale](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-locale"></a>
The preferred locale for response content, as a Best Current Practice 47 (BCP 47) language tag or a comma-separated priority list of language tags. See `Locale` for supported values, constraints, fallback behavior, and the default locale. If you omit this field, the service returns content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`
Required: No

 ** [maxResults](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-maxResults"></a>
The maximum number of fulfillment options to return in each call. If you omit this field, the default is 25. Use `nextToken` to retrieve the next page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_marketplace-discovery_ListFulfillmentOptions_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-request-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "fulfillmentOptions": [
      { ... }
   ],
   "locale": "string",
   "nextToken": "string"
}
```

## Response Elements
<a name="API_marketplace-discovery_ListFulfillmentOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fulfillmentOptions](#API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-response-fulfillmentOptions"></a>
The fulfillment options available for the product. Each option describes how you can deploy or access the product.
Type: Array of [FulfillmentOption](API_marketplace-discovery_FulfillmentOption.md) objects

 ** [locale](#API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-response-locale"></a>
A Best Current Practice 47 (BCP 47) language tag or comma-separated priority list of language tags that specifies the preferred locale for response content. The field accepts a maximum of two language tags.
The service resolves a locale string to the nearest supported locale. A locale string can contain the following tags:
+  **Preferred locale** (first tag) – The locale you want the service to return content in.
+  **Fallback locale** (optional, second tag) – The service default locale (`en-US` or `en`). The service returns content in this locale when translated content for the preferred locale is unavailable.
The field is optional. If you omit this field or set it to null, the service returns content in the default locale (`en-US`).
The service supports the following locales:
en-US
English (service default, also resolves from `en`)
fr
French
es
Spanish
ko
Korean
ja
Japanese
The fallback behavior is as follows:
+ If translated content for the preferred locale is unavailable, the service returns content in the default locale.
+ If the preferred locale is not supported and you provide no fallback, the service returns a `ValidationException`.
+ If you provide an unsupported locale with the default locale as fallback (for example, `xx, en-US`), the service returns content in the default locale.
The `locale` field in Get API responses indicates the locale of the returned content. You can use this field to determine whether the response contains content in the requested locale or the default locale.
The following examples show how the field works:
fr
Request French content. If unavailable, falls back to `en-US`.
fr, en-US
Request French content with explicit fallback to English.
en-US
Request content in the default locale.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^;,]+(\s*,\s*[^;,]+){0,1}`

 ** [nextToken](#API_marketplace-discovery_ListFulfillmentOptions_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-discovery_ListFulfillmentOptions-response-nextToken"></a>
If the service returns `nextToken`, more results are available. The value of `nextToken` is a unique pagination token for each page. Make the call again with the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. An expired pagination token returns a `ValidationException`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[a-zA-Z0-9+/=]+`

## Errors
<a name="API_marketplace-discovery_ListFulfillmentOptions_Errors"></a>

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
<a name="API_marketplace-discovery_ListFulfillmentOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListFulfillmentOptions)
