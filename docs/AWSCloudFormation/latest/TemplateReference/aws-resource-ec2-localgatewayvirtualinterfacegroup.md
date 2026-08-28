---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-localgatewayvirtualinterfacegroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::LocalGatewayVirtualInterfaceGroup
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup"></a>

Describes a local gateway virtual interface group.

## Syntax
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::LocalGatewayVirtualInterfaceGroup",
  "Properties" : {
      "[LocalBgpAsn](#cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasn)" : {{Integer}},
      "[LocalBgpAsnExtended](#cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasnextended)" : {{Integer}},
      "[LocalGatewayId](#cfn-ec2-localgatewayvirtualinterfacegroup-localgatewayid)" : {{String}},
      "[Tags](#cfn-ec2-localgatewayvirtualinterfacegroup-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-syntax.yaml"></a>

```
Type: AWS::EC2::LocalGatewayVirtualInterfaceGroup
Properties:
  [LocalBgpAsn](#cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasn): {{Integer}}
  [LocalBgpAsnExtended](#cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasnextended): {{Integer}}
  [LocalGatewayId](#cfn-ec2-localgatewayvirtualinterfacegroup-localgatewayid): {{String}}
  [Tags](#cfn-ec2-localgatewayvirtualinterfacegroup-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-properties"></a>

`LocalBgpAsn`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasn"></a>
The Autonomous System Number(ASN) for the local Border Gateway Protocol (BGP).
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalBgpAsnExtended`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-localbgpasnextended"></a>
The extended 32-bit ASN for the local BGP configuration.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LocalGatewayId`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-localgatewayid"></a>
The ID of the local gateway.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-localgatewayvirtualinterfacegroup-tags"></a>
The tags assigned to the virtual interface group.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-localgatewayvirtualinterfacegroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-return-values"></a>

### Ref
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the local gateway virtual interface group. For example:

 `{ "Ref": "lgw-vif-grp-07145b276bEXAMPLE" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-localgatewayvirtualinterfacegroup-return-values-fn--getatt-fn--getatt"></a>

`ConfigurationState`  <a name="ConfigurationState-fn::getatt"></a>
The current state of the local gateway virtual interface group.

`LocalGatewayVirtualInterfaceGroupArn`  <a name="LocalGatewayVirtualInterfaceGroupArn-fn::getatt"></a>
The Amazon Resource Number (ARN) of the local gateway virtual interface group.

`LocalGatewayVirtualInterfaceGroupId`  <a name="LocalGatewayVirtualInterfaceGroupId-fn::getatt"></a>
The ID of the virtual interface group.

`LocalGatewayVirtualInterfaceIds`  <a name="LocalGatewayVirtualInterfaceIds-fn::getatt"></a>
The IDs of the virtual interfaces.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the local gateway virtual interface group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
