---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-participant_AttachmentItem.html
---

# AttachmentItem
<a name="API_connect-participant_AttachmentItem"></a>

The case-insensitive input to indicate standard MIME type that describes the format of the file that will be uploaded.

## Contents
<a name="API_connect-participant_AttachmentItem_Contents"></a>

 ** AttachmentId **   <a name="connect-Type-connect-participant_AttachmentItem-AttachmentId"></a>
A unique identifier for the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** AttachmentName **   <a name="connect-Type-connect-participant_AttachmentItem-AttachmentName"></a>
A case-sensitive name of the attachment being uploaded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ContentType **   <a name="connect-Type-connect-participant_AttachmentItem-ContentType"></a>
Describes the MIME file type of the attachment. For a list of supported file types, see [Feature specifications](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html) in the *Amazon Connect Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** Status **   <a name="connect-Type-connect-participant_AttachmentItem-Status"></a>
Status of the attachment.
Type: String
Valid Values: `APPROVED | REJECTED | IN_PROGRESS`
Required: No

## See Also
<a name="API_connect-participant_AttachmentItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/AttachmentItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/AttachmentItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/AttachmentItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
