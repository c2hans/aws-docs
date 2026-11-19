---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html
---

# CreateSpace

Creates a space. A space is an AWS resource that stores the events you send and the memories extracted from them, and defines the memory strategies that extract those memories.

The operation returns before provisioning finishes, with `status` `CREATING`. Call `GetSpace` until the status is `ACTIVE`, and then use the space. If provisioning fails, the status becomes `FAILED` and `statusReason` says why.

## Request Syntax
<a name="API_CreateSpace_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "encryptionConfiguration": {
      "kmsKeyArn": "{{string}}"
   },
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
   "name": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-clientToken"></a>
A unique, case-sensitive identifier that makes the request idempotent. A retry with the same token and the same parameters within 2 hours returns the space that the first request created, instead of creating another. Reusing the token with different parameters, or while the first request is still in progress, fails with `ConflictException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[!-~]+`
Required: No

 ** [encryptionConfiguration](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-encryptionConfiguration"></a>
The AWS KMS key that encrypts the space's data. Omit it, or omit its `kmsKeyArn`, to use an AWS owned key. You can't change the key after you create the space.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [eventExpiryDays](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-eventExpiryDays"></a>
How many days the space keeps each event, from 1 to 365. The default is 90.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 365.
Required: No

 ** [extractionModelId](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-extractionModelId"></a>
The model that extracts and consolidates memories for every strategy in the space, as an Amazon Bedrock model ID without an inference-profile prefix: `anthropic.claude-opus-5-5` or `anthropic.claude-haiku-5-5`. Another value fails with `ValidationException`, and the message lists the supported IDs. Omit it to use the service default, which is currently `anthropic.claude-haiku-5-5`. The default can change over time and isn't returned by `GetSpace`. Setting a value pins the model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9._:-]*`
Required: No

 ** [memoryExpiryDays](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-memoryExpiryDays"></a>
How many days the space keeps each memory, from 0 to 3650, counted from when the service writes the memory. Updating a memory with `UpdateMemory` doesn't restart the count. 0 means memories never expire. If you omit it, memories never expire.
Searches and lists leave out a memory past its expiry, and reading, updating, or deleting it returns `ResourceNotFoundException`.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3650.
Required: No

 ** [memoryStrategies](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-memoryStrategies"></a>
The memory strategies that extract memories from the space's events: up to 10 strategies, each with a name that is unique within the space.
Optional. Omit it, or send an empty list, to create a space with no memory strategies. Such a space stores the conversation events you send it and returns them through `SearchEvents` and `ListEvents`, but extracts no memories and has none to search. You can add strategies later with `UpdateSpace`.
The serialized list can be at most 384 KiB.
Type: Array of [MemoryStrategy](API_MemoryStrategy.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [name](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-name"></a>
A name for the space, unique within your account in the Region. If another space already has the name, the request fails with `ConflictException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9 _-]*`
Required: Yes

 ** [tags](#API_CreateSpace_RequestSyntax) **   <a name="opensearchmemory-CreateSpace-request-tags"></a>
The tags to add to the space.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateSpace_ResponseSyntax"></a>

```
{
   "arn": "string",
   "createdAt": number,
   "name": "string",
   "spaceId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateSpace_ResponseSyntax) **   <a name="opensearchmemory-CreateSpace-response-arn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:osm:[a-z0-9-]+:[0-9]{12}:space/sp-[a-f0-9]{12}`

 ** [createdAt](#API_CreateSpace_ResponseSyntax) **   <a name="opensearchmemory-CreateSpace-response-createdAt"></a>
When the space was created.
Type: Timestamp

 ** [name](#API_CreateSpace_ResponseSyntax) **   <a name="opensearchmemory-CreateSpace-response-name"></a>
The name of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][a-zA-Z0-9 _-]*`

 ** [spaceId](#API_CreateSpace_ResponseSyntax) **   <a name="opensearchmemory-CreateSpace-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`

 ** [status](#API_CreateSpace_ResponseSyntax) **   <a name="opensearchmemory-CreateSpace-response-status"></a>
The status of the space: `CREATING`.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

## Errors
<a name="API_CreateSpace_Errors"></a>

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
<a name="API_CreateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/CreateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/CreateSpace)
