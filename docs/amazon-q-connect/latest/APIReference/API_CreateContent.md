---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateContent.html
---

# CreateContent
<a name="API_amazon-q-connect_CreateContent"></a>

Creates Amazon Q in Connect content. Before to calling this API, use [StartContentUpload](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html) to upload an asset.

## Request Syntax
<a name="API_amazon-q-connect_CreateContent_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/contents HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "name": "{{string}}",
   "overrideLinkOutUri": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "title": "{{string}}",
   "uploadId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [metadata](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-metadata"></a>
A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [name](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-name"></a>
The name of the content. Each piece of content in a knowledge base must have a unique name. You can retrieve a piece of content using only its knowledge base and its name with the [SearchContent](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchContent.html) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** [overrideLinkOutUri](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-overrideLinkOutUri"></a>
The URI you want to use for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [tags](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [title](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-title"></a>
The title of the content. If not set, the title is equal to the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [uploadId](#API_amazon-q-connect_CreateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateContent-request-uploadId"></a>
A pointer to the uploaded asset. This value is returned by [StartContentUpload](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1200.
Required: Yes

## Response Syntax
<a name="API_amazon-q-connect_CreateContent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "content": {
      "contentArn": "string",
      "contentId": "string",
      "contentType": "string",
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "linkOutUri": "string",
      "metadata": {
         "string" : "string"
      },
      "name": "string",
      "revisionId": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "title": "string",
      "url": "string",
      "urlExpiry": number
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [content](#API_amazon-q-connect_CreateContent_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateContent-response-content"></a>
The content.
Type: [ContentData](API_amazon-q-connect_ContentData.md) object

## Errors
<a name="API_amazon-q-connect_CreateContent_Errors"></a>

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

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_CreateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateContent)
