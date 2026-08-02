---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds or overwrites only the specified tags for the specified resource. When you specify an existing tag key, the value is overwritten with the new value.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /v1/tags/tag-resource HTTP/1.1
Content-type: application/json

{
   "resourceArn": "{{string}}",
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

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="Social-TagResource-request-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to tag.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="Social-TagResource-request-tags"></a>
The tags to add to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "statusCode": number
}
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [statusCode](#API_TagResource_ResponseSyntax) **   <a name="Social-TagResource-response-statusCode"></a>
The status code of the tag resource operation.
Type: Integer

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/TagResource)
