---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html
---

# UpdateMemory
<a name="API_UpdateMemory"></a>

Updates a memory in place. Supply only the fields to change. Omitted fields keep their stored values. A request must supply `content` or `metadata`, or it fails with `ValidationException`. Supplying `content` re-embeds the memory. A change to metadata alone doesn't.

The memory keeps its `memoryId` across updates. Shortly after an update, searches stop returning the previous content.

 `memoryType` can't be changed. To change it, delete the memory and create a new one.

A memory past its expiry (set from the space's `memoryExpiryDays` when the memory is written) reads as not found: the operation fails with `ResourceNotFoundException` and changes nothing. An update does not move the expiry.

Concurrent updates to one memory are last-writer-wins. There is no version check. To avoid lost updates, serialize your updates to a memory.

If you supply `content` and the request would exceed the service's rate for embedding requests, it fails with `ThrottlingException`. Retry with exponential backoff.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_UpdateMemory_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "content": "{{string}}",
   "memoryId": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "metadataMode": "{{string}}",
   "spaceId": "{{string}}",
   "strategyName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMemory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-actorId"></a>
The identifier of the actor associated with the memory. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [content](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-content"></a>
Replacement memory text. Supplying it re-embeds the memory. Omit to leave the text unchanged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16000.
Required: No

 ** [memoryId](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-memoryId"></a>
The ID of the memory to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [metadata](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-metadata"></a>
The metadata tags to apply. By default this map replaces the stored metadata, and any key not present is removed. Set `metadataMode` to `MERGE` to keep the keys you don't supply. Limits apply to the resulting metadata, not to the request. Keys that begin with `x-amz-` and the key `documentS3Source` are reserved: a request that sets one fails with `ValidationException`.
A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with `ValidationException`. Reuse an existing key instead.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** [metadataMode](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-metadataMode"></a>
How `metadata` combines with what is stored. The default is `REPLACE`.
Type: String
Valid Values: `REPLACE | MERGE`
Required: No

 ** [spaceId](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-spaceId"></a>
The ID of the space that owns the memory, for example `sp-02864597b164`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

 ** [strategyName](#API_UpdateMemory_RequestSyntax) **   <a name="opensearchmemory-UpdateMemory-request-strategyName"></a>
The name of the memory extraction strategy associated with the memory. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateMemory_ResponseSyntax"></a>

```
{
   "memory": {
      "content": "string",
      "memoryId": "string",
      "memoryType": "string",
      "metadata": {
         "string" : "string"
      },
      "strategyName": "string",
      "systemMetadata": {
         "actorId": "string",
         "createdAt": "string",
         "sessionId": "string",
         "updatedAt": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateMemory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memory](#API_UpdateMemory_ResponseSyntax) **   <a name="opensearchmemory-UpdateMemory-response-memory"></a>
The updated memory, in the same shape that `GetMemory` returns.
Type: [Memory](API_Memory.md) object

## Errors
<a name="API_UpdateMemory_Errors"></a>

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
<a name="API_UpdateMemory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/UpdateMemory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/UpdateMemory)
