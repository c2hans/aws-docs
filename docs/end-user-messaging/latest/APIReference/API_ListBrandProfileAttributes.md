---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_ListBrandProfileAttributes.html
---

# ListBrandProfileAttributes
<a name="API_ListBrandProfileAttributes"></a>

Retrieves a paginated list of the attributes for a brand profile.

## Request Syntax
<a name="API_ListBrandProfileAttributes_RequestSyntax"></a>

```
GET /v1/brand-profiles/{{brandProfileId}}/attributes?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBrandProfileAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_ListBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-ListBrandProfileAttributes-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

 ** [maxResults](#API_ListBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-ListBrandProfileAttributes-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-ListBrandProfileAttributes-request-uri-nextToken"></a>
The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`

## Request Body
<a name="API_ListBrandProfileAttributes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBrandProfileAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "brandProfileAttributes": [
      {
         "attributeName": "string",
         "attributeType": "string",
         "category": "string",
         "createdAt": number,
         "description": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBrandProfileAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [brandProfileAttributes](#API_ListBrandProfileAttributes_ResponseSyntax) **   <a name="endusermessaging-ListBrandProfileAttributes-response-brandProfileAttributes"></a>
The list of brand profile attributes.
Type: Array of [BrandProfileAttributeSummary](API_BrandProfileAttributeSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListBrandProfileAttributes_ResponseSyntax) **   <a name="endusermessaging-ListBrandProfileAttributes-response-nextToken"></a>
The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.+`

## Errors
<a name="API_ListBrandProfileAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.
 ** resourceId **
The identifier of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListBrandProfileAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/ListBrandProfileAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/ListBrandProfileAttributes)
