---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_MessageTemplateContentProvider.html
---

# MessageTemplateContentProvider
<a name="API_amazon-q-connect_MessageTemplateContentProvider"></a>

The container of message template content.

## Contents
<a name="API_amazon-q-connect_MessageTemplateContentProvider_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** email **   <a name="connect-Type-amazon-q-connect_MessageTemplateContentProvider-email"></a>
The content of the message template that applies to the email channel subtype.
Type: [EmailMessageTemplateContent](API_amazon-q-connect_EmailMessageTemplateContent.md) object
Required: No

 ** push **   <a name="connect-Type-amazon-q-connect_MessageTemplateContentProvider-push"></a>
The content of the message template that applies to the push channel subtype.
Type: [PushMessageTemplateContent](API_amazon-q-connect_PushMessageTemplateContent.md) object
Required: No

 ** sms **   <a name="connect-Type-amazon-q-connect_MessageTemplateContentProvider-sms"></a>
The content of the message template that applies to the SMS channel subtype.
Type: [SMSMessageTemplateContent](API_amazon-q-connect_SMSMessageTemplateContent.md) object
Required: No

 ** whatsApp **   <a name="connect-Type-amazon-q-connect_MessageTemplateContentProvider-whatsApp"></a>
The content of the message template that applies to the WHATSAPP channel subtype.
Type: [WhatsAppMessageTemplateContent](API_amazon-q-connect_WhatsAppMessageTemplateContent.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateContentProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateContentProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateContentProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateContentProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
