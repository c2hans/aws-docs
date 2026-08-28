---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/apiref/API_CreateGraphSnapshot.html
---

# CreateGraphSnapshot
<a name="API_CreateGraphSnapshot"></a>

Creates a snapshot of the specific graph.

## Request Syntax
<a name="API_CreateGraphSnapshot_RequestSyntax"></a>

```
POST /snapshots HTTP/1.1
Content-type: application/json

{
   "graphIdentifier": "{{string}}",
   "snapshotName": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateGraphSnapshot_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateGraphSnapshot_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [graphIdentifier](#API_CreateGraphSnapshot_RequestSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-request-graphIdentifier"></a>
The unique identifier of the Neptune Analytics graph.
Type: String
Pattern: `g-[a-z0-9]{10}`
Required: Yes

 ** [snapshotName](#API_CreateGraphSnapshot_RequestSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-request-snapshotName"></a>
The snapshot name. For example: `my-snapshot-1`.
The name must contain from 1 to 63 letters, numbers, or hyphens, and its first character must be a letter. It cannot end with a hyphen or contain two consecutive hyphens. Only lowercase letters are allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*`
Required: Yes

 ** [tags](#API_CreateGraphSnapshot_RequestSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-request-tags"></a>
Adds metadata tags to the new graph. These tags can also be used with cost allocation reporting, or used in a Condition statement in an IAM policy.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateGraphSnapshot_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateGraphSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-arn"></a>
The ARN of the snapshot created.
Type: String

 ** [id](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-id"></a>
The ID of the snapshot created.
Type: String
Pattern: `gs-[a-z0-9]{10}`

 ** [kmsKeyIdentifier](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-kmsKeyIdentifier"></a>
The ID of the KMS key used to encrypt and decrypt graph data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

 ** [name](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-name"></a>
The name of the snapshot created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!gs-)[a-z][a-z0-9]*(-[a-z0-9]+)*`

 ** [snapshotCreateTime](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-snapshotCreateTime"></a>
The snapshot creation time
Type: Timestamp

 ** [sourceGraphId](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-sourceGraphId"></a>
The Id of the Neptune Analytics graph from which the snapshot is created.
Type: String
Pattern: `g-[a-z0-9]{10}`

 ** [status](#API_CreateGraphSnapshot_ResponseSyntax) **   <a name="neptunegraph-CreateGraphSnapshot-response-status"></a>
The current state of the snapshot.
Type: String
Valid Values: `CREATING | AVAILABLE | DELETING | FAILED`

## Errors
<a name="API_CreateGraphSnapshot_Errors"></a>

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
<a name="API_CreateGraphSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-graph-2023-11-29/CreateGraphSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-graph-2023-11-29/CreateGraphSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for NeptuneAnalyticsAPI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
