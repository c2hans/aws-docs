---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_AttachmentInput.html
---

# AttachmentInput
<a name="API_AttachmentInput"></a>

This is either a file directly uploaded into a web experience chat or a reference to an existing attachment that is part of a web experience chat.

## Contents
<a name="API_AttachmentInput_Contents"></a>

 ** copyFrom **   <a name="qbusiness-Type-AttachmentInput-copyFrom"></a>
A reference to an existing attachment.
Type: [CopyFromSource](API_CopyFromSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** data **   <a name="qbusiness-Type-AttachmentInput-data"></a>
The contents of the attachment.
Type: Base64-encoded binary data object
Required: No

 ** name **   <a name="qbusiness-Type-AttachmentInput-name"></a>
The filename of the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `\P{C}*`
Required: No

## See Also
<a name="API_AttachmentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/AttachmentInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/AttachmentInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/AttachmentInput)
