---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ConnectAttachment.html
---

# ConnectAttachment
<a name="API_ConnectAttachment"></a>

Describes a core network Connect attachment.

## Contents
<a name="API_ConnectAttachment_Contents"></a>

 ** Attachment **   <a name="networkmanager-Type-ConnectAttachment-Attachment"></a>
The attachment details.
Type: [Attachment](API_Attachment.md) object
Required: No

 ** Options **   <a name="networkmanager-Type-ConnectAttachment-Options"></a>
Options for connecting an attachment.
Type: [ConnectAttachmentOptions](API_ConnectAttachmentOptions.md) object
Required: No

 ** TransportAttachmentId **   <a name="networkmanager-Type-ConnectAttachment-TransportAttachmentId"></a>
The ID of the transport attachment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^attachment-([0-9a-f]{8,17})$`
Required: No

## See Also
<a name="API_ConnectAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ConnectAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ConnectAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ConnectAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
