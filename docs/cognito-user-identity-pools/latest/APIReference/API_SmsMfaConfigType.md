---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SmsMfaConfigType.html
---

# SmsMfaConfigType
<a name="API_SmsMfaConfigType"></a>

The configuration of multi-factor authentication (MFA) with SMS messages in a user pool.

This data type is a request parameter of [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) and a response parameter of [GetUserPoolMfaConfig](API_GetUserPoolMfaConfig.md).

## Contents
<a name="API_SmsMfaConfigType_Contents"></a>

 ** SmsAuthenticationMessage **   <a name="CognitoUserPools-Type-SmsMfaConfigType-SmsAuthenticationMessage"></a>
The SMS authentication message that will be sent to users with the code they must sign in with. The message must contain the `{####}` placeholder. Your user pool replaces the placeholder with the MFA code. If this parameter isn't provided, your user pool sends a default message.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 140.
Pattern: `.*\{####\}.*`
Required: No

 ** SmsConfiguration **   <a name="CognitoUserPools-Type-SmsMfaConfigType-SmsConfiguration"></a>
User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the AWS Region that you want, the Amazon Cognito user pool uses an AWS Identity and Access Management (IAM) role in your AWS account.
You can set `SmsConfiguration` in `CreateUserPool` and ` UpdateUserPool`, or in `SetUserPoolMfaConfig`.
Type: [SmsConfigurationType](API_SmsConfigurationType.md) object
Required: No

## See Also
<a name="API_SmsMfaConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SmsMfaConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SmsMfaConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SmsMfaConfigType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
