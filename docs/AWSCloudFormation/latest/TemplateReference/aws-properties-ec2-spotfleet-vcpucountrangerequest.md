---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-spotfleet-vcpucountrangerequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SpotFleet VCpuCountRangeRequest
<a name="aws-properties-ec2-spotfleet-vcpucountrangerequest"></a>

The minimum and maximum number of vCPUs.

## Syntax
<a name="aws-properties-ec2-spotfleet-vcpucountrangerequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-spotfleet-vcpucountrangerequest-syntax.json"></a>

```
{
  "[Max](#cfn-ec2-spotfleet-vcpucountrangerequest-max)" : {{Integer}},
  "[Min](#cfn-ec2-spotfleet-vcpucountrangerequest-min)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-spotfleet-vcpucountrangerequest-syntax.yaml"></a>

```
  [Max](#cfn-ec2-spotfleet-vcpucountrangerequest-max): {{Integer}}
  [Min](#cfn-ec2-spotfleet-vcpucountrangerequest-min): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-spotfleet-vcpucountrangerequest-properties"></a>

`Max`  <a name="cfn-ec2-spotfleet-vcpucountrangerequest-max"></a>
The maximum number of vCPUs. To specify no maximum limit, omit this parameter.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-ec2-spotfleet-vcpucountrangerequest-min"></a>
The minimum number of vCPUs. To specify no minimum limit, specify `0`.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
