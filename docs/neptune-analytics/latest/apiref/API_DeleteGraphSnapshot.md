---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_DeleteGraphSnapshot.html
---

# DeleteGraphSnapshot
<a name="API_DeleteGraphSnapshot"></a>

Deletes the specifed graph snapshot.

## Request Syntax
<a name="API_DeleteGraphSnapshot_RequestSyntax"></a>

```
DELETE /snapshots/{{snapshotIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteGraphSnapshot_RequestParameters"></a>

The request uses the following URI parameters.

 ** [snapshotIdentifier](#API_DeleteGraphSnapshot_RequestSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-request-uri-snapshotIdentifier"></a>
ID of the graph snapshot to be deleted.
Pattern: `gs-[a-z0-9]{10}`
Required: Yes

## Request Body
<a name="API_DeleteGraphSnapshot_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteGraphSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "id": "string",
   "kmsKeyIdentifier": "string",
   "name": "string",
   "snapshotCreateTime": number,
   "sourceGraphId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteGraphSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-arn"></a>
The ARN of the graph snapshot.
Type: String

 ** [id](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-id"></a>
The unique identifier of the graph snapshot.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt the snapshot.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-name"></a>
The snapshot name. For example: `my-snapshot-1`.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [snapshotCreateTime](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-snapshotCreateTime"></a>
The time when the snapshot was created.
Type: Timestamp

 ** [sourceGraphId](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-sourceGraphId"></a>
The graph identifier for the graph from which the snapshot was created.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [status](#API_DeleteGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-DeleteGraphSnapshot-response-status"></a>
The status of the graph snapshot.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`

## Errors
<a name="API_DeleteGraphSnapshot_Errors"></a>

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
<a name="API_DeleteGraphSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/DeleteGraphSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/DeleteGraphSnapshot)
