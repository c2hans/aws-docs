---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds the specified tag keys and values to a resource share or managed permission. If you choose a resource share, the tags are attached to only the resource share, not to the resources that are in the resource share.

The tags on a managed permission are the same for all versions of the managed permission.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tagresource HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
   "resourceShareArn": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="ram-TagResource-request-tags"></a>
A list of one or more tag key and value pairs. The tag key must be present and not be an empty string. The tag value must be present but can be an empty string.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="ram-TagResource-request-resourceArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the managed permission that you want to add tags to. You must specify *either* `resourceArn`, or `resourceShareArn`, but not both.
Type: String
Required: No

 ** [resourceShareArn](#API_TagResource_RequestSyntax) **   <a name="ram-TagResource-request-resourceShareArn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share that you want to add tags to. You must specify *either* `resourceShareArn`, or `resourceArn`, but not both.
Type: String
Required: No

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** ResourceArnNotFoundException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) was not found.
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** TagLimitExceededException **
The operation failed because it would exceed the limit for tags for your AWS account.
HTTP Status Code: 400

 ** TagPolicyViolationException **
The operation failed because the specified tag key is a reserved word and can't be used.
HTTP Status Code: 400

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/TagResource)
