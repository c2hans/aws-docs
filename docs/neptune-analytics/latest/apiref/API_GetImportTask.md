---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_GetImportTask.html
---

# GetImportTask
<a name="API_GetImportTask"></a>

Retrieves a specified import task.

## Request Syntax
<a name="API_GetImportTask_RequestSyntax"></a>

```
GET /importtasks/{{taskIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskIdentifier](#API_GetImportTask_RequestSyntax) **   <a name="neptunegraph-GetImportTask-request-uri-taskIdentifier"></a>
The unique identifier of the import task.
Pattern: `t-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_GetImportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attemptNumber": number,
   "format": "string",
   "graphId": "string",
   "importOptions": { ... },
   "importTaskDetails": {
      "dictionaryEntryCount": number,
      "errorCount": number,
      "errorDetails": "string",
      "progressPercentage": number,
      "startTime": number,
      "statementCount": number,
      "status": "string",
      "timeElapsedSeconds": number
   },
   "parquetType": "string",
   "roleArn": "string",
   "source": "string",
   "status": "string",
   "statusReason": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_GetImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attemptNumber](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-attemptNumber"></a>
The number of the current attempts to execute the import task.
Type: Integer

 ** [format](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) or `OPENCYPHER`, which identies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html).
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`

 ** [graphId](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-graphId"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [importOptions](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-importOptions"></a>
Contains options for controlling the import process. For example, if the `failOnError` key is set to `false`, the import skips problem data and attempts to continue (whereas if set to `true`, the default, or if omitted, the import operation halts immediately when an error is encountered.
Type: [ImportOptions](API_ImportOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [importTaskDetails](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-importTaskDetails"></a>
Contains details about the specified import task.
Type: [ImportTaskDetails](API_ImportTaskDetails.md) object

 ** [parquetType](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [source](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-source"></a>
A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot
Type: String

 ** [status](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-status"></a>
The status of the import task:
+  **INITIALIZING**   –   The necessary resources needed to create the graph are being prepared.
+  **ANALYZING\_DATA**   –   The data is being analyzed to determine the optimal infrastructure configuration for the new graph.
+  **RE\_PROVISIONING**   –   The data did not fit into the provisioned graph, so it is being re-provisioned with more capacity.
+  **IMPORTING**   –   The data is being loaded.
+  **ERROR\_ENCOUNTERED**   –   An error has been encountered while trying to create the graph and import the data.
+  **ERROR\_ENCOUNTERED\_ROLLING\_BACK**   –   Because of the error that was encountered, the graph is being rolled back and all its resources released.
+  **SUCCEEDED**   –   Graph creation and data loading succeeded.
+  **FAILED**   –   Graph creation or data loading failed. When the status is `FAILED`, you can use `get-graphs` to get more information about the state of the graph.
+  **CANCELLING**   –   Because you cancelled the import task, cancellation is in progress.
+  **CANCELLED**   –   You have successfully cancelled the import task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | ANALYZING_DATA | IMPORTING | REPROVISIONING | ROLLING_BACK | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [statusReason](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-statusReason"></a>
The reason that the import task has this status value.
Type: String

 ** [taskId](#API_GetImportTask_ResponseSyntax) **   <a name="neptunegraph-GetImportTask-response-taskId"></a>
The unique identifier of the import task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_GetImportTask_Errors"></a>

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
<a name="API_GetImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/GetImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/GetImportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
