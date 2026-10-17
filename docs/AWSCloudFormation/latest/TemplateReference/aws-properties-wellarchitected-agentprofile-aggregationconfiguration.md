---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-agentprofile-aggregationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentProfile AggregationConfiguration
<a name="aws-properties-wellarchitected-agentprofile-aggregationconfiguration"></a>

Configuration settings that define the scope of AWS resources to analyze for optimization recommendations.

## Syntax
<a name="aws-properties-wellarchitected-agentprofile-aggregationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-agentprofile-aggregationconfiguration-syntax.json"></a>

```
{
  "[AccessRoleArn](#cfn-wellarchitected-agentprofile-aggregationconfiguration-accessrolearn)" : {{String}},
  "[AccountId](#cfn-wellarchitected-agentprofile-aggregationconfiguration-accountid)" : {{String}},
  "[Regions](#cfn-wellarchitected-agentprofile-aggregationconfiguration-regions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wellarchitected-agentprofile-aggregationconfiguration-syntax.yaml"></a>

```
  [AccessRoleArn](#cfn-wellarchitected-agentprofile-aggregationconfiguration-accessrolearn): {{String}}
  [AccountId](#cfn-wellarchitected-agentprofile-aggregationconfiguration-accountid): {{String}}
  [Regions](#cfn-wellarchitected-agentprofile-aggregationconfiguration-regions): {{
    - String}}
```

## Properties
<a name="aws-properties-wellarchitected-agentprofile-aggregationconfiguration-properties"></a>

`AccessRoleArn`  <a name="cfn-wellarchitected-agentprofile-aggregationconfiguration-accessrolearn"></a>
The ARN of an IAM role to assume for resource analysis in this account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:([a-z\-]+):iam::[0-9]{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AccountId`  <a name="cfn-wellarchitected-agentprofile-aggregationconfiguration-accountid"></a>
The AWS account ID to analyze.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-wellarchitected-agentprofile-aggregationconfiguration-regions"></a>
A list of AWS Regions to include in the analysis.
*Required*: Yes
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `64 | 25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
