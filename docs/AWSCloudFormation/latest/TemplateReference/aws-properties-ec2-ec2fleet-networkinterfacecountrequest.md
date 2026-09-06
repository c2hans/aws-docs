---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-networkinterfacecountrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet NetworkInterfaceCountRequest
<a name="aws-properties-ec2-ec2fleet-networkinterfacecountrequest"></a>

The minimum and maximum number of network interfaces.

## Syntax
<a name="aws-properties-ec2-ec2fleet-networkinterfacecountrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-networkinterfacecountrequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-ec2fleet-networkinterfacecountrequest-max)" : {{Integer}},
  "[Min](#cfn-ec2-ec2fleet-networkinterfacecountrequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-networkinterfacecountrequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-ec2fleet-networkinterfacecountrequest-max): {{Integer}}
  [Min](#cfn-ec2-ec2fleet-networkinterfacecountrequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-networkinterfacecountrequest-properties"></a>

`Max`  <a name="cfn-ec2-ec2fleet-networkinterfacecountrequest-max"></a>
The maximum number of network interfaces. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Min`  <a name="cfn-ec2-ec2fleet-networkinterfacecountrequest-min"></a>
The minimum number of network interfaces. To specify no minimum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
