---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ImportPolicy.html
---

# ImportPolicy
<a name="API_ImportPolicy"></a>

Imports a V1 policy into V2, mapping RTO/RPO values from V1 scenarios.

## Request Syntax
<a name="API_ImportPolicy_RequestSyntax"></a>

```
POST /v2/import-policy HTTP/1.1
Content-type: application/json

{
   "availabilitySlo": {
      "target": {{number}}
   },
   "clientToken": "{{string}}",
   "kmsKeyId": "{{string}}",
   "multiAzDisasterRecoveryApproach": "{{string}}",
   "multiRegionDisasterRecoveryApproach": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "v1PolicyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilitySlo](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-availabilitySlo"></a>
The availability SLO to set on the imported policy.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** [clientToken](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [kmsKeyId](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [multiAzDisasterRecoveryApproach](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-multiAzDisasterRecoveryApproach"></a>
The multi-AZ disaster recovery approach for the imported policy.
Type: String
Valid Values: `ACTIVE_ACTIVE | HOT_STANDBY | WARM_STANDBY | PILOT_LIGHT | BACKUP_AND_RESTORE`
Required: No

 ** [multiRegionDisasterRecoveryApproach](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-multiRegionDisasterRecoveryApproach"></a>
The multi-Region disaster recovery approach for the imported policy.
Type: String
Valid Values: `ACTIVE_ACTIVE | HOT_STANDBY | WARM_STANDBY | PILOT_LIGHT | BACKUP_AND_RESTORE`
Required: No

 ** [tags](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** [v1PolicyArn](#API_ImportPolicy_RequestSyntax) **   <a name="ngresiliencehub-ImportPolicy-request-v1PolicyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_ImportPolicy_ResponseSyntax"></a>

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
<a name="API_ImportPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_ImportPolicy_ResponseSyntax) **   <a name="ngresiliencehub-ImportPolicy-response-policy"></a>
The imported policy.
Type: [Policy](API_Policy.md) object

## Errors
<a name="API_ImportPolicy_Errors"></a>

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

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ImportPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ImportPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ImportPolicy)
