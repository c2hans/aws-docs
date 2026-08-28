---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudformation-stackset-stackinstances.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::StackSet StackInstances
<a name="aws-properties-cloudformation-stackset-stackinstances"></a>

Stack instances in some specific accounts and Regions.

## Syntax
<a name="aws-properties-cloudformation-stackset-stackinstances-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudformation-stackset-stackinstances-syntax.json"></a>

```
{
  "[DeploymentTargets](#cfn-cloudformation-stackset-stackinstances-deploymenttargets)" : {{DeploymentTargets}},
  "[ParameterOverrides](#cfn-cloudformation-stackset-stackinstances-parameteroverrides)" : {{[ Parameter, ... ]}},
  "[Regions](#cfn-cloudformation-stackset-stackinstances-regions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudformation-stackset-stackinstances-syntax.yaml"></a>

```
  [DeploymentTargets](#cfn-cloudformation-stackset-stackinstances-deploymenttargets): {{
    DeploymentTargets}}
  [ParameterOverrides](#cfn-cloudformation-stackset-stackinstances-parameteroverrides): {{
    - Parameter}}
  [Regions](#cfn-cloudformation-stackset-stackinstances-regions): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudformation-stackset-stackinstances-properties"></a>

`DeploymentTargets`  <a name="cfn-cloudformation-stackset-stackinstances-deploymenttargets"></a>
The AWS Organizations accounts or AWS accounts to deploy stacks to in the specified Regions.
*Required*: Yes
*Type*: [DeploymentTargets](aws-properties-cloudformation-stackset-deploymenttargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterOverrides`  <a name="cfn-cloudformation-stackset-stackinstances-parameteroverrides"></a>
A list of StackSet parameters whose values you want to override in the selected stack instances.
*Required*: No
*Type*: Array of [Parameter](aws-properties-cloudformation-stackset-parameter.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Regions`  <a name="cfn-cloudformation-stackset-stackinstances-regions"></a>
The names of one or more Regions where you want to create stack instances using the specified AWS accounts.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
