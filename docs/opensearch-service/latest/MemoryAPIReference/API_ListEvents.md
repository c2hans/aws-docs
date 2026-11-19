---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html
---

# ListEvents

Lists the events in a session, sorted by time. Optionally limit the results to events whose `eventTimestamp` falls between `eventTimestampAfter` and `eventTimestampBefore`. Returns event metadata only. Call `GetEvent` for the payload. For full-text or relevance search, use `SearchEvents`.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_ListEvents_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "eventTimestampAfter": "{{string}}",
   "eventTimestampBefore": "{{string}}",
   "maxResults": {{number}},
   "metadataFilters": {
      "{{string}}" : "{{string}}"
   },
   "nextToken": "{{string}}",
   "sessionId": "{{string}}",
   "sortOrder": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-actorId"></a>
The actor whose events to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [eventTimestampAfter](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-eventTimestampAfter"></a>
Inclusive lower bound on `eventTimestamp`: only events at or after this time are returned. Omit for no lower bound.
If it's later than `eventTimestampBefore`, the request fails with `ValidationException`.
Type: Timestamp
Required: No

 ** [eventTimestampBefore](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-eventTimestampBefore"></a>
Inclusive upper bound on `eventTimestamp`: only events at or before this time are returned. Omit for no upper bound.
Type: Timestamp
Required: No

 ** [maxResults](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-maxResults"></a>
The maximum number of events to return, from 1 to 100. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [metadataFilters](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-metadataFilters"></a>
Returns only events whose metadata contains every one of these key-value pairs. Omit, or leave empty, for no metadata filter. The service applies the filter after it reads events, so a page can hold fewer than `maxResults` events, or none, and still return a `nextToken`. Keep paging until `nextToken` is absent.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** [nextToken](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [sessionId](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-sessionId"></a>
The session whose events to list. To find events across sessions, use `SearchEvents`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [sortOrder](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-sortOrder"></a>
The order of the results by `eventTimestamp`: `ASC` or `DESC`. The default is `DESC`, most recent first.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [spaceId](#API_ListEvents_RequestSyntax) **   <a name="opensearchmemory-ListEvents-request-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_ListEvents_ResponseSyntax"></a>

```
{
   "events": [
      {
         "eventId": "string",
         "eventTimestamp": "string",
         "metadata": {
            "string" : "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_ListEvents_ResponseSyntax) **   <a name="opensearchmemory-ListEvents-response-events"></a>
The events, without their payloads. Call `GetEvent` for an event's payload.
Type: Array of [EventSummary](API_EventSummary.md) objects

 ** [nextToken](#API_ListEvents_ResponseSyntax) **   <a name="opensearchmemory-ListEvents-response-nextToken"></a>
The token for the next set of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListEvents_Errors"></a>

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
<a name="API_ListEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/ListEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/ListEvents)
