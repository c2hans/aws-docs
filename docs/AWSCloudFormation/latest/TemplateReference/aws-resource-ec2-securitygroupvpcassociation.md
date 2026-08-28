---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-securitygroupvpcassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SecurityGroupVpcAssociation
<a name="aws-resource-ec2-securitygroupvpcassociation"></a>

A security group association with a VPC.

## Syntax
<a name="aws-resource-ec2-securitygroupvpcassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-securitygroupvpcassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SecurityGroupVpcAssociation",
  "Properties" : {
      "[GroupId](#cfn-ec2-securitygroupvpcassociation-groupid)" : {{String}},
      "[VpcId](#cfn-ec2-securitygroupvpcassociation-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-securitygroupvpcassociation-syntax.yaml"></a>

```
Type: AWS::EC2::SecurityGroupVpcAssociation
Properties:
  [GroupId](#cfn-ec2-securitygroupvpcassociation-groupid): {{String}}
  [VpcId](#cfn-ec2-securitygroupvpcassociation-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-securitygroupvpcassociation-properties"></a>

`GroupId`  <a name="cfn-ec2-securitygroupvpcassociation-groupid"></a>
The association's security group ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcId`  <a name="cfn-ec2-securitygroupvpcassociation-vpcid"></a>
The association's VPC ID.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-securitygroupvpcassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-securitygroupvpcassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a concatenation of the security group ID and VPC ID in the format `sg-id|vpc-id`. Example:`sg-a1b2c3d4e5a6b7d8e|vpc-a1b2c3d4e5a6b7d8e`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-securitygroupvpcassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-securitygroupvpcassociation-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The association's state.

`StateReason`  <a name="StateReason-fn::getatt"></a>
The association's state reason.

`VpcOwnerId`  <a name="VpcOwnerId-fn::getatt"></a>
The AWS account ID of the owner of the VPC.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
