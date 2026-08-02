---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes tags from a resource. For usage examples, see the [https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html](https://docs.aws.amazon.com/controltower/latest/controlreference/control-api-examples-short.html).

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="controltower-UntagResource-request-uri-resourceArn"></a>
The ARN of the resource.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[0-9a-zA-Z_\-:\/]+`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="controltower-UntagResource-request-uri-tagKeys"></a>
Tag keys to be removed from the resource.
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/UntagResource)
