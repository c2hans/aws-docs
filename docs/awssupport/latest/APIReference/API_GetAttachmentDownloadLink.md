---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_GetAttachmentDownloadLink.html
---

# GetAttachmentDownloadLink
<a name="API_GetAttachmentDownloadLink"></a>

Returns a presigned download URL for an attachment that is associated with a case communication. The download link works for an attachment of any size, including attachments added through `AddAttachmentsToSet` and attachments uploaded through [GetAttachmentUploadLinks](API_GetAttachmentUploadLinks.md). The download URL is time-limited and expires at the date and time indicated in the `downloadUrl` response field. Download the attachment from the URL before it expires.

**Note**
You must have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan to use the AWS Support API. If you're in an AWS Region that doesn't offer one of these AWS Support plans, or if you haven't transitioned to one of these plans, you can use the AWS Support API with a Business, Enterprise On-Ramp, or Enterprise Support plan.
If you call the AWS Support API from an account that doesn't have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_GetAttachmentDownloadLink_RequestSyntax"></a>

```
{
   "attachmentId": "{{string}}",
   "dryRun": {{boolean}}
}
```

## Request Parameters
<a name="API_GetAttachmentDownloadLink_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachmentId](#API_GetAttachmentDownloadLink_RequestSyntax) **   <a name="AWSSupport-GetAttachmentDownloadLink-request-attachmentId"></a>
The unique identifier of the attachment for which to retrieve a download link. Attachment IDs are returned in the `AttachmentDetails` objects in the `attachments` field of a [Communication](API_Communication.md) returned by [DescribeCommunications](API_DescribeCommunications.md) or [DescribeCases](API_DescribeCases.md).
Type: String

 ** [dryRun](#API_GetAttachmentDownloadLink_RequestSyntax) **   <a name="AWSSupport-GetAttachmentDownloadLink-request-dryRun"></a>
Specifies whether to validate the request without actually returning a download link. When set to `true`, the request is validated but no URL is returned, and the operation returns a `DryRunOperationException`. When omitted or set to `false`, the request runs normally.
Type: Boolean

## Response Syntax
<a name="API_GetAttachmentDownloadLink_ResponseSyntax"></a>

```
{
   "downloadUrl": {
      "expiryDate": "string",
      "url": "string"
   },
   "fileName": "string"
}
```

## Response Elements
<a name="API_GetAttachmentDownloadLink_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [downloadUrl](#API_GetAttachmentDownloadLink_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentDownloadLink-response-downloadUrl"></a>
The presigned download URL and the date and time the URL expires.
Type: [DownloadUrl](API_DownloadUrl.md) object

 ** [fileName](#API_GetAttachmentDownloadLink_ResponseSyntax) **   <a name="AWSSupport-GetAttachmentDownloadLink-response-fileName"></a>
The name of the attachment file, including the file extension.
Type: String

## Errors
<a name="API_GetAttachmentDownloadLink_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AttachmentIdNotFound **
An attachment with the specified ID could not be found.
 ** message **
An attachment with the specified ID could not be found.
HTTP Status Code: 400

 ** DryRunOperationException **
The request was valid, but the operation wasn't performed because `dryRun` was set to `true`.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_GetAttachmentDownloadLink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/GetAttachmentDownloadLink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/GetAttachmentDownloadLink)
