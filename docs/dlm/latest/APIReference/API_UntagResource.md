---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes the specified tags from the specified resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{TagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="dlm-UntagResource-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `^arn:aws(-[a-z]{1,4}){0,2}:dlm:[A-Za-z0-9_/.-]{0,63}:\d+:policy/[0-9A-Za-z_-]{1,128}$`
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="dlm-UntagResource-request-uri-TagKeys"></a>
The tag keys.
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
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
The service failed in an unexpected way.
HTTP Status Code: 500

 ** InvalidRequestException **
Bad request. The request is missing required parameters or has invalid parameters.
 ** MutuallyExclusiveParameters **
The request included parameters that cannot be provided together.
 ** RequiredParameters **
The request omitted one or more required parameters.
HTTP Status Code: 400

 ** LimitExceededException **
The request failed because a limit was exceeded.
 ** ResourceType **
Value is the type of resource for which a limit was exceeded.
HTTP Status Code: 429

 ** ResourceNotFoundException **
A requested resource was not found.
 ** ResourceIds **
Value is a list of resource IDs that were not found.
 ** ResourceType **
Value is the type of resource that was not found.
HTTP Status Code: 404

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dlm-2018-01-12/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dlm-2018-01-12/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dlm-2018-01-12/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dlm-2018-01-12/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dlm-2018-01-12/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dlm-2018-01-12/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dlm-2018-01-12/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/UntagResource)
