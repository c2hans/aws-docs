---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphUsingImportTask.html
---

# CreateGraphUsingImportTask
<a name="API_CreateGraphUsingImportTask"></a>

Creates a new Neptune Analytics graph and imports data into it, either from Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune database snapshot.

The data can be loaded from files in S3 that in either the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html) or the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html).

## Request Syntax
<a name="API_CreateGraphUsingImportTask_RequestSyntax"></a>

```
POST /importtasks HTTP/1.1
Content-type: application/json

{
   "blankNodeHandling": "{{string}}",
   "deletionProtection": {{boolean}},
   "failOnError": {{boolean}},
   "format": "{{string}}",
   "graphName": "{{string}}",
   "importOptions": { ... },
   "kmsKeyIdentifier": "{{string}}",
   "maxProvisionedMemory": {{number}},
   "minProvisionedMemory": {{number}},
   "parquetType": "{{string}}",
   "publicConnectivity": {{boolean}},
   "replicaCount": {{number}},
   "roleArn": "{{string}}",
   "source": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vectorSearchConfiguration": {
      "dimension": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateGraphUsingImportTask_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGraphUsingImportTask_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blankNodeHandling](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-blankNodeHandling"></a>
The method to handle blank nodes in the dataset. Currently, only `convertToIri` is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is `ntriples`. For more information, see [Handling RDF values](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling).
Type: String
Valid Values: `convertToIri`
Required: No

 ** [deletionProtection](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-deletionProtection"></a>
Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (`true` or `false`).
Type: Boolean
Required: No

 ** [failOnError](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-failOnError"></a>
If set to `true`, the task halts when an import error is encountered. If set to `false`, the task skips the data that caused the error and continues if possible.
Type: Boolean
Required: No

 ** [format](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html), `OPEN_CYPHER`, which identifies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html), or `ntriples`, which identifies the [RDF n-triples](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html) format.
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`
Required: No

 ** [graphName](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-graphName"></a>
A name for the new Neptune Analytics graph to be created.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** [importOptions](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-importOptions"></a>
Contains options for controlling the import process. For example, if the `failOnError` key is set to `false`, the import skips problem data and attempts to continue (whereas if set to `true`, the default, or if omitted, the import operation halts immediately when an error is encountered.
Type: [ImportOptions](API_ImportOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [kmsKeyIdentifier](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-kmsKeyIdentifier"></a>
Specifies a KMS key to use to encrypt data imported into the new graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** [maxProvisionedMemory](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-maxProvisionedMemory"></a>
The maximum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 1024, or the approved upper limit for your account.
 If both the minimum and maximum values are specified, the final `provisioned-memory` will be chosen per the actual size of your imported data. If neither value is specified, 128 m-NCUs are used.
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: No

 ** [minProvisionedMemory](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-minProvisionedMemory"></a>
The minimum provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Default: 16
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: No

 ** [parquetType](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`
Required: No

 ** [publicConnectivity](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-publicConnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (`true` to enable, or `false` to disable).
Type: Boolean
Required: No

 ** [replicaCount](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-replicaCount"></a>
The number of replicas in other AZs to provision on the new graph after import. Default = 0, Min = 0, Max = 2.
 Additional charges equivalent to the m-NCUs selected for the graph apply for each replica.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** [roleArn](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`
Required: Yes

 ** [source](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-source"></a>
A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
Type: String
Required: Yes

 ** [tags](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-tags"></a>
Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vectorSearchConfiguration](#API_CreateGraphUsingImportTask_RequestSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-request-vectorSearchConfiguration"></a>
Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as `dimension=`value. Max = 65,535
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateGraphUsingImportTask_ResponseSyntax"></a>

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
<a name="API_CreateGraphUsingImportTask_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [format](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-format"></a>
Specifies the format of S3 data to be imported. Valid values are `CSV`, which identifies the [Gremlin CSV format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html), `OPENCYPHER`, which identifies the [openCypher load format](https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html), or `ntriples`, which identifies the [RDF n-triples](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html) format.
Type: String
Valid Values: `CSV | OPEN_CYPHER | PARQUET | NTRIPLES`

 ** [graphId](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-graphId"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [importOptions](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-importOptions"></a>
Contains options for controlling the import process. For example, if the `failOnError` key is set to `false`, the import skips problem data and attempts to continue (whereas if set to `true`, the default, or if omitted, the import operation halts immediately when an error is encountered.
Type: [ImportOptions](API_ImportOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [parquetType](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-parquetType"></a>
The parquet type of the import task.
Type: String
Valid Values: `COLUMNAR`

 ** [roleArn](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-roleArn"></a>
The ARN of the IAM role that will allow access to the data that is to be imported.
Type: String
Pattern: `arn:aws[^:]*:iam::\d{12}:(role|role/service-role)(/[\w+=,.@-]+)+`

 ** [source](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-source"></a>
A URL identifying to the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.
Type: String

 ** [status](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-status"></a>
The status of the import task.
Type: String
Valid Values: `INITIALIZING | EXPORTING | ANALYZING_DATA | IMPORTING | REPROVISIONING | ROLLING_BACK | SUCCEEDED | FAILED | CANCELLING | CANCELLED | DELETED`

 ** [taskId](#API_CreateGraphUsingImportTask_ResponseSyntax) **   <a name="neptunegraph-CreateGraphUsingImportTask-response-taskId"></a>
The unique identifier of the import task.
Type: String
Pattern: `t-[a-z0-9]{10}`

## Errors
<a name="API_CreateGraphUsingImportTask_Errors"></a>

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

 ** ServiceQuotaExceededException **
A service quota was exceeded.
 ** quotaCode **
Service quota code of the resource for which quota was exceeded.
 ** resourceId **
The identifier of the resource that exceeded quota.
 ** resourceType **
The type of the resource that exceeded quota. Ex: Graph, Snapshot
 ** serviceCode **
The service code that exceeded quota.
HTTP Status Code: 402

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
<a name="API_CreateGraphUsingImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CreateGraphUsingImportTask)
