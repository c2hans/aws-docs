---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraph.html
---

# DeleteGraph
<a name="API_DeleteGraph"></a>

Deletes the specified graph. Graphs cannot be deleted if delete-protection is enabled.

## Request Syntax
<a name="API_DeleteGraph_RequestSyntax"></a>

```
DELETE /graphs/{{graphIdentifier}}?skipSnapshot={{skipSnapshot}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGraph_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_DeleteGraph_RequestSyntax) **   <a name="neptunegraph-DeleteGraph-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [skipSnapshot](#API_DeleteGraph_RequestSyntax) **   <a name="neptunegraph-DeleteGraph-request-uri-skipSnapshot"></a>
Determines whether a final graph snapshot is created before the graph is deleted. If `true` is specified, no graph snapshot is created. If `false` is specified, a graph snapshot is created before the graph is deleted.
Required: Yes

## Request Body
<a name="API_DeleteGraph_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGraph_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "buildNumber": "string",
   "createTime": number,
   "deletionProtection": boolean,
   "endpoint": "string",
   "id": "string",
   "kmsKeyIdentifier": "string",
   "name": "string",
   "provisionedMemory": number,
   "publicConnectivity": boolean,
   "replicaCount": number,
   "sourceSnapshotId": "string",
   "status": "string",
   "statusReason": "string",
   "vectorSearchConfiguration": {
      "dimension": number
   }
}
```

## Response Elements
<a name="API_DeleteGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-arn"></a>
The ARN associated with the graph.
Type: String

 ** [buildNumber](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-buildNumber"></a>
The build number associated with the graph.
Type: String

 ** [createTime](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-createTime"></a>
The time at which the graph was created.
Type: Timestamp

 ** [deletionProtection](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-deletionProtection"></a>
If `true`, deletion protection was enabled for the graph.
Type: Boolean

 ** [endpoint](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-endpoint"></a>
The graph endpoint.
Type: String

 ** [id](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-id"></a>
The unique identifier of the graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt graph data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-name"></a>
The name of the graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [provisionedMemory](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-provisionedMemory"></a>
The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.

 ** [publicConnectivity](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-publicConnectivity"></a>
If `true`, the graph has a public endpoint, otherwise not.
Type: Boolean

 ** [replicaCount](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-replicaCount"></a>
The number of replicas for the graph.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

 ** [sourceSnapshotId](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-sourceSnapshotId"></a>
The ID of the snapshot from which the graph was created, if the graph was recovered from a snapshot.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [status](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-status"></a>
The status of the graph.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | RESETTING | UPDATING | SNAPSHOTTING | FAILED | IMPORTING | STARTING | STOPPING | STOPPED`

 ** [statusReason](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-statusReason"></a>
The reason for the status of the graph.
Type: String

 ** [vectorSearchConfiguration](#API_DeleteGraph_ResponseSyntax) **   <a name="neptunegraph-DeleteGraph-response-vectorSearchConfiguration"></a>
Specifies the number of dimensions for vector embeddings loaded into the graph. Max = 65535
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object

## Errors
<a name="API_DeleteGraph_Errors"></a>

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
<a name="API_DeleteGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/DeleteGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/DeleteGraph)
