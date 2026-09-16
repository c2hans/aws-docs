---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_GetScene.html
---

# GetScene
<a name="API_GetScene"></a>

Retrieves information about a scene.

## Request Syntax
<a name="API_GetScene_RequestSyntax"></a>

```
GET /workspaces/{{workspaceId}}/scenes/{{sceneId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetScene_RequestParameters"></a>

The request uses the following URI parameters.

 ** [sceneId](#API_GetScene_RequestSyntax) **   <a name="tm-GetScene-request-uri-sceneId"></a>
The ID of the scene.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

 ** [workspaceId](#API_GetScene_RequestSyntax) **   <a name="tm-GetScene-request-uri-workspaceId"></a>
The ID of the workspace that contains the scene.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_GetScene_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetScene_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "capabilities": [ "string" ],
   "contentLocation": "string",
   "creationDateTime": number,
   "description": "string",
   "error": {
      "code": "string",
      "message": "string"
   },
   "generatedSceneMetadata": {
      "string" : "string"
   },
   "sceneId": "string",
   "sceneMetadata": {
      "string" : "string"
   },
   "updateDateTime": number,
   "workspaceId": "string"
}
```

## Response Elements
<a name="API_GetScene_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-arn"></a>
The ARN of the scene.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`

 ** [capabilities](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-capabilities"></a>
A list of capabilities that the scene uses to render.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*`

 ** [contentLocation](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-contentLocation"></a>
The relative path that specifies the location of the content definition file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[sS]3://[A-Za-z0-9._/-]+`

 ** [creationDateTime](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-creationDateTime"></a>
The date and time when the scene was created.
Type: Timestamp

 ** [description](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-description"></a>
The description of the scene.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`

 ** [error](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-error"></a>
The SceneResponse error.
Type: [SceneError](API_SceneError.md) object

 ** [generatedSceneMetadata](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-generatedSceneMetadata"></a>
The generated scene metadata.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `.*`

 ** [sceneId](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-sceneId"></a>
The ID of the scene.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

 ** [sceneMetadata](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-sceneMetadata"></a>
The response metadata.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[a-zA-Z_\-0-9]+`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `.*`

 ** [updateDateTime](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-updateDateTime"></a>
The date and time when the scene was last updated.
Type: Timestamp

 ** [workspaceId](#API_GetScene_ResponseSyntax) **   <a name="tm-GetScene-response-workspaceId"></a>
The ID of the workspace that contains the scene.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`

## Errors
<a name="API_GetScene_Errors"></a>

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
<a name="API_GetScene_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/GetScene)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/GetScene)
