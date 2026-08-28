---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UpdateStack.html
---

# UpdateStack
<a name="API_UpdateStack"></a>

Updates the specified fields for the specified stack.

## Request Syntax
<a name="API_UpdateStack_RequestSyntax"></a>

```
{
   "AccessEndpoints": [
      {
         "EndpointType": "{{string}}",
         "VpceId": "{{string}}"
      }
   ],
   "AgentAccessConfig": {
      "S3BucketArn": "{{string}}",
      "ScreenImageFormat": "{{string}}",
      "ScreenResolution": "{{string}}",
      "ScreenshotsUploadEnabled": {{boolean}},
      "Settings": [
         {
            "AgentAction": "{{string}}",
            "Permission": "{{string}}"
         }
      ],
      "UserControlMode": "{{string}}"
   },
   "ApplicationSettings": {
      "Enabled": {{boolean}},
      "SettingsGroup": "{{string}}"
   },
   "AttributesToDelete": [ "{{string}}" ],
   "DeleteStorageConnectors": {{boolean}},
   "Description": "{{string}}",
   "DisplayName": "{{string}}",
   "EmbedHostDomains": [ "{{string}}" ],
   "FeedbackURL": "{{string}}",
   "Name": "{{string}}",
   "RedirectURL": "{{string}}",
   "StorageConnectors": [
      {
         "ConnectorType": "{{string}}",
         "Domains": [ "{{string}}" ],
         "DomainsRequireAdminConsent": [ "{{string}}" ],
         "ResourceIdentifier": "{{string}}"
      }
   ],
   "StreamingExperienceSettings": {
      "PreferredProtocol": "{{string}}"
   },
   "UserSettings": [
      {
         "Action": "{{string}}",
         "MaximumLength": {{number}},
         "Permission": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoints](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-AccessEndpoints"></a>
The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** [AgentAccessConfig](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-AgentAccessConfig"></a>
The configuration for agent access on the stack. Specify this to update agent access settings. To remove agent access, use AttributesToDelete with the AGENT\_ACCESS\_CONFIG value.
Type: [AgentAccessConfigForUpdate](API_AgentAccessConfigForUpdate.md) object
Required: No

 ** [ApplicationSettings](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-ApplicationSettings"></a>
The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
Type: [ApplicationSettings](API_ApplicationSettings.md) object
Required: No

 ** [AttributesToDelete](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-AttributesToDelete"></a>
The stack attributes to delete.
Type: Array of strings
Valid Values: `STORAGE_CONNECTORS | STORAGE_CONNECTOR_HOMEFOLDERS | STORAGE_CONNECTOR_GOOGLE_DRIVE | STORAGE_CONNECTOR_ONE_DRIVE | REDIRECT_URL | FEEDBACK_URL | THEME_NAME | USER_SETTINGS | EMBED_HOST_DOMAINS | IAM_ROLE_ARN | ACCESS_ENDPOINTS | STREAMING_EXPERIENCE_SETTINGS | AGENT_ACCESS_CONFIG`
Required: No

 ** [DeleteStorageConnectors](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-DeleteStorageConnectors"></a>
 *This parameter has been deprecated.*
Deletes the storage connectors currently enabled for the stack.
Type: Boolean
Required: No

 ** [Description](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-Description"></a>
The description to display.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-DisplayName"></a>
The stack name to display.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [EmbedHostDomains](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-EmbedHostDomains"></a>
The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Maximum length of 128.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: No

 ** [FeedbackURL](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-FeedbackURL"></a>
The URL that users are redirected to after they choose the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** [Name](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-Name"></a>
The name of the stack.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [RedirectURL](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-RedirectURL"></a>
The URL that users are redirected to after their streaming session ends.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** [StorageConnectors](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-StorageConnectors"></a>
The storage connectors to enable.
Type: Array of [StorageConnector](API_StorageConnector.md) objects
Required: No

 ** [StreamingExperienceSettings](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-StreamingExperienceSettings"></a>
The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
Type: [StreamingExperienceSettings](API_StreamingExperienceSettings.md) object
Required: No

 ** [UserSettings](#API_UpdateStack_RequestSyntax) **   <a name="WorkSpacesApplications-UpdateStack-request-UserSettings"></a>
The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
Type: Array of [UserSetting](API_UserSetting.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_UpdateStack_ResponseSyntax"></a>

```
{
   "Stack": {
      "AccessEndpoints": [
         {
            "EndpointType": "string",
            "VpceId": "string"
         }
      ],
      "AgentAccessConfig": {
         "S3BucketArn": "string",
         "ScreenImageFormat": "string",
         "ScreenResolution": "string",
         "ScreenshotsUploadEnabled": boolean,
         "Settings": [
            {
               "AgentAction": "string",
               "Permission": "string"
            }
         ],
         "UserControlMode": "string"
      },
      "ApplicationSettings": {
         "Enabled": boolean,
         "S3BucketName": "string",
         "SettingsGroup": "string"
      },
      "Arn": "string",
      "CreatedTime": number,
      "Description": "string",
      "DisplayName": "string",
      "EmbedHostDomains": [ "string" ],
      "FeedbackURL": "string",
      "Name": "string",
      "RedirectURL": "string",
      "StackErrors": [
         {
            "ErrorCode": "string",
            "ErrorMessage": "string"
         }
      ],
      "StorageConnectors": [
         {
            "ConnectorType": "string",
            "Domains": [ "string" ],
            "DomainsRequireAdminConsent": [ "string" ],
            "ResourceIdentifier": "string"
         }
      ],
      "StreamingExperienceSettings": {
         "PreferredProtocol": "string"
      },
      "UserSettings": [
         {
            "Action": "string",
            "MaximumLength": number,
            "Permission": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_UpdateStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Stack](#API_UpdateStack_ResponseSyntax) **   <a name="WorkSpacesApplications-UpdateStack-response-Stack"></a>
Information about the stack.
Type: [Stack](API_Stack.md) object

## Errors
<a name="API_UpdateStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** IncompatibleImageException **
The image can't be updated because it's not compatible for updates.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidAccountStatusException **
The resource cannot be created because your AWS account is suspended. For assistance, contact AWS Support.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidRoleException **
The specified role is invalid.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceInUseException **
The specified resource is in use.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_UpdateStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/UpdateStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/UpdateStack)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
