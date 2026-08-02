---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_EmailMessageTemplateContent.html
---

# EmailMessageTemplateContent
<a name="API_amazon-q-connect_EmailMessageTemplateContent"></a>

The content of the message template that applies to the email channel subtype.

## Contents
<a name="API_amazon-q-connect_EmailMessageTemplateContent_Contents"></a>

 ** body **   <a name="connect-Type-amazon-q-connect_EmailMessageTemplateContent-body"></a>
The body to use in email messages.
Type: [EmailMessageTemplateContentBody](API_amazon-q-connect_EmailMessageTemplateContentBody.md) object
Required: No

 ** headers **   <a name="connect-Type-amazon-q-connect_EmailMessageTemplateContent-headers"></a>
The email headers to include in email messages.
Type: Array of [EmailHeader](API_amazon-q-connect_EmailHeader.md) objects
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Required: No

 ** subject **   <a name="connect-Type-amazon-q-connect_EmailMessageTemplateContent-subject"></a>
The subject line, or title, to use in email messages.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_amazon-q-connect_EmailMessageTemplateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/EmailMessageTemplateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/EmailMessageTemplateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/EmailMessageTemplateContent)
