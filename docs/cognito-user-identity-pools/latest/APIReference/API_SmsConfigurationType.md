---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.html
---

# SmsConfigurationType
<a name="API_SmsConfigurationType"></a>

User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account.

This data type is a request parameter of [CreateUserPool](API_CreateUserPool.md), [UpdateUserPool](API_UpdateUserPool.md), and [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md), and a response parameter of [CreateUserPool](API_CreateUserPool.md), [UpdateUserPool](API_UpdateUserPool.md), and [GetUserPoolMfaConfig](API_GetUserPoolMfaConfig.md).

## Contents
<a name="API_SmsConfigurationType_Contents"></a>

 ** EumsSms **   <a name="CognitoUserPools-Type-SmsConfigurationType-EumsSms"></a>
The configuration for sending SMS messages through AWS End User Messaging SMS, as an alternative to Amazon SNS. In a user pool, provide either the Amazon SNS configuration (`SnsCallerArn`) or this configuration, but not both. In AWS Regions where Amazon SNS is not available, this configuration is required.
Type: [EumsSmsConfigurationType](API_EumsSmsConfigurationType.md) object
Required: No

 ** ExternalId **   <a name="CognitoUserPools-Type-SmsConfigurationType-ExternalId"></a>
The external ID provides additional security for your IAM role. You can use an `ExternalId` with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an `ExternalId`, your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the `ExternalID`. If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the `ExternalId`.
For more information about the `ExternalId` of a role, see [How to use an external ID when granting access to your AWS resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** SnsCallerArn **   <a name="CognitoUserPools-Type-SmsConfigurationType-SnsCallerArn"></a>
The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your AWS account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a [spending limit](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?)?`
Required: No

 ** SnsRegion **   <a name="CognitoUserPools-Type-SmsConfigurationType-SnsRegion"></a>
The AWS Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported **Legacy Amazon SNS alternate Region**.
 Amazon Cognito resources in the Asia Pacific (Seoul) AWS Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see [SMS message settings for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: No

## See Also
<a name="API_SmsConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SmsConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SmsConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SmsConfigurationType)
