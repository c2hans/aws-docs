---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes a key-value pair from a monitor or probe.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="networksyntheticmonitor-UntagResource-request-uri-resourceArn"></a>
The ARN of the monitor or probe that the tag should be removed from.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="networksyntheticmonitor-UntagResource-request-uri-tagKeys"></a>
The key-value pa
Array Members: Minimum number of 0 items. Maximum number of 200 items.
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

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
This operation attempted to create a resource that already exists.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling
HTTP Status Code: 429

 ** ValidationException **
One of the parameters for the request is not valid.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/networkmonitor-2023-08-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmonitor-2023-08-01/UntagResource)
