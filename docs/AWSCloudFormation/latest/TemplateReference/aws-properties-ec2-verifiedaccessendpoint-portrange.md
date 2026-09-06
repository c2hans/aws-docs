---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-verifiedaccessendpoint-portrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VerifiedAccessEndpoint PortRange
<a name="aws-properties-ec2-verifiedaccessendpoint-portrange"></a>

Describes the port range for a Verified Access endpoint.

## Syntax
<a name="aws-properties-ec2-verifiedaccessendpoint-portrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-verifiedaccessendpoint-portrange-syntax.json"></a>

```
{
  "[FromPort](#cfn-ec2-verifiedaccessendpoint-portrange-fromport)" : {{Integer}},
  "[ToPort](#cfn-ec2-verifiedaccessendpoint-portrange-toport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ec2-verifiedaccessendpoint-portrange-syntax.yaml"></a>

```
  [FromPort](#cfn-ec2-verifiedaccessendpoint-portrange-fromport): {{Integer}}
  [ToPort](#cfn-ec2-verifiedaccessendpoint-portrange-toport): {{Integer}}
```

## Properties
<a name="aws-properties-ec2-verifiedaccessendpoint-portrange-properties"></a>

`FromPort`  <a name="cfn-ec2-verifiedaccessendpoint-portrange-fromport"></a>
The start of the port range.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ToPort`  <a name="cfn-ec2-verifiedaccessendpoint-portrange-toport"></a>
The end of the port range.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
