---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html
---

# DeleteSpace
<a name="API_DeleteSpace"></a>

Deletes a space and its memories. Deletion can't be undone. After you delete the space, you can't retrieve its events, and the service removes them when they reach their expiry.

The operation returns with `status` `DELETING`. When deletion finishes, `GetSpace` returns `ResourceNotFoundException`. If deletion fails, the status becomes `FAILED`. A space that is `CREATING` or `UPDATING` can't be deleted until that finishes: the request fails with `ConflictException`. Deleting a space that is already `DELETING` returns `DELETING` again.

## Request Syntax
<a name="API_DeleteSpace_RequestSyntax"></a>

```
{
   "spaceId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSpace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [spaceId](#API_DeleteSpace_RequestSyntax) **   <a name="opensearchmemory-DeleteSpace-request-spaceId"></a>
The ID of the space to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_DeleteSpace_ResponseSyntax"></a>

```
{
   "spaceId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_DeleteSpace_ResponseSyntax) **   <a name="opensearchmemory-DeleteSpace-response-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`

 ** [status](#API_DeleteSpace_ResponseSyntax) **   <a name="opensearchmemory-DeleteSpace-response-status"></a>
The status of the space: `DELETING`.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | DELETED | FAILED`

## Errors
<a name="API_DeleteSpace_Errors"></a>

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
<a name="API_DeleteSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/DeleteSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/DeleteSpace)
