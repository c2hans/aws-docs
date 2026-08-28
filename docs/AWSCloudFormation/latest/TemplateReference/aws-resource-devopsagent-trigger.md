---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-trigger.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Trigger
<a name="aws-resource-devopsagent-trigger"></a>

The `AWS::DevOpsAgent::Trigger` resource specifies a time-based trigger attached to an Agent Space that fires scheduled automation workflows within the AWS DevOps Agent service.

## Syntax
<a name="aws-resource-devopsagent-trigger-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-trigger-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::Trigger",
  "Properties" : {
      "[Action](#cfn-devopsagent-trigger-action)" : {{Json}},
      "[AgentSpaceId](#cfn-devopsagent-trigger-agentspaceid)" : {{String}},
      "[Condition](#cfn-devopsagent-trigger-condition)" : {{Condition}},
      "[Status](#cfn-devopsagent-trigger-status)" : {{String}},
      "[Type](#cfn-devopsagent-trigger-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-trigger-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::Trigger
Properties:
  [Action](#cfn-devopsagent-trigger-action): {{Json}}
  [AgentSpaceId](#cfn-devopsagent-trigger-agentspaceid): {{String}}
  [Condition](#cfn-devopsagent-trigger-condition): {{
    Condition}}
  [Status](#cfn-devopsagent-trigger-status): {{String}}
  [Type](#cfn-devopsagent-trigger-type): {{String}}
```

## Properties
<a name="aws-resource-devopsagent-trigger-properties"></a>

`Action`  <a name="cfn-devopsagent-trigger-action"></a>
The action to perform when the trigger fires. A JSON object specifying the action type and task configuration.
*Required*: Yes
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AgentSpaceId`  <a name="cfn-devopsagent-trigger-agentspaceid"></a>
The unique identifier of the parent Agent Space.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Condition`  <a name="cfn-devopsagent-trigger-condition"></a>
The condition that determines when the trigger fires.
*Required*: Yes
*Type*: [Condition](aws-properties-devopsagent-trigger-condition.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-devopsagent-trigger-status"></a>
The status of the trigger. `Active` triggers fire on schedule; `Inactive` triggers are paused.
*Required*: No
*Type*: String
*Allowed values*: `Active | Inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-devopsagent-trigger-type"></a>
The type of trigger. Currently only `TIME_BASED` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `TIME_BASED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-devopsagent-trigger-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-trigger-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the TriggerId.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-trigger-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-trigger-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the trigger.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the trigger was created.

`TriggerId`  <a name="TriggerId-fn::getatt"></a>
The unique identifier of the trigger.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the trigger was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
