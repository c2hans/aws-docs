---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-warmpool-instancereusepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::WarmPool InstanceReusePolicy
<a name="aws-properties-autoscaling-warmpool-instancereusepolicy"></a>

A structure that specifies an instance reuse policy for the `InstanceReusePolicy` property of the [AWS::AutoScaling::WarmPool](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-warmpool.html) resource.

For more information, see [Warm pools for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-warmpool-instancereusepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-warmpool-instancereusepolicy-syntax.json"></a>

```
{
  "[ReuseOnScaleIn](#cfn-autoscaling-warmpool-instancereusepolicy-reuseonscalein)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-autoscaling-warmpool-instancereusepolicy-syntax.yaml"></a>

```
  [ReuseOnScaleIn](#cfn-autoscaling-warmpool-instancereusepolicy-reuseonscalein): {{Boolean}}
```

## Properties
<a name="aws-properties-autoscaling-warmpool-instancereusepolicy-properties"></a>

`ReuseOnScaleIn`  <a name="cfn-autoscaling-warmpool-instancereusepolicy-reuseonscalein"></a>
Specifies whether instances in the Auto Scaling group can be returned to the warm pool on scale in.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
