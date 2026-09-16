---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_UpdateQApp.html
---

# UpdateQApp
<a name="API_qapps_UpdateQApp"></a>

Updates an existing Amazon Q App, allowing modifications to its title, description, and definition.

## Request Syntax
<a name="API_qapps_UpdateQApp_RequestSyntax"></a>

```
POST /apps.update HTTP/1.1
instance-id: {{instanceId}}
Content-type: application/json

{
   "appDefinition": {
      "cards": [
         { ... }
      ],
      "initialPrompt": "{{string}}"
   },
   "appId": "{{string}}",
   "description": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_qapps_UpdateQApp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceId](#API_qapps_UpdateQApp_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQApp-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_UpdateQApp_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [appDefinition](#API_qapps_UpdateQApp_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQApp-request-appDefinition"></a>
The new definition specifying the cards and flow for the Q App.
Type: [AppDefinitionInput](API_qapps_AppDefinitionInput.md) object
Required: No

 ** [appId](#API_qapps_UpdateQApp_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQApp-request-appId"></a>
The unique identifier of the Q App to update.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [description](#API_qapps_UpdateQApp_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQApp-request-description"></a>
The new description for the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [title](#API_qapps_UpdateQApp_RequestSyntax) **   <a name="qbusiness-qapps_UpdateQApp-request-title"></a>
The new title for the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: No

## Response Syntax
<a name="API_qapps_UpdateQApp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appId": "string",
   "appVersion": number,
   "createdAt": "string",
   "createdBy": "string",
   "description": "string",
   "initialPrompt": "string",
   "requiredCapabilities": [ "string" ],
   "status": "string",
   "title": "string",
   "updatedAt": "string",
   "updatedBy": "string"
}
```

## Response Elements
<a name="API_qapps_UpdateQApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-appArn"></a>
The Amazon Resource Name (ARN) of the updated Q App.
Type: String

 ** [appId](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-appId"></a>
The unique identifier of the updated Q App.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [appVersion](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-appVersion"></a>
The new version of the updated Q App.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [createdAt](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-createdAt"></a>
The date and time the Q App was originally created.
Type: Timestamp

 ** [createdBy](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-createdBy"></a>
The user who originally created the Q App.
Type: String

 ** [description](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-description"></a>
The new description of the updated Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [initialPrompt](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-initialPrompt"></a>
The initial prompt for the updated Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.

 ** [requiredCapabilities](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-requiredCapabilities"></a>
The capabilities required for the updated Q App.
Type: Array of strings
Valid Values: `FileUpload | CreatorMode | RetrievalMode | PluginMode`

 ** [status](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-status"></a>
The status of the updated Q App.
Type: String
Valid Values: `PUBLISHED | DRAFT | DELETED`

 ** [title](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-title"></a>
The new title of the updated Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`

 ** [updatedAt](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-updatedAt"></a>
The date and time the Q App was last updated.
Type: Timestamp

 ** [updatedBy](#API_qapps_UpdateQApp_ResponseSyntax) **   <a name="qbusiness-qapps_UpdateQApp-response-updatedBy"></a>
The user who last updated the Q App.
Type: String

## Errors
<a name="API_qapps_UpdateQApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

 ** ContentTooLargeException **
The requested operation could not be completed because the content exceeds the maximum allowed size.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 413

 ** InternalServerException **
An internal service error occurred while processing the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
 ** resourceId **
The unique identifier of the resource
 ** resourceType **
The type of the resource
HTTP Status Code: 404

 ** ThrottlingException **
The requested operation could not be completed because too many requests were sent at once. Wait a bit and try again later.
 ** quotaCode **
The code of the quota that was exceeded
 ** retryAfterSeconds **
The number of seconds to wait before retrying the operation
 ** serviceCode **
The code for the service where the quota was exceeded
HTTP Status Code: 429

 ** UnauthorizedException **
The client is not authenticated or authorized to perform the requested operation.
HTTP Status Code: 401

 ** ValidationException **
The input failed to satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_qapps_UpdateQApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/UpdateQApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/UpdateQApp)
