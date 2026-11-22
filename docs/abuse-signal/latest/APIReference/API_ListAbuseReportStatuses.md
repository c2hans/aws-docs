---
source_url: https://docs.aws.amazon.com/abuse-signal/latest/APIReference/API_ListAbuseReportStatuses.html
---

# ListAbuseReportStatuses

Lists abuse report statuses for the calling account, ordered by submission time, with optional filtering and pagination.

Use the `correlationId` parameter to filter results by the reporter-provided correlation ID that was specified during report submission.

Results are paginated. Use `nextToken` to retrieve additional results.

## Request Syntax
<a name="API_ListAbuseReportStatuses_RequestSyntax"></a>

```
GET /v1/abusestatuses?correlationId={{correlationId}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAbuseReportStatuses_RequestParameters"></a>

The request uses the following URI parameters.

 ** [correlationId](#API_ListAbuseReportStatuses_RequestSyntax) **   <a name="abusesignal-ListAbuseReportStatuses-request-uri-correlationId"></a>
Filters results by the reporter-provided correlation ID.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9-_]{1,256}`

 ** [maxResults](#API_ListAbuseReportStatuses_RequestSyntax) **   <a name="abusesignal-ListAbuseReportStatuses-request-uri-maxResults"></a>
The maximum number of results to return in a single page. Valid range: 1–50. The default is 50.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListAbuseReportStatuses_RequestSyntax) **   <a name="abusesignal-ListAbuseReportStatuses-request-uri-nextToken"></a>
The pagination token for retrieving the next page of results. Omit this parameter to return the first page of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x00-\x7F]+`

## Request Body
<a name="API_ListAbuseReportStatuses_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAbuseReportStatuses_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reports": [
      {
         "correlationId": "string",
         "description": "string",
         "reasonCode": "string",
         "reportId": "string",
         "status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAbuseReportStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListAbuseReportStatuses_ResponseSyntax) **   <a name="abusesignal-ListAbuseReportStatuses-response-nextToken"></a>
The pagination token for the next page of results. This value is `null` when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\x00-\x7F]+`

 ** [reports](#API_ListAbuseReportStatuses_ResponseSyntax) **   <a name="abusesignal-ListAbuseReportStatuses-response-reports"></a>
A list of abuse report status items. This list is empty when no reports are found for the calling account, or when no reports match the specified `correlationId` filter.
Type: Array of [ReportStatusListItem](API_ReportStatusListItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

## Errors
<a name="API_ListAbuseReportStatuses_Errors"></a>

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
<a name="API_ListAbuseReportStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/abuse-signal-2026-01-12/ListAbuseReportStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/abuse-signal-2026-01-12/ListAbuseReportStatuses)
