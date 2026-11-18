---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html
---

# UpdateSpace
<a name="API_UpdateSpace"></a>

Updates a space's memory strategies, retention settings, or extraction model. Supply only the fields to change. Omitted fields keep their current values.

If the request changes the set of strategies, a strategy's configuration, a retention setting, or the extraction model, the space moves to `UPDATING`. When the change is complete, the space returns to `ACTIVE`, or moves to `FAILED` if the change can't be applied. While the space is `UPDATING`, `GetSpace` returns the previous configuration. A request that only changes strategy descriptions or repeats the values the space has stored is applied immediately and doesn't change the status. Sending a retention value that the space never set also moves the space to `UPDATING`, even one that matches the behavior without it, such as 90 for `eventExpiryDays` or 0 for `memoryExpiryDays`. A space that is `CREATING`, `UPDATING`, or `DELETING` can't be updated: the request fails with `ConflictException`.

## Request Syntax
<a name="API_UpdateSpace_RequestSyntax"></a>

```
{
   "eventExpiryDays": {{number}},
   "extractionModelId": "{{string}}",
   "memoryExpiryDays": {{number}},
   "memoryStrategies": [
      {
         "configuration": {
            "consolidationEnabled": {{boolean}},
            "extractEveryNMessages": {{number}},
            "extractEveryNTokens": {{number}},
            "extractionPrompt": "{{string}}",
            "extractionSeedRecentN": {{number}},
            "extractionSeedTopK": {{number}},
            "idleTimeoutSeconds": {{number}}
         },
         "description": "{{string}}",
         "name": "{{string}}",
         "type": "{{string}}"
      }
   ],
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [eventExpiryDays](#API_UpdateSpace_RequestSyntax) **   <a name="opensearchmemory-UpdateSpace-request-eventExpiryDays"></a>
How many days the space keeps each event, from 1 to 365. Omit it to leave the current value unchanged. Events already stored keep the expiry they were written with.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: No

 ** [extractionModelId](#API_UpdateSpace_RequestSyntax) **   <a name="opensearchmemory-UpdateSpace-request-extractionModelId"></a>
The model that extracts and consolidates memories for every strategy in the space: `anthropic.claude-opus-5-5` or `anthropic.claude-haiku-5-5`. Omit it to leave the current value unchanged. Once set, it can't be cleared back to the service default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._:-]*`
Required: No

 ** [memoryExpiryDays](#API_UpdateSpace_RequestSyntax) **   <a name="opensearchmemory-UpdateSpace-request-memoryExpiryDays"></a>
How many days the space keeps each memory, from 0 to 3650. 0 means memories never expire. Omit it to leave the current value unchanged. You can't clear the setting. To make memories written from then on never expire, send 0. `GetSpace` then returns 0.
A change applies to memories written after it. Memories already stored keep the expiry they were written with. A memory the service rewrites later, such as a summary it keeps up to date, takes the setting in force at that rewrite. A change moves the space to `UPDATING`. Sending the value that the space has stored doesn't.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3650.
Required: No

 ** [memoryStrategies](#API_UpdateSpace_RequestSyntax) **   <a name="opensearchmemory-UpdateSpace-request-memoryStrategies"></a>
The complete new list of memory strategies. The service removes strategies that aren't in the list from the space. Removing a strategy stops extraction for it but doesn't delete its memories: they're kept, until they expire if the space sets `memoryExpiryDays`, and they're available again if you later add a strategy with the same `type` and `name`. To delete them, use `DeleteMemory` before you remove the strategy, or delete the space.
To keep a strategy, include it with the same `type` and `name` that `GetSpace` returns. For a kept strategy, any `configuration` member you omit keeps its current value. It doesn't return to the default, and you can't clear a member once it's set. Omit this field to leave the strategies unchanged. The list must name at least one strategy. You can't remove every strategy from a space with `UpdateSpace`.
The serialized list can be at most 384 KiB.
Type: Array of [MemoryStrategy](API_MemoryStrategy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [spaceId](#API_UpdateSpace_RequestSyntax) **   <a name="opensearchmemory-UpdateSpace-request-spaceId"></a>
The ID of the space to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_UpdateSpace_ResponseSyntax"></a>

```
{
   "spaceId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_UpdateSpace_ResponseSyntax) **   <a name="opensearchmemory-UpdateSpace-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`

 ** [status](#API_UpdateSpace_ResponseSyntax) **   <a name="opensearchmemory-UpdateSpace-response-status"></a>
The status of the space: `UPDATING` when the change has to be applied to the space's strategies, retention, or extraction model. Otherwise, the space's current status.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

## Errors
<a name="API_UpdateSpace_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would exceed a quota, such as the number of spaces in your account or the number of strategies in a space.
 ** message **
A message that describes which quota the request would exceed.
 ** quotaCode **
The Service Quotas code of the quota that the request would exceed. Not currently returned.
 ** serviceCode **
The Service Quotas code of the service. Not currently returned.
HTTP Status Code: 402

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
<a name="API_UpdateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/UpdateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/UpdateSpace)
