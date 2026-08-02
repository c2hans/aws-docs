---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_UpdateScene.html
---

# UpdateScene
<a name="API_UpdateScene"></a>

Updates a scene.

## Request Syntax
<a name="API_UpdateScene_RequestSyntax"></a>

```
PUT /workspaces/{{workspaceId}}/scenes/{{sceneId}} HTTP/1.1
Content-type: application/json

{
   "capabilities": [ "{{string}}" ],
   "contentLocation": "{{string}}",
   "description": "{{string}}",
   "sceneMetadata": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateScene_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sceneId](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-uri-sceneId"></a>
The ID of the scene.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

 ** [workspaceId](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-uri-workspaceId"></a>
The ID of the workspace that contains the scene.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_UpdateScene_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [capabilities](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-capabilities"></a>
A list of capabilities that the scene uses to render.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`
Required: No

 ** [contentLocation](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-contentLocation"></a>
The relative path that specifies the location of the content definition file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[sS]3://[A-Za-z0-9._/-]+`
Required: No

 ** [description](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-description"></a>
The description of this scene.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: No

 ** [sceneMetadata](#API_UpdateScene_RequestSyntax) **   <a name="tm-UpdateScene-request-sceneMetadata"></a>
The scene metadata.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateScene_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "updateDateTime": number
}
```

## Response Elements
<a name="API_UpdateScene_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateDateTime](#API_UpdateScene_ResponseSyntax) **   <a name="tm-UpdateScene-response-updateDateTime"></a>
The date and time when the scene was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateScene_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource wasn't found.
HTTP Status Code: 404

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_UpdateScene_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/UpdateScene)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/UpdateScene)
