---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_RuleAction.html
---

# RuleAction
<a name="API_RuleAction"></a>

The action for a rule to take. Only one of the contained actions can be set.

## Contents
<a name="API_RuleAction_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AddHeader **   <a name="sesmailmanager-Type-RuleAction-AddHeader"></a>
This action adds a header. This can be used to add arbitrary email headers.
Type: [AddHeaderAction](API_AddHeaderAction.md) object
Required: No

 ** Archive **   <a name="sesmailmanager-Type-RuleAction-Archive"></a>
This action archives the email. This can be used to deliver an email to an archive.
Type: [ArchiveAction](API_ArchiveAction.md) object
Required: No

 ** Bounce **   <a name="sesmailmanager-Type-RuleAction-Bounce"></a>
This action sends a bounce response for the email.
Type: [BounceAction](API_BounceAction.md) object
Required: No

 ** DeliverToMailbox **   <a name="sesmailmanager-Type-RuleAction-DeliverToMailbox"></a>
This action delivers an email to a WorkMail mailbox.
Type: [DeliverToMailboxAction](API_DeliverToMailboxAction.md) object
Required: No

 ** DeliverToQBusiness **   <a name="sesmailmanager-Type-RuleAction-DeliverToQBusiness"></a>
This action delivers an email to an Amazon Q Business application for ingestion into its knowledge base.
Type: [DeliverToQBusinessAction](API_DeliverToQBusinessAction.md) object
Required: No

 ** Drop **   <a name="sesmailmanager-Type-RuleAction-Drop"></a>
This action terminates the evaluation of rules in the rule set.
Type: [DropAction](API_DropAction.md) object
Required: No

 ** InvokeLambda **   <a name="sesmailmanager-Type-RuleAction-InvokeLambda"></a>
This action invokes an AWS Lambda function to process the email.
Type: [InvokeLambdaAction](API_InvokeLambdaAction.md) object
Required: No

 ** PublishToSns **   <a name="sesmailmanager-Type-RuleAction-PublishToSns"></a>
This action publishes the email content to an Amazon SNS topic.
Type: [SnsAction](API_SnsAction.md) object
Required: No

 ** Relay **   <a name="sesmailmanager-Type-RuleAction-Relay"></a>
This action relays the email to another SMTP server.
Type: [RelayAction](API_RelayAction.md) object
Required: No

 ** ReplaceRecipient **   <a name="sesmailmanager-Type-RuleAction-ReplaceRecipient"></a>
The action replaces certain or all recipients with a different set of recipients.
Type: [ReplaceRecipientAction](API_ReplaceRecipientAction.md) object
Required: No

 ** Send **   <a name="sesmailmanager-Type-RuleAction-Send"></a>
This action sends the email to the internet.
Type: [SendAction](API_SendAction.md) object
Required: No

 ** WriteToS3 **   <a name="sesmailmanager-Type-RuleAction-WriteToS3"></a>
This action writes the MIME content of the email to an S3 bucket.
Type: [S3Action](API_S3Action.md) object
Required: No

## See Also
<a name="API_RuleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/RuleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/RuleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/RuleAction)
