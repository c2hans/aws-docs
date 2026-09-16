---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateSystem.html
---

# CreateSystem
<a name="API_CreateSystem"></a>

Creates a system that represents a logical grouping of services.

## Request Syntax
<a name="API_CreateSystem_RequestSyntax"></a>

```
POST /v2/create-system HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "sharingEnabled": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSystem_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSystem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [description](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [kmsKeyId](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [name](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [sharingEnabled](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-sharingEnabled"></a>
Indicates whether cross-account sharing is enabled for the system.
Type: Boolean
Required: No

 ** [tags](#API_CreateSystem_RequestSyntax) **   <a name="ngresiliencehub-CreateSystem-request-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## Response Syntax
<a name="API_CreateSystem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "system": {
      "createdAt": number,
      "description": "string",
      "kmsKeyId": "string",
      "name": "string",
      "organizationId": "string",
      "ouId": "string",
      "sharingEnabled": boolean,
      "systemArn": "string",
      "systemId": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateSystem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [system](#API_CreateSystem_ResponseSyntax) **   <a name="ngresiliencehub-CreateSystem-response-system"></a>
The created system.
Type: [System](API_System.md) object

## Errors
<a name="API_CreateSystem_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** ConflictException **
Conflict — resource already exists.
HTTP Status Code: 409

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Service quota exceeded.
HTTP Status Code: 402

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_CreateSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateSystem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateSystem)
