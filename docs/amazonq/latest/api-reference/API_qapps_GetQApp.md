---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_GetQApp.html
---

# GetQApp
<a name="API_qapps_GetQApp"></a>

Retrieves the full details of an Q App, including its definition specifying the cards and flow.

## Request Syntax
<a name="API_qapps_GetQApp_RequestSyntax"></a>

```
GET /apps.get?appId={{appId}}&appVersion={{appVersion}} HTTP/1.1
instance-id: {{instanceId}}
```

## URI Request Parameters
<a name="API_qapps_GetQApp_RequestParameters"></a>

The request uses the following URI parameters.

 ** [appId](#API_qapps_GetQApp_RequestSyntax) **   <a name="qbusiness-qapps_GetQApp-request-uri-appId"></a>
The unique identifier of the Q App to retrieve.
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** [appVersion](#API_qapps_GetQApp_RequestSyntax) **   <a name="qbusiness-qapps_GetQApp-request-uri-appVersion"></a>
The version of the Q App.
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [instanceId](#API_qapps_GetQApp_RequestSyntax) **   <a name="qbusiness-qapps_GetQApp-request-instanceId"></a>
The unique identifier of the Amazon Q Business application environment instance.
Required: Yes

## Request Body
<a name="API_qapps_GetQApp_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_qapps_GetQApp_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "appArn": "string",
   "appDefinition": {
      "appDefinitionVersion": "string",
      "canEdit": boolean,
      "cards": [
         { ... }
      ]
   },
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
<a name="API_qapps_GetQApp_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [appArn](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-appArn"></a>
The Amazon Resource Name (ARN) of the Q App.
Type: String

 ** [appDefinition](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-appDefinition"></a>
The full definition of the Q App, specifying the cards and flow.
Type: [AppDefinition](API_qapps_AppDefinition.md) object

 ** [appId](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-appId"></a>
The unique identifier of the Q App.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`

 ** [appVersion](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-appVersion"></a>
The version of the Q App.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 2147483647.

 ** [createdAt](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-createdAt"></a>
The date and time the Q App was created.
Type: Timestamp

 ** [createdBy](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-createdBy"></a>
The user who created the Q App.
Type: String

 ** [description](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-description"></a>
The description of the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [initialPrompt](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-initialPrompt"></a>
The initial prompt displayed when the Q App is started.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.

 ** [requiredCapabilities](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-requiredCapabilities"></a>
The capabilities required to run the Q App, such as file upload or third-party integrations.
Type: Array of strings
Valid Values: `FileUpload | CreatorMode | RetrievalMode | PluginMode`

 ** [status](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-status"></a>
The status of the Q App.
Type: String
Valid Values: `PUBLISHED | DRAFT | DELETED`

 ** [title](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-title"></a>
The title of the Q App.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`

 ** [updatedAt](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-updatedAt"></a>
The date and time the Q App was last updated.
Type: Timestamp

 ** [updatedBy](#API_qapps_GetQApp_ResponseSyntax) **   <a name="qbusiness-qapps_GetQApp-response-updatedBy"></a>
The user who last updated the Q App.
Type: String

## Errors
<a name="API_qapps_GetQApp_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The client is not authorized to perform the requested operation.
HTTP Status Code: 403

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
<a name="API_qapps_GetQApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qapps-2023-11-27/GetQApp)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qapps-2023-11-27/GetQApp)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/GetQApp)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qapps-2023-11-27/GetQApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/GetQApp)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qapps-2023-11-27/GetQApp)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qapps-2023-11-27/GetQApp)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qapps-2023-11-27/GetQApp)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qapps-2023-11-27/GetQApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/GetQApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
