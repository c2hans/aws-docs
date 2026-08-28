---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-launchtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup LaunchTemplate
<a name="aws-properties-autoscaling-autoscalinggroup-launchtemplate"></a>

Use this structure to specify the launch templates and instance types (overrides) for a mixed instances policy.

`LaunchTemplate` is a property of the [AWS::AutoScaling::AutoScalingGroup MixedInstancesPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-mixedinstancespolicy.html) property type.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-launchtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-launchtemplate-syntax.json"></a>

```
{
  "[LaunchTemplateSpecification](#cfn-autoscaling-autoscalinggroup-launchtemplate-launchtemplatespecification)" : {{LaunchTemplateSpecification}},
  "[Overrides](#cfn-autoscaling-autoscalinggroup-launchtemplate-overrides)" : {{[ LaunchTemplateOverrides, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-launchtemplate-syntax.yaml"></a>

```
  [LaunchTemplateSpecification](#cfn-autoscaling-autoscalinggroup-launchtemplate-launchtemplatespecification): {{
    LaunchTemplateSpecification}}
  [Overrides](#cfn-autoscaling-autoscalinggroup-launchtemplate-overrides): {{
    - LaunchTemplateOverrides}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-launchtemplate-properties"></a>

`LaunchTemplateSpecification`  <a name="cfn-autoscaling-autoscalinggroup-launchtemplate-launchtemplatespecification"></a>
The launch template.
*Required*: Yes
*Type*: [LaunchTemplateSpecification](aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Overrides`  <a name="cfn-autoscaling-autoscalinggroup-launchtemplate-overrides"></a>
Any properties that you specify override the same properties in the launch template.
*Required*: No
*Type*: Array of [LaunchTemplateOverrides](aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
