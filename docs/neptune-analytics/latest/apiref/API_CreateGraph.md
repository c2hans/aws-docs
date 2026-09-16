---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraph.html
---

# CreateGraph
<a name="API_CreateGraph"></a>

Creates a new Neptune Analytics graph.

## Request Syntax
<a name="API_CreateGraph_RequestSyntax"></a>

```
POST /graphs HTTP/1.1
Content-type: application/json

{
   "deletionProtection": {{boolean}},
   "graphName": "{{string}}",
   "kmsKeyIdentifier": "{{string}}",
   "provisionedMemory": {{number}},
   "publicConnectivity": {{boolean}},
   "replicaCount": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vectorSearchConfiguration": {
      "dimension": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateGraph_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deletionProtection](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-deletionProtection"></a>
Indicates whether or not to enable deletion protection on the graph. The graph can’t be deleted when deletion protection is enabled. (`true` or `false`).
Type: Boolean
Required: No

 ** [graphName](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-graphName"></a>
A name for the new Neptune Analytics graph to be created.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** [kmsKeyIdentifier](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-kmsKeyIdentifier"></a>
Specifies a KMS key to use to encrypt data in the new graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** [provisionedMemory](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-provisionedMemory"></a>
The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph. Min = 16
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: Yes

 ** [publicConnectivity](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-publicConnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (`true` to enable, or `false` to disable.
Type: Boolean
Required: No

 ** [replicaCount](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-replicaCount"></a>
The number of replicas in other AZs. Min =0, Max = 2, Default = 1.
 Additional charges equivalent to the m-NCUs selected for the graph apply for each replica.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** [tags](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-tags"></a>
Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vectorSearchConfiguration](#API_CreateGraph_RequestSyntax) **   <a name="neptunegraph-CreateGraph-request-vectorSearchConfiguration"></a>
Specifies the number of dimensions for vector embeddings that will be loaded into the graph. The value is specified as `dimension=`value. Max = 65,535
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object
Required: No

## Response Syntax
<a name="API_CreateGraph_ResponseSyntax"></a>

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
<a name="API_CreateGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-arn"></a>
The ARN of the graph.
Type: String

 ** [buildNumber](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-buildNumber"></a>
The build number of the graph software.
Type: String

 ** [createTime](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-createTime"></a>
The time when the graph was created.
Type: Timestamp

 ** [deletionProtection](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-deletionProtection"></a>
A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
Type: Boolean

 ** [endpoint](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-endpoint"></a>
The graph endpoint.
Type: String

 ** [id](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-id"></a>
The ID of the graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-kmsKeyIdentifier"></a>
Specifies the KMS key used to encrypt data in the new graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-name"></a>
The graph name. For example: `my-graph-1`.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [provisionedMemory](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-provisionedMemory"></a>
The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.
Min = 16
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.

 ** [publicConnectivity](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-publicConnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated.
If enabling public connectivity for the first time, there will be a delay while it is enabled.
Type: Boolean

 ** [replicaCount](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-replicaCount"></a>
The number of replicas in other AZs.
Default: If not specified, the default value is 1.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

 ** [sourceSnapshotId](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-sourceSnapshotId"></a>
The ID of the source graph.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [status](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-status"></a>
The current status of the graph.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | RESETTING | UPDATING | SNAPSHOTTING | FAILED | IMPORTING | STARTING | STOPPING | STOPPED`

 ** [statusReason](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-statusReason"></a>
The reason the status was given.
Type: String

 ** [vectorSearchConfiguration](#API_CreateGraph_ResponseSyntax) **   <a name="neptunegraph-CreateGraph-response-vectorSearchConfiguration"></a>
The vector-search configuration for the graph, which specifies the vector dimension to use in the vector index, if any.
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object

## Errors
<a name="API_CreateGraph_Errors"></a>

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
<a name="API_CreateGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CreateGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CreateGraph)
