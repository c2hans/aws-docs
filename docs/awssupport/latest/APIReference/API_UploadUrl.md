---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_UploadUrl.html
---

# UploadUrl
<a name="API_UploadUrl"></a>

A presigned URL for uploading a single part of a multipart attachment upload, along with the part index and the date and time the URL expires. Returned by [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md).

## Contents
<a name="API_UploadUrl_Contents"></a>

 ** expiryDate **   <a name="AWSSupport-Type-UploadUrl-expiryDate"></a>
The date and time, in ISO-8601 format, when the presigned URL expires. Upload the part before this time.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 30.

 ** partIndex **   <a name="AWSSupport-Type-UploadUrl-partIndex"></a>
The index of the part that this URL uploads.
Type: Integer

 ** url **   <a name="AWSSupport-Type-UploadUrl-url"></a>
The presigned HTTPS URL that you use to upload a single part with HTTP `PUT`. Upload URLs are served from `uploadv1.attachments.support.{region}.amazonaws.com`. The `uploadv1` prefix is subject to change.
Type: String
Length Constraints: Minimum length of 8.
Pattern: `^https://[a-zA-Z0-9][a-zA-Z0-9.-]*[a-zA-Z0-9]\.[a-zA-Z]{2,}(/.*)?$`

## See Also
<a name="API_UploadUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/UploadUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/UploadUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/UploadUrl)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
