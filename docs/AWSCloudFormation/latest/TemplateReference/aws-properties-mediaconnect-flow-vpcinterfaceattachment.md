---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow VpcInterfaceAttachment
<a name="aws-properties-mediaconnect-flow-vpcinterfaceattachment"></a>

 The settings for attaching a VPC interface to an resource.

## Syntax
<a name="aws-properties-mediaconnect-flow-vpcinterfaceattachment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-vpcinterfaceattachment-syntax.json"></a>

```
{
  "[VpcInterfaceName](#cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-vpcinterfaceattachment-syntax.yaml"></a>

```
  [VpcInterfaceName](#cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename): {{String}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-vpcinterfaceattachment-properties"></a>

`VpcInterfaceName`  <a name="cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename"></a>
 The name of the VPC interface to use for this resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
