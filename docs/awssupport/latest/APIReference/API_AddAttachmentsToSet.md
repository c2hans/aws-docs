---
source_url: https://docs.aws.amazon.com/awssupport/latest/APIReference/API_AddAttachmentsToSet.html
---

# AddAttachmentsToSet
<a name="API_AddAttachmentsToSet"></a>

Adds one or more attachments to an attachment set.

An attachment set is a temporary container for attachments that you add to a case or case communication. The set is available for 1 hour after it's created. The `expiryTime` returned in the response is when the set expires.

**Note**
You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the AWS Support API.
If you call the AWS Support API from an account that doesn't have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Request Syntax
<a name="API_AddAttachmentsToSet_RequestSyntax"></a>

```
{
   "attachments": [
      {
         "data": {{blob}},
         "fileName": "{{string}}"
      }
   ],
   "attachmentSetId": "{{string}}"
}
```

## Request Parameters
<a name="API_AddAttachmentsToSet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attachments](#API_AddAttachmentsToSet_RequestSyntax) **   <a name="AWSSupport-AddAttachmentsToSet-request-attachments"></a>
One or more attachments to add to the set. You can add up to three attachments per set. The size limit is 5 MB per attachment.
In the `Attachment` object, use the `data` parameter to specify the contents of the attachment file. In the previous request syntax, the value for `data` appear as `blob`, which is represented as a base64-encoded string. The value for `fileName` is the name of the attachment, such as `troubleshoot-screenshot.png`.
Type: Array of [Attachment](API_Attachment.md) objects

 ** [attachmentSetId](#API_AddAttachmentsToSet_RequestSyntax) **   <a name="AWSSupport-AddAttachmentsToSet-request-attachmentSetId"></a>
The ID of the attachment set. If an `attachmentSetId` is not specified, a new attachment set is created, and the ID of the set is returned in the response. If an `attachmentSetId` is specified, the attachments are added to the specified set, if it exists.
Type: String

## Response Syntax
<a name="API_AddAttachmentsToSet_ResponseSyntax"></a>

```
{
   "attachmentSetId": "string",
   "expiryTime": "string"
}
```

## Response Elements
<a name="API_AddAttachmentsToSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachmentSetId](#API_AddAttachmentsToSet_ResponseSyntax) **   <a name="AWSSupport-AddAttachmentsToSet-response-attachmentSetId"></a>
The ID of the attachment set. If an `attachmentSetId` was not specified, a new attachment set is created, and the ID of the set is returned in the response. If an `attachmentSetId` was specified, the attachments are added to the specified set, if it exists.
Type: String

 ** [expiryTime](#API_AddAttachmentsToSet_ResponseSyntax) **   <a name="AWSSupport-AddAttachmentsToSet-response-expiryTime"></a>
The time and date when the attachment set expires.
Type: String

## Errors
<a name="API_AddAttachmentsToSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AttachmentLimitExceeded **
The limit for the number of attachment sets created in a short period of time has been exceeded.
 ** message **
The limit for the number of attachment sets created in a short period of time has been exceeded.
HTTP Status Code: 400

 ** AttachmentSetExpired **
The expiration time of the attachment set has passed. The set expires 1 hour after it is created.
 ** message **
The expiration time of the attachment set has passed. The set expires one hour after it is created.
HTTP Status Code: 400

 ** AttachmentSetIdNotFound **
An attachment set with the specified ID could not be found.
 ** message **
An attachment set with the specified ID could not be found.
HTTP Status Code: 400

 ** AttachmentSetSizeLimitExceeded **
A limit for the size of an attachment set has been exceeded. The limits are three attachments and 5 MB per attachment.
 ** message **
A limit for the size of an attachment set has been exceeded. The limits are three attachments and 5 MB per attachment.
HTTP Status Code: 400

 ** InternalServerError **
An internal server error occurred.
 ** message **
An internal server error occurred.
HTTP Status Code: 500

## See Also
<a name="API_AddAttachmentsToSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/AddAttachmentsToSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/support-2013-04-15/AddAttachmentsToSet)
