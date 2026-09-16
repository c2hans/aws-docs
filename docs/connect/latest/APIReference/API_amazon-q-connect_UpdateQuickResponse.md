---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_UpdateQuickResponse.html
---

# UpdateQuickResponse
<a name="API_amazon-q-connect_UpdateQuickResponse"></a>

Updates an existing Amazon Q in Connect quick response.

## Request Syntax
<a name="API_amazon-q-connect_UpdateQuickResponse_RequestSyntax"></a>

```
POST /knowledgeBases/{{knowledgeBaseId}}/quickResponses/{{quickResponseId}} HTTP/1.1
Content-type: application/json

{
   "channels": [ "{{string}}" ],
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
   "removeDescription": {{boolean}},
   "removeGroupingConfiguration": {{boolean}},
   "removeShortcutKey": {{boolean}},
   "shortcutKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_amazon-q-connect_UpdateQuickResponse_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [quickResponseId](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-uri-quickResponseId"></a>
The identifier of the quick response.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_UpdateQuickResponse_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [channels](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-channels"></a>
The Connect Customer contact channels this quick response applies to. The supported contact channel types include `Chat`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** [content](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-content"></a>
The updated content of the quick response.
Type: [QuickResponseDataProvider](API_amazon-q-connect_QuickResponseDataProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [contentType](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-contentType"></a>
The media type of the quick response content.
+ Use `application/x.quickresponse;format=plain` for quick response written in plain text.
+ Use `application/x.quickresponse;format=markdown` for quick response written in richtext.
Type: String
Pattern: `(application/x\.quickresponse;format=(plain|markdown))`
Required: No

 ** [description](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-description"></a>
The updated description of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [groupingConfiguration](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-groupingConfiguration"></a>
The updated grouping configuration of the quick response.
Type: [GroupingConfiguration](API_amazon-q-connect_GroupingConfiguration.md) object
Required: No

 ** [isActive](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-isActive"></a>
Whether the quick response is active.
Type: Boolean
Required: No

 ** [language](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** [name](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-name"></a>
The name of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [removeDescription](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-removeDescription"></a>
Whether to remove the description from the quick response.
Type: Boolean
Required: No

 ** [removeGroupingConfiguration](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-removeGroupingConfiguration"></a>
Whether to remove the grouping configuration of the quick response.
Type: Boolean
Required: No

 ** [removeShortcutKey](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-removeShortcutKey"></a>
Whether to remove the shortcut key of the quick response.
Type: Boolean
Required: No

 ** [shortcutKey](#API_amazon-q-connect_UpdateQuickResponse_RequestSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-request-shortcutKey"></a>
The shortcut key of the quick response. The value should be unique across the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

## Response Syntax
<a name="API_amazon-q-connect_UpdateQuickResponse_ResponseSyntax"></a>

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
<a name="API_amazon-q-connect_UpdateQuickResponse_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [quickResponse](#API_amazon-q-connect_UpdateQuickResponse_ResponseSyntax) **   <a name="connect-amazon-q-connect_UpdateQuickResponse-response-quickResponse"></a>
The quick response.
Type: [QuickResponseData](API_amazon-q-connect_QuickResponseData.md) object

## Errors
<a name="API_amazon-q-connect_UpdateQuickResponse_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource. For example, if you're using a `Create` API (such as `CreateAssistant`) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.
HTTP Status Code: 409

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
<a name="API_amazon-q-connect_UpdateQuickResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/UpdateQuickResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/UpdateQuickResponse)
