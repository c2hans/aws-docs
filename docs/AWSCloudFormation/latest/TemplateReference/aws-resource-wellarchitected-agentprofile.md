---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-agentprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentProfile
<a name="aws-resource-wellarchitected-agentprofile"></a>

**Note**
AWS Well-Architected Agent is in preview release and is subject to change.

Creates an optimization profile that defines the scope and configuration for generating recommendations. A profile specifies the execution role, target pillars, and aggregation settings for analyzing your AWS resources.

## Syntax
<a name="aws-resource-wellarchitected-agentprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-agentprofile-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::AgentProfile",
  "Properties" : {
      "[AggregationConfiguration](#cfn-wellarchitected-agentprofile-aggregationconfiguration)" : {{[ AggregationConfiguration, ... ]}},
      "[BusinessOverview](#cfn-wellarchitected-agentprofile-businessoverview)" : {{String}},
      "[DeletionProtection](#cfn-wellarchitected-agentprofile-deletionprotection)" : {{Boolean}},
      "[Description](#cfn-wellarchitected-agentprofile-description)" : {{String}},
      "[DisplayName](#cfn-wellarchitected-agentprofile-displayname)" : {{String}},
      "[ExecutionRoleArn](#cfn-wellarchitected-agentprofile-executionrolearn)" : {{String}},
      "[Name](#cfn-wellarchitected-agentprofile-name)" : {{String}},
      "[Pillars](#cfn-wellarchitected-agentprofile-pillars)" : {{[ String, ... ]}},
      "[Tags](#cfn-wellarchitected-agentprofile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-agentprofile-syntax.yaml"></a>

```
Type: AWS::WellArchitected::AgentProfile
Properties:
  [AggregationConfiguration](#cfn-wellarchitected-agentprofile-aggregationconfiguration): {{
    - AggregationConfiguration}}
  [BusinessOverview](#cfn-wellarchitected-agentprofile-businessoverview): {{String}}
  [DeletionProtection](#cfn-wellarchitected-agentprofile-deletionprotection): {{Boolean}}
  [Description](#cfn-wellarchitected-agentprofile-description): {{String}}
  [DisplayName](#cfn-wellarchitected-agentprofile-displayname): {{String}}
  [ExecutionRoleArn](#cfn-wellarchitected-agentprofile-executionrolearn): {{String}}
  [Name](#cfn-wellarchitected-agentprofile-name): {{String}}
  [Pillars](#cfn-wellarchitected-agentprofile-pillars): {{
    - String}}
  [Tags](#cfn-wellarchitected-agentprofile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-wellarchitected-agentprofile-properties"></a>

`AggregationConfiguration`  <a name="cfn-wellarchitected-agentprofile-aggregationconfiguration"></a>
The aggregation configuration that defines which AWS accounts and Regions to analyze. Not present for basic profiles.
*Required*: Yes
*Type*: [Array](aws-properties-wellarchitected-agentprofile-aggregationconfiguration.md) of [AggregationConfiguration](aws-properties-wellarchitected-agentprofile-aggregationconfiguration.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BusinessOverview`  <a name="cfn-wellarchitected-agentprofile-businessoverview"></a>
The business overview for this profile.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtection`  <a name="cfn-wellarchitected-agentprofile-deletionprotection"></a>
Indicates whether deletion protection is enabled for the profile.
If you don't specify this property, deletion protection is enabled (`true`) by default. When deletion protection is enabled, you can't delete the profile until you disable deletion protection.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-wellarchitected-agentprofile-description"></a>
A description of the profile.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-wellarchitected-agentprofile-displayname"></a>
The display name of the profile shown to users.
*Required*: No
*Type*: String
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-wellarchitected-agentprofile-executionrolearn"></a>
The ARN of the IAM execution role used for recommendation actions. Not present for basic profiles.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([a-z\-]+):iam::[0-9]{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-wellarchitected-agentprofile-name"></a>
The system name of the profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Pillars`  <a name="cfn-wellarchitected-agentprofile-pillars"></a>
The AWS Well-Architected Framework pillars associated with this profile. Not present for basic profiles.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-wellarchitected-agentprofile-tags"></a>
The tags associated with the profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-wellarchitected-agentprofile-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-agentprofile-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-agentprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent profile ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-agentprofile-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-agentprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the optimization profile.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the profile was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The identifier of the user or system that created this profile.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The timestamp when the profile was last modified.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
The identifier of the user or system that last modified this profile.
