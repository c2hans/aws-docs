---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetExportTask.html
---

# GetExportTask
<a name="API_GetExportTask"></a>

Retrieves a specified export task.

## Request Syntax
<a name="API_GetExportTask_RequestSyntax"></a>

```
GET /exporttasks/{{taskIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetExportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskIdentifier](#API_GetExportTask_RequestSyntax) **   <a name="neptunegraph-GetExportTask-request-uri-taskIdentifier"></a>
The unique identifier of the export task.
Pattern: `t-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_GetExportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "destination": "string",
   "exportFilter": {
      "edgeFilter": {
         "string" : {
            "properties": {
               "string" : {
                  "multiValueHandling": "string",
                  "outputType": "string",
                  "sourcePropertyName": "string"
               }
            }
         }
      },
      "vertexFilter": {
         "string" : {
            "properties": {
               "string" : {
                  "multiValueHandling": "string",
                  "outputType": "string",
                  "sourcePropertyName": "string"
               }
            }
         }
      }
   },
   "exportTaskDetails": {
      "numEdgesWritten": number,
      "numVerticesWritten": number,
      "progressPercentage": number,
      "startTime": number,
      "timeElapsedSeconds": number
   },
   "format": "string",
   "graphId": "string",
   "kmsKeyIdentifier": "string",
   "parquetType": "string",
   "roleArn": "string",
   "status": "string",
   "statusReason": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_GetExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destination](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-destination"></a>
The Amazon S3 URI of the export task where data will be exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [exportFilter](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-exportFilter"></a>
The export filter of the export task.
Type: [ExportFilter](API_ExportFilter.md) object

 ** [exportTaskDetails](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-exportTaskDetails"></a>
The details of the export task.
Type: [ExportTaskDetails](API_ExportTaskDetails.md) object

 ** [format](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-format"></a>
The format of the export task.
Type: String
Valid Values: `PARQUET | CSV`

 ** [graphId](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-graphId"></a>
The source graph identifier of the export task.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-kmsKeyIdentifier"></a>
The KMS key identifier of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [parquetType](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-parquetType"></a>
The parquet type of the export task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-roleArn"></a>
The ARN of the IAM role that will allow data to be exported to the destination.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [status](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-status"></a>
The current status of the export task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [statusReason](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-statusReason"></a>
The reason that the export task has this status value.
Type: String

 ** [taskId](#API_GetExportTask_ResponseSyntax) **   <a name="neptunegraph-GetExportTask-response-taskId"></a>
The unique identifier of the export task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_GetExportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
A failure occurred on the server.
 ** message **
A message describing the problem.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A specified resource could not be located.
 ** message **
A message describing the problem.
HTTP Status Code: 404

 ** ThrottlingException **
The exception was interrupted by throttling.
 ** message **
A message describing the problem.
HTTP Status Code: 429

 ** ValidationException **
A resource could not be validated.
 ** message **
A message describing the problem.
 ** reason **
The reason that the resource could not be validated.
HTTP Status Code: 400

## See Also
<a name="API_GetExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/GetExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GetExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
