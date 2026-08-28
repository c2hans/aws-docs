---
source_url: https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionAttachment.html
---

# CustomActionAttachment
<a name="API_CustomActionAttachment"></a>

Defines when a custom action button should be attached to a notification.

## Contents
<a name="API_CustomActionAttachment_Contents"></a>

 ** ButtonText **   <a name="qdevinchatapps-Type-CustomActionAttachment-ButtonText"></a>
The text of the button that appears on the notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\S\s]+`
Required: No

 ** Criteria **   <a name="qdevinchatapps-Type-CustomActionAttachment-Criteria"></a>
The criteria for when a button should be shown based on values in the notification.
Type: Array of [CustomActionAttachmentCriteria](API_CustomActionAttachmentCriteria.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** NotificationType **   <a name="qdevinchatapps-Type-CustomActionAttachment-NotificationType"></a>
The type of notification that the custom action should be attached to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** Variables **   <a name="qdevinchatapps-Type-CustomActionAttachment-Variables"></a>
The variables to extract from the notification.
Type: String to string map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[A-Za-z0-9-_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Value Pattern: `[\x21-\x7F]+`
Required: No

## See Also
<a name="API_CustomActionAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chatbot-2017-10-11/CustomActionAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chatbot-2017-10-11/CustomActionAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chatbot-2017-10-11/CustomActionAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Developer in chat applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chatbot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
