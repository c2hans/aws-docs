---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateContent.html
---

# UpdateContent
<a name="API_amazon-q-connect_UpdateContent"></a>

Updates information about the content.

## Request Syntax
<a name="API_amazon-q-connect_UpdateContent_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/contents/{{contentId}} HTTP/1.1
Content-type: application/json

{
   "metadata": {
      "{{string}}" : "{{string}}"
   },
   "overrideLinkOutUri": "{{string}}",
   "removeOverrideLinkOutUri": {{boolean}},
   "revisionId": "{{string}}",
   "title": "{{string}}",
   "uploadId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateContent_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contentId](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-uri-contentId"></a>
The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [knowledgeBaseId](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base. Can be either the ID or the ARN
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateContent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [metadata](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-metadata"></a>
A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [overrideLinkOutUri](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-overrideLinkOutUri"></a>
The URI for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. To remove an existing `overrideLinkOurUri`, exclude this argument and set `removeOverrideLinkOutUri` to true.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [removeOverrideLinkOutUri](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-removeOverrideLinkOutUri"></a>
Unset the existing `overrideLinkOutUri` if it exists.
Type: Boolean
Required: No

 ** [revisionId](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-revisionId"></a>
The `revisionId` of the content resource to update, taken from an earlier call to `GetContent`, `GetContentSummary`, `SearchContent`, or `ListContents`. If included, this argument acts as an optimistic lock to ensure content was not modified since it was last read. If it has been modified, this API throws a `PreconditionFailedException`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [title](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-title"></a>
The title of the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [uploadId](#API_amazon-q-connect_UpdateContent_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-request-uploadId"></a>
A pointer to the uploaded asset. This value is returned by [StartContentUpload](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1200.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateContent_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_UpdateContent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [content](#API_amazon-q-connect_UpdateContent_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateContent-response-content"></a>
The content.
Type: [ContentData](API_amazon-q-connect_ContentData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateContent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PreconditionFailedException **
The provided `revisionId` does not match, indicating the content has been modified since it was last read.
HTTP Status Code: 412

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_UpdateContent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateContent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateContent)
