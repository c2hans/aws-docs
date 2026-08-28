---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPlugin.html
---

# GetPlugin
<a name="API_GetPlugin"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Gets information about an existing Amazon Q Business plugin.

## Request Syntax
<a name="API_GetPlugin_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/plugins/{{pluginId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetPlugin_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetPlugin_RequestSyntax) **   <a name="qbusiness-GetPlugin-request-uri-applicationId"></a>
The identifier of the application which contains the plugin.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

 ** [pluginId](#API_GetPlugin_RequestSyntax) **   <a name="qbusiness-GetPlugin-request-uri-pluginId"></a>
The identifier of the plugin.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetPlugin_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetPlugin_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationId": "string",
   "authConfiguration": { ... },
   "buildStatus": "string",
   "createdAt": number,
   "customPluginConfiguration": {
      "apiSchema": { ... },
      "apiSchemaType": "string",
      "description": "string"
   },
   "displayName": "string",
   "pluginArn": "string",
   "pluginId": "string",
   "serverUrl": "string",
   "state": "string",
   "type": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetPlugin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [applicationId](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-applicationId"></a>
The identifier of the application which contains the plugin.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`

 ** [authConfiguration](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-authConfiguration"></a>
Authentication configuration information for an Amazon Q Business plugin.
Type: [PluginAuthConfiguration](API_PluginAuthConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [buildStatus](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-buildStatus"></a>
The current status of a plugin. A plugin is modified asynchronously.
Type: String
Valid Values: `READY | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [createdAt](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-createdAt"></a>
The timestamp for when the plugin was created.
Type: Timestamp

 ** [customPluginConfiguration](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-customPluginConfiguration"></a>
Configuration information required to create a custom plugin.
Type: [CustomPluginConfiguration](API_CustomPluginConfiguration.md) object

 ** [displayName](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-displayName"></a>
The name of the plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

 ** [pluginArn](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-pluginArn"></a>
The Amazon Resource Name (ARN) of the role with permission to access resources needed to create the plugin.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [pluginId](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-pluginId"></a>
The identifier of the plugin.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [serverUrl](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-serverUrl"></a>
The source URL used for plugin configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`

 ** [state](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-state"></a>
The current state of the plugin.
Type: String
Valid Values: `ENABLED | DISABLED`

 ** [type](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-type"></a>
The type of the plugin.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`

 ** [updatedAt](#API_GetPlugin_ResponseSyntax) **   <a name="qbusiness-GetPlugin-response-updatedAt"></a>
The timestamp for when the plugin was last updated.
Type: Timestamp

## Errors
<a name="API_GetPlugin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** InternalServerException **
An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact [Support](http://aws.amazon.com/contact-us/) for help.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.
 ** message **
The message describing a `ResourceNotFoundException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling. Reduce the number of requests and try again.
HTTP Status Code: 429

 ** ValidationException **
The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.
 ** fields **
The input field(s) that failed validation.
 ** message **
The message describing the `ValidationException`.
 ** reason **
The reason for the `ValidationException`.
HTTP Status Code: 400

## See Also
<a name="API_GetPlugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/GetPlugin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/GetPlugin)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
