---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelImportTask.html
---

# CancelImportTask
<a name="API_CancelImportTask"></a>

Deletes the specified import task.

## Request Syntax
<a name="API_CancelImportTask_RequestSyntax"></a>

```
DELETE /importtasks/{{taskIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskIdentifier](#API_CancelImportTask_RequestSyntax) **   <a name="neptunegraph-CancelImportTask-request-uri-taskIdentifier"></a>
The unique identifier of the import task.
Pattern: `t-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_CancelImportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelImportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "format": "string",
   "graphId": "string",
   "parquetType": "string",
   "roleArn": "string",
   "source": "string",
   "status": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_CancelImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [format](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) or `OPENCYPHER`, which identies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html).
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`

 ** [graphId](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-graphId"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [parquetType](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-parquetType"></a>
The parquet type of the cancelled import task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [source](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-source"></a>
A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
Type: String

 ** [status](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-status"></a>
Current status of the task. Status is CANCELLING when the import task is cancelled.
Type: String
Valid Values: `INITIALIZING | EXPORTING | ANALYZING_DATA | IMPORTING | REPROVISIONING | ROLLING_BACK | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [taskId](#API_CancelImportTask_ResponseSyntax) **   <a name="neptunegraph-CancelImportTask-response-taskId"></a>
The unique identifier of the import task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_CancelImportTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Raised when a conflict is encountered.
 ** message **
A message describing the problem.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

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
<a name="API_CancelImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CancelImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CancelImportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
