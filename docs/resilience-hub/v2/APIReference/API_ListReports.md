---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListReports.html
---

# ListReports
<a name="API_ListReports"></a>

List reports for a service, or all reports owned by the account if serviceArn is not provided.

## Request Syntax
<a name="API_ListReports_RequestSyntax"></a>

```
GET /v2/list-reports?maxResults={{maxResults}}&nextToken={{nextToken}}&reportType={{reportType}}&serviceArn={{serviceArn}}&testRunId={{testRunId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListReports_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListReports_RequestSyntax) **   <a name="ngresiliencehub-ListReports-request-uri-maxResults"></a>
Pagination page size.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListReports_RequestSyntax) **   <a name="ngresiliencehub-ListReports-request-uri-nextToken"></a>
Pagination token.
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [reportType](#API_ListReports_RequestSyntax) **   <a name="ngresiliencehub-ListReports-request-uri-reportType"></a>
Filter reports by type.
Valid Values: `FAILURE_MODE | TESTING`

 ** [serviceArn](#API_ListReports_RequestSyntax) **   <a name="ngresiliencehub-ListReports-request-uri-serviceArn"></a>
Optional. If not provided, lists all reports owned by the account.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`

 ** [testRunId](#API_ListReports_RequestSyntax) **   <a name="ngresiliencehub-ListReports-request-uri-testRunId"></a>
The unique identifier of a test run.

## Request Body
<a name="API_ListReports_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListReports_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "reportGenerationResults": [
      {
         "assessmentId": "string",
         "createdAt": number,
         "reportOutput": { ... },
         "reportType": "string",
         "serviceArn": "string",
         "status": "string",
         "testRunId": "string",
         "testTemplateArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListReports_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListReports_ResponseSyntax) **   <a name="ngresiliencehub-ListReports-response-nextToken"></a>
Pagination token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Pattern: `\S{1,2000}`

 ** [reportGenerationResults](#API_ListReports_ResponseSyntax) **   <a name="ngresiliencehub-ListReports-response-reportGenerationResults"></a>
The list of report generation results.
Type: Array of [ReportGenerationResult](API_ReportGenerationResult.md) objects

## Errors
<a name="API_ListReports_Errors"></a>

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

 ** ThrottlingException **
Too many requests — rate limit exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListReports_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListReports)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListReports)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
