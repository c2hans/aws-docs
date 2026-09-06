---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cognito-userpoolresourceserver-resourceserverscopetype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cognito::UserPoolResourceServer ResourceServerScopeType
<a name="aws-properties-cognito-userpoolresourceserver-resourceserverscopetype"></a>

One custom scope associated with a user pool resource server. This data type is a member of `ResourceServerScopeType`. For more information, see [ Scopes, M2M, and API authorization with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html).

## Syntax
<a name="aws-properties-cognito-userpoolresourceserver-resourceserverscopetype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cognito-userpoolresourceserver-resourceserverscopetype-syntax.json"></a>

```
{
  "[ScopeDescription](#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopedescription)" : {{String}},
  "[ScopeName](#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopename)" : {{String}}
}
```

### YAML
<a name="aws-properties-cognito-userpoolresourceserver-resourceserverscopetype-syntax.yaml"></a>

```
  [ScopeDescription](#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopedescription): {{String}}
  [ScopeName](#cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopename): {{String}}
```

## Properties
<a name="aws-properties-cognito-userpoolresourceserver-resourceserverscopetype-properties"></a>

`ScopeDescription`  <a name="cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopedescription"></a>
A friendly description of a custom scope.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScopeName`  <a name="cfn-cognito-userpoolresourceserver-resourceserverscopetype-scopename"></a>
The name of the scope. Amazon Cognito renders custom scopes in the format `resourceServerIdentifier/ScopeName`. For example, if this parameter is `exampleScope` in the resource server with the identifier `exampleResourceServer`, you request and receive the scope `exampleResourceServer/exampleScope`.
*Required*: Yes
*Type*: String
*Pattern*: `[\x21\x23-\x2E\x30-\x5B\x5D-\x7E]+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
