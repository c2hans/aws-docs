---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags for a resource.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /v2/tags/{{resourceArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="ngresiliencehub-ListTagsForResource-request-uri-resourceArn"></a>
ARN identifier.
Length Constraints: Minimum length of 31.
Pattern: `arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}`
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="ngresiliencehub-ListTagsForResource-response-tags"></a>
Resource tags.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^\x00-\x1f\x22]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[^\x00-\x1f\x22]*`

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied — caller lacks required permissions.
HTTP Status Code: 403

 ** InternalServerException **
Internal service error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Resource not found.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests — rate limit exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
Validation error — invalid input parameters.
 ** fieldList **
The list of fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/resiliencehubv2-2026-02-17/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ListTagsForResource)
