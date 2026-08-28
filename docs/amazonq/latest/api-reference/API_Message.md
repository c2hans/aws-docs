---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Message.html
---

# Message
<a name="API_Message"></a>

A message in an Amazon Q Business web experience.

## Contents
<a name="API_Message_Contents"></a>

 ** actionExecution **   <a name="qbusiness-Type-Message-actionExecution"></a>
Performs an Amazon Q Business plugin action during a non-streaming chat conversation.
Type: [ActionExecution](API_ActionExecution.md) object
Required: No

 ** actionReview **   <a name="qbusiness-Type-Message-actionReview"></a>
An output event that Amazon Q Business returns to an user who wants to perform a plugin action during a non-streaming chat conversation. It contains information about the selected action with a list of possible user input fields, some pre-populated by Amazon Q Business.
Type: [ActionReview](API_ActionReview.md) object
Required: No

 ** attachments **   <a name="qbusiness-Type-Message-attachments"></a>
A file directly uploaded into an Amazon Q Business web experience chat.
Type: Array of [AttachmentOutput](API_AttachmentOutput.md) objects
Required: No

 ** body **   <a name="qbusiness-Type-Message-body"></a>
The content of the Amazon Q Business web experience message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `\P{C}*$}`
Required: No

 ** messageId **   <a name="qbusiness-Type-Message-messageId"></a>
The identifier of the Amazon Q Business web experience message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** sourceAttribution **   <a name="qbusiness-Type-Message-sourceAttribution"></a>
The source documents used to generate Amazon Q Business web experience message.
Type: Array of [SourceAttribution](API_SourceAttribution.md) objects
Required: No

 ** time **   <a name="qbusiness-Type-Message-time"></a>
The timestamp of the first Amazon Q Business web experience message.
Type: Timestamp
Required: No

 ** type **   <a name="qbusiness-Type-Message-type"></a>
The type of Amazon Q Business message, whether `HUMAN` or `AI` generated.
Type: String
Valid Values: `USER | SYSTEM`
Required: No

## See Also
<a name="API_Message_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Message)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Message)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Message)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
