---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancegroupconfig-scalingconstraints.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceGroupConfig ScalingConstraints
<a name="aws-properties-emr-instancegroupconfig-scalingconstraints"></a>

`ScalingConstraints` is a subproperty of the `AutoScalingPolicy` property type. `ScalingConstraints` defines the upper and lower EC2 instance limits for an automatic scaling policy. Automatic scaling activities triggered by automatic scaling rules will not cause an instance group to grow above or shrink below these limits.

## Syntax
<a name="aws-properties-emr-instancegroupconfig-scalingconstraints-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancegroupconfig-scalingconstraints-syntax.json"></a>

```
{
  "[MaxCapacity](#cfn-emr-instancegroupconfig-scalingconstraints-maxcapacity)" : {{Integer}},
  "[MinCapacity](#cfn-emr-instancegroupconfig-scalingconstraints-mincapacity)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancegroupconfig-scalingconstraints-syntax.yaml"></a>

```
  [MaxCapacity](#cfn-emr-instancegroupconfig-scalingconstraints-maxcapacity): {{Integer}}
  [MinCapacity](#cfn-emr-instancegroupconfig-scalingconstraints-mincapacity): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancegroupconfig-scalingconstraints-properties"></a>

`MaxCapacity`  <a name="cfn-emr-instancegroupconfig-scalingconstraints-maxcapacity"></a>
The upper boundary of Amazon EC2 instances in an instance group beyond which scaling activities are not allowed to grow. Scale-out activities will not add instances beyond this boundary.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinCapacity`  <a name="cfn-emr-instancegroupconfig-scalingconstraints-mincapacity"></a>
The lower boundary of Amazon EC2 instances in an instance group below which scaling activities are not allowed to shrink. Scale-in activities will not terminate instances below this boundary.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
