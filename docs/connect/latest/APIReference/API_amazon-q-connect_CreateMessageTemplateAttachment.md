---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_CreateMessageTemplateAttachment.html
---

# CreateMessageTemplateAttachment
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment"></a>

Uploads an attachment file to the specified Amazon Q in Connect message template. The name of the message template attachment has to be unique for each message template referenced by the `$LATEST` qualifier. The body of the attachment file should be encoded using base64 encoding. After the file is uploaded, you can use the pre-signed Amazon S3 URL returned in response to download the uploaded file.

## Request Syntax
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}}/attachments HTTP/1.1
Content-type: application/json

{
   "body": "{{string}}",
   "clientToken": "{{string}}",
   "contentDisposition": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [messageTemplateId](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [body](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-body"></a>
The body of the attachment file being uploaded. It should be encoded using base64 encoding.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [clientToken](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [contentDisposition](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-contentDisposition"></a>
The presentation information for the attachment file.
Type: String
Valid Values: `ATTACHMENT`
Required: Yes

 ** [name](#API_amazon-q-connect_CreateMessageTemplateAttachment_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-request-name"></a>
The name of the attachment file being uploaded. The name should include the file extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}_\s&@()+,;=\-]+\.[A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attachment": {
      "attachmentId": "string",
      "contentDisposition": "string",
      "name": "string",
      "uploadedTime": "string",
      "url": "string",
      "urlExpiry": "string"
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attachment](#API_amazon-q-connect_CreateMessageTemplateAttachment_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateMessageTemplateAttachment-response-attachment"></a>
The message template attachment.
Type: [MessageTemplateAttachment](API_amazon-q-connect_MessageTemplateAttachment.md) object

## Errors
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateMessageTemplateAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateMessageTemplateAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateMessageTemplateAttachment)
