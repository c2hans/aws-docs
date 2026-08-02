---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteAttachment.html
---

# DeleteAttachment
<a name="API_DeleteAttachment"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Deletes an attachment associated with a specific Amazon Q Business conversation.

## Request Syntax
<a name="API_DeleteAttachment_RequestSyntax"></a>

```
DELETE /applications/{{applicationId}}/conversations/{{conversationId}}/attachments/{{attachmentId}}?userId={{userId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAttachment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_DeleteAttachment_RequestSyntax) **   <a name="qbusiness-DeleteAttachment-request-uri-applicationId"></a>
The unique identifier for the Amazon Q Business application environment.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [attachmentId](#API_DeleteAttachment_RequestSyntax) **   <a name="qbusiness-DeleteAttachment-request-uri-attachmentId"></a>
The unique identifier for the attachment.
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: Yes

 ** [conversationId](#API_DeleteAttachment_RequestSyntax) **   <a name="qbusiness-DeleteAttachment-request-uri-conversationId"></a>
The unique identifier of the conversation.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [userId](#API_DeleteAttachment_RequestSyntax) **   <a name="qbusiness-DeleteAttachment-request-uri-userId"></a>
The unique identifier of the user involved in the conversation.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\P{C}*`

## Request Body
<a name="API_DeleteAttachment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** LicenseNotFoundException **
You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/DeleteAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DeleteAttachment)
