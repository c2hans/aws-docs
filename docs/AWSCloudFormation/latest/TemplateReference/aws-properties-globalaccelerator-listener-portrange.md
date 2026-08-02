---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-globalaccelerator-listener-portrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GlobalAccelerator::Listener PortRange
<a name="aws-properties-globalaccelerator-listener-portrange"></a>

A complex type for a range of ports for a listener.

## Syntax
<a name="aws-properties-globalaccelerator-listener-portrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-globalaccelerator-listener-portrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-globalaccelerator-listener-portrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-globalaccelerator-listener-portrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-globalaccelerator-listener-portrange-syntax.yaml"></a>

```
  [FromPort](#cfn-globalaccelerator-listener-portrange-fromport): {{Integer}}
  [ToPort](#cfn-globalaccelerator-listener-portrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-globalaccelerator-listener-portrange-properties"></a>

`FromPort`  <a name="cfn-globalaccelerator-listener-portrange-fromport"></a>
The first port in the range of ports, inclusive.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-globalaccelerator-listener-portrange-toport"></a>
The last port in the range of ports, inclusive.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
