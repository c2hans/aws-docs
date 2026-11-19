---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html
---

# BatchGetEvent

Gets up to 10 events by ID, each as `GetEvent` returns it, including its payload.

If you supply `actorId` or `sessionId`, every requested event must match it. Each event has its own outcome. The operation reports an event that it can't return in `errors` instead of failing, with an error code named for the exception that `GetEvent` would return for it. The operation reports both an event that doesn't exist and an event outside the supplied scope as `RESOURCE_NOT_FOUND`.

The exception is the space's customer managed AWS KMS key: if it is disabled, pending deletion, can't be used for decryption, or was deleted, the whole call fails with `ValidationException`, as `GetEvent` does.

## Request Syntax
<a name="API_BatchGetEvent_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "eventIds": [ "{{string}}" ],
   "sessionId": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_BatchGetEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_BatchGetEvent_RequestSyntax) **   <a name="opensearchmemory-BatchGetEvent-request-actorId"></a>
The identifier of the actor that the requested events belong to. One value applies to every event in the request. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [eventIds](#API_BatchGetEvent_RequestSyntax) **   <a name="opensearchmemory-BatchGetEvent-request-eventIds"></a>
The IDs of the events to get: 1 to 10, without duplicates.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [sessionId](#API_BatchGetEvent_RequestSyntax) **   <a name="opensearchmemory-BatchGetEvent-request-sessionId"></a>
The identifier of the session that the requested events belong to. One value applies to every event in the request. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [spaceId](#API_BatchGetEvent_RequestSyntax) **   <a name="opensearchmemory-BatchGetEvent-request-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_BatchGetEvent_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "errorCode": "string",
         "eventId": "string",
         "message": "string"
      }
   ],
   "events": [
      {
         "actorId": "string",
         "eventId": "string",
         "eventTimestamp": "string",
         "metadata": {
            "string" : "string"
         },
         "payload": { ... },
         "sessionId": "string",
         "spaceId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetEvent_ResponseSyntax) **   <a name="opensearchmemory-BatchGetEvent-response-errors"></a>
An entry for each requested event that the call didn't return. Empty when the call returned every event.
Type: Array of [BatchGetEventError](API_BatchGetEventError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [events](#API_BatchGetEvent_ResponseSyntax) **   <a name="opensearchmemory-BatchGetEvent-response-events"></a>
The events found, in the order that you requested their IDs.
Type: Array of [Event](API_Event.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

## Errors
<a name="API_BatchGetEvent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. To use this operation, you must have AWS Identity and Access Management (IAM) permissions for the operation, and on the resource it acts on. If the space uses a customer managed AWS Key Management Service (AWS KMS) key, you must also have permission to use the key.
 ** message **
A message that describes which access the request is missing.
HTTP Status Code: 403

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
<a name="API_BatchGetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/BatchGetEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/BatchGetEvent)
