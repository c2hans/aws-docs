---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreatePolicy.html
---

# CreatePolicy
<a name="API_CreatePolicy"></a>

Creates a resilience policy that defines availability and disaster recovery requirements.

## Request Syntax
<a name="API_CreatePolicy_RequestSyntax"></a>

```
POST /v2/create-policy HTTP/1.1
Content-type: application/json

{
   "availabilitySlo": {
      "target": {{number}}
   },
   "clientToken": "{{string}}",
   "dataRecovery": {
      "timeBetweenBackupsInMinutes": {{number}}
   },
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "multiAz": {
      "disasterRecoveryApproach": "{{string}}",
      "rpoInMinutes": {{number}},
      "rtoInMinutes": {{number}}
   },
   "multiRegion": {
      "disasterRecoveryApproach": "{{string}}",
      "rpoInMinutes": {{number}},
      "rtoInMinutes": {{number}}
   },
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreatePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilitySlo](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-availabilitySlo"></a>
The availability SLO for the resilience policy.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** [clientToken](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [dataRecovery](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-dataRecovery"></a>
The data recovery targets for the resilience policy.
Type: [DataRecoveryTargets](API_DataRecoveryTargets.md) object
Required: No

 ** [description](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-description"></a>
Resource description for services and policies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 615.
Required: No

 ** [kmsKeyId](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [multiAz](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-multiAz"></a>
The multi-AZ disaster recovery targets for the resilience policy.
Type: [MultiAzTargets](API_MultiAzTargets.md) object
Required: No

 ** [multiRegion](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-multiRegion"></a>
The multi-Region disaster recovery targets for the resilience policy.
Type: [MultiRegionTargets](API_MultiRegionTargets.md) object
Required: No

 ** [name](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [tags](#API_CreatePolicy_RequestSyntax) **   <a name="ngresiliencehub-CreatePolicy-request-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## Response Syntax
<a name="API_CreatePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "policy": {
      "associatedServiceCount": number,
      "availabilitySlo": {
         "target": number
      },
      "createdAt": number,
      "dataRecovery": {
         "timeBetweenBackupsInMinutes": number
      },
      "description": "string",
      "kmsKeyId": "string",
      "multiAz": {
         "disasterRecoveryApproach": "string",
         "rpoInMinutes": number,
         "rtoInMinutes": number
      },
      "multiRegion": {
         "disasterRecoveryApproach": "string",
         "rpoInMinutes": number,
         "rtoInMinutes": number
      },
      "name": "string",
      "policyArn": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_CreatePolicy_ResponseSyntax) **   <a name="ngresiliencehub-CreatePolicy-response-policy"></a>
The created resilience policy.
Type: [Policy](API_Policy.md) object

## Errors
<a name="API_CreatePolicy_Errors"></a>

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
<a name="API_CreatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreatePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
