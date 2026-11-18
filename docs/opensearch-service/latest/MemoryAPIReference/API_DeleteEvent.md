---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html
---

# DeleteEvent
<a name="API_DeleteEvent"></a>

Deletes an event. Deletion can't be undone. The event stops appearing in `SearchEvents` results shortly after you delete it. Deleting an event that doesn't exist returns `ResourceNotFoundException`.

Deleting an event doesn't delete the memories derived from it, because a memory can combine content from several events. To remove them, use `DeleteMemory`.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_DeleteEvent_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "eventId": "{{string}}",
   "sessionId": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteEvent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_DeleteEvent_RequestSyntax) **   <a name="opensearchmemory-DeleteEvent-request-actorId"></a>
The identifier of the actor that the event belongs to. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [eventId](#API_DeleteEvent_RequestSyntax) **   <a name="opensearchmemory-DeleteEvent-request-eventId"></a>
The ID of the event to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [sessionId](#API_DeleteEvent_RequestSyntax) **   <a name="opensearchmemory-DeleteEvent-request-sessionId"></a>
The identifier of the session that the event belongs to. This value is intended for authorization: IAM policies can reference it in condition keys to allow or deny the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [spaceId](#API_DeleteEvent_RequestSyntax) **   <a name="opensearchmemory-DeleteEvent-request-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DeleteEvent_ResponseSyntax"></a>

```
{
   "eventId": "string"
}
```

## Response Elements
<a name="API_DeleteEvent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [eventId](#API_DeleteEvent_ResponseSyntax) **   <a name="opensearchmemory-DeleteEvent-response-eventId"></a>
The ID of the deleted event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.

## Errors
<a name="API_DeleteEvent_Errors"></a>

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
<a name="API_DeleteEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/DeleteEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/DeleteEvent)
