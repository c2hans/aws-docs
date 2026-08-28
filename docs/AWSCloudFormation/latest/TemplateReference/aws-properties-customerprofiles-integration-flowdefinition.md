---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-integration-flowdefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Integration FlowDefinition
<a name="aws-properties-customerprofiles-integration-flowdefinition"></a>

The configurations that control how Customer Profiles retrieves data from the source, Amazon AppFlow. Customer Profiles uses this information to create an AppFlow flow on behalf of customers.

## Syntax
<a name="aws-properties-customerprofiles-integration-flowdefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-integration-flowdefinition-syntax.json"></a>

```
{
  "[Description](#cfn-customerprofiles-integration-flowdefinition-description)" : {{String}},
  "[FlowName](#cfn-customerprofiles-integration-flowdefinition-flowname)" : {{String}},
  "[KmsArn](#cfn-customerprofiles-integration-flowdefinition-kmsarn)" : {{String}},
  "[SourceFlowConfig](#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig)" : {{SourceFlowConfig}},
  "[Tasks](#cfn-customerprofiles-integration-flowdefinition-tasks)" : {{[ Task, ... ]}},
  "[TriggerConfig](#cfn-customerprofiles-integration-flowdefinition-triggerconfig)" : {{TriggerConfig}}
}
```

### YAML
<a name="aws-properties-customerprofiles-integration-flowdefinition-syntax.yaml"></a>

```
  [Description](#cfn-customerprofiles-integration-flowdefinition-description): {{String}}
  [FlowName](#cfn-customerprofiles-integration-flowdefinition-flowname): {{String}}
  [KmsArn](#cfn-customerprofiles-integration-flowdefinition-kmsarn): {{String}}
  [SourceFlowConfig](#cfn-customerprofiles-integration-flowdefinition-sourceflowconfig): {{
    SourceFlowConfig}}
  [Tasks](#cfn-customerprofiles-integration-flowdefinition-tasks): {{
    - Task}}
  [TriggerConfig](#cfn-customerprofiles-integration-flowdefinition-triggerconfig): {{
    TriggerConfig}}
```

## Properties
<a name="aws-properties-customerprofiles-integration-flowdefinition-properties"></a>

`Description`  <a name="cfn-customerprofiles-integration-flowdefinition-description"></a>
A description of the flow you want to create.
*Required*: No
*Type*: String
*Pattern*: `[\w!@#\-.?,\s]*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlowName`  <a name="cfn-customerprofiles-integration-flowdefinition-flowname"></a>
The specified name of the flow. Use underscores (\_) or hyphens (-) only. Spaces are not allowed.
*Required*: Yes
*Type*: String
*Pattern*: `[a-zA-Z0-9][\w!@#.-]+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsArn`  <a name="cfn-customerprofiles-integration-flowdefinition-kmsarn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service (KMS) key you provide for encryption.
*Required*: Yes
*Type*: String
*Pattern*: `arn:aws:kms:.*:[0-9]+:.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceFlowConfig`  <a name="cfn-customerprofiles-integration-flowdefinition-sourceflowconfig"></a>
The configuration that controls how Customer Profiles retrieves data from the source.
*Required*: Yes
*Type*: [SourceFlowConfig](aws-properties-customerprofiles-integration-sourceflowconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tasks`  <a name="cfn-customerprofiles-integration-flowdefinition-tasks"></a>
A list of tasks that Customer Profiles performs while transferring the data in the flow run.
*Required*: Yes
*Type*: Array of [Task](aws-properties-customerprofiles-integration-task.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TriggerConfig`  <a name="cfn-customerprofiles-integration-flowdefinition-triggerconfig"></a>
The trigger settings that determine how and when the flow runs.
*Required*: Yes
*Type*: [TriggerConfig](aws-properties-customerprofiles-integration-triggerconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
