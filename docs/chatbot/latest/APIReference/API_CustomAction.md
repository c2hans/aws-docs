---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomAction.html
---

# CustomAction
<a name="API_CustomAction"></a>

Represents a parameterized command that can be invoked as an alias or as a notification button in the chat client.

## Contents
<a name="API_CustomAction_Contents"></a>

 ** CustomActionArn **   <a name="qdevinchatapps-Type-CustomAction-CustomActionArn"></a>
The fully defined Amazon Resource Name (ARN) of the custom action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:chatbot::[0-9]{12}:custom-action/[a-zA-Z0-9_-]{1,64}`
Required: Yes

 ** Definition **   <a name="qdevinchatapps-Type-CustomAction-Definition"></a>
The definition of the command to run when invoked an alias or as an action button.
Type: [CustomActionDefinition](API_CustomActionDefinition.md) object
Required: Yes

 ** ActionName **   <a name="qdevinchatapps-Type-CustomAction-ActionName"></a>
The name of the custom action that is included in the ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** AliasName **   <a name="qdevinchatapps-Type-CustomAction-AliasName"></a>
The name used to invoke this action in the chat channel. For example, `@Amazon Q run my-alias`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** Attachments **   <a name="qdevinchatapps-Type-CustomAction-Attachments"></a>
Defines when this custom action button should be attached to a notification.
Type: Array of [CustomActionAttachment](API_CustomActionAttachment.md) objects
Required: No

## See Also
<a name="API_CustomAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CustomAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CustomAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CustomAction)
