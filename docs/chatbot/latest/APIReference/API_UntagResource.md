---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN). Resources are users, servers, roles, and other entities.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
POST /untag-resource HTTP/1.1
Content-type: application/json

{
   "ResourceARN": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_UntagResource_RequestSyntax) **   <a name="qdevinchatapps-UntagResource-request-ResourceARN"></a>
The value of the resource that will have the tag removed. An Amazon Resource Name (ARN) is an identifier for a specific AWS resource, such as a server, user, or role.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="qdevinchatapps-UntagResource-request-TagKeys"></a>
TagKeys are key-value pairs assigned to ARNs that can be used to group and search for resources by type. This metadata can be attached to resources for any purpose.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

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

 ** InternalServiceError **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

 ** ServiceUnavailableException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 429

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/UntagResource)
