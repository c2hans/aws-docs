---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_ListSupportPermits.html
---

# ListSupportPermits
<a name="API_ListSupportPermits"></a>

Lists all support permits in the caller's account. Use pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListSupportPermits_RequestSyntax"></a>

```
GET /support-permits?maxResults={{maxResults}}&nextToken={{nextToken}}&supportPermitStatuses={{supportPermitStatuses}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSupportPermits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListSupportPermits_RequestSyntax) **   <a name="supportauthorization-ListSupportPermits-request-uri-maxResults"></a>
The maximum number of results to return in a single call. Valid range is 1 to 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListSupportPermits_RequestSyntax) **   <a name="supportauthorization-ListSupportPermits-request-uri-nextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/+=%_-]+`

 ** [supportPermitStatuses](#API_ListSupportPermits_RequestSyntax) **   <a name="supportauthorization-ListSupportPermits-request-uri-supportPermitStatuses"></a>
Filters the results by support permit status. Valid values: ACTIVE, INACTIVE, DELETING.
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Valid Values: `ACTIVE | INACTIVE | DELETING`

## Request Body
<a name="API_ListSupportPermits_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSupportPermits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "supportPermits": [
      {
         "arn": "string",
         "createdAt": number,
         "name": "string",
         "permit": {
            "actions": { ... },
            "conditions": [
               { ... }
            ],
            "resources": { ... }
         },
         "signingKeyInfo": { ... },
         "status": "string",
         "supportCaseDisplayId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSupportPermits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSupportPermits_ResponseSyntax) **   <a name="supportauthorization-ListSupportPermits-response-nextToken"></a>
The token for the next page of results, or null if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/+=%_-]+`

 ** [supportPermits](#API_ListSupportPermits_ResponseSyntax) **   <a name="supportauthorization-ListSupportPermits-response-supportPermits"></a>
The list of support permits.
Type: Array of [SupportPermitSummary](API_SupportPermitSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_ListSupportPermits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The request rate exceeded the allowed limit. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fieldList **
A list of fields that fail validation. Each entry identifies the field and the reason for the constraint violation.
HTTP Status Code: 400

## See Also
<a name="API_ListSupportPermits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supportauthz-2026-06-30/ListSupportPermits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/ListSupportPermits)
