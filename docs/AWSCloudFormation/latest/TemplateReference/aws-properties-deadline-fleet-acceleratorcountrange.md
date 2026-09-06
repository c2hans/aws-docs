---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-deadline-fleet-acceleratorcountrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Deadline::Fleet AcceleratorCountRange
<a name="aws-properties-deadline-fleet-acceleratorcountrange"></a>

Defines the maximum and minimum number of GPU accelerators required for a worker instance..

## Syntax
<a name="aws-properties-deadline-fleet-acceleratorcountrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-deadline-fleet-acceleratorcountrange-syntax.json"></a>

```
{
  "[Max](#cfn-deadline-fleet-acceleratorcountrange-max)" : {{Integer}},
  "[Min](#cfn-deadline-fleet-acceleratorcountrange-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-deadline-fleet-acceleratorcountrange-syntax.yaml"></a>

```
  [Max](#cfn-deadline-fleet-acceleratorcountrange-max): {{Integer}}
  [Min](#cfn-deadline-fleet-acceleratorcountrange-min): {{Integer}}
```

## Properties
<a name="aws-properties-deadline-fleet-acceleratorcountrange-properties"></a>

`Max`  <a name="cfn-deadline-fleet-acceleratorcountrange-max"></a>
The maximum number of GPU accelerators in the worker host.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-deadline-fleet-acceleratorcountrange-min"></a>
The minimum number of GPU accelerators in the worker host.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
