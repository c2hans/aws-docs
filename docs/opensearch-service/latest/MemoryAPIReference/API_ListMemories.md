---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html
---

# ListMemories

Lists a space's memories without a query, for example the most recent memories or the memories of one strategy. Filter by strategy and optionally by owning actor or session, sort by creation or update time, and page through the results. Results have no relevance score. To query or filter by metadata, use `SearchMemories`.

If memories are written or deleted while you page, the results can skip a memory or return it twice. You can page through only a limited number of results. A request past that limit fails with `ValidationException` (reason `invalidNextToken`), and the message gives the limit.

Memories past their expiry (set from the space's `memoryExpiryDays` when each memory is written) are left out. Unlike `SearchMemories`, this operation also returns memories that consolidation has superseded.

If the space uses a customer managed AWS KMS key, the call can also fail because of the key. It fails with `AccessDeniedException` if you aren't allowed to use the key, and with `ThrottlingException` if AWS KMS throttles the request. It fails with `ValidationException` if the key is disabled, pending deletion, or deleted.

## Request Syntax
<a name="API_ListMemories_RequestSyntax"></a>

```
{
   "actorIds": [ "{{string}}" ],
   "maxResults": {{number}},
   "memoryStrategies": [
      {
         "memoryStrategyNames": [ "{{string}}" ],
         "memoryType": "{{string}}"
      }
   ],
   "nextToken": "{{string}}",
   "sessionIds": [ "{{string}}" ],
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}",
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListMemories_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actorIds](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-actorIds"></a>
Lists only memories owned by one of these actors. Combined with `sessionIds` by AND: a memory must match both filters when both are given. Omit for no actor filter. An empty list fails validation. A memory stored without an actor never matches an actor filter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [maxResults](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-maxResults"></a>
The maximum number of memories to return, from 1 to 100. The default is 20.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [memoryStrategies](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-memoryStrategies"></a>
The strategies to list, as selectors. A selector without `memoryStrategyNames` lists every strategy of its type, and omitting `memoryStrategies` lists every strategy in the space. A name that is not a declared strategy of that type fails with `ValidationException`.
Type: Array of [StrategySelector](API_StrategySelector.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** [nextToken](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [sessionIds](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-sessionIds"></a>
Lists only memories from one of these sessions. Combined with `actorIds` by AND. Omit for no session filter. An empty list fails validation. A memory stored without a session never matches a session filter.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** [sortBy](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-sortBy"></a>
The timestamp to sort by, as returned in `systemMetadata`: `CREATED_AT` (the default) or `UPDATED_AT`.
Type: String
Valid Values: `CREATED_AT | UPDATED_AT`
Required: No

 ** [sortOrder](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-sortOrder"></a>
The sort order: `ASC` or `DESC`. The default is `DESC`, most recent first.
Type: String
Valid Values: `ASC | DESC`
Required: No

 ** [spaceId](#API_ListMemories_RequestSyntax) **   <a name="opensearchmemory-ListMemories-request-spaceId"></a>
The space whose memories to list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_ListMemories_ResponseSyntax"></a>

```
{
   "memories": [
      {
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
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMemories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [memories](#API_ListMemories_ResponseSyntax) **   <a name="opensearchmemory-ListMemories-response-memories"></a>
The memories, in the requested order. Empty when there are none.
Type: Array of [MemoryListSummary](API_MemoryListSummary.md) objects

 ** [nextToken](#API_ListMemories_ResponseSyntax) **   <a name="opensearchmemory-ListMemories-response-nextToken"></a>
The token for the next set of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListMemories_Errors"></a>

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
<a name="API_ListMemories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/ListMemories)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/ListMemories)
