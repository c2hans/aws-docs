---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartImportTask.html
---

# StartImportTask
<a name="API_StartImportTask"></a>

Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3). The graph needs to be empty and in the AVAILABLE state.

## Request Syntax
<a name="API_StartImportTask_RequestSyntax"></a>

```
POST /graphs/{{graphIdentifier}}/importtasks HTTP/1.1
Content-type: application/json

{
   "blankNodeHandling": "{{string}}",
   "failOnError": {{boolean}},
   "format": "{{string}}",
   "importOptions": { ... },
   "parquetType": "{{string}}",
   "roleArn": "{{string}}",
   "source": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StartImportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_StartImportTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blankNodeHandling](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-blankNodeHandling"></a>
The method to handle blank nodes in the dataset. Currently, only `convertToIri` is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is `ntriples`. For more information, see [Handling RDF values](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling).
Type: String
Valid Values: `convertToIri`
Required: No

 ** [failOnError](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-failOnError"></a>
If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.
Type: Boolean
Required: No

 ** [format](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-format"></a>
Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identies the openCypher load format.
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`
Required: No

 ** [importOptions](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-importOptions"></a>
Options for how to perform an import.
Type: [ImportOptions](API_ImportOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [parquetType](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`
Required: No

 ** [roleArn](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
Required: Yes

 ** [source](#API_StartImportTask_RequestSyntax) **   <a name="neptunegraph-StartImportTask-request-source"></a>
A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
Type: String
Required: Yes

## Response Syntax
<a name="API_StartImportTask_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "format": "string",
   "graphId": "string",
   "importOptions": { ... },
   "parquetType": "string",
   "roleArn": "string",
   "source": "string",
   "status": "string",
   "taskId": "string"
}
```

## Response Elements
<a name="API_StartImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [format](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-format"></a>
Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identies the openCypher load format.
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`

 ** [graphId](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-graphId"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [importOptions](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-importOptions"></a>
Options for how to perform an import.
Type: [ImportOptions](API_ImportOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [parquetType](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [source](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-source"></a>
A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
Type: String

 ** [status](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-status"></a>
The status of the import task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | ANALYZING_DATA | IMPORTING | REPROVISIONING | ROLLING_BACK | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [taskId](#API_StartImportTask_ResponseSyntax) **   <a name="neptunegraph-StartImportTask-response-taskId"></a>
The unique identifier of the import task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_StartImportTask_Errors"></a>

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
<a name="API_StartImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/StartImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/StartImportTask)
