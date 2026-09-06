---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_ListExportTasks.html
---

# ListExportTasks
<a name="API_ListExportTasks"></a>

Retrieves a list of export tasks.

## Request Syntax
<a name="API_ListExportTasks_RequestSyntax"></a>

```
GET /exporttasks?graphIdentifier={{graphIdentifier}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListExportTasks_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_ListExportTasks_RequestSyntax) **   <a name="neptunegraph-ListExportTasks-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`

 ** [maxResults](#API_ListExportTasks_RequestSyntax) **   <a name="neptunegraph-ListExportTasks-request-uri-maxResults"></a>
The maximum number of export tasks to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListExportTasks_RequestSyntax) **   <a name="neptunegraph-ListExportTasks-request-uri-nextToken"></a>
Pagination token used to paginate input.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListExportTasks_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListExportTasks_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "tasks": [
      {
         "destination": "string",
         "format": "string",
         "graphId": "string",
         "kmsKeyIdentifier": "string",
         "parquetType": "string",
         "roleArn": "string",
         "status": "string",
         "statusReason": "string",
         "taskId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListExportTasks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListExportTasks_ResponseSyntax) **   <a name="neptunegraph-ListExportTasks-response-nextToken"></a>
Pagination token used to paginate output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [tasks](#API_ListExportTasks_ResponseSyntax) **   <a name="neptunegraph-ListExportTasks-response-tasks"></a>
The requested list of export tasks.
Type: Array of [ExportTaskSummary](API_ExportTaskSummary.md) objects

## Errors
<a name="API_ListExportTasks_Errors"></a>

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
<a name="API_ListExportTasks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/ListExportTasks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/ListExportTasks)
