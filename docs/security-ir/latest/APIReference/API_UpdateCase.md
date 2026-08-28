---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCase.html
---

# UpdateCase
<a name="API_UpdateCase"></a>

Updates an existing case.

## Request Syntax
<a name="API_UpdateCase_RequestSyntax"></a>

```
POST /v1/cases/{{caseId}}/update-case HTTP/1.1
Content-type: application/json

{
   "actualIncidentStartDate": {{number}},
   "caseMetadata": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "engagementType": "{{string}}",
   "impactedAccountsToAdd": [ "{{string}}" ],
   "impactedAccountsToDelete": [ "{{string}}" ],
   "impactedAwsRegionsToAdd": [
      {
         "region": "{{string}}"
      }
   ],
   "impactedAwsRegionsToDelete": [
      {
         "region": "{{string}}"
      }
   ],
   "impactedServicesToAdd": [ "{{string}}" ],
   "impactedServicesToDelete": [ "{{string}}" ],
   "reportedIncidentStartDate": {{number}},
   "threatActorIpAddressesToAdd": [
      {
         "ipAddress": "{{string}}",
         "userAgent": "{{string}}"
      }
   ],
   "threatActorIpAddressesToDelete": [
      {
         "ipAddress": "{{string}}",
         "userAgent": "{{string}}"
      }
   ],
   "title": "{{string}}",
   "watchersToAdd": [
      {
         "email": "{{string}}",
         "jobTitle": "{{string}}",
         "name": "{{string}}"
      }
   ],
   "watchersToDelete": [
      {
         "email": "{{string}}",
         "jobTitle": "{{string}}",
         "name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-uri-caseId"></a>
Required element for UpdateCase to identify the case ID for updates.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_UpdateCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actualIncidentStartDate](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-actualIncidentStartDate"></a>
Optional element for UpdateCase to provide content for the incident start date field.
Type: Timestamp
Required: No

 ** [caseMetadata](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-caseMetadata"></a>
Metadata entries to update for the case. This allows you to modify custom key-value pairs associated with the case for organizational and tracking purposes.
Type: Array of [CaseMetadataEntry](API_CaseMetadataEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: No

 ** [description](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-description"></a>
Optional element for UpdateCase to provide content for the description field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Required: No

 ** [engagementType](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-engagementType"></a>
Optional element for UpdateCase to provide content for the engagement type field. `Available engagement types include Security Incident | Investigation`.
Type: String
Valid Values: `Security Incident | Investigation`
Required: No

 ** [impactedAccountsToAdd](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedAccountsToAdd"></a>
Optional element for UpdateCase to provide content to add accounts impacted.
 AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be `123123123` which is nine digits, and with zero-prepend would be `000123123123`. Not zero-prepending to 12 digits could result in errors.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [impactedAccountsToDelete](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedAccountsToDelete"></a>
Optional element for UpdateCase to provide content to add accounts impacted.
 AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be `123123123` which is nine digits, and with zero-prepend would be `000123123123`. Not zero-prepending to 12 digits could result in errors.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** [impactedAwsRegionsToAdd](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedAwsRegionsToAdd"></a>
Optional element for UpdateCase to provide content to add regions impacted.
Type: Array of [ImpactedAwsRegion](API_ImpactedAwsRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [impactedAwsRegionsToDelete](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedAwsRegionsToDelete"></a>
Optional element for UpdateCase to provide content to remove regions impacted.
Type: Array of [ImpactedAwsRegion](API_ImpactedAwsRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [impactedServicesToAdd](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedServicesToAdd"></a>
Optional element for UpdateCase to provide content to add services impacted.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 600 items.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-zA-Z0-9 -.():]+`
Required: No

 ** [impactedServicesToDelete](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-impactedServicesToDelete"></a>
Optional element for UpdateCase to provide content to remove services impacted.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 600 items.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-zA-Z0-9 -.():]+`
Required: No

 ** [reportedIncidentStartDate](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-reportedIncidentStartDate"></a>
Optional element for UpdateCase to provide content for the customer reported incident start date field.
Type: Timestamp
Required: No

 ** [threatActorIpAddressesToAdd](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-threatActorIpAddressesToAdd"></a>
Optional element for UpdateCase to provide content to add additional suspicious IP addresses related to a case.
Type: Array of [ThreatActorIp](API_ThreatActorIp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** [threatActorIpAddressesToDelete](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-threatActorIpAddressesToDelete"></a>
Optional element for UpdateCase to provide content to remove suspicious IP addresses from a case.
Type: Array of [ThreatActorIp](API_ThreatActorIp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** [title](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-title"></a>
Optional element for UpdateCase to provide content for the title field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

 ** [watchersToAdd](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-watchersToAdd"></a>
Optional element for UpdateCase to provide content to add additional watchers to a case.
Type: Array of [Watcher](API_Watcher.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

 ** [watchersToDelete](#API_UpdateCase_RequestSyntax) **   <a name="securityir-UpdateCase-request-watchersToDelete"></a>
Optional element for UpdateCase to provide content to remove existing watchers from a case.
Type: Array of [Watcher](API_Watcher.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: No

## Response Syntax
<a name="API_UpdateCase_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** message **
The ID of the resource which lead to the access denial.
HTTP Status Code: 403

 ** ConflictException **
Returned when there is a conflict with the current state of the resource.
For UpdateResolverType, this error may occur when attempting to change an AWS-supported case to Self-managed, which is not supported.
 ** message **
The exception message.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **

 ** message **
The exception message.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
HTTP Status Code: 500

 ** InvalidTokenException **

 ** message **
The exception message.
HTTP Status Code: 423

 ** ResourceNotFoundException **

 ** message **
The exception message.
HTTP Status Code: 404

 ** SecurityIncidentResponseNotActiveException **

 ** message **
The exception message.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

 ** message **
The exception message.
 ** quotaCode **
The code of the quota.
 ** resourceId **
The ID of the requested resource which lead to the service quota exception.
 ** resourceType **
The type of the requested resource which lead to the service quota exception.
 ** serviceCode **
The service code of the quota.
HTTP Status Code: 402

 ** ThrottlingException **

 ** message **
The exception message.
 ** quotaCode **
The quota code of the exception.
 ** retryAfterSeconds **
The number of seconds after which to retry the request.
 ** serviceCode **
The service code of the exception.
HTTP Status Code: 429

 ** ValidationException **
Returned when the request contains invalid parameters.
For UpdateResolverType, this error may occur when attempting an unsupported resolver type transition.
 ** fieldList **
The fields which lead to the exception.
 ** message **
The exception message.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/UpdateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/UpdateCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
