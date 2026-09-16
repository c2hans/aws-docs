---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_StartExportTask.html
---

# StartExportTask
<a name="API_StartExportTask"></a>

Export data from an existing Neptune Analytics graph to Amazon S3. The graph state should be `AVAILABLE`.

## Request Syntax
<a name="API_StartExportTask_RequestSyntax"></a>

```
POST /exporttasks HTTP/1.1
Content-type: application/json

{
   "destination": "{{string}}",
   "exportFilter": {
      "edgeFilter": {
         "{{string}}" : {
            "properties": {
               "{{string}}" : {
                  "multiValueHandling": "{{string}}",
                  "outputType": "{{string}}",
                  "sourcePropertyName": "{{string}}"
               }
            }
         }
      },
      "vertexFilter": {
         "{{string}}" : {
            "properties": {
               "{{string}}" : {
                  "multiValueHandling": "{{string}}",
                  "outputType": "{{string}}",
                  "sourcePropertyName": "{{string}}"
               }
            }
         }
      }
   },
   "format": "{{string}}",
   "graphIdentifier": "{{string}}",
   "kmsKeyIdentifier": "{{string}}",
   "parquetType": "{{string}}",
   "roleArn": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartExportTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartExportTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destination](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-destination"></a>
The Amazon S3 URI where data will be exported to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [exportFilter](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-exportFilter"></a>
The export filter of the export task.
Type: [ExportFilter](API_ExportFilter.md) object
Required: No

 ** [format](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-format"></a>
The format of the export task.
Type: String
Valid Values: `PARQUET | CSV`
Required: Yes

 ** [graphIdentifier](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-graphIdentifier"></a>
The source graph identifier of the export task.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [kmsKeyIdentifier](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-kmsKeyIdentifier"></a>
The KMS key identifier of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: Yes

 ** [parquetType](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-parquetType"></a>
The parquet type of the export task.
Type: String
Valid Values: `COLUMNAR`
Required: No

 ** [roleArn](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-roleArn"></a>
The ARN of the IAM role that will allow data to be exported to the destination.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
Required: Yes

 ** [tags](#API_StartExportTask_RequestSyntax) **   <a name="neptunegraph-StartExportTask-request-tags"></a>
Tags to be applied to the export task.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartExportTask_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_StartExportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [destination](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-destination"></a>
The Amazon S3 URI of the export task where data will be exported to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [exportFilter](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-exportFilter"></a>
The export filter of the export task.
Type: [ExportFilter](API_ExportFilter.md) object

 ** [format](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-format"></a>
The format of the export task.
Type: String
Valid Values: `PARQUET | CSV`

 ** [graphId](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-graphId"></a>
The source graph identifier of the export task.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-kmsKeyIdentifier"></a>
The KMS key identifier of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [parquetType](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-parquetType"></a>
The parquet type of the export task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-roleArn"></a>
The ARN of the IAM role that will allow data to be exported to the destination.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [status](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-status"></a>
The current status of the export task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [statusReason](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-statusReason"></a>
The reason that the export task has this status value.
Type: String

 ** [taskId](#API_StartExportTask_ResponseSyntax) **   <a name="neptunegraph-StartExportTask-response-taskId"></a>
The unique identifier of the export task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_StartExportTask_Errors"></a>

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
<a name="API_StartExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/StartExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/StartExportTask)
