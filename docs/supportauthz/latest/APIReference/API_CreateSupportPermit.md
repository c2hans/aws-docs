---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_CreateSupportPermit.html
---

# CreateSupportPermit
<a name="API_CreateSupportPermit"></a>

Creates a support permit that authorizes an AWS support operator to perform specified actions on specified resources. The permit is cryptographically signed using a customer-managed AWS KMS key (ECC\_NIST\_P384, SIGN\_VERIFY) to ensure non-repudiation.

## Request Syntax
<a name="API_CreateSupportPermit_RequestSyntax"></a>

```
POST /support-permits HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "permit": {
      "actions": { ... },
      "conditions": [
         { ... }
      ],
      "resources": { ... }
   },
   "signingKeyInfo": { ... },
   "supportCaseDisplayId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateSupportPermit_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSupportPermit_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service returns the existing permit without creating a duplicate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[!-~]+`
Required: No

 ** [description](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-description"></a>
A human-readable description of why this permit is being created. Maximum length of 1024 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** [name](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-name"></a>
A customer-chosen name for the support permit. Must be between 1 and 256 alphanumeric characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]{1,256}`
Required: Yes

 ** [permit](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-permit"></a>
The permit definition specifying the actions, resources, and time-window conditions that the support operator is authorized to use.
Type: [Permit](API_Permit.md) object
Required: Yes

 ** [signingKeyInfo](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-signingKeyInfo"></a>
The signing key information used to sign the permit. Must reference an AWS KMS key with key usage SIGN\_VERIFY and key spec ECC\_NIST\_P384.
Type: [SigningKeyInfo](API_SigningKeyInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [supportCaseDisplayId](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-supportCaseDisplayId"></a>
The display identifier of the AWS Support case associated with this permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: No

 ** [tags](#API_CreateSupportPermit_RequestSyntax) **   <a name="supportauthorization-CreateSupportPermit-request-tags"></a>
The tags to associate with the support permit on creation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateSupportPermit_ResponseSyntax"></a>

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
<a name="API_CreateSupportPermit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-arn"></a>
The Amazon Resource Name (ARN) of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:[a-z0-9-]+:[a-z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`

 ** [createdAt](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-createdAt"></a>
The timestamp when the permit was created.
Type: Timestamp

 ** [description](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-description"></a>
The description of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [name](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-name"></a>
The name of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]{1,256}`

 ** [permit](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-permit"></a>
The permit definition.
Type: [Permit](API_Permit.md) object

 ** [signingKeyInfo](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-signingKeyInfo"></a>
The signing key information for the permit.
Type: [SigningKeyInfo](API_SigningKeyInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-status"></a>
The current status of the support permit.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING`

 ** [supportCaseDisplayId](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-supportCaseDisplayId"></a>
The display identifier of the support case associated with the permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`

 ** [tags](#API_CreateSupportPermit_ResponseSyntax) **   <a name="supportauthorization-CreateSupportPermit-response-tags"></a>
The tags associated with the support permit.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_CreateSupportPermit_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient permissions to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An internal service error occurred. Try again later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request exceeds a service quota for your account.
 ** quotaCode **
The quota code of the exceeded quota.
 ** resourceId **
The identifier of the resource that exceeded the quota.
 ** resourceType **
The type of the resource that exceeded the quota.
 ** serviceCode **
The service code of the originating service.
HTTP Status Code: 402

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
<a name="API_CreateSupportPermit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/supportauthz-2026-06-30/CreateSupportPermit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/CreateSupportPermit)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
