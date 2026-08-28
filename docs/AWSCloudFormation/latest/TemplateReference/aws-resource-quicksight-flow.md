---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-flow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Flow
<a name="aws-resource-quicksight-flow"></a>

<a name="aws-resource-quicksight-flow-description"></a>The `AWS::QuickSight::Flow` resource Property description not available. for QuickSight.

## Syntax
<a name="aws-resource-quicksight-flow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-flow-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::Flow",
  "Properties" : {
      "[AwsAccountId](#cfn-quicksight-flow-awsaccountid)" : {{String}},
      "[Description](#cfn-quicksight-flow-description)" : {{String}},
      "[FlowDefinition](#cfn-quicksight-flow-flowdefinition)" : {{}},
      "[Name](#cfn-quicksight-flow-name)" : {{String}},
      "[Permissions](#cfn-quicksight-flow-permissions)" : {{[ Permission, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-flow-syntax.yaml"></a>

```
Type: AWS::QuickSight::Flow
Properties:
  [AwsAccountId](#cfn-quicksight-flow-awsaccountid): {{String}}
  [Description](#cfn-quicksight-flow-description): {{String}}
  [FlowDefinition](#cfn-quicksight-flow-flowdefinition): {{
    }}
  [Name](#cfn-quicksight-flow-name): {{String}}
  [Permissions](#cfn-quicksight-flow-permissions): {{
    - Permission}}
```

## Properties
<a name="aws-resource-quicksight-flow-properties"></a>

`AwsAccountId`  <a name="cfn-quicksight-flow-awsaccountid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-quicksight-flow-description"></a>
The description of the flow.
*Required*: No
*Type*: String
*Pattern*: `^(?!\s+$)[^{}"\\<>]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowDefinition`  <a name="cfn-quicksight-flow-flowdefinition"></a>
The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change.
*Required*: Yes
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-flow-name"></a>
The display name of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s+$)[^{}"\\<>]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-flow-permissions"></a>
Property description not available.
*Required*: No
*Type*: Array of [Permission](aws-properties-quicksight-flow-permission.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-flow-return-values"></a>

### Ref
<a name="aws-resource-quicksight-flow-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-flow-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-flow-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the flow.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The time this flow was created.

`FlowId`  <a name="FlowId-fn::getatt"></a>
The unique identifier of the flow.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The last time this flow was modified.

`PublishState`  <a name="PublishState-fn::getatt"></a>
The publish state of the flow. Valid values are `DRAFT`, `PUBLISHED`, or `PENDING_APPROVAL`.

`StepAliases`  <a name="StepAliases-fn::getatt"></a>
A list of step alias mappings for the flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
