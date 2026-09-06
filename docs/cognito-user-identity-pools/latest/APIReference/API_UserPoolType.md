---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolType.html
---

# UserPoolType
<a name="API_UserPoolType"></a>

The configuration of a user pool.

This data type is a response parameter of [CreateUserPool](API_CreateUserPool.md), [UpdateUserPool](API_UpdateUserPool.md), and [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_UserPoolType_Contents"></a>

 ** AccountRecoverySetting **   <a name="CognitoUserPools-Type-UserPoolType-AccountRecoverySetting"></a>
The available verified method a user can use to recover their password when they call `ForgotPassword`. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.
Type: [AccountRecoverySettingType](API_AccountRecoverySettingType.md) object
Required: No

 ** AdminCreateUserConfig **   <a name="CognitoUserPools-Type-UserPoolType-AdminCreateUserConfig"></a>
The configuration for `AdminCreateUser` requests.
Type: [AdminCreateUserConfigType](API_AdminCreateUserConfigType.md) object
Required: No

 ** AliasAttributes **   <a name="CognitoUserPools-Type-UserPoolType-AliasAttributes"></a>
Attributes supported as an alias for this user pool. An alias is an attribute that users can enter as an alternative username. Possible values: **phone\_number**, **email**, or **preferred\_username**.
Type: Array of strings
Valid Values: `phone_number | email | preferred_username`
Required: No

 ** Arn **   <a name="CognitoUserPools-Type-UserPoolType-Arn"></a>
The Amazon Resource Name (ARN) of the user pool.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** AutoVerifiedAttributes **   <a name="CognitoUserPools-Type-UserPoolType-AutoVerifiedAttributes"></a>
The attributes that are auto-verified in a user pool.
Type: Array of strings
Valid Values: `phone_number | email`
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-UserPoolType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** CustomDomain **   <a name="CognitoUserPools-Type-UserPoolType-CustomDomain"></a>
A custom domain name that you provide to Amazon Cognito. This parameter applies only if you use a custom domain to host the sign-up and sign-in pages for your application. An example of a custom domain name might be `auth.example.com`.
For more information about adding a custom domain to your user pool, see [Using Your Own Domain for the Hosted UI](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: No

 ** DeletionProtection **   <a name="CognitoUserPools-Type-UserPoolType-DeletionProtection"></a>
When active, `DeletionProtection` prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.
When you try to delete a protected user pool in a `DeleteUserPool` API request, Amazon Cognito returns an `InvalidParameterException` error. To delete a protected user pool, send a new `DeleteUserPool` request after you deactivate deletion protection in an `UpdateUserPool` API request.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** DeviceConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-DeviceConfiguration"></a>
The device-remembering configuration for a user pool. A null value indicates that you have deactivated device remembering in your user pool.
When you provide a value for any `DeviceConfiguration` field, you activate the Amazon Cognito device-remembering feature.
Type: [DeviceConfigurationType](API_DeviceConfigurationType.md) object
Required: No

 ** Domain **   <a name="CognitoUserPools-Type-UserPoolType-Domain"></a>
The domain prefix, if the user pool has a domain associated with it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?$`
Required: No

 ** EmailConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-EmailConfiguration"></a>
The email configuration of your user pool. The email configuration type sets your preferred sending method, AWS Region, and sender for messages from your user pool.
Type: [EmailConfigurationType](API_EmailConfigurationType.md) object
Required: No

 ** EmailConfigurationFailure **   <a name="CognitoUserPools-Type-UserPoolType-EmailConfigurationFailure"></a>
Deprecated. Review error codes from API requests with `EventSource:cognito-idp.amazonaws.com` in AWS CloudTrail for information about problems with user pool email configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** EmailVerificationMessage **   <a name="CognitoUserPools-Type-UserPoolType-EmailVerificationMessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** EmailVerificationSubject **   <a name="CognitoUserPools-Type-UserPoolType-EmailVerificationSubject"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

 ** EstimatedNumberOfUsers **   <a name="CognitoUserPools-Type-UserPoolType-EstimatedNumberOfUsers"></a>
A number estimating the size of the user pool.
Type: Integer
Required: No

 ** Id **   <a name="CognitoUserPools-Type-UserPoolType-Id"></a>
The ID of the user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

 ** IssuerConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-IssuerConfiguration"></a>
The issuer configuration for the user pool, including token issuing settings.
Type: [IssuerConfigurationType](API_IssuerConfigurationType.md) object
Required: No

 ** KeyConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-KeyConfiguration"></a>
The key configuration for the user pool, including encryption settings.
Type: [KeyConfigurationType](API_KeyConfigurationType.md) object
Required: No

 ** LambdaConfig **   <a name="CognitoUserPools-Type-UserPoolType-LambdaConfig"></a>
A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.
Type: [LambdaConfigType](API_LambdaConfigType.md) object
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-UserPoolType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** MfaConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-MfaConfiguration"></a>
Can be one of the following values:
+  `OFF` - MFA tokens aren't required and can't be specified during user registration.
+  `ON` - MFA tokens are required for all user registrations. You can only specify required when you're initially creating a user pool.
+  `OPTIONAL` - Users have the option when registering to create an MFA token.
Type: String
Valid Values: `OFF | ON | OPTIONAL`
Required: No

 ** Name **   <a name="CognitoUserPools-Type-UserPoolType-Name"></a>
The name of the user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** Policies **   <a name="CognitoUserPools-Type-UserPoolType-Policies"></a>
A list of user pool policies. Contains the policy that sets password-complexity requirements.
Type: [UserPoolPolicyType](API_UserPoolPolicyType.md) object
Required: No

 ** SchemaAttributes **   <a name="CognitoUserPools-Type-UserPoolType-SchemaAttributes"></a>
A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a `custom:` prefix, and developer attributes with a `dev:` prefix. For more information, see [User pool attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html).
Developer-only attributes are a legacy feature of user pools, and are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.
Type: Array of [SchemaAttributeType](API_SchemaAttributeType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** SmsAuthenticationMessage **   <a name="CognitoUserPools-Type-UserPoolType-SmsAuthenticationMessage"></a>
The contents of the SMS authentication message.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

 ** SmsConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-SmsConfiguration"></a>
User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account.
Type: [SmsConfigurationType](API_SmsConfigurationType.md) object
Required: No

 ** SmsConfigurationFailure **   <a name="CognitoUserPools-Type-UserPoolType-SmsConfigurationFailure"></a>
The reason why the SMS configuration can't send the messages to your users.
This message might include comma-separated values to describe why your SMS configuration can't send messages to user pool end users.
InvalidSmsRoleAccessPolicyException
The AWS Identity and Access Management role that Amazon Cognito uses to send SMS messages isn't properly configured. For more information, see [SmsConfigurationType](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.html).
SNSSandbox
The AWS account is in the SNS SMS Sandbox and messages will only reach verified end users. This parameter won’t get populated with SNSSandbox if the user creating the user pool doesn’t have SNS permissions. To learn how to move your AWS account out of the sandbox, see [Moving out of the SMS sandbox](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-moving-to-production.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** SmsVerificationMessage **   <a name="CognitoUserPools-Type-UserPoolType-SmsVerificationMessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

 ** Status **   <a name="CognitoUserPools-Type-UserPoolType-Status"></a>
 *This member has been deprecated.*
This parameter is no longer used.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** UserAttributeUpdateSettings **   <a name="CognitoUserPools-Type-UserPoolType-UserAttributeUpdateSettings"></a>
The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate`, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see [ Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates).
Type: [UserAttributeUpdateSettingsType](API_UserAttributeUpdateSettingsType.md) object
Required: No

 ** UsernameAttributes **   <a name="CognitoUserPools-Type-UserPoolType-UsernameAttributes"></a>
Specifies whether a user can use an email address or phone number as a username when they sign up.
Type: Array of strings
Valid Values: `phone_number | email`
Required: No

 ** UsernameConfiguration **   <a name="CognitoUserPools-Type-UserPoolType-UsernameConfiguration"></a>
Case sensitivity of the username input for the selected sign-in option. When case sensitivity is set to `False` (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, `username`, `USERNAME`, or `UserName`, or for email, `email@example.com` or `EMaiL@eXamplE.Com`. For most use cases, set case sensitivity to `False` (case insensitive) as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.
This configuration is immutable after you set it. For more information, see [UsernameConfigurationType](API_UsernameConfigurationType.md).
Type: [UsernameConfigurationType](API_UsernameConfigurationType.md) object
Required: No

 ** UserPoolAddOns **   <a name="CognitoUserPools-Type-UserPoolType-UserPoolAddOns"></a>
Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to `AUDIT`. To configure automatic security responses to potentially unwanted traffic to your user pool, set to `ENFORCED`.
For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html). To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).
Type: [UserPoolAddOnsType](API_UserPoolAddOnsType.md) object
Required: No

 ** UserPoolTags **   <a name="CognitoUserPools-Type-UserPoolType-UserPoolTags"></a>
The tags that are assigned to the user pool. A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** UserPoolTier **   <a name="CognitoUserPools-Type-UserPoolType-UserPoolTier"></a>
The user pool [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html), or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to `ESSENTIALS`.
Type: String
Valid Values: `LITE | ESSENTIALS | PLUS`
Required: No

 ** VerificationMessageTemplate **   <a name="CognitoUserPools-Type-UserPoolType-VerificationMessageTemplate"></a>
The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.
Type: [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md) object
Required: No

## See Also
<a name="API_UserPoolType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolType)
