---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CancelExportTask.html
---

# CancelExportTask
<a name="API_CancelExportTask"></a>

Cancel the specified export task.

## Request Syntax
<a name="API_CancelExportTask_RequestSyntax"></a>

```
DELETE /exporttasks/{{taskIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelExportTask_RequestParameters"></a>

The request uses the following URI parameters.

 ** [taskIdentifier](#API_CancelExportTask_RequestSyntax) **   <a name="neptunegraph-CancelExportTask-request-uri-taskIdentifier"></a>
The unique identifier of the export task.
Pattern: `t-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_CancelExportTask_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelExportTask_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements
<a name="API_CancelExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [destination](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-destination"></a>
The Amazon S3 URI of the cancelled export task where data will be exported to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [format](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-format"></a>
The format of the cancelled export task.
Type: String
Valid Values: `PARQUET | CSV`

 ** [graphId](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-graphId"></a>
The source graph identifier of the cancelled export task.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-kmsKeyIdentifier"></a>
The KMS key identifier of the cancelled export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [parquetType](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-parquetType"></a>
The parquet type of the cancelled export task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-roleArn"></a>
The ARN of the IAM role that will allow the exporting of data to the destination.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [status](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-status"></a>
The current status of the export task. The status is `CANCELLING` when the export task is cancelled.
Type: String
Valid Values: `INITIALIZING | EXPORTING | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [statusReason](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-statusReason"></a>
The reason that the export task has this status value.
Type: String

 ** [taskId](#API_CancelExportTask_ResponseSyntax) **   <a name="neptunegraph-CancelExportTask-response-taskId"></a>
The unique identifier of the export task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_CancelExportTask_Errors"></a>

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
<a name="API_CancelExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CancelExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CancelExportTask)
