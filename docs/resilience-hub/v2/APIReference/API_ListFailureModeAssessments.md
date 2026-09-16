---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListFailureModeAssessments.html
---

# ListFailureModeAssessments
<a name="API_ListFailureModeAssessments"></a>

Lists failure mode assessments.

## Request Syntax
<a name="API_ListFailureModeAssessments_RequestSyntax"></a>

```
GET /v2/list-failure-mode-assessments?assessmentStatuses={{assessmentStatuses}}&endedBefore={{endedBefore}}&maxResults={{maxResults}}&nextToken={{nextToken}}&serviceArn={{serviceArn}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&startedAfter={{startedAfter}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFailureModeAssessments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assessmentStatuses](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-assessmentStatuses"></a>
Specifies the assessment statuses to include in the results.
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Valid Values: `NOT_STARTED | PENDING | IN_PROGRESS | FAILED | SUCCESS`

 ** [endedBefore](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-endedBefore"></a>
Specifies that only assessments that ended at or before this timestamp appear in the results.

 ** [maxResults](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [serviceArn](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-serviceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

 ** [sortBy](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-sortBy"></a>
The field to use for sorting failure mode assessments.
Valid Values: `STARTED_AT`

 ** [sortOrder](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-sortOrder"></a>
The sort order for results.
Valid Values: `ASC | DESC`

 ** [startedAfter](#API_ListFailureModeAssessments_RequestSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-request-uri-startedAfter"></a>
Specifies that only assessments that started at or after this timestamp appear in the results.

## Request Body
<a name="API_ListFailureModeAssessments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFailureModeAssessments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentSummaries": [
      {
         "achievability": {
            "availabilitySlo": "string",
            "dataRecoveryTimeBetweenBackups": "string",
            "multiAzRtoRpo": "string",
            "multiRegionRtoRpo": "string"
         },
         "assessmentCost": {
            "amount": number,
            "currency": "string"
         },
         "assessmentId": "string",
         "assessmentStatus": "string",
         "assessmentStep": "string",
         "billableAssessmentUnitCount": number,
         "endedAt": number,
         "errorCode": "string",
         "errorMessage": "string",
         "serviceArn": "string",
         "startedAt": number,
         "totalFindings": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListFailureModeAssessments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentSummaries](#API_ListFailureModeAssessments_ResponseSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-response-assessmentSummaries"></a>
The list of assessment summaries.
Type: Array of [AssessmentSummary](API_AssessmentSummary.md) objects

 ** [nextToken](#API_ListFailureModeAssessments_ResponseSyntax) **   <a name="ngresiliencehub-ListFailureModeAssessments-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListFailureModeAssessments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

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
<a name="API_ListFailureModeAssessments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListFailureModeAssessments)
