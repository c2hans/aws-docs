---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_Message.html
---

# Message
<a name="API_Message"></a>

The object that provides message text and its type.

## Contents
<a name="API_Message_Contents"></a>

 ** customPayload **   <a name="lexv2-Type-Message-customPayload"></a>
A message in a custom format defined by the client application.
Type: [CustomPayload](API_CustomPayload.md) object
Required: No

 ** imageResponseCard **   <a name="lexv2-Type-Message-imageResponseCard"></a>
A message that defines a response card that the client application can show to the user.
Type: [ImageResponseCard](API_ImageResponseCard.md) object
Required: No

 ** plainTextMessage **   <a name="lexv2-Type-Message-plainTextMessage"></a>
A message in plain text format.
Type: [PlainTextMessage](API_PlainTextMessage.md) object
Required: No

 ** ssmlMessage **   <a name="lexv2-Type-Message-ssmlMessage"></a>
A message in Speech Synthesis Markup Language (SSML).
Type: [SSMLMessage](API_SSMLMessage.md) object
Required: No

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/Message)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
