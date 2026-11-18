---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html
---

# CreateEvent
<a name="API_CreateEvent"></a>

Submits an event (conversation turns, structured data, or a PDF, PNG, or JPEG file stored in Amazon S3) to a session in a space.

The operation returns as soon as the event is saved. `GetEvent` and `ListEvents` return it immediately. `SearchEvents` returns it after it's indexed. `SearchMemories` returns memories extracted from it only after a strategy's extraction trigger fires and the memories are indexed.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_CreateEvent_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "clientToken": "{{string}}",
   "eventTimestamp": "{{string}}",
   "infer": {{boolean}},
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "payload": { ... },
   "sessionId": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-actorId"></a>
The ID of the actor (end user or agent) that the event belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [clientToken](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-clientToken"></a>
A unique, case-sensitive identifier that makes the request idempotent. Within 2 hours of the first request, a retry with the same token and the same request, including the same `sessionId`, returns the same event. If you omit `sessionId`, the service generates a new one on each attempt, so a retry fails with `ConflictException`. Reusing the token with different request content also fails with `ConflictException`. `eventTimestamp` isn't compared. After 2 hours, the token starts a new event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!-~]+`
Required: No

 ** [eventTimestamp](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-eventTimestamp"></a>
When the event occurred. The default is the time that the service receives the request.
Type: Timestamp
Required: No

 ** [infer](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-infer"></a>
Specifies whether to extract memories from this event. The default is `true`. Set it to `false` to store the event without extraction: the service skips strategies that infer memories, and still indexes the event's turns for `SearchEvents`. A document submitted as a `blob` is still extracted.
Type: Boolean
Required: No

 ** [metadata](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-metadata"></a>
Metadata tags to store with the event. Memories derived from the event carry the same tags. Keys that begin with `x-amz-`, the keys `documentS3Source` and `documentS3Url`, and other keys that the service uses internally are reserved: a request that sets one fails with `ValidationException`, and the message names the key.
A space can use at most 50 distinct metadata keys across all of its events and memories. A request that would add a key beyond that fails with `ValidationException`. Reuse an existing key instead.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** [payload](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-payload"></a>
The event content. Set exactly one union member.
Type: [EventPayload](API_EventPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [sessionId](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-sessionId"></a>
The session the event belongs to. Send every event of one conversation with the same session ID, so that `SUMMARY` strategies summarize the conversation as one session. If you omit it, the service generates a session ID and returns it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [spaceId](#API_CreateEvent_RequestSyntax) **   <a name="opensearchmemory-CreateEvent-request-spaceId"></a>
The ID of the space that owns the event, for example `sp-02864597b164`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_CreateEvent_ResponseSyntax"></a>

```
{
   "event": {
      "actorId": "string",
      "eventId": "string",
      "eventTimestamp": "string",
      "sessionId": "string",
      "spaceId": "string"
   }
}
```

## Response Elements
<a name="API_CreateEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [event](#API_CreateEvent_ResponseSyntax) **   <a name="opensearchmemory-CreateEvent-response-event"></a>
The stored event's identifiers: its ID, session, and timestamp.
Type: [EventDetail](API_EventDetail.md) object

## Errors
<a name="API_CreateEvent_Errors"></a>

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
<a name="API_CreateEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/CreateEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/CreateEvent)
