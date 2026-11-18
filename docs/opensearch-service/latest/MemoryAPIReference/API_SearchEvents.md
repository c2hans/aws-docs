---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html
---

# SearchEvents
<a name="API_SearchEvents"></a>

Searches a space's events by relevance. It works like `SearchMemories` without the memory type and strategy selector. The query is a subset of the OpenSearch Query DSL. The service validates it, limits the search to the actor in `actorId` and the sessions in `sessionIds`, and returns ranked results. Each result is the matching chunk of an event, not the whole event. You can page through only a limited number of results. A request past that limit fails with `ValidationException` (reason `invalidNextToken`), and the message gives the limit.

If the results are larger than 5 MiB, the request fails with `ValidationException` (reason `queryBodyTooLarge`). Lower `maxResults`.

If the request would exceed the service's rate for embedding requests, it fails with `ThrottlingException`. Retry with exponential backoff.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_SearchEvents_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "query": {{JSON value}},
   "sessionIds": [ "{{string}}" ],
   "sort": {{JSON value}},
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchEvents_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-actorId"></a>
The actor whose events to search (exact match). Required: every search covers exactly one actor, and an event stored without an actor is never returned. Narrow the search further with `sessionIds`, combined by AND. This is the only way to filter by actor: a query that references `system_metadata.actor_id` fails with `ValidationException` (reason `nonFilterableField`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [maxResults](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-maxResults"></a>
The maximum number of events to return, from 1 to 100. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [query](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-query"></a>
The query: a subset of the OpenSearch Query DSL (see `SearchQuery`), validated by the same rules as on `SearchMemories`. Query event text as `text` and embeddings as `vector`. A search covers both conversation turns and chunks of documents submitted as a `blob`. You can't use actor and session fields here. Use the top-level `actorId` and `sessionIds`.
To search only the content of particular events, filter on `event_ids` with `term` or `terms`, for example with the `sourceEventIds` that a `SearchMemories` result returns. A `terms` clause on `event_ids` can list up to 10 event IDs. More IDs fail with `ValidationException` (reason `queryBodyTooLarge`). You can use `event_ids` only in `term`, `terms`, and `exists` queries.
Type: JSON value
Required: Yes

 ** [sessionIds](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-sessionIds"></a>
Returns only events from one of these sessions (exact match). Combined with `actorId` by AND. Omit for no session filter. An empty list fails validation. An event stored without a session never matches a session filter. This is the only way to filter by session: a query that references `system_metadata.session_id` fails with `ValidationException` (reason `nonFilterableField`).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [sort](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-sort"></a>
The sort order (see `SearchSort`). Omit to return the most relevant events first.
Type: JSON value
Required: No

 ** [spaceId](#API_SearchEvents_RequestSyntax) **   <a name="opensearchmemory-SearchEvents-request-spaceId"></a>
The space whose events to search. Use `actorId` and `sessionIds` to narrow the search within it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_SearchEvents_ResponseSyntax"></a>

```
{
   "events": [
      {
         "eventId": "string",
         "matchedContent": "string",
         "metadata": {
            "string" : "string"
         },
         "score": number,
         "systemMetadata": {
            "actorId": "string",
            "createdAt": "string",
            "sessionId": "string",
            "updatedAt": "string"
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_SearchEvents_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [events](#API_SearchEvents_ResponseSyntax) **   <a name="opensearchmemory-SearchEvents-response-events"></a>
The matching event chunks, in the order `sort` requests, or most relevant first when it has none. Empty when nothing matches. Each result is the matching chunk of an event. Call `GetEvent` for the whole event.
Type: Array of [EventSearchSummary](API_EventSearchSummary.md) objects

 ** [nextToken](#API_SearchEvents_ResponseSyntax) **   <a name="opensearchmemory-SearchEvents-response-nextToken"></a>
The token for the next set of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_SearchEvents_Errors"></a>

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
<a name="API_SearchEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/SearchEvents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/SearchEvents)
