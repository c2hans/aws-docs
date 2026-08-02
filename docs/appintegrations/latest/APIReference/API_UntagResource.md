---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_connect-app-integrations_UntagResource"></a>

Removes the specified tags from the specified resource.

## Request Syntax
<a name="API_connect-app-integrations_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-app-integrations_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_connect-app-integrations_UntagResource_RequestSyntax) **   <a name="connect-connect-app-integrations_UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [tagKeys](#API_connect-app-integrations_UntagResource_RequestSyntax) **   <a name="connect-connect-app-integrations_UntagResource-request-uri-tagKeys"></a>
The tag keys.
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Required: Yes

## Request Body
<a name="API_connect-app-integrations_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-app-integrations_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-app-integrations_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-app-integrations_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing failed due to an error or failure with the service.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_connect-app-integrations_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appintegrations-2020-07-29/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/UntagResource)
