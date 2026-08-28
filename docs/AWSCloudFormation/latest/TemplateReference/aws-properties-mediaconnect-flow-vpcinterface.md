---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediaconnect-flow-vpcinterface.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaConnect::Flow VpcInterface
<a name="aws-properties-mediaconnect-flow-vpcinterface"></a>

The details of a VPC interface.

**Note**
When configuring VPC interfaces for NDI outputs, keep in mind the following:
VPC interfaces must be defined as nested attributes within the `AWS::MediaConnect::Flow` resource, and not within the top-level `AWS::MediaConnect::FlowVpcInterface` resource.
There's a maximum limit of three VPC interfaces for each flow. If you've already reached this limit, you can't update the flow to use a different VPC interface without first removing an existing one.
To update your VPC interfaces in this scenario, you must first remove the VPC interface that’s not being used. Next, add the new VPC interfaces. Lastly, update the `VpcInterfaceAdapter` in the `NDIConfig` property. These changes must be performed as separate manual operations and cannot be done through a single template update.

## Syntax
<a name="aws-properties-mediaconnect-flow-vpcinterface-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediaconnect-flow-vpcinterface-syntax.json"></a>

```
{
  "[Name](#cfn-mediaconnect-flow-vpcinterface-name)" : {{String}},
  "[NetworkInterfaceIds](#cfn-mediaconnect-flow-vpcinterface-networkinterfaceids)" : {{[ String, ... ]}},
  "[NetworkInterfaceType](#cfn-mediaconnect-flow-vpcinterface-networkinterfacetype)" : {{String}},
  "[RoleArn](#cfn-mediaconnect-flow-vpcinterface-rolearn)" : {{String}},
  "[SecurityGroupIds](#cfn-mediaconnect-flow-vpcinterface-securitygroupids)" : {{[ String, ... ]}},
  "[SubnetId](#cfn-mediaconnect-flow-vpcinterface-subnetid)" : {{String}},
  "[Tags](#cfn-mediaconnect-flow-vpcinterface-tags)" : {{[ Tag, ... ]}}
}
```

### YAML
<a name="aws-properties-mediaconnect-flow-vpcinterface-syntax.yaml"></a>

```
  [Name](#cfn-mediaconnect-flow-vpcinterface-name): {{String}}
  [NetworkInterfaceIds](#cfn-mediaconnect-flow-vpcinterface-networkinterfaceids): {{
    - String}}
  [NetworkInterfaceType](#cfn-mediaconnect-flow-vpcinterface-networkinterfacetype): {{String}}
  [RoleArn](#cfn-mediaconnect-flow-vpcinterface-rolearn): {{String}}
  [SecurityGroupIds](#cfn-mediaconnect-flow-vpcinterface-securitygroupids): {{
    - String}}
  [SubnetId](#cfn-mediaconnect-flow-vpcinterface-subnetid): {{String}}
  [Tags](#cfn-mediaconnect-flow-vpcinterface-tags): {{
    - Tag}}
```

## Properties
<a name="aws-properties-mediaconnect-flow-vpcinterface-properties"></a>

`Name`  <a name="cfn-mediaconnect-flow-vpcinterface-name"></a>
 Immutable and has to be a unique against other VpcInterfaces in this Flow.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceIds`  <a name="cfn-mediaconnect-flow-vpcinterface-networkinterfaceids"></a>
 IDs of the network interfaces created in customer's account by MediaConnect.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkInterfaceType`  <a name="cfn-mediaconnect-flow-vpcinterface-networkinterfacetype"></a>
 The type of network interface.
*Required*: No
*Type*: String
*Allowed values*: `ena | efa`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-mediaconnect-flow-vpcinterface-rolearn"></a>
 A role Arn MediaConnect can assume to create ENIs in your account.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws[a-zA-Z-]*):iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityGroupIds`  <a name="cfn-mediaconnect-flow-vpcinterface-securitygroupids"></a>
 Security Group IDs to be used on ENI.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetId`  <a name="cfn-mediaconnect-flow-vpcinterface-subnetid"></a>
 Subnet must be in the AZ of the Flow.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediaconnect-flow-vpcinterface-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediaconnect-flow-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
