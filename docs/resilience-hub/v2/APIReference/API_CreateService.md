---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateService.html
---

# CreateService
<a name="API_CreateService"></a>

Creates a service.

## Request Syntax
<a name="API_CreateService_RequestSyntax"></a>

```
POST /v2/create-service HTTP/1.1
Content-type: application/json

{
   "associatedSystems": [
      {
         "systemArn": "{{string}}",
         "systemName": "{{string}}",
         "userJourneyIds": [ "{{string}}" ]
      }
   ],
   "clientToken": "{{string}}",
   "dependencyDiscovery": "{{string}}",
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "permissionModel": {
      "crossAccountRoles": [
         {
            "crossAccountRoleArn": "{{string}}",
            "externalId": "{{string}}"
         }
      ],
      "invokerRoleName": "{{string}}"
   },
   "policyArn": "{{string}}",
   "regions": [ "{{string}}" ],
   "reportConfiguration": {
      "reportOutputs": [
         { ... }
      ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateService_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateService_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedSystems](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-associatedSystems"></a>
The systems to associate with the service.
Type: Array of [AssociatedSystem](API_AssociatedSystem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [clientToken](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [dependencyDiscovery](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-dependencyDiscovery"></a>
Caller-settable values for dependency discovery. INITIALIZING is system-managed.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [description](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-description"></a>
Resource description for services and policies.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 615.
Required: No

 ** [kmsKeyId](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [name](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-name"></a>
Resource name (used in ARN — no spaces allowed).
Type: String
Length Constraints: Minimum length of 2. Maximum length of 60.
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** [permissionModel](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-permissionModel"></a>
The permission model for the service.
Type: [PermissionModel](API_PermissionModel.md) object
Required: Yes

 ** [policyArn](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [regions](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-regions"></a>
The Regions where the service operates.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 6.
Pattern: `[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]`
Required: Yes

 ** [reportConfiguration](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-reportConfiguration"></a>
Configuration for automatic report generation on a Service.
Type: [ServiceReportConfiguration](API_ServiceReportConfiguration.md) object
Required: No

 ** [tags](#API_CreateService_RequestSyntax) **   <a name="ngresiliencehub-CreateService-request-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

## Response Syntax
<a name="API_CreateService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "service": {
      "accountId": "string",
      "achievability": {
         "availabilitySlo": "string",
         "dataRecoveryTimeBetweenBackups": "string",
         "multiAzRtoRpo": "string",
         "multiRegionRtoRpo": "string"
      },
      "assessmentStatus": "string",
      "associatedSystems": [
         {
            "systemArn": "string",
            "systemName": "string",
            "userJourneyIds": [ "string" ]
         }
      ],
      "createdAt": number,
      "dependencyDiscovery": {
         "eligibleResourceCount": number,
         "message": "string",
         "status": "string",
         "updatedAt": number
      },
      "description": "string",
      "effectivePolicyValues": {
         "availabilitySlo": {
            "policyName": "string",
            "source": "string",
            "value": number
         },
         "dataRecoveryTimeBetweenBackups": {
            "policyName": "string",
            "source": "string",
            "value": number
         },
         "multiAzDrApproach": {
            "policyName": "string",
            "source": "string",
            "value": "string"
         },
         "multiAzRpo": {
            "policyName": "string",
            "source": "string",
            "value": number
         },
         "multiAzRto": {
            "policyName": "string",
            "source": "string",
            "value": number
         },
         "multiRegionDrApproach": {
            "policyName": "string",
            "source": "string",
            "value": "string"
         },
         "multiRegionRpo": {
            "policyName": "string",
            "source": "string",
            "value": number
         },
         "multiRegionRto": {
            "policyName": "string",
            "source": "string",
            "value": number
         }
      },
      "estimatedAssessmentCost": {
         "amount": number,
         "currency": "string"
      },
      "kmsKeyId": "string",
      "name": "string",
      "openFindingsCount": number,
      "organizationId": "string",
      "ouId": "string",
      "permissionModel": {
         "crossAccountRoles": [
            {
               "crossAccountRoleArn": "string",
               "externalId": "string"
            }
         ],
         "invokerRoleName": "string"
      },
      "policyArn": "string",
      "regions": [ "string" ],
      "reportConfiguration": {
         "reportOutputs": [
            { ... }
         ]
      },
      "rerunAssessment": boolean,
      "resolvedFindingsCount": number,
      "resourceDiscovery": {
         "errorCode": "string",
         "errorMessage": "string",
         "lastRunAt": number,
         "status": "string"
      },
      "serviceArn": "string",
      "tags": {
         "string" : "string"
      },
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_CreateService_ResponseSyntax) **   <a name="ngresiliencehub-CreateService-response-service"></a>
The created service.
Type: [Service](API_Service.md) object

## Errors
<a name="API_CreateService_Errors"></a>

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
<a name="API_CreateService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateService)
