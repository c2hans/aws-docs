---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html
---

# CreateStack
<a name="API_CreateStack"></a>

Creates a stack to start streaming applications to users. A stack consists of an associated fleet, user access policies, and storage configurations.

## Request Syntax
<a name="API_CreateStack_RequestSyntax"></a>

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
   "Tags": {
      "{{string}}" : "{{string}}"
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
<a name="API_CreateStack_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessEndpoints](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-AccessEndpoints"></a>
The list of interface VPC endpoint (interface endpoint) objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.
Type: Array of [AccessEndpoint](API_AccessEndpoint.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

 ** [AgentAccessConfig](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-AgentAccessConfig"></a>
The configuration for agent access on the stack. If specified, agent access is enabled for the stack.
Type: [AgentAccessConfig](API_AgentAccessConfig.md) object
Required: No

 ** [ApplicationSettings](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-ApplicationSettings"></a>
The persistent application settings for users of a stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
Type: [ApplicationSettings](API_ApplicationSettings.md) object
Required: No

 ** [Description](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-Description"></a>
The description to display.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** [DisplayName](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-DisplayName"></a>
The stack name to display.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [EmbedHostDomains](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-EmbedHostDomains"></a>
The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Maximum length of 128.
Pattern: `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
Required: No

 ** [FeedbackURL](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-FeedbackURL"></a>
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** [Name](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-Name"></a>
The name of the stack.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [RedirectURL](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-RedirectURL"></a>
The URL that users are redirected to after their streaming session ends.
Type: String
Length Constraints: Maximum length of 1000.
Required: No

 ** [StorageConnectors](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-StorageConnectors"></a>
The storage connectors to enable.
Type: Array of [StorageConnector](API_StorageConnector.md) objects
Required: No

 ** [StreamingExperienceSettings](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-StreamingExperienceSettings"></a>
The streaming protocol you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
Type: [StreamingExperienceSettings](API_StreamingExperienceSettings.md) object
Required: No

 ** [Tags](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-Tags"></a>
The tags to associate with the stack. A tag is a key-value pair, and the value is optional. For example, Environment=Test. If you do not specify a value, Environment=.
If you do not specify a value, the value is set to an empty string.
Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following special characters:
\_ . : / = \+ \\ - @
For more information about tags, see [Tagging Your Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/tagging-basic.html) in the *Amazon WorkSpaces Applications Administration Guide*.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(^(?!aws:).[\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [UserSettings](#API_CreateStack_RequestSyntax) **   <a name="WorkSpacesApplications-CreateStack-request-UserSettings"></a>
The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
Type: Array of [UserSetting](API_UserSetting.md) objects
Array Members: Minimum number of 1 item.
Required: No

## Response Syntax
<a name="API_CreateStack_ResponseSyntax"></a>

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
<a name="API_CreateStack_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Stack](#API_CreateStack_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateStack-response-Stack"></a>
Information about the stack.
Type: [Stack](API_Stack.md) object

## Errors
<a name="API_CreateStack_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
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

 ** ResourceAlreadyExistsException **
The specified resource already exists.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateStack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateStack)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateStack)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateStack)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateStack)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateStack)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateStack)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateStack)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateStack)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateStack)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateStack)
