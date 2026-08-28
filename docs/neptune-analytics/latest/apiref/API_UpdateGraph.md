---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_UpdateGraph.html
---

# UpdateGraph
<a name="API_UpdateGraph"></a>

Updates the configuration of a specified Neptune Analytics graph

## Request Syntax
<a name="API_UpdateGraph_RequestSyntax"></a>

```
PATCH /graphs/{{graphIdentifier}} HTTP/1.1
Content-type: application/json

{
   "deletionProtection": {{boolean}},
   "provisionedMemory": {{number}},
   "publicConnectivity": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateGraph_RequestParameters"></a>

The request uses the following URI parameters.

 ** [graphIdentifier](#API_UpdateGraph_RequestSyntax) **   <a name="neptunegraph-UpdateGraph-request-uri-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Pattern: `g-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_UpdateGraph_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [deletionProtection](#API_UpdateGraph_RequestSyntax) **   <a name="neptunegraph-UpdateGraph-request-deletionProtection"></a>
A value that indicates whether the graph has deletion protection enabled. The graph can't be deleted when deletion protection is enabled.
Type: Boolean
Required: No

 ** [provisionedMemory](#API_UpdateGraph_RequestSyntax) **   <a name="neptunegraph-UpdateGraph-request-provisionedMemory"></a>
The provisioned memory-optimized Neptune Capacity Units (m-NCUs) to use for the graph.
Min = 16
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.
Required: No

 ** [publicConnectivity](#API_UpdateGraph_RequestSyntax) **   <a name="neptunegraph-UpdateGraph-request-publicConnectivity"></a>
Specifies whether or not the graph can be reachable over the internet. All access to graphs is IAM authenticated. (`true` to enable, or `false` to disable.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateGraph_ResponseSyntax"></a>

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
<a name="API_UpdateGraph_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-arn"></a>
The ARN associated with the graph.
Type: String

 ** [buildNumber](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-buildNumber"></a>
The build number of the graph.
Type: String

 ** [createTime](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-createTime"></a>
The time at which the graph was created.
Type: Timestamp

 ** [deletionProtection](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-deletionProtection"></a>
If `true`, deletion protection is enabled for the graph.
Type: Boolean

 ** [endpoint](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-endpoint"></a>
The graph endpoint.
Type: String

 ** [id](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-id"></a>
The unique identifier of the graph.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt graph data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-name"></a>
The name of the graph.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!g-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [provisionedMemory](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-provisionedMemory"></a>
The number of memory-optimized Neptune Capacity Units (m-NCUs) allocated to the graph.
Type: Integer
Valid Range: Minimum value of 16. Maximum value of 24576.

 ** [publicConnectivity](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-publicConnectivity"></a>
If `true`, the graph has a public endpoint, otherwise not.
Type: Boolean

 ** [replicaCount](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-replicaCount"></a>
The number of replicas for the graph.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2.

 ** [sourceSnapshotId](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-sourceSnapshotId"></a>
The ID of the snapshot from which the graph was created, if any.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [status](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-status"></a>
The status of the graph.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | RESETTING | UPDATING | SNAPSHOTTING | FAILED | IMPORTING | STARTING | STOPPING | STOPPED`

 ** [statusReason](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-statusReason"></a>
The reason that the graph has this status.
Type: String

 ** [vectorSearchConfiguration](#API_UpdateGraph_ResponseSyntax) **   <a name="neptunegraph-UpdateGraph-response-vectorSearchConfiguration"></a>
Specifies the number of dimensions for vector embeddings loaded into the graph. Max = 65535
Type: [VectorSearchConfiguration](API_VectorSearchConfiguration.md) object

## Errors
<a name="API_UpdateGraph_Errors"></a>

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
<a name="API_UpdateGraph_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/UpdateGraph)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/UpdateGraph)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
