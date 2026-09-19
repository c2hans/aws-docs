---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEventAttachment.html
---

# NotificationEventAttachment
<a name="API_NotificationEventAttachment"></a>

A file attached to a notification event.

## Contents
<a name="API_NotificationEventAttachment_Contents"></a>

 ** contentType **   <a name="Notifications-Type-NotificationEventAttachment-contentType"></a>
The MIME content type of the attachment, for example `application/pdf`.
Type: String
Pattern: `[a-zA-Z0-9]+/[a-zA-Z0-9][a-zA-Z0-9!#$&\-^_.+]*`
Required: Yes

 ** displayName **   <a name="Notifications-Type-NotificationEventAttachment-displayName"></a>
The name of the attachment that recipients see.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** attachmentDownloadUrl **   <a name="Notifications-Type-NotificationEventAttachment-attachmentDownloadUrl"></a>
A temporary URL for downloading the attachment. The URL expires shortly after it's issued.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `(https?):\/\/.*`
Required: No

## See Also
<a name="API_NotificationEventAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationEventAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationEventAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationEventAttachment)
