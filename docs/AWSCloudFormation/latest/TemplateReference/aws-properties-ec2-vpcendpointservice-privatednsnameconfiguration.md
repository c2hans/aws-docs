---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEndpointService PrivateDnsNameConfiguration
<a name="aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration"></a>

Information about the private DNS name for the service endpoint.

## Syntax
<a name="aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration-syntax.json"></a>

```
{
  "[Name](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-name)" : {{String}},
  "[State](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-state)" : {{String}},
  "[Type](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-type)" : {{String}},
  "[Value](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration-syntax.yaml"></a>

```
  [Name](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-name): {{String}}
  [State](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-state): {{String}}
  [Type](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-type): {{String}}
  [Value](#cfn-ec2-vpcendpointservice-privatednsnameconfiguration-value): {{String}}
```

## Properties
<a name="aws-properties-ec2-vpcendpointservice-privatednsnameconfiguration-properties"></a>

`Name`  <a name="cfn-ec2-vpcendpointservice-privatednsnameconfiguration-name"></a>
The name of the record subdomain the service provider needs to create. The service provider adds the `value` text to the `name`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-ec2-vpcendpointservice-privatednsnameconfiguration-state"></a>
The verification state of the VPC endpoint service.
Consumers of the endpoint service can use the private name only when the state is `verified`.
*Required*: No
*Type*: String
*Allowed values*: `pendingVerification | verified | failed`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-ec2-vpcendpointservice-privatednsnameconfiguration-type"></a>
The endpoint service verification type, for example TXT.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-ec2-vpcendpointservice-privatednsnameconfiguration-value"></a>
The value the service provider adds to the private DNS name domain record before verification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
