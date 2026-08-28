---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCase.html
---

# GetCase
<a name="API_GetCase"></a>

Returns the attributes of a case.

## Request Syntax
<a name="API_GetCase_RequestSyntax"></a>

```
GET /v1/cases/{{caseId}}/get-case HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_GetCase_RequestSyntax) **   <a name="securityir-GetCase-request-uri-caseId"></a>
Required element for GetCase to identify the requested case ID.
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

## Request Body
<a name="API_GetCase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actualIncidentStartDate": number,
   "caseArn": "string",
   "caseAttachments": [
      {
         "attachmentId": "string",
         "attachmentStatus": "string",
         "createdDate": number,
         "creator": "string",
         "fileName": "string"
      }
   ],
   "caseMetadata": [
      {
         "key": "string",
         "value": "string"
      }
   ],
   "caseStatus": "string",
   "closedDate": number,
   "closureCode": "string",
   "createdDate": number,
   "description": "string",
   "engagementType": "string",
   "impactedAccounts": [ "string" ],
   "impactedAwsRegions": [
      {
         "region": "string"
      }
   ],
   "impactedServices": [ "string" ],
   "lastUpdatedDate": number,
   "pendingAction": "string",
   "reportedIncidentStartDate": number,
   "resolverType": "string",
   "threatActorIpAddresses": [
      {
         "ipAddress": "string",
         "userAgent": "string"
      }
   ],
   "title": "string",
   "watchers": [
      {
         "email": "string",
         "jobTitle": "string",
         "name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actualIncidentStartDate](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-actualIncidentStartDate"></a>
Response element for GetCase that provides the actual incident start date as identified by data analysis during the investigation.
Type: Timestamp

 ** [caseArn](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-caseArn"></a>
Response element for GetCase that provides the case ARN
Type: String
Length Constraints: Minimum length of 12. Maximum length of 80.
Pattern: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:case/[0-9]{10}`

 ** [caseAttachments](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-caseAttachments"></a>
Response element for GetCase that provides a list of current case attachments.
Type: Array of [CaseAttachmentAttributes](API_CaseAttachmentAttributes.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [caseMetadata](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-caseMetadata"></a>
Case response metadata
Type: Array of [CaseMetadataEntry](API_CaseMetadataEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.

 ** [caseStatus](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-caseStatus"></a>
Response element for GetCase that provides the case status. Options for statuses include `Submitted | Detection and Analysis | Eradication, Containment and Recovery | Post-Incident Activities | Closed `
Type: String
Valid Values: `Submitted | Acknowledged | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities | Ready to Close | Closed`

 ** [closedDate](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-closedDate"></a>
Response element for GetCase that provides the date a specified case was closed.
Type: Timestamp

 ** [closureCode](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-closureCode"></a>
Response element for GetCase that provides the summary code for why a case was closed.
Type: String
Valid Values: `Investigation Completed | Not Resolved | False Positive | Duplicate`

 ** [createdDate](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-createdDate"></a>
Response element for GetCase that provides the date the case was created.
Type: Timestamp

 ** [description](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-description"></a>
Response element for GetCase that provides contents of the case description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.

 ** [engagementType](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-engagementType"></a>
Response element for GetCase that provides the engagement type. Options for engagement type include `Active Security Event | Investigations`
Type: String
Valid Values: `Security Incident | Investigation`

 ** [impactedAccounts](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-impactedAccounts"></a>
Response element for GetCase that provides a list of impacted accounts.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [impactedAwsRegions](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-impactedAwsRegions"></a>
Response element for GetCase that provides the impacted regions.
Type: Array of [ImpactedAwsRegion](API_ImpactedAwsRegion.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [impactedServices](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-impactedServices"></a>
Response element for GetCase that provides a list of impacted services.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 600 items.
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `[a-zA-Z0-9 -.():]+`

 ** [lastUpdatedDate](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-lastUpdatedDate"></a>
Response element for GetCase that provides the date a case was last modified.
Type: Timestamp

 ** [pendingAction](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-pendingAction"></a>
Response element for GetCase that identifies the case is waiting on customer input.
Type: String
Valid Values: `Customer | None`

 ** [reportedIncidentStartDate](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-reportedIncidentStartDate"></a>
Response element for GetCase that provides the customer provided incident start date.
Type: Timestamp

 ** [resolverType](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-resolverType"></a>
Response element for GetCase that provides the current resolver types.
Type: String
Valid Values: `AWS | Self`

 ** [threatActorIpAddresses](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-threatActorIpAddresses"></a>
Response element for GetCase that provides a list of suspicious IP addresses associated with unauthorized activity.
Type: Array of [ThreatActorIp](API_ThreatActorIp.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [title](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-title"></a>
Response element for GetCase that provides the case title.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [watchers](#API_GetCase_ResponseSyntax) **   <a name="securityir-GetCase-response-watchers"></a>
Response element for GetCase that provides a list of Watchers added to the case.
Type: Array of [Watcher](API_Watcher.md) objects
Array Members: Minimum number of 0 items. Maximum number of 30 items.

## Errors
<a name="API_GetCase_Errors"></a>

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
<a name="API_GetCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/GetCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/GetCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/GetCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/GetCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/GetCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/GetCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/GetCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
