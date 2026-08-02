---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes tags from the resource with the specified ARN.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="ivs-UntagResource-request-uri-resourceArn"></a>
The ARN of the resource to be untagged. The ARN must be URL-encoded.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivschat:[a-z0-9-]+:[0-9]+:[a-z-]/[a-zA-Z0-9-]+`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="ivs-UntagResource-request-uri-tagKeys"></a>
Array of tag keys (strings) for the tags to be removed. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints on tags beyond what is documented there.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **

HTTP Status Code: 500

 ** ResourceNotFoundException **

HTTP Status Code: 404

 ** ValidationException **

HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivschat-2020-07-14/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/UntagResource)
