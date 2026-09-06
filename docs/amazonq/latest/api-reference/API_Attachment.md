---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Attachment.html
---

# Attachment
<a name="API_Attachment"></a>

An attachment in an Amazon Q Business conversation.

## Contents
<a name="API_Attachment_Contents"></a>

 ** attachmentId **   <a name="qbusiness-Type-Attachment-attachmentId"></a>
The identifier of the Amazon Q Business attachment.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** conversationId **   <a name="qbusiness-Type-Attachment-conversationId"></a>
The identifier of the Amazon Q Business conversation the attachment is associated with.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** copyFrom **   <a name="qbusiness-Type-Attachment-copyFrom"></a>
A CopyFromSource containing a reference to the original source of the Amazon Q Business attachment.
Type: [CopyFromSource](API_CopyFromSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** createdAt **   <a name="qbusiness-Type-Attachment-createdAt"></a>
The Unix timestamp when the Amazon Q Business attachment was created.
Type: Timestamp
Required: No

 ** error **   <a name="qbusiness-Type-Attachment-error"></a>
ErrorDetail providing information about a Amazon Q Business attachment error.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** fileSize **   <a name="qbusiness-Type-Attachment-fileSize"></a>
Size in bytes of the Amazon Q Business attachment.
Type: Integer
Required: No

 ** fileType **   <a name="qbusiness-Type-Attachment-fileType"></a>
Filetype of the Amazon Q Business attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** md5chksum **   <a name="qbusiness-Type-Attachment-md5chksum"></a>
MD5 checksum of the Amazon Q Business attachment contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** name **   <a name="qbusiness-Type-Attachment-name"></a>
Filename of the Amazon Q Business attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

 ** status **   <a name="qbusiness-Type-Attachment-status"></a>
AttachmentStatus of the Amazon Q Business attachment.
Type: String
Valid Values: `FAILED | SUCCESS`
Required: No

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Attachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Attachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Attachment)
