---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_Communication.html
---

# Communication
<a name="API_Communication"></a>

A communication associated with a support case. The communication consists of the case ID, the message body, attachment information, the submitter of the communication, and the date and time of the communication.

## Contents
<a name="API_Communication_Contents"></a>

 ** attachments **   <a name="AWSSupport-Type-Communication-attachments"></a>
Information about all attachments on the case communication. This includes attachments added through `AddAttachmentsToSet` and attachments uploaded through `GetAttachmentUploadLinks`.
Use this field to enumerate every attachment on the communication. To download an attachment listed in this field, use [GetAttachmentDownloadLink](API_GetAttachmentDownloadLink.md). `GetAttachmentDownloadLink` returns a presigned URL that works for attachments of any size.
Type: Array of [AttachmentDetails](API_AttachmentDetails.md) objects

 ** attachmentSet **   <a name="AWSSupport-Type-Communication-attachmentSet"></a>
Information about the attachments to the case communication that are 5 MB or smaller. This field doesn't include attachments larger than 5 MB. To enumerate every attachment on the communication, including attachments larger than 5 MB, use the `attachments` field instead.
Type: Array of [AttachmentDetails](API_AttachmentDetails.md) objects

 ** body **   <a name="AWSSupport-Type-Communication-body"></a>
The text of the communication between the customer and AWS Support.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8000.

 ** caseId **   <a name="AWSSupport-Type-Communication-caseId"></a>
The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-*12345678910-exen-2025-c4c1d2bf33c5cf47*
Type: String

 ** submittedBy **   <a name="AWSSupport-Type-Communication-submittedBy"></a>
The identity of the account that submitted, or responded to, the support case. Customer entries include the IAM role as well as the email address (for example, "AdminRole (Role) <janedoe@example.com>). Entries from the AWS Support team display "Amazon Web Services," and don't show an email address.
Type: String

 ** timeCreated **   <a name="AWSSupport-Type-Communication-timeCreated"></a>
The time the communication was created.
Type: String

## See Also
<a name="API_Communication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/Communication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/Communication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/Communication)
