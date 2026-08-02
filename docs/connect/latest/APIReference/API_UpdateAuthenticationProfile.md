---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateAuthenticationProfile.html
---

# UpdateAuthenticationProfile
<a name="API_UpdateAuthenticationProfile"></a>

This API is in preview release for Connect Customer and is subject to change. To request access to this API, contact Support.

Updates the selected authentication profile.

## Request Syntax
<a name="API_UpdateAuthenticationProfile_RequestSyntax"></a>

```
POST /authentication-profiles/{{InstanceId}}/{{AuthenticationProfileId}} HTTP/1.1
Content-type: application/json

{
   "AllowedIps": [ "{{string}}" ],
   "BlockedIps": [ "{{string}}" ],
   "Description": "{{string}}",
   "Name": "{{string}}",
   "PeriodicSessionDuration": {{number}},
   "SessionInactivityDuration": {{number}},
   "SessionInactivityHandlingEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateAuthenticationProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AuthenticationProfileId](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-uri-AuthenticationProfileId"></a>
A unique identifier for the authentication profile.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [InstanceId](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_UpdateAuthenticationProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AllowedIps](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-AllowedIps"></a>
A list of IP address range strings that are allowed to access the instance. For more information on how to configure IP addresses, see[Configure session timeouts](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts) in the *Connect Customer Administrator Guide*.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `^[A-Za-z0-9:/]*$`
Required: No

 ** [BlockedIps](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-BlockedIps"></a>
A list of IP address range strings that are blocked from accessing the instance. For more information on how to configure IP addresses, For more information on how to configure IP addresses, see [Configure IP-based access control](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-ip-based-ac) in the *Connect Customer Administrator Guide*.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 50.
Pattern: `^[A-Za-z0-9:/]*$`
Required: No

 ** [Description](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-Description"></a>
The description for the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** [Name](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-Name"></a>
The name for the authentication profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [PeriodicSessionDuration](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-PeriodicSessionDuration"></a>
 *This parameter has been deprecated.*
The short lived session duration configuration for users logged in to Connect Customer, in minutes. This value determines the maximum possible time before an agent is authenticated. For more information, For more information on how to configure IP addresses, see [Configure session timeouts](https://docs.aws.amazon.com/connect/latest/adminguide/authentication-profiles.html#configure-session-timeouts) in the *Connect Customer Administrator Guide*.
Type: Integer
Valid Range: Minimum value of 10. Maximum value of 60.
Required: No

 ** [SessionInactivityDuration](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-SessionInactivityDuration"></a>
The period, in minutes, before an agent is automatically signed out of the contact center when they go inactive.
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 720.
Required: No

 ** [SessionInactivityHandlingEnabled](#API_UpdateAuthenticationProfile_RequestSyntax) **   <a name="connect-UpdateAuthenticationProfile-request-SessionInactivityHandlingEnabled"></a>
Determines if automatic logout on user inactivity is enabled.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateAuthenticationProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateAuthenticationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateAuthenticationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateAuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateAuthenticationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateAuthenticationProfile)
