---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisAttachment.html
---

# RealTimeContactAnalysisAttachment
<a name="API_RealTimeContactAnalysisAttachment"></a>

Object that describes attached file.

## Contents
<a name="API_RealTimeContactAnalysisAttachment_Contents"></a>

 ** AttachmentId **   <a name="connect-Type-RealTimeContactAnalysisAttachment-AttachmentId"></a>
A unique identifier for the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** AttachmentName **   <a name="connect-Type-RealTimeContactAnalysisAttachment-AttachmentName"></a>
A case-sensitive name of the attachment being uploaded. Can be redacted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ContentType **   <a name="connect-Type-RealTimeContactAnalysisAttachment-ContentType"></a>
Describes the MIME file type of the attachment. For a list of supported file types, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html) in the *Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Status **   <a name="connect-Type-RealTimeContactAnalysisAttachment-Status"></a>
Status of the attachment.
Type: String
Valid Values: `APPROVED | REJECTED | IN_PROGRESS`
Required: No

## See Also
<a name="API_RealTimeContactAnalysisAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisAttachment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
