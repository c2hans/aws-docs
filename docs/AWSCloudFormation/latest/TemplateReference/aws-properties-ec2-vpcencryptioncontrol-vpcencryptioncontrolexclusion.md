---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEncryptionControl VpcEncryptionControlExclusion
<a name="aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion"></a>

Describes an exclusion configuration for VPC Encryption Control.

For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.

## Syntax
<a name="aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-syntax.json"></a>

```
{
  "[State](#cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-state)" : {{String}},
  "[StateMessage](#cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-statemessage)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-syntax.yaml"></a>

```
  [State](#cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-state): {{String}}
  [StateMessage](#cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-statemessage): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-properties"></a>

`State`  <a name="cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-state"></a>
The current state of the exclusion configuration.
*Required*: No
*Type*: String
*Allowed values*: `enabling | enabled | disabling | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StateMessage`  <a name="cfn-ec2-vpcencryptioncontrol-vpcencryptioncontrolexclusion-statemessage"></a>
A message providing additional information about the exclusion state.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
