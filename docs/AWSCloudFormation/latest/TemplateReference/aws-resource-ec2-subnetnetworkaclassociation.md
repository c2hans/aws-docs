---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnetnetworkaclassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::SubnetNetworkAclAssociation
<a name="aws-resource-ec2-subnetnetworkaclassociation"></a>

Associates a subnet with a network ACL. For more information, see [ReplaceNetworkAclAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-ReplaceNetworkAclAssociation.html) in the *Amazon EC2 API Reference*.

When `AWS::EC2::SubnetNetworkAclAssociation` resources are created during create or update operations, AWS CloudFormation adopts existing resources that share the same key properties (the properties that contribute to uniquely identify the resource). However, if the operation fails and rolls back, AWS CloudFormation deletes the previously out-of-band resources. You can protect against this behavior by using `Retain` deletion policies. For more information, see [DeletionPolicy Attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html).

## Syntax
<a name="aws-resource-ec2-subnetnetworkaclassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-subnetnetworkaclassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::SubnetNetworkAclAssociation",
  "Properties" : {
      "[NetworkAclId](#cfn-ec2-subnetnetworkaclassociation-networkaclid)" : {{String}},
      "[SubnetId](#cfn-ec2-subnetnetworkaclassociation-subnetid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-subnetnetworkaclassociation-syntax.yaml"></a>

```
Type: AWS::EC2::SubnetNetworkAclAssociation
Properties:
  [NetworkAclId](#cfn-ec2-subnetnetworkaclassociation-networkaclid): {{String}}
  [SubnetId](#cfn-ec2-subnetnetworkaclassociation-subnetid): {{String}}
```

## Properties
<a name="aws-resource-ec2-subnetnetworkaclassociation-properties"></a>

`NetworkAclId`  <a name="cfn-ec2-subnetnetworkaclassociation-networkaclid"></a>
The ID of the network ACL.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SubnetId`  <a name="cfn-ec2-subnetnetworkaclassociation-subnetid"></a>
The ID of the subnet.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-subnetnetworkaclassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-subnetnetworkaclassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the subnet network ACL association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-subnetnetworkaclassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-subnetnetworkaclassociation-return-values-fn--getatt-fn--getatt"></a>

`AssociationId`  <a name="AssociationId-fn::getatt"></a>
Returns the value of this object's AssociationId property.

## Examples
<a name="aws-resource-ec2-subnetnetworkaclassociation--examples"></a>

### Subnet network ACL association
<a name="aws-resource-ec2-subnetnetworkaclassociation--examples--Subnet_network_ACL_association"></a>

The following example associates subnet mySubnet with the myNetworkAcl network ACL.

#### JSON
<a name="aws-resource-ec2-subnetnetworkaclassociation--examples--Subnet_network_ACL_association--json"></a>

```
"mySubnetNetworkAclAssociation" : {
   "Type" : "AWS::EC2::SubnetNetworkAclAssociation",
   "Properties" : {
      "SubnetId" : { "Ref" : "mySubnet" },
      "NetworkAclId" : { "Ref" : "myNetworkAcl" }
   }
}
```

#### YAML
<a name="aws-resource-ec2-subnetnetworkaclassociation--examples--Subnet_network_ACL_association--yaml"></a>

```
   mySubnetNetworkAclAssociation:
     Type: AWS::EC2::SubnetNetworkAclAssociation
     Properties:
       SubnetId:
         Ref: mySubnet
       NetworkAclId:
         Ref: myNetworkAcl
```
