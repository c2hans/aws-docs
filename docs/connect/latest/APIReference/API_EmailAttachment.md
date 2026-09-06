---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EmailAttachment.html
---

# EmailAttachment
<a name="API_EmailAttachment"></a>

Information about the email attachment files.

## Contents
<a name="API_EmailAttachment_Contents"></a>

 ** FileName **   <a name="connect-Type-EmailAttachment-FileName"></a>
A case-sensitive name of the attached file being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^\P{C}*$`
Required: Yes

 ** S3Url **   <a name="connect-Type-EmailAttachment-S3Url"></a>
The pre-signed URLs for the S3 bucket where the email attachment is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## See Also
<a name="API_EmailAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EmailAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EmailAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EmailAttachment)
