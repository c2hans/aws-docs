---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-workteam.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Workteam
<a name="aws-resource-sagemaker-workteam"></a>

Creates a new work team for labeling your data. A work team is defined by one or more Amazon Cognito user pools. You must first create the user pools before you can create a work team.

You cannot create more than 25 work teams in an account and region.

## Syntax
<a name="aws-resource-sagemaker-workteam-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-workteam-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Workteam",
  "Properties" : {
      "[Description](#cfn-sagemaker-workteam-description)" : {{String}},
      "[MemberDefinitions](#cfn-sagemaker-workteam-memberdefinitions)" : {{[ MemberDefinition, ... ]}},
      "[NotificationConfiguration](#cfn-sagemaker-workteam-notificationconfiguration)" : {{NotificationConfiguration}},
      "[Tags](#cfn-sagemaker-workteam-tags)" : {{[ Tag, ... ]}},
      "[WorkforceName](#cfn-sagemaker-workteam-workforcename)" : {{String}},
      "[WorkteamName](#cfn-sagemaker-workteam-workteamname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-workteam-syntax.yaml"></a>

```
Type: AWS::SageMaker::Workteam
Properties:
  [Description](#cfn-sagemaker-workteam-description): {{String}}
  [MemberDefinitions](#cfn-sagemaker-workteam-memberdefinitions): {{
    - MemberDefinition}}
  [NotificationConfiguration](#cfn-sagemaker-workteam-notificationconfiguration): {{
    NotificationConfiguration}}
  [Tags](#cfn-sagemaker-workteam-tags): {{
    - Tag}}
  [WorkforceName](#cfn-sagemaker-workteam-workforcename): {{String}}
  [WorkteamName](#cfn-sagemaker-workteam-workteamname): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-workteam-properties"></a>

`Description`  <a name="cfn-sagemaker-workteam-description"></a>
A description of the work team.
*Required*: No
*Type*: String
*Pattern*: `.+`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MemberDefinitions`  <a name="cfn-sagemaker-workteam-memberdefinitions"></a>
A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.
Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition`. For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition`.
*Required*: No
*Type*: Array of [MemberDefinition](aws-properties-sagemaker-workteam-memberdefinition.md)
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NotificationConfiguration`  <a name="cfn-sagemaker-workteam-notificationconfiguration"></a>
Configures SNS notifications of available or expiring work items for work teams.
*Required*: No
*Type*: [NotificationConfiguration](aws-properties-sagemaker-workteam-notificationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-workteam-tags"></a>
An array of key-value pairs.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-workteam-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkforceName`  <a name="cfn-sagemaker-workteam-workforcename"></a>
The name of the workforce.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9]([a-zA-Z0-9\-]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkteamName`  <a name="cfn-sagemaker-workteam-workteamname"></a>
The name of the work team.
*Required*: No
*Type*: String
*Pattern*: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-workteam-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-workteam-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-workteam-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-workteam-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The name of the work team.

`WorkteamName`  <a name="WorkteamName-fn::getatt"></a>
The name of the work team.
