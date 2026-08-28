---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-vcpucountrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup VCpuCountRequest
<a name="aws-properties-autoscaling-autoscalinggroup-vcpucountrequest"></a>

`VCpuCountRequest` is a property of the `InstanceRequirements` property of the [AWS::AutoScaling::AutoScalingGroup LaunchTemplateOverrides](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplateoverrides.html) property type that describes the minimum and maximum number of vCPUs for an instance type.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-vcpucountrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-vcpucountrequest-syntax.json"></a>

```
{
  "[Max](#cfn-autoscaling-autoscalinggroup-vcpucountrequest-max)" : {{Integer}},
  "[Min](#cfn-autoscaling-autoscalinggroup-vcpucountrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-vcpucountrequest-syntax.yaml"></a>

```
  [Max](#cfn-autoscaling-autoscalinggroup-vcpucountrequest-max): {{Integer}}
  [Min](#cfn-autoscaling-autoscalinggroup-vcpucountrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-vcpucountrequest-properties"></a>

`Max`  <a name="cfn-autoscaling-autoscalinggroup-vcpucountrequest-max"></a>
The maximum number of vCPUs.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`Min`  <a name="cfn-autoscaling-autoscalinggroup-vcpucountrequest-min"></a>
The minimum number of vCPUs.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
