---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_CreateReport.html
---

# CreateReport
<a name="API_CreateReport"></a>

On-demand report creation. Idempotent — duplicate requests with same clientToken return existing result.

## Request Syntax
<a name="API_CreateReport_RequestSyntax"></a>

```
POST /v2/create-report HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "reportType": "{{string}}",
   "serviceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateReport_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateReport_RequestSyntax) **   <a name="ngresiliencehub-CreateReport-request-clientToken"></a>
Idempotency token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[A-Za-z0-9_.-]{0,63}`
Required: No

 ** [reportType](#API_CreateReport_RequestSyntax) **   <a name="ngresiliencehub-CreateReport-request-reportType"></a>
The type of report to generate.
Type: String
Valid Values: `FAILURE_MODE | TESTING`
Required: Yes

 ** [serviceArn](#API_CreateReport_RequestSyntax) **   <a name="ngresiliencehub-CreateReport-request-serviceArn"></a>
ARN identifier.
Type: String
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_CreateReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "reportGenerationResult": {
      "assessmentId": "string",
      "createdAt": number,
      "reportOutput": { ... },
      "reportType": "string",
      "serviceArn": "string",
      "status": "string",
      "testRunId": "string",
      "testTemplateArn": "string"
   }
}
```

## Response Elements
<a name="API_CreateReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [reportGenerationResult](#API_CreateReport_ResponseSyntax) **   <a name="ngresiliencehub-CreateReport-response-reportGenerationResult"></a>
The result of the report generation request.
Type: [ReportGenerationResult](API_ReportGenerationResult.md) object

## Errors
<a name="API_CreateReport_Errors"></a>

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
<a name="API_CreateReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/CreateReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/CreateReport)
