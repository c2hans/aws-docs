---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes a tag from a resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{ResourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="internetmonitor-UntagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) for a tag you remove a resource from.
Length Constraints: Minimum length of 20. Maximum length of 512.
Pattern: `arn:.*`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="internetmonitor-UntagResource-request-uri-TagKeys"></a>
Tag keys that you remove from a resource.
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

 ** AccessDeniedException **
You don't have sufficient permission to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
A bad request was received.
HTTP Status Code: 400

 ** InternalServerErrorException **
There was an internal server error.
HTTP Status Code: 500

 ** NotFoundException **
The request specifies something that doesn't exist.
HTTP Status Code: 404

 ** TooManyRequestsException **
There were too many requests.
HTTP Status Code: 429

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/internetmonitor-2021-06-03/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/UntagResource)
