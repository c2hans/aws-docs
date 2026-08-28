---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-tagproperty.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup TagProperty
<a name="aws-properties-autoscaling-autoscalinggroup-tagproperty"></a>

A structure that specifies a tag for the `Tags` property of [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource.

For more information, see [Tag Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide*. You can find a sample template snippet in the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html#aws-resource-autoscaling-autoscalinggroup--examples) section of the `AWS::AutoScaling::AutoScalingGroup` resource.

CloudFormation adds the following tags to all Auto Scaling groups and associated instances:
+ aws:cloudformation:stack-name
+ aws:cloudformation:stack-id
+ aws:cloudformation:logical-id

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-tagproperty-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-tagproperty-syntax.json"></a>

```
{
  "[Key](#cfn-autoscaling-autoscalinggroup-tagproperty-key)" : {{String}},
  "[PropagateAtLaunch](#cfn-autoscaling-autoscalinggroup-tagproperty-propagateatlaunch)" : {{Boolean}},
  "[Value](#cfn-autoscaling-autoscalinggroup-tagproperty-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-tagproperty-syntax.yaml"></a>

```
  [Key](#cfn-autoscaling-autoscalinggroup-tagproperty-key): {{String}}
  [PropagateAtLaunch](#cfn-autoscaling-autoscalinggroup-tagproperty-propagateatlaunch): {{Boolean}}
  [Value](#cfn-autoscaling-autoscalinggroup-tagproperty-value): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-tagproperty-properties"></a>

`Key`  <a name="cfn-autoscaling-autoscalinggroup-tagproperty-key"></a>
The tag key.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PropagateAtLaunch`  <a name="cfn-autoscaling-autoscalinggroup-tagproperty-propagateatlaunch"></a>
Set to `true` if you want CloudFormation to copy the tag to EC2 instances that are launched as part of the Auto Scaling group. Set to `false` if you want the tag attached only to the Auto Scaling group and not copied to any instances launched as part of the Auto Scaling group.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-autoscaling-autoscalinggroup-tagproperty-value"></a>
The tag value.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
