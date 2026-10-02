---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetFindingMetrics.html
---

# GetFindingMetrics
<a name="API_GetFindingMetrics"></a>

Returns finding-lifecycle metrics for a membership over a specified date range. This read-only operation provides aggregate counts that describe how security findings progressed through the finding lifecycle, from ingestion through triage, investigation, and escalation, including false-positive, true-positive, and in-progress counts. The metrics are scoped to a single membership and to a day-aligned UTC date range.

## Request Syntax
<a name="API_GetFindingMetrics_RequestSyntax"></a>

```
GET /v1/membership/{{membershipId}}/finding-metrics?endDate={{endDate}}&startDate={{startDate}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFindingMetrics_RequestParameters"></a>

The request uses the following URI parameters.

 ** [endDate](#API_GetFindingMetrics_RequestSyntax) **   <a name="securityir-GetFindingMetrics-request-uri-endDate"></a>
The end of the date range to retrieve metrics for. This value is the end of a day-aligned UTC window and is inclusive.
Required: Yes

 ** [membershipId](#API_GetFindingMetrics_RequestSyntax) **   <a name="securityir-GetFindingMetrics-request-uri-membershipId"></a>
The unique identifier of the membership to retrieve finding-lifecycle metrics for.
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `m-[a-z0-9]{10,32}`
Required: Yes

 ** [startDate](#API_GetFindingMetrics_RequestSyntax) **   <a name="securityir-GetFindingMetrics-request-uri-startDate"></a>
The start of the date range to retrieve metrics for. This value is the beginning of a day-aligned UTC window and is inclusive.
Required: Yes

## Request Body
<a name="API_GetFindingMetrics_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFindingMetrics_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "findingsEscalated": number,
   "findingsEscalatedFalsePositive": number,
   "findingsEscalatedInProgress": number,
   "findingsIngestedGuardDuty": number,
   "findingsIngestedSecurityHub": number,
   "findingsInvestigated": number,
   "findingsInvestigatedFalsePositive": number,
   "findingsInvestigatedInProgress": number,
   "findingsTriaged": number,
   "findingsTriagedFalsePositive": number,
   "findingsTruePositive": number
}
```

## Response Elements
<a name="API_GetFindingMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [findingsEscalated](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsEscalated"></a>
The number of findings escalated during the requested date range.
Type: Long

 ** [findingsEscalatedFalsePositive](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsEscalatedFalsePositive"></a>
The number of escalated findings that were closed as false positives during the requested date range.
Type: Long

 ** [findingsEscalatedInProgress](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsEscalatedInProgress"></a>
The number of findings whose escalation was in progress during the requested date range.
Type: Long

 ** [findingsIngestedGuardDuty](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsIngestedGuardDuty"></a>
The number of findings ingested from Amazon GuardDuty during the requested date range.
Type: Long

 ** [findingsIngestedSecurityHub](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsIngestedSecurityHub"></a>
The number of findings ingested from AWS Security Hub during the requested date range.
Type: Long

 ** [findingsInvestigated](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsInvestigated"></a>
The number of findings investigated during the requested date range.
Type: Long

 ** [findingsInvestigatedFalsePositive](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsInvestigatedFalsePositive"></a>
The number of investigated findings that were closed as false positives during the requested date range.
Type: Long

 ** [findingsInvestigatedInProgress](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsInvestigatedInProgress"></a>
The number of findings whose investigation was in progress during the requested date range.
Type: Long

 ** [findingsTriaged](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsTriaged"></a>
The number of findings triaged during the requested date range.
Type: Long

 ** [findingsTriagedFalsePositive](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsTriagedFalsePositive"></a>
The number of triaged findings that were closed as false positives during the requested date range.
Type: Long

 ** [findingsTruePositive](#API_GetFindingMetrics_ResponseSyntax) **   <a name="securityir-GetFindingMetrics-response-findingsTruePositive"></a>
The number of findings confirmed as true positives during the requested date range.
Type: Long

## Errors
<a name="API_GetFindingMetrics_Errors"></a>

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
<a name="API_GetFindingMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/security-ir-2018-05-10/GetFindingMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetFindingMetrics)
