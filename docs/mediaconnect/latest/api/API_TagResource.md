---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

 Associates the specified tags to a resource with the specified `resourceArn` in the current region. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are deleted as well.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="mediaconnect-TagResource-request-uri-resourceArn"></a>
 The Amazon Resource Name (ARN) that identifies the MediaConnect resource to which to add tags.
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="mediaconnect-TagResource-request-tags"></a>
 A map from tag keys to values. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.
Type: String to string map
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/TagResource)
