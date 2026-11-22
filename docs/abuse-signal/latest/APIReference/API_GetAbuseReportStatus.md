---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_GetAbuseReportStatus.html
---

# GetAbuseReportStatus

Retrieves the current processing status of a previously submitted abuse report, including the status, submission timestamp, and last-update time.

You can poll this operation to track the report's status. `PROCESSING` confirms that AWS received your report and is processing it. `COMPLETED` means AWS finished resolving the report, and the response includes a `reasonCode`. The time to reach `COMPLETED` varies and can take up to several days, depending on the scope and complexity of the suspected abuse.

**Note**
 `COMPLETED` is the only terminal status. To wait for a report, use the `ReportProcessing` waiter, which succeeds when the report reaches `PROCESSING` or `COMPLETED`. If you poll this operation yourself, wait 1–5 seconds between calls.

## Request Syntax
<a name="API_GetAbuseReportStatus_RequestSyntax"></a>

```
GET /v1/abuse/{{reportId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAbuseReportStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reportId](#API_GetAbuseReportStatus_RequestSyntax) **   <a name="abusesignal-GetAbuseReportStatus-request-uri-reportId"></a>
The unique identifier of the abuse report to retrieve status for. This is the `reportId` that is returned by [CreateAbuseReport](API_CreateAbuseReport.md).
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-zA-Z0-9]{20,64}`
Required: Yes

## Request Body
<a name="API_GetAbuseReportStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAbuseReportStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "correlationId": "string",
   "description": "string",
   "lastUpdatedAt": number,
   "reasonCode": "string",
   "reportId": "string",
   "status": "string",
   "submittedAt": number
}
```

## Response Elements
<a name="API_GetAbuseReportStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [correlationId](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-correlationId"></a>
The reporter-provided correlation ID for cross-referencing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_]{1,256}`

 ** [description](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-description"></a>
A human-readable description of the current status.
Type: String

 ** [lastUpdatedAt](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-lastUpdatedAt"></a>
The date and time when the status was last updated.
Type: Timestamp

 ** [reasonCode](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-reasonCode"></a>
A code that explains the resolution outcome. This value is returned only after the report reaches the terminal `COMPLETED` status; it is absent while the report is `QUEUED` or `PROCESSING`. Treat an unrecognized value as opaque, because the set of reason codes is append-only.
Type: String
Valid Values: `ACTIONED | NOT_RESOLVABLE_TO_AWS | REVIEWED_NO_AWS_ACTION | CONTENT_DOWN_OR_INACCESSIBLE | NEED_MORE_INFORMATION`

 ** [reportId](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-reportId"></a>
The unique identifier of the abuse report.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-zA-Z0-9]{20,64}`

 ** [status](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-status"></a>
The current processing status of the abuse report. Valid values are `QUEUED` (the report has been received and queued for processing), `PROCESSING` (the report has been received and is being processed), and `COMPLETED` (the report has been processed).
Type: String
Valid Values: `QUEUED | PROCESSING | COMPLETED`

 ** [submittedAt](#API_GetAbuseReportStatus_ResponseSyntax) **   <a name="abusesignal-GetAbuseReportStatus-response-submittedAt"></a>
The date and time when the abuse report was submitted.
Type: Timestamp

## Errors
<a name="API_GetAbuseReportStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have sufficient access to perform this operation. Verify that the caller has the specific IAM permission for the operation it is calling (for example, `abuse:CreateAbuseReport`, `abuse:GetAbuseReportStatus`, or `abuse:ListAbuseReportStatuses`). Grant only the actions each caller requires.
 ** message **
A description of the access-denied error.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request. This error is retryable; check the `Retry-After` header before you retry.
 ** message **
A description of the error.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request. The service also returns this value in the `Retry-After` HTTP header.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the `reportId` is correct.
 ** message **
A description of the error.
 ** resourceId **
The identifier of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. This error is retryable; retry with exponential backoff.
 ** message **
A description of the throttling error.
 ** quotaCode **
The code for the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request. The service also returns this value in the `Retry-After` HTTP header.
 ** serviceCode **
The code for the AWS service that is associated with the quota that was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service, which indicates that the request is not well-formed. Check `fieldList` for the specific members that failed validation.
 ** fieldList **
A list of the specific input fields that failed validation.
 ** message **
A summary of the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_GetAbuseReportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/abuse-signal-2026-01-12/GetAbuseReportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/GetAbuseReportStatus)
