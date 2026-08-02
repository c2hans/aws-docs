---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_RestoreGraphFromSnapshot.html
---

# RestoreGraphFromSnapshot
<a name="API_RestoreGraphFromSnapshot"></a>

Restores a graph from a snapshot.

## Request Syntax
<a name="API_RestoreGraphFromSnapshot_RequestSyntax"></a>

```
POST /snapshots/{{snapshotIdentifier}}/restore HTTP/1.1
Content-type: application/json

{
   "deletionProtection": {{boolean}},
   "graphName": "{{string}}",
   "provisionedMemory": {{number}},
   "publicConnectivity": {{boolean}},
   "replicaCount": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_RestoreGraphFromSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [snapshotIdentifier](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-uri-snapshotIdentifier"></a>
The ID of the snapshot in question.
Pattern: `gs-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_RestoreGraphFromSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deletionProtection](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-deletionProtection"></a>
A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
Type: Boolean
Required: No

 ** [graphName](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-graphName"></a>
A name for the new Neptune Analytics graph to be created from the snapshot.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** [provisionedMemory](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-provisionedMemory"></a>
The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.
Min = 16
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: No

 ** [publicConnectivity](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-publicConnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (`true` to enable, or `false` to disable).
Type: Boolean
Required: No

 ** [replicaCount](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-replicaCount"></a>
The number of replicas in other AZs. Min =0, Max = 2, Default =1
 Additional charges equivalent to the m-NCUs selected for the graph apply for each replica.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** [tags](#API_RestoreGraphFromSnapshot_RequestSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-request-tags"></a>
Adds metadata tags to the snapshot. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_RestoreGraphFromSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_RestoreGraphFromSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-arn"></a>
The ARN associated with the graph.
Type: String

 ** [buildNumber](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-buildNumber"></a>
The build number of the graph.
Type: String

 ** [createTime](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-createTime"></a>
The time at which the graph was created.
Type: Timestamp

 ** [deletionProtection](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-deletionProtection"></a>
If `true`, deletion protection is enabled for the graph.
Type: Boolean

 ** [endpoint](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-endpoint"></a>
The graph endpoint.
Type: String

 ** [id](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-id"></a>
The unique identifier of the graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt graph data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-name"></a>
The name of the graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [provisionedMemory](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-provisionedMemory"></a>
The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.

 ** [publicConnectivity](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-publicConnectivity"></a>
If `true`, the graph has a public endpoint, otherwise not.
Type: Boolean

 ** [replicaCount](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-replicaCount"></a>
The number of replicas for the graph.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

 ** [sourceSnapshotId](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-sourceSnapshotId"></a>
The ID of the snapshot from which the graph was created, if any.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [status](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-status"></a>
The status of the graph.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | RESETTING | UPDATING | SNAPSHOTTING | FAILED | IMPORTING | STARTING | STOPPING | STOPPED`

 ** [statusReason](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-statusReason"></a>
The reason that the graph has this status.
Type: String

 ** [vectorSearchConfiguration](#API_RestoreGraphFromSnapshot_ResponseSyntax) **   <a name="neptunegraph-RestoreGraphFromSnapshot-response-vectorSearchConfiguration"></a>
Specifies the number of dimensions for vector embeddings loaded into the graph. Max = 65535
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object

## Errors
<a name="API_RestoreGraphFromSnapshot_Errors"></a>

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
<a name="API_RestoreGraphFromSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/RestoreGraphFromSnapshot)
