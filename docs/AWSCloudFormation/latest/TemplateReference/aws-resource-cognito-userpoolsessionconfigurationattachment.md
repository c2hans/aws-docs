---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cognito-userpoolsessionconfigurationattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolSessionConfigurationAttachment

<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-description"></a>The `AWS::Cognito::UserPoolSessionConfigurationAttachment` resource Property description not available. for Cognito.

## Syntax
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-syntax.json"></a>

```json
{
  "Type" : "AWS::Cognito::UserPoolSessionConfigurationAttachment",
  "Properties" : {
      "[TokenSession](#cfn-cognito-userpoolsessionconfigurationattachment-tokensession)" : {{TokenSession}},
      "[UserPoolId](#cfn-cognito-userpoolsessionconfigurationattachment-userpoolid)" : {{String}},
      "[UserSessionTracking](#cfn-cognito-userpoolsessionconfigurationattachment-usersessiontracking)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-syntax.yaml"></a>

```yaml
Type: AWS::Cognito::UserPoolSessionConfigurationAttachment
Properties:
  [TokenSession](#cfn-cognito-userpoolsessionconfigurationattachment-tokensession): {{
    TokenSession}}
  [UserPoolId](#cfn-cognito-userpoolsessionconfigurationattachment-userpoolid): {{String}}
  [UserSessionTracking](#cfn-cognito-userpoolsessionconfigurationattachment-usersessiontracking): {{String}}
```

## Properties
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-properties"></a>

`TokenSession`  <a name="cfn-cognito-userpoolsessionconfigurationattachment-tokensession"></a>
Property description not available.
*Required*: Yes
*Type*: [TokenSession](aws-properties-cognito-userpoolsessionconfigurationattachment-tokensession.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserPoolId`  <a name="cfn-cognito-userpoolsessionconfigurationattachment-userpoolid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserSessionTracking`  <a name="cfn-cognito-userpoolsessionconfigurationattachment-usersessiontracking"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-return-values"></a>

### Ref
<a name="aws-resource-cognito-userpoolsessionconfigurationattachment-return-values-ref"></a>
