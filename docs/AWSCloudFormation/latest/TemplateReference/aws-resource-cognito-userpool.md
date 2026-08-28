---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpool.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool
<a name="aws-resource-cognito-userpool"></a>

The `AWS::Cognito::UserPool` resource creates an Amazon Cognito user pool. For more information on working with Amazon Cognito user pools, see [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) and [CreateUserPool](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.html).

**Note**
If you don't specify a value for a parameter, Amazon Cognito sets it to a default value.

## Syntax
<a name="aws-resource-cognito-userpool-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpool-syntax.json"></a>

```
{
  "Type" : "AWS::Cognito::UserPool",
  "Properties" : {
      "[AccountRecoverySetting](#cfn-cognito-userpool-accountrecoverysetting)" : {{AccountRecoverySetting}},
      "[AdminCreateUserConfig](#cfn-cognito-userpool-admincreateuserconfig)" : {{AdminCreateUserConfig}},
      "[AliasAttributes](#cfn-cognito-userpool-aliasattributes)" : {{[ String, ... ]}},
      "[AutoVerifiedAttributes](#cfn-cognito-userpool-autoverifiedattributes)" : {{[ String, ... ]}},
      "[DeletionProtection](#cfn-cognito-userpool-deletionprotection)" : {{String}},
      "[DeviceConfiguration](#cfn-cognito-userpool-deviceconfiguration)" : {{DeviceConfiguration}},
      "[EmailAuthenticationMessage](#cfn-cognito-userpool-emailauthenticationmessage)" : {{String}},
      "[EmailAuthenticationSubject](#cfn-cognito-userpool-emailauthenticationsubject)" : {{String}},
      "[EmailConfiguration](#cfn-cognito-userpool-emailconfiguration)" : {{EmailConfiguration}},
      "[EmailVerificationMessage](#cfn-cognito-userpool-emailverificationmessage)" : {{String}},
      "[EmailVerificationSubject](#cfn-cognito-userpool-emailverificationsubject)" : {{String}},
      "[EnabledMfas](#cfn-cognito-userpool-enabledmfas)" : {{[ String, ... ]}},
      "[IssuerConfiguration](#cfn-cognito-userpool-issuerconfiguration)" : {{IssuerConfiguration}},
      "[KeyConfiguration](#cfn-cognito-userpool-keyconfiguration)" : {{KeyConfiguration}},
      "[LambdaConfig](#cfn-cognito-userpool-lambdaconfig)" : {{LambdaConfig}},
      "[MfaConfiguration](#cfn-cognito-userpool-mfaconfiguration)" : {{String}},
      "[Policies](#cfn-cognito-userpool-policies)" : {{Policies}},
      "[Schema](#cfn-cognito-userpool-schema)" : {{[ SchemaAttribute, ... ]}},
      "[SmsAuthenticationMessage](#cfn-cognito-userpool-smsauthenticationmessage)" : {{String}},
      "[SmsConfiguration](#cfn-cognito-userpool-smsconfiguration)" : {{SmsConfiguration}},
      "[SmsVerificationMessage](#cfn-cognito-userpool-smsverificationmessage)" : {{String}},
      "[UserAttributeUpdateSettings](#cfn-cognito-userpool-userattributeupdatesettings)" : {{UserAttributeUpdateSettings}},
      "[UsernameAttributes](#cfn-cognito-userpool-usernameattributes)" : {{[ String, ... ]}},
      "[UsernameConfiguration](#cfn-cognito-userpool-usernameconfiguration)" : {{UsernameConfiguration}},
      "[UserPoolAddOns](#cfn-cognito-userpool-userpooladdons)" : {{UserPoolAddOns}},
      "[UserPoolName](#cfn-cognito-userpool-userpoolname)" : {{String}},
      "[UserPoolTags](#cfn-cognito-userpool-userpooltags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[UserPoolTier](#cfn-cognito-userpool-userpooltier)" : {{String}},
      "[VerificationMessageTemplate](#cfn-cognito-userpool-verificationmessagetemplate)" : {{VerificationMessageTemplate}},
      "[WebAuthnFactorConfiguration](#cfn-cognito-userpool-webauthnfactorconfiguration)" : {{String}},
      "[WebAuthnRelyingPartyID](#cfn-cognito-userpool-webauthnrelyingpartyid)" : {{String}},
      "[WebAuthnUserVerification](#cfn-cognito-userpool-webauthnuserverification)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpool-syntax.yaml"></a>

```
Type: AWS::Cognito::UserPool
Properties:
  [AccountRecoverySetting](#cfn-cognito-userpool-accountrecoverysetting): {{
    AccountRecoverySetting}}
  [AdminCreateUserConfig](#cfn-cognito-userpool-admincreateuserconfig): {{
    AdminCreateUserConfig}}
  [AliasAttributes](#cfn-cognito-userpool-aliasattributes): {{
    - String}}
  [AutoVerifiedAttributes](#cfn-cognito-userpool-autoverifiedattributes): {{
    - String}}
  [DeletionProtection](#cfn-cognito-userpool-deletionprotection): {{String}}
  [DeviceConfiguration](#cfn-cognito-userpool-deviceconfiguration): {{
    DeviceConfiguration}}
  [EmailAuthenticationMessage](#cfn-cognito-userpool-emailauthenticationmessage): {{String}}
  [EmailAuthenticationSubject](#cfn-cognito-userpool-emailauthenticationsubject): {{String}}
  [EmailConfiguration](#cfn-cognito-userpool-emailconfiguration): {{
    EmailConfiguration}}
  [EmailVerificationMessage](#cfn-cognito-userpool-emailverificationmessage): {{String}}
  [EmailVerificationSubject](#cfn-cognito-userpool-emailverificationsubject): {{String}}
  [EnabledMfas](#cfn-cognito-userpool-enabledmfas): {{
    - String}}
  [IssuerConfiguration](#cfn-cognito-userpool-issuerconfiguration): {{
    IssuerConfiguration}}
  [KeyConfiguration](#cfn-cognito-userpool-keyconfiguration): {{
    KeyConfiguration}}
  [LambdaConfig](#cfn-cognito-userpool-lambdaconfig): {{
    LambdaConfig}}
  [MfaConfiguration](#cfn-cognito-userpool-mfaconfiguration): {{String}}
  [Policies](#cfn-cognito-userpool-policies): {{
    Policies}}
  [Schema](#cfn-cognito-userpool-schema): {{
    - SchemaAttribute}}
  [SmsAuthenticationMessage](#cfn-cognito-userpool-smsauthenticationmessage): {{String}}
  [SmsConfiguration](#cfn-cognito-userpool-smsconfiguration): {{
    SmsConfiguration}}
  [SmsVerificationMessage](#cfn-cognito-userpool-smsverificationmessage): {{String}}
  [UserAttributeUpdateSettings](#cfn-cognito-userpool-userattributeupdatesettings): {{
    UserAttributeUpdateSettings}}
  [UsernameAttributes](#cfn-cognito-userpool-usernameattributes): {{
    - String}}
  [UsernameConfiguration](#cfn-cognito-userpool-usernameconfiguration): {{
    UsernameConfiguration}}
  [UserPoolAddOns](#cfn-cognito-userpool-userpooladdons): {{
    UserPoolAddOns}}
  [UserPoolName](#cfn-cognito-userpool-userpoolname): {{String}}
  [UserPoolTags](#cfn-cognito-userpool-userpooltags): {{
    {{Key}}: {{Value}}}}
  [UserPoolTier](#cfn-cognito-userpool-userpooltier): {{String}}
  [VerificationMessageTemplate](#cfn-cognito-userpool-verificationmessagetemplate): {{
    VerificationMessageTemplate}}
  [WebAuthnFactorConfiguration](#cfn-cognito-userpool-webauthnfactorconfiguration): {{String}}
  [WebAuthnRelyingPartyID](#cfn-cognito-userpool-webauthnrelyingpartyid): {{String}}
  [WebAuthnUserVerification](#cfn-cognito-userpool-webauthnuserverification): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpool-properties"></a>

`AccountRecoverySetting`  <a name="cfn-cognito-userpool-accountrecoverysetting"></a>
The available verified method a user can use to recover their password when they call `ForgotPassword`. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.
*Required*: No
*Type*: [AccountRecoverySetting](aws-properties-cognito-userpool-accountrecoverysetting.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AdminCreateUserConfig`  <a name="cfn-cognito-userpool-admincreateuserconfig"></a>
The settings for administrator creation of users in a user pool. Contains settings for allowing user sign-up, customizing invitation messages to new users, and the amount of time before temporary passwords expire.
*Required*: No
*Type*: [AdminCreateUserConfig](aws-properties-cognito-userpool-admincreateuserconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AliasAttributes`  <a name="cfn-cognito-userpool-aliasattributes"></a>
Attributes supported as an alias for this user pool. For more information about alias attributes, see [Customizing sign-in attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoVerifiedAttributes`  <a name="cfn-cognito-userpool-autoverifiedattributes"></a>
The attributes that you want your user pool to automatically verify. For more information, see [Verifying contact information at sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#allowing-users-to-sign-up-and-confirm-themselves).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-cognito-userpool-deletionprotection"></a>
When active, `DeletionProtection` prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.
When you try to delete a protected user pool in a `DeleteUserPool` API request, Amazon Cognito returns an `InvalidParameterException` error. To delete a protected user pool, send a new `DeleteUserPool` request after you deactivate deletion protection in an `UpdateUserPool` API request.
*Required*: No
*Type*: String
*Allowed values*: `ACTIVE | INACTIVE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceConfiguration`  <a name="cfn-cognito-userpool-deviceconfiguration"></a>
The device-remembering configuration for a user pool. Device remembering or device tracking is a "Remember me on this device" option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see [Working with user devices in your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html). A null value indicates that you have deactivated device remembering in your user pool.
When you provide a value for any `DeviceConfiguration` field, you activate the Amazon Cognito device-remembering feature. For more information, see [Working with devices](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html).
*Required*: No
*Type*: [DeviceConfiguration](aws-properties-cognito-userpool-deviceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAuthenticationMessage`  <a name="cfn-cognito-userpool-emailauthenticationmessage"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAuthenticationSubject`  <a name="cfn-cognito-userpool-emailauthenticationsubject"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailConfiguration`  <a name="cfn-cognito-userpool-emailconfiguration"></a>
The email configuration of your user pool. The email configuration type sets your preferred sending method, AWS Region, and sender for messages from your user pool.
*Required*: No
*Type*: [EmailConfiguration](aws-properties-cognito-userpool-emailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailVerificationMessage`  <a name="cfn-cognito-userpool-emailverificationmessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html).
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `20000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailVerificationSubject`  <a name="cfn-cognito-userpool-emailverificationsubject"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html).
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnabledMfas`  <a name="cfn-cognito-userpool-enabledmfas"></a>
Set enabled MFA options on a specified user pool. To disable all MFAs after it has been enabled, set `MfaConfiguration` to `OFF` and remove EnabledMfas. MFAs can only be all disabled if `MfaConfiguration` is `OFF`. After you enable `SMS_MFA`, you can only disable it by setting `MfaConfiguration` to `OFF`. Can be one of the following values:
+ `SMS_MFA` - Enables MFA with SMS for the user pool. To select this option, you must also provide values for `SmsConfiguration`.
+ `SOFTWARE_TOKEN_MFA` - Enables software token MFA for the user pool.
+ `EMAIL_OTP` - Enables MFA with email for the user pool. To select this option, you must provide values for `EmailConfiguration` and within those, set `EmailSendingAccount` to `DEVELOPER`.
Allowed values: `SMS_MFA` \| `SOFTWARE_TOKEN_MFA` \| `EMAIL_OTP`
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IssuerConfiguration`  <a name="cfn-cognito-userpool-issuerconfiguration"></a>
The issuer configuration for the user pool, including token issuing settings.
*Required*: No
*Type*: [IssuerConfiguration](aws-properties-cognito-userpool-issuerconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyConfiguration`  <a name="cfn-cognito-userpool-keyconfiguration"></a>
The key configuration for the user pool, including encryption settings.
*Required*: No
*Type*: [KeyConfiguration](aws-properties-cognito-userpool-keyconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LambdaConfig`  <a name="cfn-cognito-userpool-lambdaconfig"></a>
A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.
*Required*: No
*Type*: [LambdaConfig](aws-properties-cognito-userpool-lambdaconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MfaConfiguration`  <a name="cfn-cognito-userpool-mfaconfiguration"></a>
Displays the state of multi-factor authentication (MFA) as on, off, or optional. When `ON`, all users must set up MFA before they can sign in. When `OPTIONAL`, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose `OPTIONAL`.
When `MfaConfiguration` is `OPTIONAL`, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.
*Required*: No
*Type*: String
*Allowed values*: `OFF | ON | OPTIONAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Policies`  <a name="cfn-cognito-userpool-policies"></a>
A list of user pool policies. Contains the policy that sets password-complexity requirements.
*Required*: No
*Type*: [Policies](aws-properties-cognito-userpool-policies.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Schema`  <a name="cfn-cognito-userpool-schema"></a>
An array of attributes for the new user pool. You can add custom attributes and modify the properties of default attributes. The specifications in this parameter set the required attributes in your user pool. For more information, see [Working with user attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html).
*Required*: No
*Type*: Array of [SchemaAttribute](aws-properties-cognito-userpool-schemaattribute.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsAuthenticationMessage`  <a name="cfn-cognito-userpool-smsauthenticationmessage"></a>
The contents of the SMS authentication message.
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsConfiguration`  <a name="cfn-cognito-userpool-smsconfiguration"></a>
The settings for your Amazon Cognito user pool to send SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account. For more information see [SMS message settings](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html).
*Required*: No
*Type*: [SmsConfiguration](aws-properties-cognito-userpool-smsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmsVerificationMessage`  <a name="cfn-cognito-userpool-smsverificationmessage"></a>
This parameter is no longer used. See [VerificationMessageTemplateType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-verificationmessagetemplate.html).
*Required*: No
*Type*: String
*Minimum*: `6`
*Maximum*: `140`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserAttributeUpdateSettings`  <a name="cfn-cognito-userpool-userattributeupdatesettings"></a>
The settings for updates to user attributes. These settings include the property `AttributesRequireVerificationBeforeUpdate`, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see [ Verifying updates to email addresses and phone numbers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates).
*Required*: No
*Type*: [UserAttributeUpdateSettings](aws-properties-cognito-userpool-userattributeupdatesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsernameAttributes`  <a name="cfn-cognito-userpool-usernameattributes"></a>
Specifies whether a user can use an email address or phone number as a username when they sign up.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsernameConfiguration`  <a name="cfn-cognito-userpool-usernameconfiguration"></a>
Sets the case sensitivity option for sign-in usernames. When `CaseSensitive` is `false` (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, `username`, `USERNAME`, or `UserName`, or for email, `email@example.com` or `EMaiL@eXamplE.Com`. For most use cases, set case sensitivity to `false` as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.
When `CaseSensitive` is `true` (case sensitive), Amazon Cognito interprets `USERNAME` and `UserName` as distinct users.
This configuration is immutable after you set it.
*Required*: No
*Type*: [UsernameConfiguration](aws-properties-cognito-userpool-usernameconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolAddOns`  <a name="cfn-cognito-userpool-userpooladdons"></a>
Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to `AUDIT`. To configure automatic security responses to potentially unwanted traffic to your user pool, set to `ENFORCED`.
For more information, see [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html). To activate this setting, your user pool must be on the [ Plus tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html).
*Required*: No
*Type*: [UserPoolAddOns](aws-properties-cognito-userpool-userpooladdons.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolName`  <a name="cfn-cognito-userpool-userpoolname"></a>
A friendly name for your user pool.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolTags`  <a name="cfn-cognito-userpool-userpooltags"></a>
The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolTier`  <a name="cfn-cognito-userpool-userpooltier"></a>
The user pool [feature plan](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html), or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to `ESSENTIALS`.
*Required*: No
*Type*: String
*Allowed values*: `LITE | ESSENTIALS | PLUS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerificationMessageTemplate`  <a name="cfn-cognito-userpool-verificationmessagetemplate"></a>
The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.
Set the email message type that corresponds to your `DefaultEmailOption` selection. For `CONFIRM_WITH_LINK`, specify an `EmailMessageByLink` and leave `EmailMessage` blank. For `CONFIRM_WITH_CODE`, specify an `EmailMessage` and leave `EmailMessageByLink` blank. When you supply both parameters with either choice, Amazon Cognito returns an error.
*Required*: No
*Type*: [VerificationMessageTemplate](aws-properties-cognito-userpool-verificationmessagetemplate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAuthnFactorConfiguration`  <a name="cfn-cognito-userpool-webauthnfactorconfiguration"></a>
Sets whether passkeys can be used as multi-factor authentication (MFA). When set to `MULTI_FACTOR_WITH_USER_VERIFICATION`, passkey authentication with user verification satisfies MFA requirements. When set to `SINGLE_FACTOR` or not set, passkeys are a single authentication factor. To activate this setting, your user pool must be in the [ Essentials tier](https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html) or higher.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_FACTOR | MULTI_FACTOR_WITH_USER_VERIFICATION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAuthnRelyingPartyID`  <a name="cfn-cognito-userpool-webauthnrelyingpartyid"></a>
Sets or displays the authentication domain, typically your user pool domain, that passkey providers must use as a relying party (RP) in their configuration.
Under the following conditions, the passkey relying party ID must be the fully-qualified domain name of your custom domain:
+ The user pool is configured for passkey authentication.
+ The user pool has a custom domain, whether or not it also has a prefix domain.
+ Your application performs authentication with managed login or the classic hosted UI.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WebAuthnUserVerification`  <a name="cfn-cognito-userpool-webauthnuserverification"></a>
When `required`, users can only register and sign in users with passkeys that are capable of [user verification](https://www.w3.org/TR/webauthn-2/#enum-userVerificationRequirement). When `preferred`, your user pool doesn't require the use of authenticators with user verification but encourages it.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `9`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cognito-userpool-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpool-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a generated ID, such as `us-east-2_zgaEXAMPLE`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cognito-userpool-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cognito-userpool-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the user pool, such as `arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_123412341`.

`ProviderName`  <a name="ProviderName-fn::getatt"></a>
A friendly name for the IdP.

`ProviderURL`  <a name="ProviderURL-fn::getatt"></a>
The URL of the provider of the Amazon Cognito user pool, specified as a `String`.

`UserPoolId`  <a name="UserPoolId-fn::getatt"></a>
The ID of the user pool.

## Examples
<a name="aws-resource-cognito-userpool--examples"></a>

### Creating a new user pool
<a name="aws-resource-cognito-userpool--examples--Creating_a_new_user_pool"></a>

The following example creates a user pool with values for all possible parameters.

#### JSON
<a name="aws-resource-cognito-userpool--examples--Creating_a_new_user_pool--json"></a>

```
{
    "UserPool": {
        "Properties": {
            "AccountRecoverySetting": {
                "RecoveryMechanisms": [
                    {
                        "Name": "verified_email",
                        "Priority": 1
                    },
                    {
                        "Name": "verified_phone_number",
                        "Priority": 2
                    }
                ]
            },
            "AdminCreateUserConfig": {
                "AllowAdminCreateUserOnly": false,
                "InviteMessageTemplate": {
                    "EmailMessage": "Your username is {username} and your temporary password is {####}",
                    "EmailSubject": "Welcome to MyApp",
                    "SMSMessage": "Your username for MyApp is {username} and your temporary password is {####}."
                }
            },
            "AliasAttributes": [
                "email",
                "phone_number",
                "preferred_username"
            ],
            "AutoVerifiedAttributes": [
                "email",
                "phone_number"
            ],
            "DeletionProtection": "ACTIVE",
            "DeviceConfiguration": {
                "ChallengeRequiredOnNewDevice": true,
                "DeviceOnlyRememberedOnUserPrompt": true
            },
            "EmailAuthenticationMessage": "This is your sign-in code: \"{####}\"",
            "EmailAuthenticationSubject": "Your sign-in code",
            "EmailConfiguration": {
                "ConfigurationSet": "my-test-configuration-set",
                "EmailSendingAccount": "DEVELOPER",
                "From": "admin@example.com",
                "ReplyToEmailAddress": "no-reply@example.com",
                "SourceArn": "arn:aws:ses:us-west-2:123456789012:identity/admin@example.com"
            },
            "EmailVerificationMessage": "This is your verification code: \"{####}\"",
            "EmailVerificationSubject": "Your verification code",
            "EnabledMfas": [
                "EMAIL_OTP",
                "SMS_MFA",
                "SOFTWARE_TOKEN_MFA"
            ],
            "LambdaConfig": {
                "CreateAuthChallenge": "arn:aws:lambda:us-west-2:123456789012:function:my-CreateAuthChallenge-function",
                "CustomEmailSender": {
                    "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:my-CustomEmailSender-function",
                    "LambdaVersion": "V1_0"
                },
                "CustomMessage": "arn:aws:lambda:us-west-2:123456789012:function:my-CustomMessage-function",
                "CustomSMSSender": {
                    "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:my-CustomSMSSender-function",
                    "LambdaVersion": "V1_0"
                },
                "DefineAuthChallenge": "arn:aws:lambda:us-west-2:123456789012:function:my-DefineAuthChallenge-function",
                "KMSKeyID": "arn:aws:kms:us-west-2:123456789012:key/4d43904c-8edf-4bb4-9fca-fb1a80e41cbe",
                "PostAuthentication": "arn:aws:lambda:us-west-2:123456789012:function:my-PostAuthentication-function",
                "PostConfirmation": "arn:aws:lambda:us-west-2:123456789012:function:my-PostConfirmation-function",
                "PreAuthentication": "arn:aws:lambda:us-west-2:123456789012:function:my-PreAuthentication-function",
                "PreSignUp": "arn:aws:lambda:us-west-2:123456789012:function:my-PreSignUp-function",
                "PreTokenGenerationConfig": {
                    "LambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:my-PreTokenGenerationConfig-function",
                    "LambdaVersion": "V2_0"
                },
                "UserMigration": "arn:aws:lambda:us-west-2:123456789012:function:my-UserMigration-function",
                "VerifyAuthChallengeResponse": "arn:aws:lambda:us-west-2:123456789012:function:my-VerifyAuthChallengeResponse-function"
            },
            "MfaConfiguration": "OPTIONAL",
            "Policies": {
                "PasswordPolicy": {
                    "MinimumLength": 12,
                    "PasswordHistorySize": 22,
                    "RequireLowercase": true,
                    "RequireNumbers": true,
                    "RequireSymbols": true,
                    "RequireUppercase": true,
                    "TemporaryPasswordValidityDays": 7
                },
                "SignInPolicy": {
                    "AllowedFirstAuthFactors": [
                        "EMAIL_OTP",
                        "SMS_OTP",
                        "WEB_AUTHN",
                        "PASSWORD"
                    ]
                }
            },
            "Schema": [
                {
                    "AttributeDataType": "String",
                    "DeveloperOnlyAttribute": false,
                    "Mutable": true,
                    "Name": "ResidenceType",
                    "Required": false,
                    "StringAttributeConstraints": {
                        "MaxLength": "999",
                        "MinLength": "1"
                    }
                },
                {
                    "AttributeDataType": "Number",
                    "DeveloperOnlyAttribute": true,
                    "Mutable": true,
                    "Name": "NumberOfResidents",
                    "NumberAttributeConstraints": {
                        "MaxValue": "9999999",
                        "MinValue": "1"
                    },
                    "Required": false
                },
                {
                    "AttributeDataType": "String",
                    "DeveloperOnlyAttribute": false,
                    "Mutable": true,
                    "Name": "email",
                    "Required": true,
                    "StringAttributeConstraints": {
                        "MaxLength": "99",
                        "MinLength": "1"
                    }
                }
            ],
            "SmsAuthenticationMessage": "This is your sign-in code: \"{####}\"",
            "SmsConfiguration": {
                "ExternalId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
                "SnsCallerArn": "arn:aws:iam::123456789012:role/service-role/my-test-SMS-Role",
                "SnsRegion": "us-west-2"
            },
            "SmsVerificationMessage": "This is your verification code: \"{####}\"",
            "UserAttributeUpdateSettings": {
                "AttributesRequireVerificationBeforeUpdate": [
                    "email",
                    "phone_number"
                ]
            },
            "UsernameConfiguration": {
                "CaseSensitive": true
            },
            "UserPoolAddOns": {
                "AdvancedSecurityAdditionalFlows": {
                    "CustomAuthMode": "AUDIT"
                },
                "AdvancedSecurityMode": "AUDIT"
            },
            "UserPoolName": "Example_CloudFormation_UserPool",
            "UserPoolTags": {
                "administrator": "Jie",
                "tenant": "ExampleCorp"
            },
            "UserPoolTier": "PLUS",
            "VerificationMessageTemplate": {
                "DefaultEmailOption": "CONFIRM_WITH_CODE",
                "EmailMessage": "This is your verification code: \"{####}\"",
                "EmailMessageByLink": "Choose this link to {##verify your email##}",
                "EmailSubject": "Your confirmation code",
                "EmailSubjectByLink": "Your confirmation link",
                "SmsMessage": "This is your verification code: \"{####}\""
            },
            "WebAuthnRelyingPartyID": "auth.example.com",
            "WebAuthnUserVerification": "preferred"
        },
        "Type": "AWS::Cognito::UserPool"
    }
}
```

#### YAML
<a name="aws-resource-cognito-userpool--examples--Creating_a_new_user_pool--yaml"></a>

```
ExampleUserPool:
    Type: AWS::Cognito::UserPool
    Properties:
      AccountRecoverySetting:
        RecoveryMechanisms:
          - Name: verified_email
            Priority: 1
          - Name: verified_phone_number
            Priority: 2
      AdminCreateUserConfig:
        AllowAdminCreateUserOnly: false
        InviteMessageTemplate:
          EmailMessage: Your username is {username} and your temporary password is {####}
          EmailSubject: Welcome to MyApp
          SMSMessage: Your username for MyApp is {username} and your temporary password is {####}.
      AliasAttributes:
        - email
        - phone_number
        - preferred_username
      AutoVerifiedAttributes:
        - email
        - phone_number
      DeletionProtection: ACTIVE
      DeviceConfiguration:
        ChallengeRequiredOnNewDevice: true
        DeviceOnlyRememberedOnUserPrompt: true
      EmailAuthenticationMessage: 'This is your sign-in code: "{####}"'
      EmailAuthenticationSubject: Your sign-in code
      EmailConfiguration:
        ConfigurationSet: my-test-configuration-set
        EmailSendingAccount: DEVELOPER
        From: admin@example.com
        ReplyToEmailAddress: no-reply@example.com
        SourceArn: arn:aws:ses:us-west-2:123456789012:identity/admin@example.com
      EmailVerificationMessage: 'This is your verification code: "{####}"'
      EmailVerificationSubject: Your verification code
      EnabledMfas:
        - EMAIL_OTP
        - SMS_MFA
        - SOFTWARE_TOKEN_MFA
      LambdaConfig:
        CreateAuthChallenge: arn:aws:lambda:us-west-2:123456789012:function:my-CreateAuthChallenge-function
        CustomEmailSender:
          LambdaArn: arn:aws:lambda:us-west-2:123456789012:function:my-CustomEmailSender-function
          LambdaVersion: V1_0
        CustomMessage: arn:aws:lambda:us-west-2:123456789012:function:my-CustomMessage-function
        CustomSMSSender:
          LambdaArn: arn:aws:lambda:us-west-2:123456789012:function:my-CustomSMSSender-function
          LambdaVersion: V1_0
        DefineAuthChallenge: arn:aws:lambda:us-west-2:123456789012:function:my-DefineAuthChallenge-function
        KMSKeyID: arn:aws:kms:us-west-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222
        PostAuthentication: arn:aws:lambda:us-west-2:123456789012:function:my-PostAuthentication-function
        PostConfirmation: arn:aws:lambda:us-west-2:123456789012:function:my-PostConfirmation-function
        PreAuthentication: arn:aws:lambda:us-west-2:123456789012:function:my-PreAuthentication-function
        PreSignUp: arn:aws:lambda:us-west-2:123456789012:function:my-PreSignUp-function
        PreTokenGenerationConfig:
          LambdaArn: arn:aws:lambda:us-west-2:123456789012:function:my-PreTokenGeneration-function
          LambdaVersion: V2_0
        UserMigration: arn:aws:lambda:us-west-2:123456789012:function:my-UserMigration-function
        VerifyAuthChallengeResponse: arn:aws:lambda:us-west-2:123456789012:function:my-VerifyAuthChallengeResponse-function
      MfaConfiguration: OPTIONAL
      Policies:
        PasswordPolicy:
          MinimumLength: 12
          PasswordHistorySize: 22
          RequireLowercase: true
          RequireNumbers: true
          RequireSymbols: true
          RequireUppercase: true
          TemporaryPasswordValidityDays: 7
        SignInPolicy:
          AllowedFirstAuthFactors:
            - EMAIL_OTP
            - SMS_OTP
            - WEB_AUTHN
            - PASSWORD
      Schema:
        - AttributeDataType: String
          DeveloperOnlyAttribute: false
          Mutable: true
          Name: ResidenceType
          Required: false
          StringAttributeConstraints:
            MaxLength: "999"
            MinLength: "1"
        - AttributeDataType: Number
          DeveloperOnlyAttribute: true
          Mutable: true
          Name: NumberOfResidents
          NumberAttributeConstraints:
            MaxValue: "9999999"
            MinValue: "1"
          Required: false
        - AttributeDataType: String
          DeveloperOnlyAttribute: false
          Mutable: true
          Name: email
          Required: true
          StringAttributeConstraints:
            MaxLength: "99"
            MinLength: "1"
      SmsAuthenticationMessage: 'This is your sign-in code: "{####}"'
      SmsConfiguration:
        ExternalId: a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
        SnsCallerArn: arn:aws:iam::123456789012:role/service-role/my-test-SMS-Role
        SnsRegion: us-west-2
      SmsVerificationMessage: 'This is your verification code: "{####}"'
      UserAttributeUpdateSettings:
        AttributesRequireVerificationBeforeUpdate:
          - email
          - phone_number
      UsernameConfiguration:
        CaseSensitive: true
      UserPoolAddOns:
        AdvancedSecurityAdditionalFlows:
          CustomAuthMode: AUDIT
        AdvancedSecurityMode: AUDIT
      UserPoolName: Example_CloudFormation_UserPool
      UserPoolTags:
        administrator: Jie
        tenant: ExampleCorp
      UserPoolTier: PLUS
      VerificationMessageTemplate:
        DefaultEmailOption: CONFIRM_WITH_CODE
        EmailMessage: 'This is your verification code: "{####}"'
        EmailMessageByLink: Choose this link to {##verify your email##}
        EmailSubject: Your confirmation code
        EmailSubjectByLink: Your confirmation link
        SmsMessage: 'This is your verification code: "{####}"'
      WebAuthnRelyingPartyID: auth.example.com
      WebAuthnUserVerification: preferred
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
