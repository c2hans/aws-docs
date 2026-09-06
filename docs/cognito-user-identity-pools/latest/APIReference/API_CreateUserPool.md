---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html
---

# CreateUserPool
<a name="API_CreateUserPool"></a>

Creates a new Amazon Cognito user pool. This operation sets basic and advanced configuration options.

You can create a user pool in the Amazon Cognito console to your preferences and use the output of [DescribeUserPool](API_DescribeUserPool.md) to generate requests from that baseline.

**Important**
If you don't provide a value for an attribute, Amazon Cognito sets it to its default value.

**Note**
This action might generate an SMS text message. Starting June 1, 2021, US telecom carriers require you to register an origination phone number before you can send SMS messages to US phone numbers. If you use SMS text messages in Amazon Cognito, you must register a phone number with [Amazon Pinpoint](https://console.aws.amazon.com/pinpoint/home/). Amazon Cognito uses the registered number automatically. Otherwise, Amazon Cognito users who must receive SMS messages might not be able to sign up, activate their accounts, or sign in.
If you have never used SMS text messages with Amazon Cognito or any other AWS service, Amazon Simple Notification Service might place your account in the SMS sandbox. In * [sandbox mode](https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox.html) *, you can send messages only to verified phone numbers. After you test your app while in the sandbox environment, you can move out of the sandbox and into production. For more information, see [ SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html) in the *Amazon Cognito Developer Guide*.

**Note**
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html)
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html)

## Request Syntax
<a name="API_CreateUserPool_RequestSyntax"></a>

```
{
   "AccountRecoverySetting": {
      "RecoveryMechanisms": [
         {
            "Name": "{{string}}",
            "Priority": {{number}}
         }
      ]
   },
   "AdminCreateUserConfig": {
      "AllowAdminCreateUserOnly": {{boolean}},
      "InviteMessageTemplate": {
         "EmailMessage": "{{string}}",
         "EmailSubject": "{{string}}",
         "SMSMessage": "{{string}}"
      },
      "UnusedAccountValidityDays": {{number}}
   },
   "AliasAttributes": [ "{{string}}" ],
   "AutoVerifiedAttributes": [ "{{string}}" ],
   "DeletionProtection": "{{string}}",
   "DeviceConfiguration": {
      "ChallengeRequiredOnNewDevice": {{boolean}},
      "DeviceOnlyRememberedOnUserPrompt": {{boolean}}
   },
   "EmailConfiguration": {
      "ConfigurationSet": "{{string}}",
      "EmailSendingAccount": "{{string}}",
      "From": "{{string}}",
      "ReplyToEmailAddress": "{{string}}",
      "SourceArn": "{{string}}"
   },
   "EmailVerificationMessage": "{{string}}",
   "EmailVerificationSubject": "{{string}}",
   "IssuerConfiguration": {
      "Type": "{{string}}"
   },
   "KeyConfiguration": {
      "KeyType": "{{string}}",
      "KmsKeyArn": "{{string}}"
   },
   "LambdaConfig": {
      "CreateAuthChallenge": "{{string}}",
      "CustomEmailSender": {
         "LambdaArn": "{{string}}",
         "LambdaVersion": "{{string}}"
      },
      "CustomMessage": "{{string}}",
      "CustomSMSSender": {
         "LambdaArn": "{{string}}",
         "LambdaVersion": "{{string}}"
      },
      "DefineAuthChallenge": "{{string}}",
      "InboundFederation": {
         "LambdaArn": "{{string}}",
         "LambdaVersion": "{{string}}"
      },
      "KMSKeyID": "{{string}}",
      "PostAuthentication": "{{string}}",
      "PostConfirmation": "{{string}}",
      "PreAuthentication": "{{string}}",
      "PreSignUp": "{{string}}",
      "PreTokenGeneration": "{{string}}",
      "PreTokenGenerationConfig": {
         "LambdaArn": "{{string}}",
         "LambdaVersion": "{{string}}"
      },
      "UserMigration": "{{string}}",
      "VerifyAuthChallengeResponse": "{{string}}"
   },
   "MfaConfiguration": "{{string}}",
   "Policies": {
      "PasswordPolicy": {
         "MinimumLength": {{number}},
         "PasswordHistorySize": {{number}},
         "RequireLowercase": {{boolean}},
         "RequireNumbers": {{boolean}},
         "RequireSymbols": {{boolean}},
         "RequireUppercase": {{boolean}},
         "TemporaryPasswordValidityDays": {{number}}
      },
      "SignInPolicy": {
         "AllowedFirstAuthFactors": [ "{{string}}" ]
      }
   },
   "PoolName": "{{string}}",
   "Schema": [
      {
         "AttributeDataType": "{{string}}",
         "DeveloperOnlyAttribute": {{boolean}},
         "Mutable": {{boolean}},
         "Name": "{{string}}",
         "NumberAttributeConstraints": {
            "MaxValue": "{{string}}",
            "MinValue": "{{string}}"
         },
         "Required": {{boolean}},
         "StringAttributeConstraints": {
            "MaxLength": "{{string}}",
            "MinLength": "{{string}}"
         }
      }
   ],
   "SmsAuthenticationMessage": "{{string}}",
   "SmsConfiguration": {
      "EumsSms": {
         "CallerArn": "{{string}}",
         "ConfigurationSetName": "{{string}}",
         "ExternalId": "{{string}}",
         "InEntityId": "{{string}}",
         "InTemplateId": "{{string}}",
         "OriginationIdentity": "{{string}}",
         "Region": "{{string}}"
      },
      "ExternalId": "{{string}}",
      "SnsCallerArn": "{{string}}",
      "SnsRegion": "{{string}}"
   },
   "SmsVerificationMessage": "{{string}}",
   "UserAttributeUpdateSettings": {
      "AttributesRequireVerificationBeforeUpdate": [ "{{string}}" ]
   },
   "UsernameAttributes": [ "{{string}}" ],
   "UsernameConfiguration": {
      "CaseSensitive": {{boolean}}
   },
   "UserPoolAddOns": {
      "AdvancedSecurityAdditionalFlows": {
         "CustomAuthMode": "{{string}}"
      },
      "AdvancedSecurityMode": "{{string}}"
   },
   "UserPoolTags": {
      "{{string}}" : "{{string}}"
   },
   "UserPoolTier": "{{string}}",
   "VerificationMessageTemplate": {
      "DefaultEmailOption": "{{string}}",
      "EmailMessage": "{{string}}",
      "EmailMessageByLink": "{{string}}",
      "EmailSubject": "{{string}}",
      "EmailSubjectByLink": "{{string}}",
      "SmsMessage": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateUserPool_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccountRecoverySetting](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-AccountRecoverySetting"></a>
The available verified method a user can use to recover their password when they call `ForgotPassword`. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. Email MFA is also disqualifying for account recovery with email. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.
As a best practice, configure both `verified_email` and `verified_phone_number`, with one having a higher priority than the other.
Type: [AccountRecoverySettingType](API_AccountRecoverySettingType.md) object
Required: No

 ** [AdminCreateUserConfig](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-AdminCreateUserConfig"></a>
The configuration for administrative creation of users. Includes the template for the invitation message for new users, the duration of temporary passwords, and permitting self-service sign-up.
Type: [AdminCreateUserConfigType](API_AdminCreateUserConfigType.md) object
Required: No

 ** [AliasAttributes](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-AliasAttributes"></a>
Attributes supported as an alias for this user pool. For more information about alias attributes, see [Customizing sign-in attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases).
Type: Array of strings
Valid Values: `phone_number | email | preferred_username`
Required: No

 ** [AutoVerifiedAttributes](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-AutoVerifiedAttributes"></a>
The attributes that you want your user pool to automatically verify. For more information, see [Verifying contact information at sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#allowing-users-to-sign-up-and-confirm-themselves).
Type: Array of strings
Valid Values: `phone_number | email`
Required: No

 ** [DeletionProtection](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-DeletionProtection"></a>
When active, `DeletionProtection` prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.
When you try to delete a protected user pool in a `DeleteUserPool` API request, Amazon Cognito returns an `InvalidParameterException` error. To delete a protected user pool, send a new `DeleteUserPool` request after you deactivate deletion protection in an `UpdateUserPool` API request.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: No

 ** [DeviceConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-DeviceConfiguration"></a>
The device-remembering configuration for a user pool. Device remembering or device tracking is a "Remember me on this device" option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html). A null value indicates that you have deactivated device remembering in your user pool.
When you provide a value for any `DeviceConfiguration` field, you activate the Amazon Cognito device-remembering feature. For more information, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).
Type: [DeviceConfigurationType](API_DeviceConfigurationType.md) object
Required: No

 ** [EmailConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-EmailConfiguration"></a>
The email configuration of your user pool. The email configuration type sets your preferred sending method, AWS Region, and sender for messages from your user pool.
Type: [EmailConfigurationType](API_EmailConfigurationType.md) object
Required: No

 ** [EmailVerificationMessage](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-EmailVerificationMessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 20000.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*\{####\}[\p{L}\p{M}\p{S}\p{N}\p{P}\s*]*`
Required: No

 ** [EmailVerificationSubject](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-EmailVerificationSubject"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\s]+`
Required: No

 ** [IssuerConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-IssuerConfiguration"></a>
The issuer configuration for the user pool. Specifies the issuer type for token generation.
Type: [IssuerConfigurationType](API_IssuerConfigurationType.md) object
Required: No

 ** [KeyConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-KeyConfiguration"></a>
The key configuration for the user pool. Specifies the key type and AWS KMS key ARN for encryption.
Type: [KeyConfigurationType](API_KeyConfigurationType.md) object
Required: No

 ** [LambdaConfig](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-LambdaConfig"></a>
A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.
Type: [LambdaConfigType](API_LambdaConfigType.md) object
Required: No

 ** [MfaConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-MfaConfiguration"></a>
Sets multi-factor authentication (MFA) to be on, off, or optional. When `ON`, all users must set up MFA before they can sign in. When `OPTIONAL`, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL`.
When `MfaConfiguration` is `OPTIONAL`, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.
The `CreateUserPool` operation supports only SMS MFA configuration. If you set `MfaConfiguration` to either of these values, include an `SmsConfiguration` in the same request:
+  `ON` – Requires MFA for all users
+  `OPTIONAL` – Makes MFA optional for each user
If you omit `SmsConfiguration`, the operation returns an `InvalidParameterException`. To configure TOTP or email MFA, use the [SetUserPoolMfaConfig](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SetUserPoolMfaConfig.html) operation. You can also use `SetUserPoolMfaConfig` to add MFA factors later.
Type: String
Valid Values: `OFF | ON | OPTIONAL`
Required: No

 ** [Policies](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-Policies"></a>
The password policy and sign-in policy in the user pool. The password policy sets options like password complexity requirements and password history. The sign-in policy sets the options available to applications in [choice-based authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice).
Type: [UserPoolPolicyType](API_UserPoolPolicyType.md) object
Required: No

 ** [PoolName](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-PoolName"></a>
A friendly name for your user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: Yes

 ** [Schema](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-Schema"></a>
An array of attributes for the new user pool. You can add custom attributes and modify the properties of default attributes. The specifications in this parameter set the required attributes in your user pool. For more information, see [Working with user attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html).
Type: Array of [SchemaAttributeType](API_SchemaAttributeType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [SmsAuthenticationMessage](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-SmsAuthenticationMessage"></a>
The contents of the SMS message that your user pool sends to users in SMS OTP and MFA authentication.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

 ** [SmsConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-SmsConfiguration"></a>
The settings for your Amazon Cognito user pool to send SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account. For more information see [SMS message settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html).
Type: [SmsConfigurationType](API_SmsConfigurationType.md) object
Required: No

 ** [SmsVerificationMessage](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-SmsVerificationMessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md).
This parameter is no longer used.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

 ** [UserAttributeUpdateSettings](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UserAttributeUpdateSettings"></a>
The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate`, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see [ Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates).
Type: [UserAttributeUpdateSettingsType](API_UserAttributeUpdateSettingsType.md) object
Required: No

 ** [UsernameAttributes](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UsernameAttributes"></a>
Specifies whether a user can use an email address or phone number as a username when they sign up. For more information, see [Customizing sign-in attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases).
Type: Array of strings
Valid Values: `phone_number | email`
Required: No

 ** [UsernameConfiguration](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UsernameConfiguration"></a>
Sets the case sensitivity option for sign-in usernames. When `CaseSensitive` is `false` (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, `username`, `USERNAME`, or `UserName`, or for email, `email@example.com` or `EMaiL@eXamplE.Com`. For most use cases, set case sensitivity to `false` as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.
When `CaseSensitive` is `true` (case sensitive), Amazon Cognito interprets `USERNAME` and `UserName` as distinct users.
This configuration is immutable after you set it.
Type: [UsernameConfigurationType](API_UsernameConfigurationType.md) object
Required: No

 ** [UserPoolAddOns](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UserPoolAddOns"></a>
Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to `AUDIT`. To configure automatic security responses to potentially unwanted traffic to your user pool, set to `ENFORCED`.
For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html). To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).
Type: [UserPoolAddOnsType](API_UserPoolAddOnsType.md) object
Required: No

 ** [UserPoolTags](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UserPoolTags"></a>
The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [UserPoolTier](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-UserPoolTier"></a>
The user pool [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html), or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to `ESSENTIALS`.
Type: String
Valid Values: `LITE | ESSENTIALS | PLUS`
Required: No

 ** [VerificationMessageTemplate](#API_CreateUserPool_RequestSyntax) **   <a name="CognitoUserPools-CreateUserPool-request-VerificationMessageTemplate"></a>
The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.
Set the email message type that corresponds to your `DefaultEmailOption` selection. For `CONFIRM_WITH_LINK`, specify an `EmailMessageByLink` and leave `EmailMessage` blank. For `CONFIRM_WITH_CODE`, specify an `EmailMessage` and leave `EmailMessageByLink` blank. When you supply both parameters with either choice, Amazon Cognito returns an error.
Type: [VerificationMessageTemplateType](API_VerificationMessageTemplateType.md) object
Required: No

## Response Syntax
<a name="API_CreateUserPool_ResponseSyntax"></a>

```
{
   "UserPool": {
      "AccountRecoverySetting": {
         "RecoveryMechanisms": [
            {
               "Name": "string",
               "Priority": number
            }
         ]
      },
      "AdminCreateUserConfig": {
         "AllowAdminCreateUserOnly": boolean,
         "InviteMessageTemplate": {
            "EmailMessage": "string",
            "EmailSubject": "string",
            "SMSMessage": "string"
         },
         "UnusedAccountValidityDays": number
      },
      "AliasAttributes": [ "string" ],
      "Arn": "string",
      "AutoVerifiedAttributes": [ "string" ],
      "CreationDate": number,
      "CustomDomain": "string",
      "DeletionProtection": "string",
      "DeviceConfiguration": {
         "ChallengeRequiredOnNewDevice": boolean,
         "DeviceOnlyRememberedOnUserPrompt": boolean
      },
      "Domain": "string",
      "EmailConfiguration": {
         "ConfigurationSet": "string",
         "EmailSendingAccount": "string",
         "From": "string",
         "ReplyToEmailAddress": "string",
         "SourceArn": "string"
      },
      "EmailConfigurationFailure": "string",
      "EmailVerificationMessage": "string",
      "EmailVerificationSubject": "string",
      "EstimatedNumberOfUsers": number,
      "Id": "string",
      "IssuerConfiguration": {
         "Type": "string"
      },
      "KeyConfiguration": {
         "KeyType": "string",
         "KmsKeyArn": "string"
      },
      "LambdaConfig": {
         "CreateAuthChallenge": "string",
         "CustomEmailSender": {
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "CustomMessage": "string",
         "CustomSMSSender": {
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "DefineAuthChallenge": "string",
         "InboundFederation": {
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "KMSKeyID": "string",
         "PostAuthentication": "string",
         "PostConfirmation": "string",
         "PreAuthentication": "string",
         "PreSignUp": "string",
         "PreTokenGeneration": "string",
         "PreTokenGenerationConfig": {
            "LambdaArn": "string",
            "LambdaVersion": "string"
         },
         "UserMigration": "string",
         "VerifyAuthChallengeResponse": "string"
      },
      "LastModifiedDate": number,
      "MfaConfiguration": "string",
      "Name": "string",
      "Policies": {
         "PasswordPolicy": {
            "MinimumLength": number,
            "PasswordHistorySize": number,
            "RequireLowercase": boolean,
            "RequireNumbers": boolean,
            "RequireSymbols": boolean,
            "RequireUppercase": boolean,
            "TemporaryPasswordValidityDays": number
         },
         "SignInPolicy": {
            "AllowedFirstAuthFactors": [ "string" ]
         }
      },
      "SchemaAttributes": [
         {
            "AttributeDataType": "string",
            "DeveloperOnlyAttribute": boolean,
            "Mutable": boolean,
            "Name": "string",
            "NumberAttributeConstraints": {
               "MaxValue": "string",
               "MinValue": "string"
            },
            "Required": boolean,
            "StringAttributeConstraints": {
               "MaxLength": "string",
               "MinLength": "string"
            }
         }
      ],
      "SmsAuthenticationMessage": "string",
      "SmsConfiguration": {
         "EumsSms": {
            "CallerArn": "string",
            "ConfigurationSetName": "string",
            "ExternalId": "string",
            "InEntityId": "string",
            "InTemplateId": "string",
            "OriginationIdentity": "string",
            "Region": "string"
         },
         "ExternalId": "string",
         "SnsCallerArn": "string",
         "SnsRegion": "string"
      },
      "SmsConfigurationFailure": "string",
      "SmsVerificationMessage": "string",
      "Status": "string",
      "UserAttributeUpdateSettings": {
         "AttributesRequireVerificationBeforeUpdate": [ "string" ]
      },
      "UsernameAttributes": [ "string" ],
      "UsernameConfiguration": {
         "CaseSensitive": boolean
      },
      "UserPoolAddOns": {
         "AdvancedSecurityAdditionalFlows": {
            "CustomAuthMode": "string"
         },
         "AdvancedSecurityMode": "string"
      },
      "UserPoolTags": {
         "string" : "string"
      },
      "UserPoolTier": "string",
      "VerificationMessageTemplate": {
         "DefaultEmailOption": "string",
         "EmailMessage": "string",
         "EmailMessageByLink": "string",
         "EmailSubject": "string",
         "EmailSubjectByLink": "string",
         "SmsMessage": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateUserPool_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPool](#API_CreateUserPool_ResponseSyntax) **   <a name="CognitoUserPools-CreateUserPool-response-UserPool"></a>
The details of the created user pool.
Type: [UserPoolType](API_UserPoolType.md) object

## Errors
<a name="API_CreateUserPool_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureUnavailableInTierException **
This exception is thrown when a feature you attempted to configure isn't available in your current feature plan.
HTTP Status Code: 400

 ** InternalErrorException **
This exception is thrown when Amazon Cognito encounters an internal error.
 ** message **
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidEmailRoleAccessPolicyException **
This exception is thrown when Amazon Cognito isn't allowed to use your email identity. HTTP status code: 400.
 ** message **
The message returned when you have an unverified email address or the identity policy isn't set on an email address that Amazon Cognito can access.
HTTP Status Code: 400

 ** InvalidParameterException **
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.
 ** message **
The message returned when the Amazon Cognito service throws an invalid parameter exception.
 ** reasonCode **
The reason code of the exception.
HTTP Status Code: 400

 ** InvalidSmsRoleAccessPolicyException **
This exception is returned when the role provided for SMS configuration doesn't have permission to publish using Amazon SNS.
 ** message **
The message returned when the invalid SMS role access policy exception is thrown.
HTTP Status Code: 400

 ** InvalidSmsRoleTrustRelationshipException **
This exception is thrown when the trust relationship is not valid for the role provided for SMS configuration. This can happen if you don't trust `cognito-idp.amazonaws.com` or the external ID provided in the role does not match what is provided in the SMS configuration for the user pool.
 ** message **
The message returned when the role trust relationship for the SMS message is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
This exception is thrown when a user exceeds the limit for a requested AWS resource.
 ** message **
The message returned when Amazon Cognito throws a limit exceeded exception.
HTTP Status Code: 400

 ** NotAuthorizedException **
This exception is thrown when a user isn't authorized.
 ** message **
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** TierChangeNotAllowedException **
This exception is thrown when you've attempted to change your feature plan but the operation isn't permitted.
HTTP Status Code: 400

 ** TooManyRequestsException **
This exception is thrown when the user has made too many requests for a given operation.
 ** message **
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

 ** UserPoolTaggingException **
This exception is thrown when a user pool tag can't be set or updated.
HTTP Status Code: 400

## Examples
<a name="API_CreateUserPool_Examples"></a>

### Example
<a name="API_CreateUserPool_Example_1"></a>

The following example creates a user pool with all configurable properties set to an example value. The resulting user pool allows sign-in with username or email address, has optional MFA, and has a Lambda function assigned to each possible trigger.

#### Sample Request
<a name="API_CreateUserPool_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateUserPool
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
    "AccountRecoverySetting": {
        "RecoveryMechanisms": [
            {
                "Name": "verified_email",
                "Priority": 1
            }
        ]
    },
    "AdminCreateUserConfig": {
        "AllowAdminCreateUserOnly": false,
        "InviteMessageTemplate": {
            "EmailMessage": "Your username is {username} and temporary password is {####}.",
            "EmailSubject": "Your sign-in information",
            "SMSMessage": "Your username is {username} and temporary password is {####}."
        }
    },
    "AliasAttributes": [
        "email"
    ],
    "AutoVerifiedAttributes": [
        "email"
    ],
    "DeviceConfiguration": {
        "ChallengeRequiredOnNewDevice": true,
        "DeviceOnlyRememberedOnUserPrompt": true
    },
    "DeletionProtection": "ACTIVE",
    "EmailConfiguration": {
        "ConfigurationSet": "my-test-ses-configuration-set",
        "EmailSendingAccount": "DEVELOPER",
        "From": "support@example.com",
        "ReplyToEmailAddress": "support@example.com",
        "SourceArn": "arn:aws:ses:us-east-1:123456789012:identity/support@example.com"
    },
    "EmailVerificationMessage": "Your verification code is {####}.",
    "EmailVerificationSubject": "Verify your email address",
    "LambdaConfig": {
        "KMSKeyID": "arn:aws:kms:us-east-1:123456789012:key/a6c4f8e2-0c45-47db-925f-87854bc9e357",
        "CustomEmailSender": {
            "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "LambdaVersion": "V1_0"
        },
        "CustomSMSSender": {
            "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "LambdaVersion": "V1_0"
        },
        "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "DefineAuthChallenge": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "PostAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "PostConfirmation": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "PreAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "VerifyAuthChallengeResponse": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
        "InboundFederation": {
            "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "LambdaVersion": "V1_0"
        }
    },
    "MfaConfiguration": "OPTIONAL",
    "Policies": {
        "PasswordPolicy": {
            "MinimumLength": 6,
            "RequireLowercase": true,
            "RequireNumbers": true,
            "RequireSymbols": true,
            "RequireUppercase": true,
            "TemporaryPasswordValidityDays": 7
        },
        "SignInPolicy": {
            "AllowedFirstAuthFactors": [
                "PASSWORD",
                "EMAIL_OTP",
                "WEB_AUTHN"
            ]
        }
    },
    "PoolName": "my-test-user-pool",
    "Schema": [
        {
            "AttributeDataType": "Number",
            "DeveloperOnlyAttribute": true,
            "Mutable": true,
            "Name": "mydev",
            "NumberAttributeConstraints": {
                "MaxValue": "99",
                "MinValue": "1"
            },
            "Required": false,
            "StringAttributeConstraints": {
                "MaxLength": "99",
                "MinLength": "1"
            }
        }
    ],
    "SmsAuthenticationMessage": "Your verification code is {####}.",
    "SmsConfiguration": {
        "ExternalId": "my-role-external-id",
        "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-cognito-SMS-Role"
    },
    "SmsVerificationMessage": "Your verification code is {####}.",
    "UserAttributeUpdateSettings": {
        "AttributesRequireVerificationBeforeUpdate": [
            "email"
        ]
    },
    "UsernameConfiguration": {
        "CaseSensitive": true
    },
    "UserPoolAddOns": {
        "AdvancedSecurityMode": "OFF"
    },
    "UserPoolTags": {
        "my-test-tag-key": "my-test-tag-key"
    },
    "UserPoolTier": "ESSENTIALS",
    "VerificationMessageTemplate": {
        "DefaultEmailOption": "CONFIRM_WITH_CODE",
        "EmailMessage": "Your confirmation code is {####}",
        "EmailMessageByLink": "Choose this link to {##verify your email##}",
        "EmailSubject": "Here is your confirmation code",
        "EmailSubjectByLink": "Here is your confirmation link",
        "SmsMessage": "Your confirmation code is {####}"
    }
}
```

#### Sample Response
<a name="API_CreateUserPool_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
    "UserPool": {
        "AccountRecoverySetting": {
            "RecoveryMechanisms": [
                {
                    "Name": "verified_email",
                    "Priority": 1
                }
            ]
        },
        "AdminCreateUserConfig": {
            "AllowAdminCreateUserOnly": false,
            "InviteMessageTemplate": {
                "EmailMessage": "Your username is {username} and temporary password is {####}.",
                "EmailSubject": "Your sign-in information",
                "SMSMessage": "Your username is {username} and temporary password is {####}."
            },
            "UnusedAccountValidityDays": 7
        },
        "AliasAttributes": [
            "email"
        ],
        "Arn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_EXAMPLE",
        "AutoVerifiedAttributes": [
            "email"
        ],
        "CreationDate": 1689721665.239,
        "DeletionProtection": "ACTIVE",
        "DeviceConfiguration": {
            "ChallengeRequiredOnNewDevice": true,
            "DeviceOnlyRememberedOnUserPrompt": true
        },
        "EmailConfiguration": {
            "ConfigurationSet": "my-test-ses-configuration-set",
            "EmailSendingAccount": "DEVELOPER",
            "From": "support@example.com",
            "ReplyToEmailAddress": "support@example.com",
            "SourceArn": "arn:aws:ses:us-east-1:123456789012:identity/support@example.com"
        },
        "EmailVerificationMessage": "Your verification code is {####}.",
        "EmailVerificationSubject": "Verify your email address",
        "EstimatedNumberOfUsers": 0,
        "Id": "us-east-1_EXAMPLE",
        "LambdaConfig": {
            "CustomEmailSender": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            },
            "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "CustomSMSSender": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            },
            "DefineAuthChallenge": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "KMSKeyID": "arn:aws:kms:us-east-1:767671399759:key/4d43904c-8edf-4bb4-9fca-fb1a80e41cbe",
            "PostAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PostConfirmation": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreAuthentication": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "VerifyAuthChallengeResponse": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
            "InboundFederation": {
                "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "LambdaVersion": "V1_0"
            }
        },
        "LastModifiedDate": 1689721665.239,
        "MfaConfiguration": "OPTIONAL",
        "Name": "my-test-user-pool",
        "Policies": {
            "PasswordPolicy": {
                "MinimumLength": 6,
                "RequireLowercase": true,
                "RequireNumbers": true,
                "RequireSymbols": true,
                "RequireUppercase": true,
                "TemporaryPasswordValidityDays": 7
            }
        },
        "SchemaAttributes": [
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": false,
                "Name": "sub",
                "Required": true,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "1"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "given_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "family_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "middle_name",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "nickname",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "preferred_username",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "profile",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "picture",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "website",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "email",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Boolean",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "email_verified",
                "Required": false
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "gender",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "birthdate",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "10",
                    "MinLength": "10"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "zoneinfo",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "locale",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "phone_number",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Boolean",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "phone_number_verifie",
                "Required": false
            },
            {
                "AttributeDataType": "String",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "address",
                "Required": false,
                "StringAttributeConstraints": {
                    "MaxLength": "2048",
                    "MinLength": "0"
                }
            },
            {
                "AttributeDataType": "Number",
                "DeveloperOnlyAttribute": false,
                "Mutable": true,
                "Name": "updated_at",
                "NumberAttributeConstraints": {
                    "MinValue": "0"
                },
                "Required": false
            },
            {
                "AttributeDataType": "Number",
                "DeveloperOnlyAttribute": true,
                "Mutable": true,
                "Name": "dev:custom:mydev",
                "NumberAttributeConstraints": {
                    "MaxValue": "99",
                    "MinValue": "1"
                },
                "Required": false
            }
        ],
        "SmsAuthenticationMessage": "Your verification code is {####}.",
        "SmsConfiguration": {
            "ExternalId": "my-role-external-id",
            "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/test-cognito-SMS-Role",
            "SnsRegion": "us-east-1"
        },
        "SmsVerificationMessage": "Your verification code is {####}.",
        "UserAttributeUpdateSettings": {
            "AttributesRequireVerificationBeforeUpdate": [
                "email"
            ]
        },
        "UserPoolAddOns": {
            "AdvancedSecurityMode": "OFF"
        },
        "UserPoolTags": {
            "my-test-tag-key": "my-test-tag-value"
        },
        "UserPoolTier": "ESSENTIALS",
        "UsernameConfiguration": {
            "CaseSensitive": true
        },
        "VerificationMessageTemplate": {
            "DefaultEmailOption": "CONFIRM_WITH_CODE",
            "EmailMessage": "Your confirmation code is {####}",
            "EmailMessageByLink": "Choose this link to {##verify your email##}",
            "EmailSubject": "Here is your confirmation code",
            "EmailSubjectByLink": "Here is your confirmation link",
            "SmsMessage": "Your confirmation code is {####}"
        }
    }
}
```

## See Also
<a name="API_CreateUserPool_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateUserPool)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateUserPool)
