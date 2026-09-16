---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_GetSupportPermit.html
---

# GetSupportPermit
<a name="API_GetSupportPermit"></a>

Retrieves the details of a support permit by its ARN or name.

## Request Syntax
<a name="API_GetSupportPermit_RequestSyntax"></a>

```
GET /support-permits/{{supportPermitIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetSupportPermit_RequestParameters"></a>

The request uses the following URI parameters.

 ** [supportPermitIdentifier](#API_GetSupportPermit_RequestSyntax) **   <a name="supportauthorization-GetSupportPermit-request-uri-supportPermitIdentifier"></a>
The ARN or name of the support permit to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: Yes

## Request Body
<a name="API_GetSupportPermit_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetSupportPermit_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "createdAt": number,
   "description": "string",
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
   "supportCaseDisplayId": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetSupportPermit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-arn"></a>
The ARN of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:[a-z0-9-]+:[a-z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`

 ** [createdAt](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-createdAt"></a>
The timestamp when the permit was created.
Type: Timestamp

 ** [description](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-description"></a>
The description of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [name](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-name"></a>
The name of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]{1,256}`

 ** [permit](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-permit"></a>
The permit definition.
Type: [Permit](API_Permit.md) object

 ** [signingKeyInfo](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-signingKeyInfo"></a>
The signing key information for the permit.
Type: [SigningKeyInfo](API_SigningKeyInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-status"></a>
The current status of the support permit.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING`

 ** [supportCaseDisplayId](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-supportCaseDisplayId"></a>
The display identifier of the support case associated with the permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`

 ** [tags](#API_GetSupportPermit_ResponseSyntax) **   <a name="supportauthorization-GetSupportPermit-response-tags"></a>
The tags associated with the support permit.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetSupportPermit_Errors"></a>

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
<a name="API_GetSupportPermit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supportauthz-2026-06-30/GetSupportPermit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/GetSupportPermit)
