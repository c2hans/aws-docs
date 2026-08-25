---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpool-lambdaconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPool LambdaConfig
<a name="aws-properties-cognito-userpool-lambdaconfig"></a>

A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.

## Syntax
<a name="aws-properties-cognito-userpool-lambdaconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpool-lambdaconfig-syntax.json"></a>

```
{
  "[CreateAuthChallenge](#cfn-cognito-userpool-lambdaconfig-createauthchallenge)" : {{String}},
  "[CustomEmailSender](#cfn-cognito-userpool-lambdaconfig-customemailsender)" : {{CustomEmailSender}},
  "[CustomMessage](#cfn-cognito-userpool-lambdaconfig-custommessage)" : {{String}},
  "[CustomSMSSender](#cfn-cognito-userpool-lambdaconfig-customsmssender)" : {{CustomSMSSender}},
  "[DefineAuthChallenge](#cfn-cognito-userpool-lambdaconfig-defineauthchallenge)" : {{String}},
  "[InboundFederation](#cfn-cognito-userpool-lambdaconfig-inboundfederation)" : {{InboundFederation}},
  "[KMSKeyID](#cfn-cognito-userpool-lambdaconfig-kmskeyid)" : {{String}},
  "[PostAuthentication](#cfn-cognito-userpool-lambdaconfig-postauthentication)" : {{String}},
  "[PostConfirmation](#cfn-cognito-userpool-lambdaconfig-postconfirmation)" : {{String}},
  "[PreAuthentication](#cfn-cognito-userpool-lambdaconfig-preauthentication)" : {{String}},
  "[PreSignUp](#cfn-cognito-userpool-lambdaconfig-presignup)" : {{String}},
  "[PreTokenGeneration](#cfn-cognito-userpool-lambdaconfig-pretokengeneration)" : {{String}},
  "[PreTokenGenerationConfig](#cfn-cognito-userpool-lambdaconfig-pretokengenerationconfig)" : {{PreTokenGenerationConfig}},
  "[UserMigration](#cfn-cognito-userpool-lambdaconfig-usermigration)" : {{String}},
  "[VerifyAuthChallengeResponse](#cfn-cognito-userpool-lambdaconfig-verifyauthchallengeresponse)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpool-lambdaconfig-syntax.yaml"></a>

```
  [CreateAuthChallenge](#cfn-cognito-userpool-lambdaconfig-createauthchallenge): {{String}}
  [CustomEmailSender](#cfn-cognito-userpool-lambdaconfig-customemailsender): {{
    CustomEmailSender}}
  [CustomMessage](#cfn-cognito-userpool-lambdaconfig-custommessage): {{String}}
  [CustomSMSSender](#cfn-cognito-userpool-lambdaconfig-customsmssender): {{
    CustomSMSSender}}
  [DefineAuthChallenge](#cfn-cognito-userpool-lambdaconfig-defineauthchallenge): {{String}}
  [InboundFederation](#cfn-cognito-userpool-lambdaconfig-inboundfederation): {{
    InboundFederation}}
  [KMSKeyID](#cfn-cognito-userpool-lambdaconfig-kmskeyid): {{String}}
  [PostAuthentication](#cfn-cognito-userpool-lambdaconfig-postauthentication): {{String}}
  [PostConfirmation](#cfn-cognito-userpool-lambdaconfig-postconfirmation): {{String}}
  [PreAuthentication](#cfn-cognito-userpool-lambdaconfig-preauthentication): {{String}}
  [PreSignUp](#cfn-cognito-userpool-lambdaconfig-presignup): {{String}}
  [PreTokenGeneration](#cfn-cognito-userpool-lambdaconfig-pretokengeneration): {{String}}
  [PreTokenGenerationConfig](#cfn-cognito-userpool-lambdaconfig-pretokengenerationconfig): {{
    PreTokenGenerationConfig}}
  [UserMigration](#cfn-cognito-userpool-lambdaconfig-usermigration): {{String}}
  [VerifyAuthChallengeResponse](#cfn-cognito-userpool-lambdaconfig-verifyauthchallengeresponse): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpool-lambdaconfig-properties"></a>

`CreateAuthChallenge`  <a name="cfn-cognito-userpool-lambdaconfig-createauthchallenge"></a>
The configuration of a create auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomEmailSender`  <a name="cfn-cognito-userpool-lambdaconfig-customemailsender"></a>
The configuration of a custom email sender Lambda trigger. This trigger routes all email notifications from a user pool to a Lambda function that delivers the message using custom logic.
*Required*: No
*Type*: [CustomEmailSender](aws-properties-cognito-userpool-customemailsender.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomMessage`  <a name="cfn-cognito-userpool-lambdaconfig-custommessage"></a>
A custom message Lambda trigger. This trigger is an opportunity to customize all SMS and email messages from your user pool. When a custom message trigger is active, your user pool routes all messages to a Lambda function that returns a runtime-customized message subject and body for your user pool to deliver to a user.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSMSSender`  <a name="cfn-cognito-userpool-lambdaconfig-customsmssender"></a>
The configuration of a custom SMS sender Lambda trigger. This trigger routes all SMS notifications from a user pool to a Lambda function that delivers the message using custom logic.
*Required*: No
*Type*: [CustomSMSSender](aws-properties-cognito-userpool-customsmssender.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefineAuthChallenge`  <a name="cfn-cognito-userpool-lambdaconfig-defineauthchallenge"></a>
The configuration of a define auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundFederation`  <a name="cfn-cognito-userpool-lambdaconfig-inboundfederation"></a>
Property description not available.
*Required*: No
*Type*: [InboundFederation](aws-properties-cognito-userpool-inboundfederation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSKeyID`  <a name="cfn-cognito-userpool-lambdaconfig-kmskeyid"></a>
The ARN of an [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). Amazon Cognito uses the key to encrypt codes and temporary passwords sent to custom sender Lambda triggers.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostAuthentication`  <a name="cfn-cognito-userpool-lambdaconfig-postauthentication"></a>
The configuration of a [post authentication Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html) in a user pool. This trigger can take custom actions after a user signs in.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostConfirmation`  <a name="cfn-cognito-userpool-lambdaconfig-postconfirmation"></a>
The configuration of a [post confirmation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html) in a user pool. This trigger can take custom actions after a user confirms their user account and their email address or phone number.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreAuthentication`  <a name="cfn-cognito-userpool-lambdaconfig-preauthentication"></a>
The configuration of a [pre authentication trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html) in a user pool. This trigger can evaluate and modify user sign-in events.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreSignUp`  <a name="cfn-cognito-userpool-lambdaconfig-presignup"></a>
The configuration of a [pre sign-up Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) in a user pool. This trigger evaluates new users and can bypass confirmation, [link a federated user profile](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html), or block sign-up requests.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreTokenGeneration`  <a name="cfn-cognito-userpool-lambdaconfig-pretokengeneration"></a>
The legacy configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool.
Set this parameter for legacy purposes. If you also set an ARN in `PreTokenGenerationConfig`, its value must be identical to `PreTokenGeneration`. For new instances of pre token generation triggers, set the `LambdaArn` of `PreTokenGenerationConfig`.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreTokenGenerationConfig`  <a name="cfn-cognito-userpool-lambdaconfig-pretokengenerationconfig"></a>
The detailed configuration of a [pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in a user pool. If you also set an ARN in `PreTokenGeneration`, its value must be identical to `PreTokenGenerationConfig`.
*Required*: No
*Type*: [PreTokenGenerationConfig](aws-properties-cognito-userpool-pretokengenerationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserMigration`  <a name="cfn-cognito-userpool-lambdaconfig-usermigration"></a>
The configuration of a [migrate user Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) in a user pool. This trigger can create user profiles when users sign in or attempt to reset their password with credentials that don't exist yet.
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerifyAuthChallengeResponse`  <a name="cfn-cognito-userpool-lambdaconfig-verifyauthchallengeresponse"></a>
The configuration of a verify auth challenge Lambda trigger, one of three triggers in the sequence of the [custom authentication challenge triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html).
*Required*: No
*Type*: String
*Pattern*: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
