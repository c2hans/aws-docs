---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html
---

# CreateMemory

Writes a memory that you have already formed, without extracting it from events. The service embeds the text as given and stores it as a memory of the named strategy. To have the service extract memories from conversation turns, use `CreateEvent` instead.

The operation returns before the memory is searchable. The returned `memoryId` is final, but until the memory is indexed, `GetMemory`, `UpdateMemory`, and `DeleteMemory` return `ResourceNotFoundException` for it.

If the request would exceed the service's rate for embedding requests, it fails with `ThrottlingException`. Retry with exponential backoff.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_CreateMemory_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "clientToken": "{{string}}",
   "content": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "name": "{{string}}",
   "sessionId": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMemory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-actorId"></a>
The actor (end user or agent) that owns the memory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [clientToken](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-clientToken"></a>
A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token returns the same `memoryId` instead of creating a second memory. Reusing the token with a different `name`, `content`, `metadata`, `actorId`, or `sessionId` fails with `ConflictException`. If you omit `sessionId`, a retry with the same token gets the same session. If you omit the token, each call creates a new memory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!-~]+`
Required: No

 ** [content](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-content"></a>
The memory text, stored and embedded as provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16000.
Required: Yes

 ** [metadata](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-metadata"></a>
Metadata tags to store with the memory. Keys that begin with `x-amz-`, the key `documentS3Source`, and other keys that the service uses internally are reserved: a request that sets one fails with `ValidationException`, and the message names the key.
A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with `ValidationException`. Reuse an existing key instead.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** [name](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-name"></a>
The name of the strategy that the memory belongs to. The space must already declare the strategy, and the memory's type comes from that strategy. The name must be 1 to 64 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [sessionId](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-sessionId"></a>
The session that the memory belongs to. If you omit it, the service generates a session ID and returns it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [spaceId](#API_CreateMemory_RequestSyntax) **   <a name="opensearchmemory-CreateMemory-request-spaceId"></a>
The ID of the space that owns the memory, for example `sp-02864597b164`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_CreateMemory_ResponseSyntax"></a>

```
{
   "memory": {
      "actorId": "string",
      "memoryId": "string",
      "name": "string",
      "sessionId": "string",
      "spaceId": "string"
   }
}
```

## Response Elements
<a name="API_CreateMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memory](#API_CreateMemory_ResponseSyntax) **   <a name="opensearchmemory-CreateMemory-response-memory"></a>
The memory, identified but not yet indexed.
Type: [CreateMemoryDetail](API_CreateMemoryDetail.md) object

## Errors
<a name="API_CreateMemory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.
 ** message **
A message that describes which access the request is missing.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. For example, the space is being created, updated, or deleted, a space with the same name already exists, or you reused a client token with different parameters. Wait for the space to finish being created, updated, or deleted, or use a different name or client token, and then retry.
 ** message **
A message that describes the conflict.
 ** resourceId **
The ID of the resource that caused the conflict.
 ** resourceType **
The type of the resource that caused the conflict.
HTTP Status Code: 409

 ** InternalServerException **
The service couldn't process the request because of an internal error. Retry the request.
 ** message **
A message that describes the internal error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource doesn't exist. Check the IDs in the request.
 ** message **
A message that describes which resource wasn't found.
 ** resourceId **
The ID of the resource that wasn't found.
 ** resourceType **
The type of the resource that wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The service throttled the request. Retry the request with exponential backoff.
 ** message **
A message that describes the throttling.
 ** retryAfterSeconds **
The number of seconds to wait before you retry the request.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. The `reason`, `message`, and `fieldList` members describe the problem. Fix the request, and then try again.
 ** fieldList **
The fields that failed validation, if any.
 ** message **
A message that describes why the request failed validation, such as the field, key, or limit involved.
 ** reason **
The reason that the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/CreateMemory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/CreateMemory)
