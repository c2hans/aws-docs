---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CompletedUpload.html
---

# CompletedUpload
<a name="API_CompletedUpload"></a>

Identifies a single uploaded part of a multipart attachment upload. Pass a list of `CompletedUpload` objects to [CompleteAttachmentUpload](API_CompleteAttachmentUpload.md) to finalize the upload.

## Contents
<a name="API_CompletedUpload_Contents"></a>

 ** eTag **   <a name="AWSSupport-Type-CompletedUpload-eTag"></a>
The ETag returned in the response headers when the part was uploaded to Amazon S3. The `ETag` value identifies the part contents.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** partIndex **   <a name="AWSSupport-Type-CompletedUpload-partIndex"></a>
The index of the uploaded part. This is the same `partIndex` value returned for the corresponding entry in the `uploadUrls` field of the `GetAttachmentUploadLinks` response.
Type: Integer

## See Also
<a name="API_CompletedUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/CompletedUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/CompletedUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/CompletedUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
