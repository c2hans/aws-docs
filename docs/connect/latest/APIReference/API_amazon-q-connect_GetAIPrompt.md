---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_GetAIPrompt.html
---

# GetAIPrompt
<a name="API_amazon-q-connect_GetAIPrompt"></a>

Gets and Amazon Q in Connect AI Prompt.

## Request Syntax
<a name="API_amazon-q-connect_GetAIPrompt_RequestSyntax"></a>

```
GET /assistants/{{assistantId}}/aiprompts/{{aiPromptId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_GetAIPrompt_RequestParameters"></a>

The request uses the following URI parameters.

 ** [aiPromptId](#API_amazon-q-connect_GetAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_GetAIPrompt-request-uri-aiPromptId"></a>
The identifier of the Amazon Q in Connect AI prompt.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** [assistantId](#API_amazon-q-connect_GetAIPrompt_RequestSyntax) **   <a name="connect-amazon-q-connect_GetAIPrompt-request-uri-assistantId"></a>
The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

## Request Body
<a name="API_amazon-q-connect_GetAIPrompt_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_GetAIPrompt_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aiPrompt": {
      "aiPromptArn": "string",
      "aiPromptId": "string",
      "apiFormat": "string",
      "assistantArn": "string",
      "assistantId": "string",
      "description": "string",
      "inferenceConfiguration": {
         "maxTokensToSample": number,
         "temperature": number,
         "topK": number,
         "topP": number
      },
      "modelId": "string",
      "modifiedTime": number,
      "name": "string",
      "origin": "string",
      "status": "string",
      "tags": {
         "string" : "string"
      },
      "templateConfiguration": { ... },
      "templateType": "string",
      "type": "string",
      "visibilityStatus": "string"
   },
   "versionNumber": number
}
```

## Response Elements
<a name="API_amazon-q-connect_GetAIPrompt_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aiPrompt](#API_amazon-q-connect_GetAIPrompt_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetAIPrompt-response-aiPrompt"></a>
The data of the AI Prompt.
Type: [AIPromptData](API_amazon-q-connect_AIPromptData.md) object

 ** [versionNumber](#API_amazon-q-connect_GetAIPrompt_ResponseSyntax) **   <a name="connect-amazon-q-connect_GetAIPrompt-response-versionNumber"></a>
The version number of the AI Prompt version (returned if an AI Prompt version was specified via use of a qualifier for the `aiPromptId` on the request).
Type: Long
Valid Range: Minimum value of 1.

## Errors
<a name="API_amazon-q-connect_GetAIPrompt_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

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
<a name="API_amazon-q-connect_GetAIPrompt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/GetAIPrompt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/GetAIPrompt)
