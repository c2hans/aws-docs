---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-stepfunctions-statemachinealias-routingconfigurationversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::StepFunctions::StateMachineAlias RoutingConfigurationVersion
<a name="aws-properties-stepfunctions-statemachinealias-routingconfigurationversion"></a>

The state machine version to which you want to route the execution traffic.

## Syntax
<a name="aws-properties-stepfunctions-statemachinealias-routingconfigurationversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-stepfunctions-statemachinealias-routingconfigurationversion-syntax.json"></a>

```
{
  "[StateMachineVersionArn](#cfn-stepfunctions-statemachinealias-routingconfigurationversion-statemachineversionarn)" : {{String}},
  "[Weight](#cfn-stepfunctions-statemachinealias-routingconfigurationversion-weight)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-stepfunctions-statemachinealias-routingconfigurationversion-syntax.yaml"></a>

```
  [StateMachineVersionArn](#cfn-stepfunctions-statemachinealias-routingconfigurationversion-statemachineversionarn): {{String}}
  [Weight](#cfn-stepfunctions-statemachinealias-routingconfigurationversion-weight): {{Integer}}
```

## Properties
<a name="aws-properties-stepfunctions-statemachinealias-routingconfigurationversion-properties"></a>

`StateMachineVersionArn`  <a name="cfn-stepfunctions-statemachinealias-routingconfigurationversion-statemachineversionarn"></a>
The Amazon Resource Name (ARN) that identifies one or two state machine versions defined in the routing configuration.
If you specify the ARN of a second version, it must belong to the same state machine as the first version.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-stepfunctions-statemachinealias-routingconfigurationversion-weight"></a>
The percentage of traffic you want to route to the state machine version. The sum of the weights in the routing configuration must be equal to 100.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
