---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_ListScenes.html
---

# ListScenes
<a name="API_ListScenes"></a>

Lists all scenes in a workspace.

## Request Syntax
<a name="API_ListScenes_RequestSyntax"></a>

```
POST /workspaces/{{workspaceId}}/scenes-list HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListScenes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [workspaceId](#API_ListScenes_RequestSyntax) **   <a name="tm-ListScenes-request-uri-workspaceId"></a>
The ID of the workspace that contains the scenes.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_ListScenes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListScenes_RequestSyntax) **   <a name="tm-ListScenes-request-maxResults"></a>
Specifies the maximum number of results to display.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 200.
Required: No

 ** [nextToken](#API_ListScenes_RequestSyntax) **   <a name="tm-ListScenes-request-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_ListScenes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "sceneSummaries": [
      {
         "arn": "string",
         "contentLocation": "string",
         "creationDateTime": number,
         "description": "string",
         "sceneId": "string",
         "updateDateTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListScenes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListScenes_ResponseSyntax) **   <a name="tm-ListScenes-response-nextToken"></a>
The string that specifies the next page of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 17880.
Pattern: `.*`

 ** [sceneSummaries](#API_ListScenes_ResponseSyntax) **   <a name="tm-ListScenes-response-sceneSummaries"></a>
A list of objects that contain information about the scenes.
Type: Array of [SceneSummary](API_SceneSummary.md) objects

## Errors
<a name="API_ListScenes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error has occurred.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
Failed
HTTP Status Code: 400

## See Also
<a name="API_ListScenes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iottwinmaker-2021-11-29/ListScenes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/ListScenes)
