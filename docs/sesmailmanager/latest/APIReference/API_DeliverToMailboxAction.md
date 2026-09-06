---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_DeliverToMailboxAction.html
---

# DeliverToMailboxAction
<a name="API_DeliverToMailboxAction"></a>

This action to delivers an email to a mailbox.

## Contents
<a name="API_DeliverToMailboxAction_Contents"></a>

 ** MailboxArn **   <a name="sesmailmanager-Type-DeliverToMailboxAction-MailboxArn"></a>
The Amazon Resource Name (ARN) of a WorkMail organization to deliver the email to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** RoleArn **   <a name="sesmailmanager-Type-DeliverToMailboxAction-RoleArn"></a>
The Amazon Resource Name (ARN) of an IAM role to use to execute this action. The role must have access to the workmail:DeliverToMailbox API.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:_/+=,@.#-]+`
Required: Yes

 ** ActionFailurePolicy **   <a name="sesmailmanager-Type-DeliverToMailboxAction-ActionFailurePolicy"></a>
A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the mailbox ARN is no longer valid.
Type: String
Valid Values: `CONTINUE | DROP`
Required: No

## See Also
<a name="API_DeliverToMailboxAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/DeliverToMailboxAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/DeliverToMailboxAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/DeliverToMailboxAction)
