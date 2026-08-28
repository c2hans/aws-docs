---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateCase.html
---

# CreateCase
<a name="API_CreateCase"></a>

Creates a new case.

## Request Syntax
<a name="API_CreateCase_RequestSyntax"></a>

```
POST /v1/create-case HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "engagementType": "{{string}}",
   "impactedAccounts": [ "{{string}}" ],
   "impactedAwsRegions": [
      {
         "region": "{{string}}"
      }
   ],
   "impactedServices": [ "{{string}}" ],
   "reportedIncidentStartDate": {{number}},
   "resolverType": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "threatActorIpAddresses": [
      {
         "ipAddress": "{{string}}",
         "userAgent": "{{string}}"
      }
   ],
   "title": "{{string}}",
   "watchers": [
      {
         "email": "{{string}}",
         "jobTitle": "{{string}}",
         "name": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCase_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-clientToken"></a>
The `clientToken` field is an idempotency key used to ensure that repeated attempts for a single action will be ignored by the server during retries. A caller supplied unique ID (typically a UUID) should be provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [description](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-description"></a>
Required element used in combination with CreateCase
to provide a description for the new case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.
Required: Yes

 ** [engagementType](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-engagementType"></a>
Required element used in combination with CreateCase to provide an engagement type for the new cases. Available engagement types include Security Incident \| Investigation
Type: String
Valid Values: `Security Incident | Investigation`
Required: Yes

 ** [impactedAccounts](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-impactedAccounts"></a>
Required element used in combination with CreateCase to provide a list of impacted accounts.
 AWS account ID's may appear less than 12 characters and need to be zero-prepended. An example would be `123123123` which is nine digits, and with zero-prepend would be `000123123123`. Not zero-prepending to 12 digits could result in errors.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** [impactedAwsRegions](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-impactedAwsRegions"></a>
An optional element used in combination with CreateCase to provide a list of impacted regions.
Type: Array of [ImpactedAwsRegion](API_ImpactedAwsRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [impactedServices](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-impactedServices"></a>
An optional element used in combination with CreateCase to provide a list of services impacted.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 600 items.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-zA-Z0-9 -.():]+`
Required: No

 ** [reportedIncidentStartDate](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-reportedIncidentStartDate"></a>
Required element used in combination with CreateCase to provide an initial start date for the unauthorized activity.
Type: Timestamp
Required: Yes

 ** [resolverType](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-resolverType"></a>
Required element used in combination with CreateCase to identify the resolver type.
Type: String
Valid Values: `AWS | Self`
Required: Yes

 ** [tags](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-tags"></a>
An optional element used in combination with CreateCase to add customer specified tags to a case.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [threatActorIpAddresses](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-threatActorIpAddresses"></a>
An optional element used in combination with CreateCase to provide a list of suspicious internet protocol addresses associated with unauthorized activity.
Type: Array of [ThreatActorIp](API_ThreatActorIp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Required: No

 ** [title](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-title"></a>
Required element used in combination with CreateCase to provide a title for the new case.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [watchers](#API_CreateCase_RequestSyntax) **   <a name="securityir-CreateCase-request-watchers"></a>
Required element used in combination with CreateCase to provide a list of entities to receive notifications for case updates.
Type: Array of [Watcher](API_Watcher.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Required: Yes

## Response Syntax
<a name="API_CreateCase_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "caseId": "string"
}
```

## Response Elements
<a name="API_CreateCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [caseId](#API_CreateCase_ResponseSyntax) **   <a name="securityir-CreateCase-response-caseId"></a>
A response element providing responses for requests to CreateCase. This element responds with the case ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`

## Errors
<a name="API_CreateCase_Errors"></a>

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
<a name="API_CreateCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/CreateCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/CreateCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
