---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AssociateToConfiguration.html
---

# AssociateToConfiguration
<a name="API_AssociateToConfiguration"></a>

Links a resource (for example, a custom action) to a channel configuration.

## Request Syntax
<a name="API_AssociateToConfiguration_RequestSyntax"></a>

```
POST /associate-to-configuration HTTP/1.1
Content-type: application/json

{
   "ChatConfiguration": "{{string}}",
   "Resource": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateToConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateToConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfiguration](#API_AssociateToConfiguration_RequestSyntax) **   <a name="qdevinchatapps-AssociateToConfiguration-request-ChatConfiguration"></a>
The channel configuration to associate with the resource.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

 ** [Resource](#API_AssociateToConfiguration_RequestSyntax) **   <a name="qdevinchatapps-AssociateToConfiguration-request-Resource"></a>
The resource Amazon Resource Name (ARN) to link.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:custom-action/[a-zA-Z0-9_-]{1,64}`
Required: Yes

## Response Syntax
<a name="API_AssociateToConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_AssociateToConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_AssociateToConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 403

## See Also
<a name="API_AssociateToConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/AssociateToConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/AssociateToConfiguration)
