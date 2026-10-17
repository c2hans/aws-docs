---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-wellarchitected-agentgoal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::AgentGoal
<a name="aws-resource-wellarchitected-agentgoal"></a>

**Note**
AWS Well-Architected Agent is in preview release and is subject to change.

Creates an optimization goal associated with a profile. Goals define specific targets and objectives for the optimization process.

## Syntax
<a name="aws-resource-wellarchitected-agentgoal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-wellarchitected-agentgoal-syntax.json"></a>

```
{
  "Type" : "AWS::WellArchitected::AgentGoal",
  "Properties" : {
      "[Description](#cfn-wellarchitected-agentgoal-description)" : {{String}},
      "[Pillars](#cfn-wellarchitected-agentgoal-pillars)" : {{[ String, ... ]}},
      "[ProfileArn](#cfn-wellarchitected-agentgoal-profilearn)" : {{String}},
      "[Title](#cfn-wellarchitected-agentgoal-title)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-wellarchitected-agentgoal-syntax.yaml"></a>

```
Type: AWS::WellArchitected::AgentGoal
Properties:
  [Description](#cfn-wellarchitected-agentgoal-description): {{String}}
  [Pillars](#cfn-wellarchitected-agentgoal-pillars): {{
    - String}}
  [ProfileArn](#cfn-wellarchitected-agentgoal-profilearn): {{String}}
  [Title](#cfn-wellarchitected-agentgoal-title): {{String}}
```

## Properties
<a name="aws-resource-wellarchitected-agentgoal-properties"></a>

`Description`  <a name="cfn-wellarchitected-agentgoal-description"></a>
A description of the agent goal.
*Required*: No
*Type*: String
*Pattern*: `^(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+$`
*Minimum*: `1`
*Maximum*: `4000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pillars`  <a name="cfn-wellarchitected-agentgoal-pillars"></a>
The list of Well-Architected pillars this goal targets. Valid values: `COST_OPTIMIZATION` \| `SECURITY` \| `RESILIENCE` \| `PERFORMANCE`.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileArn`  <a name="cfn-wellarchitected-agentgoal-profilearn"></a>
The Amazon Resource Name (ARN) of the parent agent profile that owns this goal.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws([a-z0-9-]+)?:wellarchitected:[a-z0-9-]{6,64}:[0-9]{12}:agent-profile/[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Title`  <a name="cfn-wellarchitected-agentgoal-title"></a>
The title of the agent goal.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:(?!\$\{[a-zA-Z]+:)[\P{C}])+$`
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-wellarchitected-agentgoal-return-values"></a>

### Ref
<a name="aws-resource-wellarchitected-agentgoal-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the agent goal ARN.

### Fn::GetAtt
<a name="aws-resource-wellarchitected-agentgoal-return-values-fn--getatt"></a>

####
<a name="aws-resource-wellarchitected-agentgoal-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the agent goal.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the goal was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The identifier of the system or user that created this goal.

`Id`  <a name="Id-fn::getatt"></a>
The service-generated unique identifier of the agent goal.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The timestamp when the goal was last modified.

`LastModifiedBy`  <a name="LastModifiedBy-fn::getatt"></a>
The identifier of the system or user that last modified this goal.
