---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Attachment.html
---

# Attachment
<a name="API_Attachment"></a>

An attachment to a case communication. The attachment consists of the file name and the content of the file. Each attachment file size should not exceed 5 MB. File types that are supported include the following: pdf, jpeg,.doc, .log, .text

## Contents
<a name="API_Attachment_Contents"></a>

 ** data **   <a name="AWSSupport-Type-Attachment-data"></a>
The content of the attachment file.
Type: Base64-encoded binary data object

 ** fileName **   <a name="AWSSupport-Type-Attachment-fileName"></a>
The name of the attachment file.
Type: String

## See Also
<a name="API_Attachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/Attachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/Attachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/Attachment)
