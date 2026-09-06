---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-transitgatewaypolicytableassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::TransitGatewayPolicyTableAssociation
<a name="aws-resource-ec2-transitgatewaypolicytableassociation"></a>

Describes a transit gateway policy table association.

## Syntax
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::TransitGatewayPolicyTableAssociation",
  "Properties" : {
      "[TransitGatewayAttachmentId](#cfn-ec2-transitgatewaypolicytableassociation-transitgatewayattachmentid)" : {{String}},
      "[TransitGatewayPolicyTableId](#cfn-ec2-transitgatewaypolicytableassociation-transitgatewaypolicytableid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-syntax.yaml"></a>

```
Type: AWS::EC2::TransitGatewayPolicyTableAssociation
Properties:
  [TransitGatewayAttachmentId](#cfn-ec2-transitgatewaypolicytableassociation-transitgatewayattachmentid): {{String}}
  [TransitGatewayPolicyTableId](#cfn-ec2-transitgatewaypolicytableassociation-transitgatewaypolicytableid): {{String}}
```

## Properties
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-properties"></a>

`TransitGatewayAttachmentId`  <a name="cfn-ec2-transitgatewaypolicytableassociation-transitgatewayattachmentid"></a>
The ID of the transit gateway attachment.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TransitGatewayPolicyTableId`  <a name="cfn-ec2-transitgatewaypolicytableassociation-transitgatewaypolicytableid"></a>
The ID of the transit gateway policy table.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-return-values"></a>

### Ref
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-transitgatewaypolicytableassociation-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The state of the transit gateway policy table association.
