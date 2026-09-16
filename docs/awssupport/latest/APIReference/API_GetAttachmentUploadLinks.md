---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetAttachmentUploadLinks.html
---

# GetAttachmentUploadLinks
<a name="API_GetAttachmentUploadLinks"></a>

Returns one or more presigned upload URLs for uploading a large file attachment to a support case by using a multipart upload workflow. The maximum file size that you can upload with this workflow is 150 MB, and parts can be up to 100 MB each. Initiate a new upload by providing `fileName` and `fileSizeBytes`; the response returns a unique `uploadId`, the part size, the total number of parts, and a list of presigned upload URLs for the requested range of parts. A maximum of 10 upload URLs are returned per call. To retrieve more upload URLs for an upload that's already in progress, call `GetAttachmentUploadLinks` again with the existing `uploadId` and a new `uploadRange`.

Upload each part to its presigned URL by using HTTP `PUT` and capture the ETag from the response. After you upload all parts, call [CompleteAttachmentUpload](API_CompleteAttachmentUpload.md) with the `uploadId` and the list of part indexes and ETags to finalize the upload. You can then attach the upload to a case by passing the `uploadId` in the `uploadIds` parameter of [CreateCase](API_CreateCase.md) or [AddCommunicationToCase](API_AddCommunicationToCase.md). To monitor progress before completion, call [DescribeAttachmentUploadStatus](API_DescribeAttachmentUploadStatus.md).

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_GetAttachmentUploadLinks_RequestSyntax"></a>

```
{
   "dryRun": {{boolean}},
   "fileName": "{{string}}",
   "fileSizeBytes": {{number}},
   "uploadId": "{{string}}",
   "uploadRange": {
      "endIndex": {{number}},
      "startIndex": {{number}}
   }
}
```

## Request Parameters
<a name="API_GetAttachmentUploadLinks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dryRun](#API_GetAttachmentUploadLinks_RequestSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-request-dryRun"></a>
Specifies whether to validate the request without actually generating upload URLs. When set to `true`, the request is validated but no URLs are returned, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [fileName](#API_GetAttachmentUploadLinks_RequestSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-request-fileName"></a>
The name of the file to upload, including the file extension. This value is required when you initiate a new upload.
Type: String

 ** [fileSizeBytes](#API_GetAttachmentUploadLinks_RequestSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-request-fileSizeBytes"></a>
The total size of the file in bytes. The service uses this value to calculate the total number of parts and the size of each part. Required when you initiate a new upload (when `uploadId` isn't provided). Valid range: 1 to 157,286,400 bytes (approximately 150 MB).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 157286400.

 ** [uploadId](#API_GetAttachmentUploadLinks_RequestSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-request-uploadId"></a>
The unique identifier of an in-progress multipart upload, returned by a previous call to `GetAttachmentUploadLinks`. Specify `uploadId` to retrieve additional presigned upload URLs for an upload that has already been initiated. Required when `fileSizeBytes` isn't provided. Length: 1 to 2,048 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [uploadRange](#API_GetAttachmentUploadLinks_RequestSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-request-uploadRange"></a>
The range of part indexes for which to return presigned upload URLs. Use this parameter to page through the upload URLs for a large file across multiple calls. If you omit this parameter, the service determines the range to return.
Type: [UploadRange](API_UploadRange.md) object

## Response Syntax
<a name="API_GetAttachmentUploadLinks_ResponseSyntax"></a>

```
{
   "nextIndex": number,
   "partSizeBytes": number,
   "totalParts": number,
   "uploadId": "string",
   "uploadUrls": [
      {
         "expiryDate": "string",
         "partIndex": number,
         "url": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetAttachmentUploadLinks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextIndex](#API_GetAttachmentUploadLinks_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-response-nextIndex"></a>
The next part index to request presigned URLs for. If all upload URLs for the file have been returned, this field is `null`. Use this value as the `startIndex` in `uploadRange` on a subsequent call to `GetAttachmentUploadLinks` to retrieve the next batch of upload URLs.
Type: Integer

 ** [partSizeBytes](#API_GetAttachmentUploadLinks_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-response-partSizeBytes"></a>
The size, in bytes, of each part. Split the file into parts of this size before you upload them to the presigned URLs. For an upload with `n` total parts, parts 1 through `n` - 1 are exactly this size; the last part may be smaller. Maximum: 104,857,600 bytes (approximately 100 MB).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 104857600.

 ** [totalParts](#API_GetAttachmentUploadLinks_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-response-totalParts"></a>
The total number of parts that the file is split into. Upload one part to each presigned URL.
Type: Integer

 ** [uploadId](#API_GetAttachmentUploadLinks_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-response-uploadId"></a>
The unique identifier for the multipart upload. Use this value in subsequent calls to `GetAttachmentUploadLinks`, [DescribeAttachmentUploadStatus](API_DescribeAttachmentUploadStatus.md), and [CompleteAttachmentUpload](API_CompleteAttachmentUpload.md), and to attach the upload to a case through the `uploadIds` parameter on [CreateCase](API_CreateCase.md) or [AddCommunicationToCase](API_AddCommunicationToCase.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [uploadUrls](#API_GetAttachmentUploadLinks_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentUploadLinks-response-uploadUrls"></a>
The list of presigned upload URLs for the requested range of parts. The list contains at most 10 URLs per call. Upload each part to its corresponding URL by using HTTP `PUT` before the URL expires.
Type: Array of [UploadUrl](API_UploadUrl.md) objects

## Errors
<a name="API_GetAttachmentUploadLinks_Errors"></a>

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
<a name="API_GetAttachmentUploadLinks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/GetAttachmentUploadLinks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/GetAttachmentUploadLinks)
