---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html
---

# SearchMemories
<a name="API_SearchMemories"></a>

Searches a space's memories by relevance. The query is a subset of the OpenSearch Query DSL. The service validates it, limits the search to the requested strategies and to the actor in `actorId`, and returns one ranked list of memories. You can page through only a limited number of results. A request past that limit fails with `ValidationException` (reason `invalidNextToken`), and the message gives the limit.

Memories past their expiry (set from the space's `memoryExpiryDays` when each memory is written) are left out of the results. Only current memories are returned: a memory that consolidation has superseded (an older version of a fact that a newer memory replaced) is left out.

If the results are larger than 5 MiB, the request fails with `ValidationException` (reason `queryBodyTooLarge`). Lower `maxResults`.

If the request would exceed the service's rate for embedding requests, it fails with `ThrottlingException`. Retry with exponential backoff.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_SearchMemories_RequestSyntax"></a>

```
{
   "actorId": "{{string}}",
   "maxResults": {{number}},
   "memoryStrategies": [
      {
         "memoryStrategyNames": [ "{{string}}" ],
         "memoryType": "{{string}}"
      }
   ],
   "nextToken": "{{string}}",
   "query": {{JSON value}},
   "sort": {{JSON value}},
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_SearchMemories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorId](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-actorId"></a>
The actor whose memories to search (exact match). Required: every search covers exactly one actor, and a memory stored without an actor is never returned. This is the only way to filter by actor: a query that references `system_metadata.actor_id` fails with `ValidationException` (reason `nonFilterableField`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** [maxResults](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-maxResults"></a>
The maximum number of memories to return, from 1 to 100. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [memoryStrategies](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-memoryStrategies"></a>
The strategies to search, as a list of selectors. Each selector names a memory type and, optionally, specific strategy names of that type. A space can hold several strategies of the same type. A selector without `memoryStrategyNames` searches every strategy of its type, and omitting `memoryStrategies` searches every strategy in the space. A name that is not a declared strategy of that type fails with `ValidationException`.
Type: Array of [StrategySelector](API_StrategySelector.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [nextToken](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [query](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-query"></a>
The query: a subset of the OpenSearch Query DSL (see `SearchQuery`). You can't use the actor and session fields `system_metadata.actor_id` and `system_metadata.session_id` here. Use the top-level `actorId` to filter by actor. Searching memories doesn't filter by session.
Type: JSON value
Required: Yes

 ** [sort](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-sort"></a>
The sort order (see `SearchSort`). Omit to return the most relevant memories first.
Type: JSON value
Required: No

 ** [spaceId](#API_SearchMemories_RequestSyntax) **   <a name="opensearchmemory-SearchMemories-request-spaceId"></a>
The space to search. Use `actorId` to narrow the search within it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_SearchMemories_ResponseSyntax"></a>

```
{
   "memories": [
      {
         "content": "string",
         "memoryId": "string",
         "memoryType": "string",
         "metadata": {
            "string" : "string"
         },
         "score": number,
         "sourceEventIds": [ "string" ],
         "strategyName": "string",
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
<a name="API_SearchMemories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memories](#API_SearchMemories_ResponseSyntax) **   <a name="opensearchmemory-SearchMemories-response-memories"></a>
The matching memories, in the order `sort` requests, or most relevant first when it has none. Empty when nothing matches.
Type: Array of [MemorySearchSummary](API_MemorySearchSummary.md) objects

 ** [nextToken](#API_SearchMemories_ResponseSyntax) **   <a name="opensearchmemory-SearchMemories-response-nextToken"></a>
The token for the next set of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_SearchMemories_Errors"></a>

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
<a name="API_SearchMemories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/SearchMemories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/SearchMemories)
