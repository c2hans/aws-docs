---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentOutput.html
---

# AttachmentOutput
<a name="API_AttachmentOutput"></a>

The details of a file uploaded during chat.

## Contents
<a name="API_AttachmentOutput_Contents"></a>

 ** attachmentId **   <a name="qbusiness-Type-AttachmentOutput-attachmentId"></a>
The unique identifier of the Amazon Q Business attachment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** conversationId **   <a name="qbusiness-Type-AttachmentOutput-conversationId"></a>
The unique identifier of the Amazon Q Business conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** error **   <a name="qbusiness-Type-AttachmentOutput-error"></a>
An error associated with a file uploaded during chat.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** name **   <a name="qbusiness-Type-AttachmentOutput-name"></a>
The name of a file uploaded during chat.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** status **   <a name="qbusiness-Type-AttachmentOutput-status"></a>
The status of a file uploaded during chat.
Type: String
Valid Values: `FAILED | SUCCESS`
Required: No

## See Also
<a name="API_AttachmentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AttachmentOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AttachmentOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AttachmentOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
