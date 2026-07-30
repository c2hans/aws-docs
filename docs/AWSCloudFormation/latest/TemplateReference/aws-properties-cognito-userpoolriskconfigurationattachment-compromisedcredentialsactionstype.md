---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolRiskConfigurationAttachment CompromisedCredentialsActionsType
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype"></a>

Settings for user pool actions when Amazon Cognito detects compromised credentials with advanced security features in full-function `ENFORCED` mode.

## Syntax
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-syntax.json"></a>

```
{
  "[EventAction](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-eventaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-syntax.yaml"></a>

```
  [EventAction](#cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-eventaction): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-properties"></a>

`EventAction`  <a name="cfn-cognito-userpoolriskconfigurationattachment-compromisedcredentialsactionstype-eventaction"></a>
The action that Amazon Cognito takes when it detects compromised credentials.
*Required*: Yes
*Type*: String
*Allowed values*: `BLOCK | NO_ACTION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
