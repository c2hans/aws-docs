---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes tags from a behavior graph.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{ResourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="detective-UntagResource-request-uri-ResourceArn"></a>
The ARN of the behavior graph to remove the tags from.
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="detective-UntagResource-request-uri-TagKeys"></a>
The tag keys of the tags to remove from the behavior graph. You can remove up to 50 tags at a time.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
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

 ** AccessDeniedException **
The request issuer does not have permission to access this resource or perform this operation.
 ** ErrorCode **
The SDK default error code associated with the access denied exception.
 ** ErrorCodeReason **
The SDK default explanation of why access was denied.
 ** SubErrorCode **
The error code associated with the access denied exception.
 ** SubErrorCodeReason **
 An explanation of why access was denied.
HTTP Status Code: 403

 ** InternalServerException **
The request was valid but failed because of a problem with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request refers to a nonexistent resource.
HTTP Status Code: 404

 ** ValidationException **
The request parameters are invalid.
 ** ErrorCode **
The error code associated with the validation failure.
 ** ErrorCodeReason **
 An explanation of why validation failed.
HTTP Status Code: 400

## Examples
<a name="API_UntagResource_Examples"></a>

### Example
<a name="API_UntagResource_Example_1"></a>

This example illustrates one usage of UntagResource.

#### Sample Request
<a name="API_UntagResource_Example_1_Request"></a>

```
DELETE /tags/resourceArn?tagKeys=TagKeys HTTP/1.1
Content-type: application/json
Host: api.detective.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 126
Authorization: AUTHPARAMS
X-Amz-Date: 20200127T193018Z
User-Agent: aws-cli/1.14.29 Python/2.7.9 Windows/8 botocore/1.8.33

{
   "ResourceArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
   "TagKeys": ["Department"]
}
```

### Example
<a name="API_UntagResource_Example_2"></a>

This example illustrates one usage of UntagResource.

#### Sample Response
<a name="API_UntagResource_Example_2_Response"></a>

```
HTTP/1.1 204 OK
Content-Length: 0
Date: Thu, 21 Feb 2020 23:07:46 GMT
x-amzn-RequestId: 397d0549-0092-11e8-a0ee-a7f9aa6e7572
Connection: Keep-alive
```

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/detective-2018-10-26/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/detective-2018-10-26/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/detective-2018-10-26/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/detective-2018-10-26/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/detective-2018-10-26/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/detective-2018-10-26/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/detective-2018-10-26/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/UntagResource)
