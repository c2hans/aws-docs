---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_CreateAbuseReport.html
---

# CreateAbuseReport

Submits a structured report. AWS validates it and returns a report ID. A successful response confirms that AWS received your report. It doesn't mean that AWS has reached an outcome. Use [GetAbuseReportStatus](API_GetAbuseReportStatus.md) with the report ID to check the report's status and outcome.

## Request Syntax
<a name="API_CreateAbuseReport_RequestSyntax"></a>

```
POST /v1/abuse HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "correlationId": "{{string}}",
   "report": { ... }
}
```

## URI Request Parameters
<a name="API_CreateAbuseReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAbuseReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateAbuseReport_RequestSyntax) **   <a name="abusesignal-CreateAbuseReport-request-clientToken"></a>
An optional, client-provided idempotency token that ensures the operation completes no more than once. If the token matches a previous request within 24 hours, the service returns the existing report ID instead of creating a new report. When you omit this token, the service automatically generates one that is scoped to a 5-minute window.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]{1,128}`
Required: No

 ** [correlationId](#API_CreateAbuseReport_RequestSyntax) **   <a name="abusesignal-CreateAbuseReport-request-correlationId"></a>
An optional correlation ID for tracking the report in the reporter's system. The service echoes this value back in responses, and you can use it to filter reports with [ListAbuseReportStatuses](API_ListAbuseReportStatuses.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_]{1,256}`
Required: No

 ** [report](#API_CreateAbuseReport_RequestSyntax) **   <a name="abusesignal-CreateAbuseReport-request-report"></a>
The abuse report data in XARF format. Provide the report under the `xarf` key.
Type: [ReportData](API_ReportData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateAbuseReport_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "correlationId": "string",
   "reportId": "string"
}
```

## Response Elements
<a name="API_CreateAbuseReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [correlationId](#API_CreateAbuseReport_ResponseSyntax) **   <a name="abusesignal-CreateAbuseReport-response-correlationId"></a>
The correlation ID that you provided in the request, if any. The service echoes this value back in the response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_]{1,256}`

 ** [reportId](#API_CreateAbuseReport_ResponseSyntax) **   <a name="abusesignal-CreateAbuseReport-response-reportId"></a>
The unique identifier assigned to the submitted abuse report. Use this ID with [GetAbuseReportStatus](API_GetAbuseReportStatus.md) to track processing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-zA-Z0-9]{20,64}`

## Errors
<a name="API_CreateAbuseReport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller does not have sufficient access to perform this operation. Verify that the caller has the specific IAM permission for the operation it is calling (for example, `abuse:CreateAbuseReport`, `abuse:GetAbuseReportStatus`, or `abuse:ListAbuseReportStatuses`). Grant only the actions each caller requires.
 ** message **
A description of the access-denied error.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. For example, an idempotency token was reused with a different payload.
 ** message **
A description of the conflict.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request. This error is retryable; check the `Retry-After` header before you retry.
 ** message **
A description of the error.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request. The service also returns this value in the `Retry-After` HTTP header.
HTTP Status Code: 500

 ** SubmissionRequirementException **
The report is well-formed and satisfies the XARF schema, but it does not meet one or more submission requirements (for example, the submission lookback window or `source_identifier` restrictions). This error is distinct from `ValidationException` (HTTP 400), which indicates that the report is not well-formed. Retrying the same report will not succeed; the report content must change.
 ** message **
A summary of the unmet submission requirements.
 ** unmetRequirements **
A list of the specific submission requirements that the report did not meet.
HTTP Status Code: 422

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
<a name="API_CreateAbuseReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/abuse-signal-2026-01-12/CreateAbuseReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/CreateAbuseReport)
