---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteCustomAction.html
---

# DeleteCustomAction
<a name="API_DeleteCustomAction"></a>

Deletes a custom action.

## Request Syntax
<a name="API_DeleteCustomAction_RequestSyntax"></a>

```
POST /delete-custom-action HTTP/1.1
Content-type: application/json

{
   "CustomActionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteCustomAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteCustomAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomActionArn](#API_DeleteCustomAction_RequestSyntax) **   <a name="qdevinchatapps-DeleteCustomAction-request-CustomActionArn"></a>
The fully defined ARN of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot::[0-9]{12}:custom-action/[a-zA-Z0-9_-]{1,64}`
Required: Yes

## Response Syntax
<a name="API_DeleteCustomAction_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteCustomAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteCustomAction_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** InvalidRequestException **
Your request input doesn't meet the constraints required by Amazon Q Developer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
We were unable to find the resource for your request
HTTP Status Code: 404

 ** UnauthorizedException **
The request was rejected because it doesn't have valid credentials for the target resource.
HTTP Status Code: 403

## See Also
<a name="API_DeleteCustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/DeleteCustomAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/DeleteCustomAction)
