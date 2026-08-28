---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateCustomAction.html
---

# UpdateCustomAction
<a name="API_UpdateCustomAction"></a>

Updates a custom action.

## Request Syntax
<a name="API_UpdateCustomAction_RequestSyntax"></a>

```
POST /update-custom-action HTTP/1.1
Content-type: application/json

{
   "AliasName": "{{string}}",
   "Attachments": [
      {
         "ButtonText": "{{string}}",
         "Criteria": [
            {
               "Operator": "{{string}}",
               "Value": "{{string}}",
               "VariableName": "{{string}}"
            }
         ],
         "NotificationType": "{{string}}",
         "Variables": {
            "{{string}}" : "{{string}}"
         }
      }
   ],
   "CustomActionArn": "{{string}}",
   "Definition": {
      "CommandText": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateCustomAction_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateCustomAction_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AliasName](#API_UpdateCustomAction_RequestSyntax) **   <a name="qdevinchatapps-UpdateCustomAction-request-AliasName"></a>
The name used to invoke this action in the chat channel. For example, `@Amazon Q run my-alias`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** [Attachments](#API_UpdateCustomAction_RequestSyntax) **   <a name="qdevinchatapps-UpdateCustomAction-request-Attachments"></a>
Defines when this custom action button should be attached to a notification.
Type: Array of [CustomActionAttachment](API_CustomActionAttachment.md) objects
Required: No

 ** [CustomActionArn](#API_UpdateCustomAction_RequestSyntax) **   <a name="qdevinchatapps-UpdateCustomAction-request-CustomActionArn"></a>
The fully defined Amazon Resource Name (ARN) of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot::[0-9]{12}:custom-action/[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** [Definition](#API_UpdateCustomAction_RequestSyntax) **   <a name="qdevinchatapps-UpdateCustomAction-request-Definition"></a>
The definition of the command to run when invoked as an alias or as an action button.
Type: [CustomActionDefinition](API_CustomActionDefinition.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateCustomAction_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CustomActionArn": "string"
}
```

## Response Elements
<a name="API_UpdateCustomAction_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CustomActionArn](#API_UpdateCustomAction_ResponseSyntax) **   <a name="qdevinchatapps-UpdateCustomAction-response-CustomActionArn"></a>
The fully defined ARN of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot::[0-9]{12}:custom-action/[a-zA-Z0-9_-]{1,64}`

## Errors
<a name="API_UpdateCustomAction_Errors"></a>

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
<a name="API_UpdateCustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chatbot-2017-10-11/UpdateCustomAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/UpdateCustomAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
