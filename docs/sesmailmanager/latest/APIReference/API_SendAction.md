---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_SendAction.html
---

# SendAction
<a name="API_SendAction"></a>

Sends the email to the internet using the ses:SendRawEmail API.

## Contents
<a name="API_SendAction_Contents"></a>

 ** RoleArn **   <a name="sesmailmanager-Type-SendAction-RoleArn"></a>
The Amazon Resource Name (ARN) of the role to use for this action. This role must have access to the ses:SendRawEmail API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-SendAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the sendRawEmail API.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

## See Also
<a name="API_SendAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/SendAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/SendAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/SendAction)
