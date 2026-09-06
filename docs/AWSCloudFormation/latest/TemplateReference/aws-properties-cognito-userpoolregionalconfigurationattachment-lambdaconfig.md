---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRegionalConfigurationAttachment LambdaConfig
<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig"></a>

<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig-description"></a>The `LambdaConfig` property type specifies Property description not available. for an [AWS::Cognito::UserPoolRegionalConfigurationAttachment](aws-resource-cognito-userpoolregionalconfigurationattachment.md).

## Syntax
<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig-syntax.json"></a>

```
{
  "[CreateAuthChallenge](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-createauthchallenge)" : {{String}},
  "[CustomEmailSender](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customemailsender)" : {{CustomEmailSender}},
  "[CustomMessage](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-custommessage)" : {{String}},
  "[CustomSMSSender](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customsmssender)" : {{CustomSMSSender}},
  "[DefineAuthChallenge](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-defineauthchallenge)" : {{String}},
  "[InboundFederation](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-inboundfederation)" : {{InboundFederation}},
  "[KMSKeyID](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-kmskeyid)" : {{String}},
  "[PostAuthentication](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postauthentication)" : {{String}},
  "[PostConfirmation](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postconfirmation)" : {{String}},
  "[PreAuthentication](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-preauthentication)" : {{String}},
  "[PreSignUp](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-presignup)" : {{String}},
  "[PreTokenGeneration](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengeneration)" : {{String}},
  "[PreTokenGenerationConfig](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengenerationconfig)" : {{PreTokenGenerationConfig}},
  "[UserMigration](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-usermigration)" : {{String}},
  "[VerifyAuthChallengeResponse](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-verifyauthchallengeresponse)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig-syntax.yaml"></a>

```
  [CreateAuthChallenge](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-createauthchallenge): {{String}}
  [CustomEmailSender](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customemailsender): {{
    CustomEmailSender}}
  [CustomMessage](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-custommessage): {{String}}
  [CustomSMSSender](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customsmssender): {{
    CustomSMSSender}}
  [DefineAuthChallenge](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-defineauthchallenge): {{String}}
  [InboundFederation](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-inboundfederation): {{
    InboundFederation}}
  [KMSKeyID](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-kmskeyid): {{String}}
  [PostAuthentication](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postauthentication): {{String}}
  [PostConfirmation](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postconfirmation): {{String}}
  [PreAuthentication](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-preauthentication): {{String}}
  [PreSignUp](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-presignup): {{String}}
  [PreTokenGeneration](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengeneration): {{String}}
  [PreTokenGenerationConfig](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengenerationconfig): {{
    PreTokenGenerationConfig}}
  [UserMigration](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-usermigration): {{String}}
  [VerifyAuthChallengeResponse](#cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-verifyauthchallengeresponse): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpoolregionalconfigurationattachment-lambdaconfig-properties"></a>

`CreateAuthChallenge`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-createauthchallenge"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomEmailSender`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customemailsender"></a>
Property description not available.
*Required*: No
*Type*: [CustomEmailSender](aws-properties-cognito-userpoolregionalconfigurationattachment-customemailsender.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomMessage`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-custommessage"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSMSSender`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-customsmssender"></a>
Property description not available.
*Required*: No
*Type*: [CustomSMSSender](aws-properties-cognito-userpoolregionalconfigurationattachment-customsmssender.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefineAuthChallenge`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-defineauthchallenge"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InboundFederation`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-inboundfederation"></a>
Property description not available.
*Required*: No
*Type*: [InboundFederation](aws-properties-cognito-userpoolregionalconfigurationattachment-inboundfederation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KMSKeyID`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-kmskeyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostAuthentication`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postauthentication"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostConfirmation`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-postconfirmation"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreAuthentication`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-preauthentication"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreSignUp`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-presignup"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreTokenGeneration`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengeneration"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreTokenGenerationConfig`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-pretokengenerationconfig"></a>
Property description not available.
*Required*: No
*Type*: [PreTokenGenerationConfig](aws-properties-cognito-userpoolregionalconfigurationattachment-pretokengenerationconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserMigration`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-usermigration"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VerifyAuthChallengeResponse`  <a name="cfn-cognito-userpoolregionalconfigurationattachment-lambdaconfig-verifyauthchallengeresponse"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
