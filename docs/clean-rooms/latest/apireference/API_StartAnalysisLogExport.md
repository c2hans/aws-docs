---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_StartAnalysisLogExport.html
---

# StartAnalysisLogExport
<a name="API_StartAnalysisLogExport"></a>

Starts an export of the Apache Spark logs for a protected query to an Amazon S3 bucket that you own. Use the exported logs to diagnose a query that failed or that ran more slowly than you expected.

 AWS Clean Rooms exports a redacted copy of the Spark logs instead of the raw logs. Analyze the exported logs with the tooling of your choice, such as Spark History Server. For details about what the exported logs contain, see [https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html](https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs-contents.html).

The export runs asynchronously and returns with a `status` of `IN_PROGRESS`. Call `GetAnalysisLogExport` to poll for the final status.

**Important**
To use this operation, you must have the `CAN_EXPORT_QUERY_ANALYSIS_LOG` ability for your membership. You must also be the query runner or the query payer. Having the ability alone is not sufficient.
The query must have reached a terminal state, and it must have reached the execution stage. A query that failed validation or that was canceled before it started produces no Spark logs.
Log export isn't supported for queries that use differential privacy, and isn't supported for PySpark jobs.
The destination bucket must be in the same AWS Region as the collaboration. Cross-Region export isn't supported.

For more information, see [https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html](https://docs.aws.amazon.com/clean-rooms/latest/userguide/export-analysis-logs.html).

## Request Syntax
<a name="API_StartAnalysisLogExport_RequestSyntax"></a>

```
POST /memberships/{{membershipIdentifier}}/analysislogexports HTTP/1.1
Content-type: application/json

{
   "analysisId": "{{string}}",
   "analysisType": "{{string}}",
   "resultConfiguration": {
      "outputConfiguration": {
         "s3": {
            "bucket": "{{string}}",
            "keyPrefix": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_StartAnalysisLogExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [membershipIdentifier](#API_StartAnalysisLogExport_RequestSyntax) **   <a name="API-StartAnalysisLogExport-request-uri-membershipIdentifier"></a>
A unique identifier for the membership to export the analysis logs for. Currently accepts a membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_StartAnalysisLogExport_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analysisId](#API_StartAnalysisLogExport_RequestSyntax) **   <a name="API-StartAnalysisLogExport-request-analysisId"></a>
The unique identifier of the protected query that you want to export the analysis logs for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [analysisType](#API_StartAnalysisLogExport_RequestSyntax) **   <a name="API-StartAnalysisLogExport-request-analysisType"></a>
The type of analysis that the logs are exported for. Currently, only `PROTECTED_QUERY` is supported.
Type: String
Valid Values: `PROTECTED_QUERY`
Required: Yes

 ** [resultConfiguration](#API_StartAnalysisLogExport_RequestSyntax) **   <a name="API-StartAnalysisLogExport-request-resultConfiguration"></a>
The details needed to write the exported analysis logs.
You don't need to create an IAM role for log export. AWS Clean Rooms writes the exported logs using your own identity, so AWS Clean Rooms writes the exported logs only where your existing permissions allow.
Type: [AnalysisLogExportResultConfiguration](API_AnalysisLogExportResultConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_StartAnalysisLogExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "analysisLogExport": {
      "analysisId": "string",
      "analysisLogExportId": "string",
      "analysisType": "string",
      "createTime": number,
      "error": {
         "code": "string",
         "message": "string"
      },
      "membershipId": "string",
      "resultConfiguration": {
         "outputConfiguration": {
            "s3": {
               "bucket": "string",
               "keyPrefix": "string"
            }
         }
      },
      "status": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_StartAnalysisLogExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [analysisLogExport](#API_StartAnalysisLogExport_ResponseSyntax) **   <a name="API-StartAnalysisLogExport-response-analysisLogExport"></a>
The analysis log export that was started. The `status` is `IN_PROGRESS`.
Type: [AnalysisLogExport](API_AnalysisLogExport.md) object

## Errors
<a name="API_StartAnalysisLogExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request denied because service quota has been exceeded.
 ** quotaName **
The name of the quota.
 ** quotaValue **
The value of the quota.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_StartAnalysisLogExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/StartAnalysisLogExport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/StartAnalysisLogExport)
