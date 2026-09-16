---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_GetAction.html
---

# GetAction
<a name="API_GetAction"></a>

Retrieves the description of a specific support action.

## Request Syntax
<a name="API_GetAction_RequestSyntax"></a>

```
GET /actions/{{action}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAction_RequestParameters"></a>

The request uses the following URI parameters.

 ** [action](#API_GetAction_RequestSyntax) **   <a name="supportauthorization-GetAction-request-uri-action"></a>
The name of the support action to retrieve.
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-z][a-z0-9-]*:[A-Za-z0-9_.-]+`
Required: Yes

## Request Body
<a name="API_GetAction_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "action": "string",
   "description": "string",
   "service": "string"
}
```

## Response Elements
<a name="API_GetAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [action](#API_GetAction_ResponseSyntax) **   <a name="supportauthorization-GetAction-response-action"></a>
The name of the support action.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-z][a-z0-9-]*:[A-Za-z0-9_.-]+`

 ** [description](#API_GetAction_ResponseSyntax) **   <a name="supportauthorization-GetAction-response-description"></a>
A description of what the support action does.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

 ** [service](#API_GetAction_ResponseSyntax) **   <a name="supportauthorization-GetAction-response-service"></a>
The AWS service associated with the support action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-]+`

## Errors
<a name="API_GetAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this operation.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

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
<a name="API_GetAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supportauthz-2026-06-30/GetAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/GetAction)
