---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-vpcconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::VpcConnection
<a name="aws-resource-msk-vpcconnection"></a>

Create remote VPC connection.

## Syntax
<a name="aws-resource-msk-vpcconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-vpcconnection-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::VpcConnection",
  "Properties" : {
      "[Authentication](#cfn-msk-vpcconnection-authentication)" : {{String}},
      "[ClientSubnets](#cfn-msk-vpcconnection-clientsubnets)" : {{[ String, ... ]}},
      "[SecurityGroups](#cfn-msk-vpcconnection-securitygroups)" : {{[ String, ... ]}},
      "[Tags](#cfn-msk-vpcconnection-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[TargetClusterArn](#cfn-msk-vpcconnection-targetclusterarn)" : {{String}},
      "[VpcId](#cfn-msk-vpcconnection-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-msk-vpcconnection-syntax.yaml"></a>

```
Type: AWS::MSK::VpcConnection
Properties:
  [Authentication](#cfn-msk-vpcconnection-authentication): {{String}}
  [ClientSubnets](#cfn-msk-vpcconnection-clientsubnets): {{
    - String}}
  [SecurityGroups](#cfn-msk-vpcconnection-securitygroups): {{
    - String}}
  [Tags](#cfn-msk-vpcconnection-tags): {{
    {{Key}}: {{Value}}}}
  [TargetClusterArn](#cfn-msk-vpcconnection-targetclusterarn): {{String}}
  [VpcId](#cfn-msk-vpcconnection-vpcid): {{String}}
```

## Properties
<a name="aws-resource-msk-vpcconnection-properties"></a>

`Authentication`  <a name="cfn-msk-vpcconnection-authentication"></a>
The type of private link authentication.
*Required*: Yes
*Type*: String
*Allowed values*: `SASL_IAM | SASL_SCRAM | TLS`
*Minimum*: `3`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClientSubnets`  <a name="cfn-msk-vpcconnection-clientsubnets"></a>
The list of subnets in the client VPC to connect to.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroups`  <a name="cfn-msk-vpcconnection-securitygroups"></a>
The security groups to attach to the ENIs for the broker nodes.
*Required*: Yes
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-msk-vpcconnection-tags"></a>
An arbitrary set of tags (key-value pairs) you specify while creating the VPC connection.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetClusterArn`  <a name="cfn-msk-vpcconnection-targetclusterarn"></a>
The Amazon Resource Name (ARN) of the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:kafka:[\w-]+:\d+:cluster.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-msk-vpcconnection-vpcid"></a>
The VPC ID of the remote client.
*Required*: Yes
*Type*: String
*Pattern*: `^(vpc-)([a-z0-9]+)\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-msk-vpcconnection-return-values"></a>

### Ref
<a name="aws-resource-msk-vpcconnection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the VPC connection.

For Amazon MSK VPC connection `MyVpcConnection`, `Ref` returns the ARN of the VPC connection whose logical ID is `MyVpcConnection`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-msk-vpcconnection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-msk-vpcconnection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the VPC connection.
