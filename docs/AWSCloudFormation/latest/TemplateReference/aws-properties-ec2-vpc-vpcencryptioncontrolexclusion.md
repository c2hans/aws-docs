---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpc-vpcencryptioncontrolexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPC VpcEncryptionControlExclusion
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusion"></a>

Describes an exclusion configuration for VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusion-syntax.json"></a>

```
{
  "[State](#cfn-ec2-vpc-vpcencryptioncontrolexclusion-state)" : {{String}},
  "[StateMessage](#cfn-ec2-vpc-vpcencryptioncontrolexclusion-statemessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusion-syntax.yaml"></a>

```
  [State](#cfn-ec2-vpc-vpcencryptioncontrolexclusion-state): {{String}}
  [StateMessage](#cfn-ec2-vpc-vpcencryptioncontrolexclusion-statemessage): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpc-vpcencryptioncontrolexclusion-properties"></a>

`State`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusion-state"></a>
The current state of the exclusion configuration.
*Required*: No
*Type*: String
*Allowed values*: `enabling | enabled | disabling | disabled`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StateMessage`  <a name="cfn-ec2-vpc-vpcencryptioncontrolexclusion-statemessage"></a>
A message providing additional information about the exclusion state.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
