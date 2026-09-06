---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_ReplaceRecipientAction.html
---

# ReplaceRecipientAction
<a name="API_ReplaceRecipientAction"></a>

This action replaces the email envelope recipients with the given list of recipients. If the condition of this action applies only to a subset of recipients, only those recipients are replaced with the recipients specified in the action. The message contents and headers are unaffected by this action, only the envelope recipients are updated.

## Contents
<a name="API_ReplaceRecipientAction_Contents"></a>

 ** ReplaceWith **   <a name="sesmailmanager-Type-ReplaceRecipientAction-ReplaceWith"></a>
This action specifies the replacement recipient email addresses to insert.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 254.
Pattern: `[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+`
Required: No

## See Also
<a name="API_ReplaceRecipientAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/ReplaceRecipientAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/ReplaceRecipientAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/ReplaceRecipientAction)
