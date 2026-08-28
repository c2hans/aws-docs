---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_RegistrationAttachmentsInformation.html
---

# RegistrationAttachmentsInformation
<a name="API_RegistrationAttachmentsInformation"></a>

Provides information on the specified registration attachments.

## Contents
<a name="API_RegistrationAttachmentsInformation_Contents"></a>

 ** AttachmentStatus **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-AttachmentStatus"></a>
The status of the registration attachment.
+  `UPLOAD_IN_PROGRESS` The attachment is being uploaded.
+  `UPLOAD_COMPLETE` The attachment has been uploaded.
+  `UPLOAD_FAILED` The attachment failed to uploaded.
+  `DELETED` The attachment has been deleted..
Type: String
Valid Values: `UPLOAD_IN_PROGRESS | UPLOAD_COMPLETE | UPLOAD_FAILED | DELETED`
Required: Yes

 ** CreatedTimestamp **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-CreatedTimestamp"></a>
The time when the registration attachment was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp
Required: Yes

 ** RegistrationAttachmentArn **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-RegistrationAttachmentArn"></a>
The Amazon Resource Name (ARN) for the registration attachment.
Type: String
Required: Yes

 ** RegistrationAttachmentId **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-RegistrationAttachmentId"></a>
The unique identifier for the registration attachment.
Type: String
Required: Yes

 ** AttachmentUploadErrorReason **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-AttachmentUploadErrorReason"></a>
A description of why the upload didn't successfully complete.
Type: String
Valid Values: `INTERNAL_ERROR`
Required: No

 ** AttachmentUrl **   <a name="pinpoint-Type-RegistrationAttachmentsInformation-AttachmentUrl"></a>
The URL to the document that's associated with the registration attachment.
Type: String
Required: No

## See Also
<a name="API_RegistrationAttachmentsInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentsInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentsInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/RegistrationAttachmentsInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
