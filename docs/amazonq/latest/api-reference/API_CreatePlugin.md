---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html
---

# CreatePlugin
<a name="API_CreatePlugin"></a>

**Note**
Amazon Q Business will no longer be open to new customers starting on July 31, 2026. If you would like to use the service, please sign up prior to July 30. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

Creates an Amazon Q Business plugin.

## Request Syntax
<a name="API_CreatePlugin_RequestSyntax"></a>

```
POST /applications/{{applicationId}}/plugins HTTP/1.1
Content-type: application/json

{
   "authConfiguration": { ... },
   "clientToken": "{{string}}",
   "customPluginConfiguration": {
      "apiSchema": { ... },
      "apiSchemaType": "{{string}}",
      "description": "{{string}}"
   },
   "displayName": "{{string}}",
   "serverUrl": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreatePlugin_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-uri-applicationId"></a>
The identifier of the application that will contain the plugin.
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: Yes

## Request Body
<a name="API_CreatePlugin_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [authConfiguration](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-authConfiguration"></a>
Authentication configuration information for an Amazon Q Business plugin.
Type: [PluginAuthConfiguration](API_PluginAuthConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [clientToken](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-clientToken"></a>
A token that you provide to identify the request to create your Amazon Q Business plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [customPluginConfiguration](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-customPluginConfiguration"></a>
Contains configuration for a custom plugin.
Type: [CustomPluginConfiguration](API_CustomPluginConfiguration.md) object
Required: No

 ** [displayName](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-displayName"></a>
A the name for your plugin.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [serverUrl](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-serverUrl"></a>
The source URL used for plugin configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(https?|ftp|file)://([^\s]*)`
Required: No

 ** [tags](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-tags"></a>
A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

 ** [type](#API_CreatePlugin_RequestSyntax) **   <a name="qbusiness-CreatePlugin-request-type"></a>
The type of plugin you want to create.
Type: String
Valid Values: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
Required: Yes

## Response Syntax
<a name="API_CreatePlugin_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "buildStatus": "string",
   "pluginArn": "string",
   "pluginId": "string"
}
```

## Response Elements
<a name="API_CreatePlugin_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildStatus](#API_CreatePlugin_ResponseSyntax) **   <a name="qbusiness-CreatePlugin-response-buildStatus"></a>
The current status of a plugin. A plugin is modified asynchronously.
Type: String
Valid Values: `READY | CREATE_IN_PROGRESS | CREATE_FAILED | UPDATE_IN_PROGRESS | UPDATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`

 ** [pluginArn](#API_CreatePlugin_ResponseSyntax) **   <a name="qbusiness-CreatePlugin-response-pluginArn"></a>
The Amazon Resource Name (ARN) of a plugin.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1284.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

 ** [pluginId](#API_CreatePlugin_ResponseSyntax) **   <a name="qbusiness-CreatePlugin-response-pluginId"></a>
The identifier of the plugin created.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

## Errors
<a name="API_CreatePlugin_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.
HTTP Status Code: 403

 ** ConflictException **
You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.
 ** message **
The message describing a `ConflictException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
You have exceeded the set limits for your Amazon Q Business service.
 ** message **
The message describing a `ServiceQuotaExceededException`.
 ** resourceId **
The identifier of the resource affected.
 ** resourceType **
The type of the resource affected.
HTTP Status Code: 402

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
<a name="API_CreatePlugin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qbusiness-2023-11-27/CreatePlugin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/CreatePlugin)
