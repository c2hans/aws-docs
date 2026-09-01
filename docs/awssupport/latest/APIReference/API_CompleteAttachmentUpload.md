---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_CompleteAttachmentUpload.html
---

# CompleteAttachmentUpload
<a name="API_CompleteAttachmentUpload"></a>

Completes an attachment upload that was started with [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md). After you upload a part of the file to its presigned Amazon S3 URL, call `CompleteAttachmentUpload` with the `partIndex` and `eTag` of that part. You can include one part per call, or multiple parts in a single call. After `CompleteAttachmentUpload` has been called for every part of the file, the service processes the upload asynchronously. The `attachment-ready` status might not be reflected immediately. Use [DescribeAttachmentUploadStatus](API_DescribeAttachmentUploadStatus.md) to poll for the `uploadStatus` to become `attachment-ready` before passing the `uploadId` to [CreateCase](API_CreateCase.md) or [AddCommunicationToCase](API_AddCommunicationToCase.md).

## Request Syntax
<a name="API_CompleteAttachmentUpload_RequestSyntax"></a>

```
{
   "completedUploads": [
      {
         "eTag": "{{string}}",
         "partIndex": {{number}}
      }
   ],
   "dryRun": {{boolean}},
   "uploadId": "{{string}}"
}
```

## Request Parameters
<a name="API_CompleteAttachmentUpload_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [completedUploads](#API_CompleteAttachmentUpload_RequestSyntax) **   <a name="AWSSupport-CompleteAttachmentUpload-request-completedUploads"></a>
The list of parts being reported as completed in this call. Each entry must contain the `partIndex` of an uploaded part and the `ETag` returned by Amazon S3 when that part was uploaded.
Type: Array of [CompletedUpload](API_CompletedUpload.md) objects

 ** [dryRun](#API_CompleteAttachmentUpload_RequestSyntax) **   <a name="AWSSupport-CompleteAttachmentUpload-request-dryRun"></a>
Specifies whether to validate the request without actually completing the upload. When set to `true`, the request is validated but the upload isn't finalized, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [uploadId](#API_CompleteAttachmentUpload_RequestSyntax) **   <a name="AWSSupport-CompleteAttachmentUpload-request-uploadId"></a>
The identifier associated with the upload to complete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Response Syntax
<a name="API_CompleteAttachmentUpload_ResponseSyntax"></a>

```
{
   "uploadStatus": "string"
}
```

## Response Elements
<a name="API_CompleteAttachmentUpload_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [uploadStatus](#API_CompleteAttachmentUpload_ResponseSyntax) **   <a name="AWSSupport-CompleteAttachmentUpload-response-uploadStatus"></a>
The status of the multipart upload after the operation finalizes the attachment. Valid values: `attachment-ready`, `attachment-not-ready`, and `failed`.
Type: String
Valid Values: `attachment-ready | attachment-not-ready | failed`

## Errors
<a name="API_CompleteAttachmentUpload_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

 ** UploadIdNotFound **
The specified `uploadId` couldn't be located.
HTTP Status Code: 400

## See Also
<a name="API_CompleteAttachmentUpload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/CompleteAttachmentUpload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/CompleteAttachmentUpload)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
