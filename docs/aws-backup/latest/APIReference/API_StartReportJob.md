---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_StartReportJob.html
---

# StartReportJob
<a name="API_StartReportJob"></a>

Starts an on-demand report job for the specified report plan.

## Request Syntax
<a name="API_StartReportJob_RequestSyntax"></a>

```
POST /audit/report-jobs/{{reportPlanName}} HTTP/1.1
Content-type: application/json

{
   "IdempotencyToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartReportJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [reportPlanName](#API_StartReportJob_RequestSyntax) **   <a name="Backup-StartReportJob-request-uri-ReportPlanName"></a>
The unique name of a report plan.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z][_a-zA-Z0-9]*`
Required: Yes

## Request Body
<a name="API_StartReportJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdempotencyToken](#API_StartReportJob_RequestSyntax) **   <a name="Backup-StartReportJob-request-IdempotencyToken"></a>
A customer-chosen string that you can use to distinguish between otherwise identical calls to `StartReportJobInput`. Retrying a successful request with the same idempotency token results in a success message with no action taken.
Type: String
Required: No

## Response Syntax
<a name="API_StartReportJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ReportJobId": "string"
}
```

## Response Elements
<a name="API_StartReportJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ReportJobId](#API_StartReportJob_ResponseSyntax) **   <a name="Backup-StartReportJob-response-ReportJobId"></a>
The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded string that is at most 1,024 bytes long. The report job ID cannot be edited.
Type: String

## Errors
<a name="API_StartReportJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
Indicates that something is wrong with a parameter's value. For example, the value is out of range.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** MissingParameterValueException **
Indicates that a required parameter is missing.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
 ** Context **

 ** Type **

HTTP Status Code: 400

 ** ServiceUnavailableException **
The request failed due to a temporary failure of the server.
 ** Context **

 ** Type **

HTTP Status Code: 500

## See Also
<a name="API_StartReportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-2018-11-15/StartReportJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-2018-11-15/StartReportJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/StartReportJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-2018-11-15/StartReportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/StartReportJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-2018-11-15/StartReportJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-2018-11-15/StartReportJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-2018-11-15/StartReportJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-2018-11-15/StartReportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/StartReportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
