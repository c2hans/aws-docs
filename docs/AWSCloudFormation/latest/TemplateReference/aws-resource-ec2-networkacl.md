---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-networkacl.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::NetworkAcl
<a name="aws-resource-ec2-networkacl"></a>

Specifies a network ACL for your VPC.

To add a network ACL entry, see [AWS::EC2::NetworkAclEntry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-networkaclentry.html).

## Syntax
<a name="aws-resource-ec2-networkacl-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-networkacl-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::NetworkAcl",
  "Properties" : {
      "[Tags](#cfn-ec2-networkacl-tags)" : {{[ Tag, ... ]}},
      "[VpcId](#cfn-ec2-networkacl-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-networkacl-syntax.yaml"></a>

```
Type: AWS::EC2::NetworkAcl
Properties:
  [Tags](#cfn-ec2-networkacl-tags): {{
    - Tag}}
  [VpcId](#cfn-ec2-networkacl-vpcid): {{String}}
```

## Properties
<a name="aws-resource-ec2-networkacl-properties"></a>

`Tags`  <a name="cfn-ec2-networkacl-tags"></a>
The tags for the network ACL.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-networkacl-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-ec2-networkacl-vpcid"></a>
The ID of the VPC for the network ACL.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-networkacl-return-values"></a>

### Ref
<a name="aws-resource-ec2-networkacl-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the network ACL.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-networkacl-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-networkacl-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The ID of the network ACL.

## Examples
<a name="aws-resource-ec2-networkacl--examples"></a>

### Network ACL
<a name="aws-resource-ec2-networkacl--examples--Network_ACL"></a>

The following example creates a network ACL.

#### JSON
<a name="aws-resource-ec2-networkacl--examples--Network_ACL--json"></a>

```
"myNetworkAcl" : {
   "Type" : "AWS::EC2::NetworkAcl",
   "Properties" : {
      "VpcId" : { "Ref" : "myVPC" },
      "Tags" : [ { "Key" : "stack", "Value" : "production" } ]
   }
}
```

#### YAML
<a name="aws-resource-ec2-networkacl--examples--Network_ACL--yaml"></a>

```
   myNetworkAcl:
      Type: AWS::EC2::NetworkAcl
      Properties:
         VpcId:
           Ref: myVPC
         Tags:
         - Key: stack
           Value: production
```

## See also
<a name="aws-resource-ec2-networkacl--seealso"></a>
+ [CreateNetworkAcl](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-CreateNetworkAcl.html) in the *Amazon EC2 API Reference*
+ [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
