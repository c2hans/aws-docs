---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminCreateUserConfigType.html
---

# AdminCreateUserConfigType
<a name="API_AdminCreateUserConfigType"></a>

The settings for administrator creation of users in a user pool. Contains settings for allowing user sign-up, customizing invitation messages to new users, and the amount of time before temporary passwords expire.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_AdminCreateUserConfigType_Contents"></a>

 ** AllowAdminCreateUserOnly **   <a name="CognitoUserPools-Type-AdminCreateUserConfigType-AllowAdminCreateUserOnly"></a>
The setting for allowing self-service sign-up. When `true`, only administrators can create new user profiles. When `false`, users can register themselves and create a new user profile with the `SignUp` operation.
Type: Boolean
Required: No

 ** InviteMessageTemplate **   <a name="CognitoUserPools-Type-AdminCreateUserConfigType-InviteMessageTemplate"></a>
The template for the welcome message to new users. This template must include the `{####}` temporary password placeholder if you are creating users with passwords. If your users don't have passwords, you can omit the placeholder.
See also [Customizing User Invitation Messages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization).
Type: [MessageTemplateType](API_MessageTemplateType.md) object
Required: No

 ** UnusedAccountValidityDays **   <a name="CognitoUserPools-Type-AdminCreateUserConfigType-UnusedAccountValidityDays"></a>
This parameter is no longer in use.
Configure the duration of temporary passwords with the `TemporaryPasswordValidityDays` parameter of [PasswordPolicyType](API_PasswordPolicyType.md). For older user pools that have a `UnusedAccountValidityDays` configuration, that value is effective until you set a value for `TemporaryPasswordValidityDays`.
The password expiration limit in days for administrator-created users. When this time expires, the user can't sign in with their temporary password. To reset the account after that time limit, you must call `AdminCreateUser` again, specifying `RESEND` for the `MessageAction` parameter.
The default value for this parameter is 7.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 365.
Required: No

## See Also
<a name="API_AdminCreateUserConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AdminCreateUserConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AdminCreateUserConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AdminCreateUserConfigType)
