---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_MessageTemplateAttachment.html
---

# MessageTemplateAttachment
<a name="API_amazon-q-connect_MessageTemplateAttachment"></a>

Information about the message template attachment.

## Contents
<a name="API_amazon-q-connect_MessageTemplateAttachment_Contents"></a>

 ** attachmentId **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-attachmentId"></a>
The identifier of the attachment file.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** contentDisposition **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-contentDisposition"></a>
The presentation information for the attachment file.
Type: String
Valid Values: `ATTACHMENT`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-name"></a>
The name of the attachment file being uploaded. The name should include the file extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}_\s&@()+,;=\-]+\.[A-Za-z0-9]+`
Required: Yes

 ** uploadedTime **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-uploadedTime"></a>
The timestamp when the attachment file was uploaded.
Type: Timestamp
Required: Yes

 ** url **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-url"></a>
A pre-signed Amazon S3 URL that can be used to download the attachment file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** urlExpiry **   <a name="connect-Type-amazon-q-connect_MessageTemplateAttachment-urlExpiry"></a>
The expiration time of the pre-signed Amazon S3 URL.
Type: Timestamp
Required: Yes

## See Also
<a name="API_amazon-q-connect_MessageTemplateAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
