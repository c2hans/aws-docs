---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EumsSmsConfigurationType.html
---

# EumsSmsConfigurationType
<a name="API_EumsSmsConfigurationType"></a>

The configuration that Amazon Cognito uses to send SMS messages through AWS End User Messaging SMS. Provide this structure in the `EumsSms` member of `SmsConfigurationType` to use AWS End User Messaging SMS instead of Amazon SNS.

## Contents
<a name="API_EumsSmsConfigurationType_Contents"></a>

 ** CallerArn **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-CallerArn"></a>
The ARN of the IAM role that Amazon Cognito assumes to send SMS messages through AWS End User Messaging SMS. The role must grant permission to call the `sms-voice:SendTextMessage` operation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: Yes

 ** ConfigurationSetName **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-ConfigurationSetName"></a>
The name of the AWS End User Messaging SMS configuration set that Amazon Cognito applies to messages, for logging and event destinations. If you omit this member, Amazon Cognito sends messages without applying a configuration set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** ExternalId **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-ExternalId"></a>
The external ID that Amazon Cognito includes when it assumes the `CallerArn` role. Use this value as a condition in the role trust policy to prevent the confused deputy problem.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** InEntityId **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-InEntityId"></a>
The principal entity ID required by India's Distributed Ledger Technology (DLT) regulations for SMS messages.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** InTemplateId **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-InTemplateId"></a>
The registered template ID for the message template required by India's DLT regulations for SMS messages.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** OriginationIdentity **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-OriginationIdentity"></a>
The origination identity that AWS End User Messaging SMS uses to send messages to your users. This value can be one of the following:
+ A phone number – A long code, toll-free number, or short code that is assigned to your account.
+ A sender ID – An alphabetic name that identifies the message sender in supported countries.
+ A phone pool – A group of phone numbers that AWS End User Messaging SMS selects from when it sends messages.
You can provide an E.164 phone number or the ARN of the phone number, sender ID, or phone pool. AWS End User Messaging SMS evaluates IAM authorization with the value that you provide. If the permissions policy of your `CallerArn` role scopes the `sms-voice:SendTextMessage` resource to a specific ARN, provide that same ARN. If the formats do not match, requests fail with an `InvalidSmsRoleAccessPolicyException`.
Depending on the destination country, you must provide an origination identity. For country-specific requirements, see [Supported countries and regions for SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) in the AWS End User Messaging SMS User Guide.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** Region **   <a name="CognitoUserPools-Type-EumsSmsConfigurationType-Region"></a>
The AWS Region of the AWS End User Messaging SMS resources that Amazon Cognito uses to send messages. AWS End User Messaging SMS must be available in your user pool's Region.
If you omit this parameter, Amazon Cognito uses the same Region as your user pool. You can also set this parameter to your user pool's Region explicitly. Amazon Cognito rejects any other value with an `InvalidParameterException`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: No

## See Also
<a name="API_EumsSmsConfigurationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/EumsSmsConfigurationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/EumsSmsConfigurationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/EumsSmsConfigurationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
