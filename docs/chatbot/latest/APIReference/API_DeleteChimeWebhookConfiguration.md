---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteChimeWebhookConfiguration.html
---

# DeleteChimeWebhookConfiguration
<a name="API_DeleteChimeWebhookConfiguration"></a>

Deletes a Amazon Chime webhook configuration for Amazon Q Developer.

## Request Syntax
<a name="API_DeleteChimeWebhookConfiguration_RequestSyntax"></a>

```
POST /delete-chime-webhook-configuration HTTP/1.1
Content-type: application/json

{
   "ChatConfigurationArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteChimeWebhookConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteChimeWebhookConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChatConfigurationArn](#API_DeleteChimeWebhookConfiguration_RequestSyntax) **   <a name="qdevinchatapps-DeleteChimeWebhookConfiguration-request-ChatConfigurationArn"></a>
The Amazon Resource Name (ARN) of the ChimeWebhookConfiguration to delete.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 1169.
Pattern: `arn:aws:(wheatley|chatbot):[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: Yes

## Response Syntax
<a name="API_DeleteChimeWebhookConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteChimeWebhookConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteChimeWebhookConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DeleteChimeWebhookConfigurationException **
We can’t process your request right now because of a server issue. Try again later.
HTTP Status Code: 500

 ** InvalidParameterException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

## See Also
<a name="API_DeleteChimeWebhookConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteChimeWebhookConfiguration)
