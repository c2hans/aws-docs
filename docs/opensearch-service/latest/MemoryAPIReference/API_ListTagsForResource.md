---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags for the specified space.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "resourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="opensearchmemory-ListTagsForResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws:osm:[a-z0-9-]+:[0-9]{12}:space/sp-[a-f0-9]{12}`
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="opensearchmemory-ListTagsForResource-response-tags"></a>
The tags for the space.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchmemory-2026-08-24/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/ListTagsForResource)
