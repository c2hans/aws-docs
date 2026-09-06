---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UntagGlobalResource.html
---

# UntagGlobalResource
<a name="API_UntagGlobalResource"></a>

Removes tags from a global resource in AWS Elemental MediaConnect. The API supports the following global resources: router inputs, router outputs and router network interfaces.

## Request Syntax
<a name="API_UntagGlobalResource_RequestSyntax"></a>

```
DELETE /tags/global/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagGlobalResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagGlobalResource_RequestSyntax) **   <a name="mediaconnect-UntagGlobalResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the global resource to remove tags from.
Required: Yes

 ** [tagKeys](#API_UntagGlobalResource_RequestSyntax) **   <a name="mediaconnect-UntagGlobalResource-request-uri-tagKeys"></a>
The keys of the tags to remove from the global resource.
Required: Yes

## Request Body
<a name="API_UntagGlobalResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagGlobalResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UntagGlobalResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UntagGlobalResource_Errors"></a>

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
<a name="API_UntagGlobalResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UntagGlobalResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UntagGlobalResource)
