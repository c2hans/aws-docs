---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ImportApp.html
---

# ImportApp
<a name="API_ImportApp"></a>

Imports a V1 app into the V2 resource model, creating a service with the same name.

## Request Syntax
<a name="API_ImportApp_RequestSyntax"></a>

```
POST /v2/import-app HTTP/1.1
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
   "kmsKeyId": "{{string}}",
   "policyArn": "{{string}}",
   "skipManuallyAddedResources": {{boolean}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "v1AppArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ImportApp_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ImportApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatedSystems](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-associatedSystems"></a>
The systems to associate with the imported service.
Type: Array of [AssociatedSystem](API_AssociatedSystem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [clientToken](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [kmsKeyId](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-kmsKeyId"></a>
KMS key identifier — accepts key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [policyArn](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-policyArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: No

 ** [skipManuallyAddedResources](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-skipManuallyAddedResources"></a>
Whether to skip manually added resources during import.
Type: Boolean
Required: No

 ** [tags](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`
Required: No

 ** [v1AppArn](#API_ImportApp_RequestSyntax) **   <a name="ngresiliencehub-ImportApp-request-v1AppArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_ImportApp_ResponseSyntax"></a>

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
<a name="API_ImportApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [service](#API_ImportApp_ResponseSyntax) **   <a name="ngresiliencehub-ImportApp-response-service"></a>
The imported service.
Type: [Service](API_Service.md) object

## Errors
<a name="API_ImportApp_Errors"></a>

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
<a name="API_ImportApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ImportApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ImportApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
