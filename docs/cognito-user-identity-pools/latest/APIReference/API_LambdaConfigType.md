---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_LambdaConfigType.html
---

# LambdaConfigType
<a name="API_LambdaConfigType"></a>

A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.

This data type is a request and response parameter of [CreateUserPool](API_CreateUserPool.md) and [UpdateUserPool](API_UpdateUserPool.md), and a response parameter of [DescribeUserPool](API_DescribeUserPool.md).

## Contents
<a name="API_LambdaConfigType_Contents"></a>

 ** CreateAuthChallenge **   <a name="CognitoUserPools-Type-LambdaConfigType-CreateAuthChallenge"></a>
The configuration of a create auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** CustomEmailSender **   <a name="CognitoUserPools-Type-LambdaConfigType-CustomEmailSender"></a>
The configuration of a custom email sender Lambda trigger. This trigger routes all email notifications from a user pool to a Lambda function that delivers the message using custom logic.
Type: [CustomEmailLambdaVersionConfigType](API_CustomEmailLambdaVersionConfigType.md) object
Required: No

 ** CustomMessage **   <a name="CognitoUserPools-Type-LambdaConfigType-CustomMessage"></a>
A custom message Lambda trigger. This trigger is an opportunity to customize all SMS and email messages from your user pool. When a custom message trigger is active, your user pool routes all messages to a Lambda function that returns a runtime-customized message subject and body for your user pool to deliver to a user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** CustomSMSSender **   <a name="CognitoUserPools-Type-LambdaConfigType-CustomSMSSender"></a>
The configuration of a custom SMS sender Lambda trigger. This trigger routes all SMS notifications from a user pool to a Lambda function that delivers the message using custom logic.
Type: [CustomSMSLambdaVersionConfigType](API_CustomSMSLambdaVersionConfigType.md) object
Required: No

 ** DefineAuthChallenge **   <a name="CognitoUserPools-Type-LambdaConfigType-DefineAuthChallenge"></a>
The configuration of a define auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** InboundFederation **   <a name="CognitoUserPools-Type-LambdaConfigType-InboundFederation"></a>
The configuration of an inbound federation Lambda trigger. This trigger can transform federated user attributes during the authentication with external identity providers.
Type: [InboundFederationLambdaType](API_InboundFederationLambdaType.md) object
Required: No

 ** KMSKeyID **   <a name="CognitoUserPools-Type-LambdaConfigType-KMSKeyID"></a>
The ARN of an [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). Amazon Cognito uses the key to encrypt codes and temporary passwords sent to custom sender Lambda triggers.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PostAuthentication **   <a name="CognitoUserPools-Type-LambdaConfigType-PostAuthentication"></a>
The configuration of a [post authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html) in a user pool. This trigger can take custom actions after a user signs in.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PostConfirmation **   <a name="CognitoUserPools-Type-LambdaConfigType-PostConfirmation"></a>
The configuration of a [post confirmation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html) in a user pool. This trigger can take custom actions after a user confirms their user account and their email address or phone number.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PreAuthentication **   <a name="CognitoUserPools-Type-LambdaConfigType-PreAuthentication"></a>
The configuration of a [pre authentication trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html) in a user pool. This trigger can evaluate and modify user sign-in events.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PreSignUp **   <a name="CognitoUserPools-Type-LambdaConfigType-PreSignUp"></a>
The configuration of a [pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) in a user pool. This trigger evaluates new users and can bypass confirmation, [link a federated user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html), or block sign-up requests.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PreTokenGeneration **   <a name="CognitoUserPools-Type-LambdaConfigType-PreTokenGeneration"></a>
The legacy configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool.
Set this parameter for legacy purposes. If you also set an ARN in `PreTokenGenerationConfig`, its value must be identical to `PreTokenGeneration`. For new instances of pre token generation triggers, set the `LambdaArn` of `PreTokenGenerationConfig`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** PreTokenGenerationConfig **   <a name="CognitoUserPools-Type-LambdaConfigType-PreTokenGenerationConfig"></a>
The detailed configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool. If you also set an ARN in `PreTokenGeneration`, its value must be identical to `PreTokenGenerationConfig`.
Type: [PreTokenGenerationVersionConfigType](API_PreTokenGenerationVersionConfigType.md) object
Required: No

 ** UserMigration **   <a name="CognitoUserPools-Type-LambdaConfigType-UserMigration"></a>
The configuration of a [migrate user Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) in a user pool. This trigger can create user profiles when users sign in or attempt to reset their password with credentials that don't exist yet.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** VerifyAuthChallengeResponse **   <a name="CognitoUserPools-Type-LambdaConfigType-VerifyAuthChallengeResponse"></a>
The configuration of a verify auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

## See Also
<a name="API_LambdaConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/LambdaConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/LambdaConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/LambdaConfigType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
