---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

Creates a user account for the specified Connect Customer instance.

**Important**
Certain [UserIdentityInfo](https://docs.aws.amazon.com/connect/latest/APIReference/API_UserIdentityInfo.html) parameters are required in some situations. For example, `Email`, `FirstName` and `LastName` are required if you are using Connect Customer or SAML for identity management.

**Note**
Fields in `PhoneConfig` cannot be set simultaneously with their corresponding channel-specific configuration parameters. Specifically:
 `PhoneConfig.AutoAccept` conflicts with `AutoAcceptConfigs`
 `PhoneConfig.AfterContactWorkTimeLimit` conflicts with `AfterContactWorkConfigs`
 `PhoneConfig.PhoneType` and `PhoneConfig.PhoneNumber` conflict with `PhoneNumberConfigs`
 `PhoneConfig.PersistentConnection` conflicts with `PersistentConnectionConfigs`
We recommend using channel-specific parameters such as `AutoAcceptConfigs`, `AfterContactWorkConfigs`, `PhoneNumberConfigs`, `PersistentConnectionConfigs`, and `VoiceEnhancementConfigs` for per-channel configuration.

For information about how to create users using the Connect Customer admin website, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html) in the *Connect Customer Administrator Guide*.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
PUT /users/{{InstanceId}} HTTP/1.1
Content-type: application/json

{
   "AfterContactWorkConfigs": [
      {
         "AfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": {{number}}
         },
         "AgentFirstCallbackAfterContactWorkConfig": {
            "AfterContactWorkTimeLimit": {{number}}
         },
         "Channel": "{{string}}"
      }
   ],
   "AutoAcceptConfigs": [
      {
         "AgentFirstCallbackAutoAccept": {{boolean}},
         "AutoAccept": {{boolean}},
         "Channel": "{{string}}"
      }
   ],
   "DirectoryUserId": "{{string}}",
   "HierarchyGroupId": "{{string}}",
   "IdentityInfo": {
      "Email": "{{string}}",
      "FirstName": "{{string}}",
      "LastName": "{{string}}",
      "Mobile": "{{string}}",
      "SecondaryEmail": "{{string}}"
   },
   "Password": "{{string}}",
   "PersistentConnectionConfigs": [
      {
         "Channel": "{{string}}",
         "PersistentConnection": {{boolean}}
      }
   ],
   "PhoneConfig": {
      "AfterContactWorkTimeLimit": {{number}},
      "AutoAccept": {{boolean}},
      "DeskPhoneNumber": "{{string}}",
      "PersistentConnection": {{boolean}},
      "PhoneType": "{{string}}"
   },
   "PhoneNumberConfigs": [
      {
         "Channel": "{{string}}",
         "PhoneNumber": "{{string}}",
         "PhoneType": "{{string}}"
      }
   ],
   "RoutingProfileId": "{{string}}",
   "SecurityProfileIds": [ "{{string}}" ],
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Username": "{{string}}",
   "VoiceEnhancementConfigs": [
      {
         "Channel": "{{string}}",
         "VoiceEnhancementMode": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_CreateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AfterContactWorkConfigs](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-AfterContactWorkConfigs"></a>
The list of after contact work (ACW) timeout configuration settings for each channel.
Type: Array of [AfterContactWorkConfigPerChannel](API_AfterContactWorkConfigPerChannel.md) objects
Required: No

 ** [AutoAcceptConfigs](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-AutoAcceptConfigs"></a>
The list of auto-accept configuration settings for each channel.
Type: Array of [AutoAcceptConfig](API_AutoAcceptConfig.md) objects
Required: No

 ** [DirectoryUserId](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-DirectoryUserId"></a>
The identifier of the user account in the directory used for identity management. If Connect Customer cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Connect Customer cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.
This parameter is required if you are using an existing directory for identity management in Connect Customer when Connect Customer cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.
Type: String
Required: No

 ** [HierarchyGroupId](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-HierarchyGroupId"></a>
The identifier of the hierarchy group for the user.
Type: String
Required: No

 ** [IdentityInfo](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-IdentityInfo"></a>
The information about the identity of the user.
Type: [UserIdentityInfo](API_UserIdentityInfo.md) object
Required: No

 ** [Password](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-Password"></a>
The password for the user account. A password is required if you are using Connect Customer for identity management. Otherwise, it is an error to include a password.
Type: String
Pattern: `/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\S]{8,64}$/`
Required: No

 ** [PersistentConnectionConfigs](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-PersistentConnectionConfigs"></a>
The list of persistent connection configuration settings for each channel.
Type: Array of [PersistentConnectionConfig](API_PersistentConnectionConfig.md) objects
Required: No

 ** [PhoneConfig](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-PhoneConfig"></a>
The phone settings for the user. This parameter is optional. If not provided, the user can be configured using channel-specific parameters such as `AutoAcceptConfigs`, `AfterContactWorkConfigs`, `PhoneNumberConfigs`, `PersistentConnectionConfigs`, and `VoiceEnhancementConfigs`.
Type: [UserPhoneConfig](API_UserPhoneConfig.md) object
Required: No

 ** [PhoneNumberConfigs](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-PhoneNumberConfigs"></a>
The list of phone number configuration settings for each channel.
Type: Array of [PhoneNumberConfig](API_PhoneNumberConfig.md) objects
Required: No

 ** [RoutingProfileId](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-RoutingProfileId"></a>
The identifier of the routing profile for the user.
Type: String
Required: Yes

 ** [SecurityProfileIds](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-SecurityProfileIds"></a>
The identifier of the security profile for the user.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [Tags](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** [Username](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-Username"></a>
The user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [a-zA-Z0-9\_-.\\@]\+.
Username can include @ only if used in an email format. For example:
+ Correct: testuser
+ Correct: testuser@example.com
+ Incorrect: testuser@example
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [VoiceEnhancementConfigs](#API_CreateUser_RequestSyntax) **   <a name="connect-CreateUser-request-VoiceEnhancementConfigs"></a>
The list of voice enhancement configuration settings for each channel.
Type: Array of [VoiceEnhancementConfig](API_VoiceEnhancementConfig.md) objects
Required: No

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UserArn": "string",
   "UserId": "string"
}
```

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserArn](#API_CreateUser_ResponseSyntax) **   <a name="connect-CreateUser-response-UserArn"></a>
The Amazon Resource Name (ARN) of the user account.
Type: String

 ** [UserId](#API_CreateUser_ResponseSyntax) **   <a name="connect-CreateUser-response-UserId"></a>
The identifier of the user account.
Type: String

## Errors
<a name="API_CreateUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateUser)
