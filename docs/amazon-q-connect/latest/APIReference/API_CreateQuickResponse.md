---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateQuickResponse.html
---

# CreateQuickResponse
<a name="API_amazon-q-connect_CreateQuickResponse"></a>

Creates an Amazon Q in Connect quick response.

## Request Syntax
<a name="API_amazon-q-connect_CreateQuickResponse_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/quickResponses HTTP/1.1
Content-type: application/json

{
   "channels": [ "{{string}}" ],
   "clientToken": "{{string}}",
   "content": { ... },
   "contentType": "{{string}}",
   "description": "{{string}}",
   "groupingConfiguration": {
      "criteria": "{{string}}",
      "values": [ "{{string}}" ]
   },
   "isActive": {{boolean}},
   "language": "{{string}}",
   "name": "{{string}}",
   "shortcutKey": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_CreateQuickResponse_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_CreateQuickResponse_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channels](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-channels"></a>
The Connect Customer channels this quick response applies to.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** [clientToken](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [content](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-content"></a>
The content of the quick response.
Type: [QuickResponseDataProvider](API_amazon-q-connect_QuickResponseDataProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [contentType](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-contentType"></a>
The media type of the quick response content.
+ Use `application/x.quickresponse;format=plain` for a quick response written in plain text.
+ Use `application/x.quickresponse;format=markdown` for a quick response written in richtext.
Type: String
Pattern: `(application/x\.quickresponse;format=(plain|markdown))`
Required: No

 ** [description](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-description"></a>
The description of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [groupingConfiguration](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-groupingConfiguration"></a>
The configuration information of the user groups that the quick response is accessible to.
Type: [GroupingConfiguration](API_amazon-q-connect_GroupingConfiguration.md) object
Required: No

 ** [isActive](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-isActive"></a>
Whether the quick response is active.
Type: Boolean
Required: No

 ** [language](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** [name](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-name"></a>
The name of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [shortcutKey](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-shortcutKey"></a>
The shortcut key of the quick response. The value should be unique across the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** [tags](#API_amazon-q-connect_CreateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-request-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_CreateQuickResponse_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "quickResponse": {
      "channels": [ "string" ],
      "contents": {
         "markdown": { ... },
         "plainText": { ... }
      },
      "contentType": "string",
      "createdTime": number,
      "description": "string",
      "groupingConfiguration": {
         "criteria": "string",
         "values": [ "string" ]
      },
      "isActive": boolean,
      "knowledgeBaseArn": "string",
      "knowledgeBaseId": "string",
      "language": "string",
      "lastModifiedBy": "string",
      "lastModifiedTime": number,
      "name": "string",
      "quickResponseArn": "string",
      "quickResponseId": "string",
      "shortcutKey": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      }
   }
}
```

## Response Elements
<a name="API_amazon-q-connect_CreateQuickResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [quickResponse](#API_amazon-q-connect_CreateQuickResponse_ResponseSyntax) **   <a name="connect-amazon-q-connect_CreateQuickResponse-response-quickResponse"></a>
The quick response.
Type: [QuickResponseData](API_amazon-q-connect_QuickResponseData.md) object

## Errors
<a name="API_amazon-q-connect_CreateQuickResponse_Errors"></a>

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
<a name="API_amazon-q-connect_CreateQuickResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/CreateQuickResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/CreateQuickResponse)
