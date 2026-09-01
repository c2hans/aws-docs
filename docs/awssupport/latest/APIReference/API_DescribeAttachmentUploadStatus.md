---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_DescribeAttachmentUploadStatus.html
---

# DescribeAttachmentUploadStatus
<a name="API_DescribeAttachmentUploadStatus"></a>

Returns the current status, file name, and progress of a multipart attachment upload that was started with [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md). Use this operation to track where an upload is in the workflow. While parts are still being uploaded and reported through [CompleteAttachmentUpload](API_CompleteAttachmentUpload.md), the `uploadStatus` is `attachment-not-ready` and `uploadProgress` reports the total number of parts and how many have been completed so far. After every part has been reported and the service finishes processing the upload asynchronously, the `uploadStatus` becomes `attachment-ready` and the `uploadId` can be attached to a case through [CreateCase](API_CreateCase.md) or [AddCommunicationToCase](API_AddCommunicationToCase.md).

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_DescribeAttachmentUploadStatus_RequestSyntax"></a>

```
{
   "dryRun": {{boolean}},
   "uploadId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAttachmentUploadStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [dryRun](#API_DescribeAttachmentUploadStatus_RequestSyntax) **   <a name="AWSSupport-DescribeAttachmentUploadStatus-request-dryRun"></a>
Specifies whether to validate the request without actually returning upload status. When set to `true`, the request is validated but no status is returned, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

 ** [uploadId](#API_DescribeAttachmentUploadStatus_RequestSyntax) **   <a name="AWSSupport-DescribeAttachmentUploadStatus-request-uploadId"></a>
The unique identifier for the upload. The `uploadId` is returned by [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md) when you initiate the upload.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Response Syntax
<a name="API_DescribeAttachmentUploadStatus_ResponseSyntax"></a>

```
{
   "fileName": "string",
   "uploadProgress": {
      "completedPartsCount": number,
      "totalParts": number
   },
   "uploadStatus": "string"
}
```

## Response Elements
<a name="API_DescribeAttachmentUploadStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [fileName](#API_DescribeAttachmentUploadStatus_ResponseSyntax) **   <a name="AWSSupport-DescribeAttachmentUploadStatus-response-fileName"></a>
The name of the file being uploaded, including the file extension.
Type: String

 ** [uploadProgress](#API_DescribeAttachmentUploadStatus_ResponseSyntax) **   <a name="AWSSupport-DescribeAttachmentUploadStatus-response-uploadProgress"></a>
The progress of the multipart upload, including the total number of parts and the number of parts that have been successfully uploaded.
Type: [UploadProgress](API_UploadProgress.md) object

 ** [uploadStatus](#API_DescribeAttachmentUploadStatus_ResponseSyntax) **   <a name="AWSSupport-DescribeAttachmentUploadStatus-response-uploadStatus"></a>
The current status of the multipart upload. Valid values: `attachment-ready`, `attachment-not-ready`, and `failed`.
Type: String
Valid Values: `attachment-ready | attachment-not-ready | failed`

## Errors
<a name="API_DescribeAttachmentUploadStatus_Errors"></a>

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
<a name="API_DescribeAttachmentUploadStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeAttachmentUploadStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/DescribeAttachmentUploadStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
