---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_UpdatePolicy.html
---

# UpdatePolicy
<a name="API_UpdatePolicy"></a>

Updates an existing resilience policy.

## Request Syntax
<a name="API_UpdatePolicy_RequestSyntax"></a>

```
POST /v2/update-policy HTTP/1.1
Content-type: application/json

{
   "availabilitySlo": {
      "target": {{number}}
   },
   "dataRecovery": {
      "timeBetweenBackupsInMinutes": {{number}}
   },
   "description": "{{string}}",
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
   "policyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdatePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdatePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilitySlo](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-availabilitySlo"></a>
The updated availability SLO for the policy.
Type: [AvailabilitySlo](API_AvailabilitySlo.md) object
Required: No

 ** [dataRecovery](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-dataRecovery"></a>
The updated data recovery targets for the policy.
Type: [DataRecoveryTargets](API_DataRecoveryTargets.md) object
Required: No

 ** [description](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-description"></a>
Resource description for services and policies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 615.
Required: No

 ** [multiAz](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-multiAz"></a>
The updated multi-AZ disaster recovery targets for the policy.
Type: [MultiAzTargets](API_MultiAzTargets.md) object
Required: No

 ** [multiRegion](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-multiRegion"></a>
The updated multi-Region disaster recovery targets for the policy.
Type: [MultiRegionTargets](API_MultiRegionTargets.md) object
Required: No

 ** [policyArn](#API_UpdatePolicy_RequestSyntax) **   <a name="ngresiliencehub-UpdatePolicy-request-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_UpdatePolicy_ResponseSyntax"></a>

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
<a name="API_UpdatePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policy](#API_UpdatePolicy_ResponseSyntax) **   <a name="ngresiliencehub-UpdatePolicy-response-policy"></a>
The updated policy.
Type: [Policy](API_Policy.md) object

## Errors
<a name="API_UpdatePolicy_Errors"></a>

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
<a name="API_UpdatePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/UpdatePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/UpdatePolicy)
