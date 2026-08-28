---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-computenodegroup-scalingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::ComputeNodeGroup ScalingConfiguration
<a name="aws-properties-pcs-computenodegroup-scalingconfiguration"></a>

Specifies the boundaries of the compute node group auto scaling.

## Syntax
<a name="aws-properties-pcs-computenodegroup-scalingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-computenodegroup-scalingconfiguration-syntax.json"></a>

```
{
  "[MaxInstanceCount](#cfn-pcs-computenodegroup-scalingconfiguration-maxinstancecount)" : {{Integer}},
  "[MinInstanceCount](#cfn-pcs-computenodegroup-scalingconfiguration-mininstancecount)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-pcs-computenodegroup-scalingconfiguration-syntax.yaml"></a>

```
  [MaxInstanceCount](#cfn-pcs-computenodegroup-scalingconfiguration-maxinstancecount): {{Integer}}
  [MinInstanceCount](#cfn-pcs-computenodegroup-scalingconfiguration-mininstancecount): {{Integer}}
```

## Properties
<a name="aws-properties-pcs-computenodegroup-scalingconfiguration-properties"></a>

`MaxInstanceCount`  <a name="cfn-pcs-computenodegroup-scalingconfiguration-maxinstancecount"></a>
The upper bound of the number of instances allowed in the compute fleet.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinInstanceCount`  <a name="cfn-pcs-computenodegroup-scalingconfiguration-mininstancecount"></a>
The lower bound of the number of instances allowed in the compute fleet.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
